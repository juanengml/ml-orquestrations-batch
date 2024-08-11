import requests  # Certifique-se de ter requests instalado
from datetime import datetime
from plombery import get_logger
from scapy.all import ARP, Ether, srp
from notifications.alerts import Success, Warning, Info


import requests
from datetime import datetime
from plombery import get_logger
from notifications.alerts import Success, Warning
import random

# Lista de URLs de imagens de gatos
CAT_IMAGES = [
    "https://i.pinimg.com/originals/1c/39/80/1c39807dd3b3ab9a8a9db0f8ec25e3cd.jpg",
    "https://cdn.shopify.com/s/files/1/0264/0841/9946/products/MrFormal_CatTieBowtieCollectionBowTie_Collar_1800x1800.jpg?v=1622744651",
    "https://image.shutterstock.com/image-photo/cat-bow-tie-glasses-sitting-260nw-1201700011.jpg",
    "https://i.pinimg.com/originals/69/6d/2f/696d2f556f8d6a7cbdad7a333b19b79e.jpg",
    "https://image.shutterstock.com/image-photo/cute-kitten-wearing-tie-hat-260nw-1305460549.jpg",
    "https://i.pinimg.com/736x/6b/f0/25/6bf025eb28e519087b1491fc9c285702.jpg",
    "https://i.pinimg.com/originals/88/28/26/8828261b09f1e71c715b8de5d3a485c1.jpg",
    "https://i.pinimg.com/originals/5a/1a/d3/5a1ad34b4b629b0fa967f751f7f43713.jpg",
    "https://www.catdumb.com/wp-content/uploads/2018/02/cat-necktie-featured.jpg",
    "https://media.gettyimages.com/photos/cat-dressed-with-a-tie-and-spectacles-picture-id470789472"
]

# URL da imagem de falha (meme)
FAILURE_IMAGE_URL = "https://www.dictionary.com/e/wp-content/uploads/2018/03/This-is-Fine-300x300.jpg"







def determine_action(url):
    """Determina a ação (Ligada/Desligada) com base no parâmetro `state` na URL."""
    if 'state=1' in url:
        return 'Ligada'
    elif 'state=0' in url:
        return 'Desligada'
    return 'Indefinida'


def send_alert(title, message, success=True):
    """Envia um alerta com base no sucesso ou falha da operação."""
    image_url = random.choice(CAT_IMAGES) if success else FAILURE_IMAGE_URL
    alert_class = Success if success else Warning
    alert_class().send(
        title=title,
        message=message,
        image_url=image_url,
        service_name="Home Automation",
        pipeline_name="Light Control Pipeline"
    )


def log_and_append_status(status_list, endpoint, status_message, response=None):
    """Registra no log e adiciona o status da operação à lista de status."""
    logger = get_logger()
    logger.info("Fetched %s lights status rows", len(status_list))

    status_list.append({
        "id": endpoint["id"],
        "endpoint": endpoint["url"],
        "date": datetime.now(),
        "status": status_message,
        "response": response if response else "Failed to fetch response"
    })


def fetch_light_status(endpoint):
    """Tenta obter o status da luz via HTTP e retorna o resultado ou None se falhar."""
    try:
        response = requests.get(endpoint["url"], timeout=5)
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        return None


def control_light(endpoint):
    logger = get_logger()
    status = []

    logger.debug(f"[Lights {endpoint['name']}]...")

    response = fetch_light_status(endpoint)
    if response:
        action = determine_action(endpoint["url"])
        status_message = f"{endpoint['name']} {action}"

        # Enviar alerta de sucesso
        send_alert("Light Control Success", status_message, success=True)
    else:
        action = determine_action(endpoint["url"])
        status_message = f"{endpoint['name']} Falha ao {action}"

        # Enviar alerta de falha
        send_alert("Light Control Failure", status_message, success=False)

    log_and_append_status(status, endpoint, status_message, response=response)
    return status

def check_mac_address(mac_address, network_range="192.168.1.0/24"):
    logger = get_logger()
    status = []

    logger.debug(f"Checking presence of MAC address {mac_address} on the network...")

    try:
        # Cria um pacote ARP para broadcast na rede local
        arp = ARP(pdst=network_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        # Envia o pacote e recebe as respostas
        result = srp(packet, timeout=3, verbose=0)[0]

        # Itera sobre as respostas
        found = False
        for sent, received in result:
            if received.hwsrc.lower() == mac_address.lower():
                status_message = f"Device with MAC {mac_address} is online."
                Success.send(status_message)
                found = True
                break

        if not found:
            status_message = f"Device with MAC {mac_address} is offline."
            Warning.send(status_message)

        status.append({
            "mac_address": mac_address,
            "date": datetime.now(),
            "status": status_message,
            "details": [received.psrc for sent, received in result] if found else []
        })

    except Exception as e:
        status_message = f"Failed to check status for MAC {mac_address}"
        Warning.send(status_message)
        status.append({
            "mac_address": mac_address,
            "date": datetime.now(),
            "status": status_message,
            "error": str(e)
        })

    logger.info("Checked MAC address %s with status: %s", mac_address, status_message)
    return status

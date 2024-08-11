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
cat_images = [
    "https://rlv.zcache.com.br/cartao_postal_gato_chefe_na_gravata-r75b6de6a8e74403891ea299e60aa9921_ucbjp_644.webp",
    "https://i.pinimg.com/736x/5a/be/e1/5abee1475c587252ef681cfc05ebf59b.jpg",
    "https://www.tediado.com.br/wp-content/uploads/2019/09/gatos-com-gravatas-11.jpg",
    "https://cdn.bhdw.net/im/black-cat-with-a-tie-and-a-cup-of-coffee-wallpaper-96403_w635.webp",
    "https://cdn.pixabay.com/photo/2024/01/07/16/52/ai-generated-8493598_1280.png",
    "https://thumbs.dreamstime.com/b/la-ilustraci%C3%B3n-del-traje-gato-cyberpunk-es-un-s%C3%ADmbolo-de-rebeli%C3%B3n-y-el-estilo-tecnolog%C3%ADa-esta-muestra-una-imagen-fresca-fresco-269540889.jpg"
]

# URL da imagem de falha (meme)
failure_image_url = "https://www.dictionary.com/e/wp-content/uploads/2018/03/This-is-Fine-300x300.jpg"



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


def log_and_append_status(status_list, endpoint, status_message, response=None, error=None):
    """Registra no log e adiciona o status da operação à lista de status."""
    logger = get_logger()
    logger.info("Fetched %s lights status rows", len(status_list))

    status_list.append({
        "id": endpoint["id"],
        "endpoint": endpoint["url"],
        "date": datetime.now(),
        "status": status_message,
        "response": response if response else str(error)
    })



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

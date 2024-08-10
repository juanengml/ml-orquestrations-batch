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

def control_light(endpoint):
    logger = get_logger()
    status = []

    logger.debug(f"[Lights {endpoint['name']}]...")

    try:
        response = requests.get(endpoint["url"]).text
        action = 'Ligada' if 'on' in endpoint['url'] else 'Desligada'
        status_message = f"{endpoint['name']} {action}"

        # Seleciona uma imagem aleatória da lista de gatos para sucesso
        image_url = random.choice(cat_images)

        # Enviar alerta de sucesso
        Success().send(
            title="Light Control Success",
            message=status_message,
            image_url=image_url,
            service_name="Home Automation",
            pipeline_name="Light Control Pipeline"
        )

        status.append({
            "id": endpoint["id"],
            "endpoint": endpoint["url"],
            "date": datetime.now(),
            "status": status_message,
            "response": response
        })

    except Exception as e:
        status_message = f"{endpoint['name']} Falha ao {action}"

        # Usar a imagem de falha (meme)
        image_url = failure_image_url

        # Enviar alerta de aviso
        Warning().send(
            title="Light Control Failure",
            message=status_message,
            image_url=image_url,
            service_name="Home Automation",
            pipeline_name="Light Control Pipeline"
        )

        status.append({
            "id": endpoint["id"],
            "endpoint": endpoint["url"],
            "date": datetime.now(),
            "status": status_message,
            "response": str(e)
        })

    logger.info("Fetched %s lights status rows", len(status))
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

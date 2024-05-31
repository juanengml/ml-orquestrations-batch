import requests  # Certifique-se de ter requests instalado
from datetime import datetime
from plombery import get_logger


def control_light(endpoint):
    logger = get_logger()
    status = []

    logger.debug(f"[Lights {endpoint['name']}]...")
    try:
        response = requests.get(endpoint["url"]).text
        status.append({
            "id": endpoint["id"],
            "endpoint": endpoint["url"],
            "date": datetime.now(),
            "status": f"{endpoint['name']} {'Ligada' if 'on' in endpoint['url'] else 'Desligada'}",
            "response": response
        })
    except Exception as e:
        status.append({
            "id": endpoint["id"],
            "endpoint": endpoint["url"],
            "date": datetime.now(),
            "status": f"{endpoint['name']} Falha ao {'Ligar' if 'on' in endpoint['url'] else 'Desligar'}",
            "response": str(e)
        })

    logger.info("Fetched %s lights status rows", len(status))
    return status
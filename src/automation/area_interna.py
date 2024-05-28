from plombery import get_logger
from datetime import datetime
from requests import get


def lights_on_office_one():
    logger = get_logger()
    endpoints = [
        {"id": 4, "name": "Luz Escritorio 1", "url": "http://192.168.0.58/update?relay=1&state=1"}
    ]
    status = []

    for endpoint in endpoints:
        logger.debug(f"[Lights ON] {endpoint['name']}...")
        try:
            response = get(endpoint['url']).text
            status.append({
                "id": endpoint["id"],
                "endpoint": endpoint["url"],
                "date": datetime.now(),
                "status": f"{endpoint['name']} Ligada",
                "response": response
            })
        except Exception as e:
            status.append({
                "id": endpoint["id"],
                "endpoint": endpoint["url"],
                "date": datetime.now(),
                "status": f"{endpoint['name']} Falha ao Ligar",
                "response": str(e)
            })

    logger.info("Fetched %s lights status rows", len(status))
    return status


def lights_off_office_one():
    logger = get_logger()
    endpoints = [
        {"id": 4, "name": "Luz Escritorio 1", "url": "http://192.168.0.58/update?relay=1&state=0"}
    ]
    status = []

    for endpoint in endpoints:
        logger.debug(f"[Lights Off] {endpoint['name']}...")
        try:
            response = get(endpoint['url']).text
            status.append({
                "id": endpoint["id"],
                "endpoint": endpoint["url"],
                "date": datetime.now(),
                "status": f"{endpoint['name']} Desligada",
                "response": response
            })
        except Exception as e:
            status.append({
                "id": endpoint["id"],
                "endpoint": endpoint["url"],
                "date": datetime.now(),
                "status": f"{endpoint['name']} Falha ao Desligar",
                "response": str(e)
            })

    logger.info("Fetched %s lights status rows", len(status))
    return status



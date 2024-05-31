from src.automation.services import control_light


def lights_on_office_one():
    endpoint = {"id": 4, "name": "Luz Escritorio 1", "url": "http://192.168.0.58/update?relay=1&state=1"}
    return control_light(endpoint)

def lights_off_office_one():
    endpoint = {"id": 4, "name": "Luz Escritorio 1", "url": "http://192.168.0.58/update?relay=1&state=0"}
    return control_light(endpoint)


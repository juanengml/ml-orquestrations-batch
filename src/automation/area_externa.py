from automation.services import control_light

def lights_on_luz_rede():
    endpoint = {"id": 1, "name": "Luz da Rede", "url": "http://192.168.0.28/led/1/on"}
    return control_light(endpoint)

def lights_on_luz_quartinho():
    endpoint = {"id": 2, "name": "Luz do Quartinho", "url": "http://192.168.0.28/led/2/on"}
    return control_light(endpoint)

def lights_on_luz_garagem():
    endpoint = {"id": 3, "name": "Luz da Garagem e Corredor", "url": "http://192.168.0.58/update?relay=2&state=1"}
    return control_light(endpoint)

def lights_off_luz_rede():
    endpoint = {"id": 1, "name": "Luz da Rede", "url": "http://192.168.0.28/led/1/off"}
    return control_light(endpoint)

def lights_off_luz_quartinho():
    endpoint = {"id": 2, "name": "Luz do Quartinho", "url": "http://192.168.0.28/led/2/off"}
    return control_light(endpoint)

def lights_off_luz_garagem():
    endpoint = {"id": 3, "name": "Luz da Garagem e Corredor", "url": "http://192.168.0.58/update?relay=2&state=0"}
    return control_light(endpoint)

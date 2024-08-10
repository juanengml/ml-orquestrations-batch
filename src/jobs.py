from plombery import task, get_logger
from requests import get
from models.adeline import runner

from automation.area_externa import lights_on_luz_rede
from automation.area_externa import lights_on_luz_quartinho
from automation.area_externa import lights_on_luz_garagem
from automation.area_externa import lights_off_luz_rede
from automation.area_externa import lights_off_luz_quartinho
from automation.area_externa import lights_off_luz_garagem
from automation.area_interna import lights_on_office_one
from automation.area_interna import lights_off_office_one


@task
def job_automation_turn_off_office_one():
    status = lights_off_office_one()
    return status

@task
def job_automation_turn_on_office_one():
    status = lights_on_office_one()
    return status

@task
def job_automation_turn_off_luz_garagem():
    logger = get_logger()
    logger.debug("Fetching light on data...")
    status = lights_off_luz_garagem()
    logger.info("Fetched %s inference data rows", len(status))
    return status

@task
def job_automation_turn_on_luz_garagem():
    logger = get_logger()
    logger.debug("Fetching light on data...")
    status = lights_on_luz_garagem()
    logger.info("Fetched %s inference data rows", len(status))
    return status


@task
def job_automation_turn_on_luz_rede():
    logger = get_logger()
    logger.debug("Fetching inference data...")
    inference = lights_on_luz_rede()
    logger.info("Fetched %s inference data rows", len(inference))

    return inference

@task
def job_automation_turn_off_luz_rede():
    logger = get_logger()
    logger.debug("Fetching light off data...")
    inference = lights_off_luz_rede()
    logger.info("Fetched %s inference data rows", len(inference))

    return inference

@task
def job_automation_turn_on_luz_quartinho():
    logger = get_logger()
    logger.debug("Fetching light on data...")
    inference = lights_on_luz_quartinho()
    logger.info("Fetched %s inference data rows", len(inference))
    return inference

@task
def job_automation_turn_off_luz_quartinho():
    logger = get_logger()
    logger.debug("Fetching light off data...")
    inference = lights_off_luz_quartinho()
    logger.info("Fetched %s inference data rows", len(inference))
    return inference
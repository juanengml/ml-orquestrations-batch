from plombery import task, get_logger
from requests import get
from models.adeline import runner
from automation.area_externa import lights_off, lights_on

@task
def job_automation_turn_on():
    logger = get_logger()
    logger.debug("Fetching light on data...")
    status = lights_on()
    logger.info("Fetched %s inference data rows", len(status))
    return status

@task
def job_automation_turn_off():
    logger = get_logger()
    logger.debug("Fetching light off data...")
    status = lights_off()
    logger.info("Fetched %s inference data rows", len(status))
    return status

@task
def job_submit_ml_adeline():
    logger = get_logger()
    logger.debug("Fetching inference data...")
    inference = runner()
    logger.info("Fetched %s inference data rows", len(inference))

    return inference


@task
def job_submit_extract_address_data():
    """Fetch latest 50 sales of the day"""
    endpoint = "https://random-data-api.com/api/address/random_address?size=100"
    logger = get_logger()

    logger.debug("Fetching address data...")
    address = get(endpoint).json()
    logger.info("Fetched %s sales data rows", len(address))

    return address

@task
def job_submit_extract_beer_data():
    endpoint = "https://random-data-api.com/api/beer/random_beer?size=100"

    logger = get_logger()

    logger.debug("Fetching beer data...")

    beer = get(endpoint).json()

    logger.info("Fetched %s berr data rows", len(beer))

    return beer




@task
def job_submit_extract_cripto_data():
    endpoint = "https://random-data-api.com/api/crypto_coin/random_crypto_coin?size=100"

    logger = get_logger()

    logger.debug("Fetching cripto data...")

    cripto = get(endpoint).json()

    logger.info("Fetched %s cripto data rows", len(cripto))

    return cripto

@task
def job_submit_extract_company_data():
    endpoint = "https://random-data-api.com/api/company/random_company?size=100"

    logger = get_logger()

    logger.debug("Fetching beer data...")

    company = get(endpoint).json()

    logger.info("Fetched %s berr data rows", len(company))

    return company
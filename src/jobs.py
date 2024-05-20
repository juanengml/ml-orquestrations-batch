from plombery import task, get_logger
from requests import get
from time import sleep

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
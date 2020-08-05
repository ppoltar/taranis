import pytest,time, logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = 'C:/bin/chromedriver.exe'
SITE_PATH = 'https://unruffled-clarke-9db730.netlify.app/'

@pytest.fixture
def setup_driver():
    logging.info("Setting up driver and path to the game")
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(SITE_PATH)
    yield driver
    logging.info("Closing the window of the game")
    driver.close()

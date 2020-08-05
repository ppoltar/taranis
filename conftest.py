import pytest,time, logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = 'C:/bin/chromedriver.exe'
SITE_PATH = 'https://unruffled-clarke-9db730.netlify.app/'

def pytest_addoption(parser):
    parser.addoption("--n", action="store", default=1, help="number of game to play")

@pytest.fixture
def setup(request):
    logging.info("Setting up driver and path to the game")
    config_param = {}
    config_param["number_of_games"] = request.config.getoption("--n")
    config_param["driver"] = webdriver.Chrome(DRIVER_PATH)
    config_param["driver"].get(SITE_PATH)
    yield config_param
    logging.info("Closing the window of the game")
    config_param["driver"].close()

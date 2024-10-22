from unittest.mock import MagicMock

import pytest

from app_for_unit.car import Engine, FuelSystem, Car
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture
def engine_mock():
    mock = MagicMock(Engine)
    mock.start.return_value = "Engine started"
    mock.stop.return_value = "Engine stopped"
    return mock


@pytest.fixture
def fuel_system_mock():
    mock = MagicMock(FuelSystem)
    mock.fuel_level = 10
    mock.refuel.return_value = "Fuel level: 20"
    return mock


@pytest.fixture
def car(engine_mock, fuel_system_mock):
    return Car(engine_mock, fuel_system_mock)




# WEB
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        ValueError("Can't create instance for this browser param")

    yield browser

    browser.quit()

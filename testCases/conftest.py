import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    # s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)
    return driver

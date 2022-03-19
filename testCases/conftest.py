import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # s = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=s)
        s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser == 'firefox':
        s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    else:
        s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ***************** Pytest HTML Report  ************************#

# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customer'
#     config.metadata['Tester'] = 'Mohit'


# It is a hook for delete/modify Environment info to HTML Report #
# @pytest.mark.optional
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugin", None)

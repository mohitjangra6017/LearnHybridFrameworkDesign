import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service



# FOR LINUX
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("/home/mohit/SDET/Hybrid_Pytest_Framework/nop_comm_admin/driver/chromedriver")
        driver.maximize_window()
        # driver.fullscreen_window()

    elif browser == 'firefox':
        driver = webdriver.Firefox("/home/mohit/SDET/Hybrid_Pytest_Framework/nop_comm_admin/driver/geckodriver")
        driver.maximize_window()
        # driver.fullscreen_window()

    else:
        driver = webdriver.Chrome("/home/mohit/SDET/Hybrid_Pytest_Framework/LearnHybridFrameworkDesign/driver/chromedriver")
        driver.maximize_window()
        # driver.fullscreen_window()
    return driver


# FOR WINDOWS
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\chromedriver.exe")
#         driver = webdriver.Chrome(service=s)
#         driver.maximize_window()
#         driver.fullscreen_window()
#     elif browser == 'firefox':
#         s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\geckodriver.exe")
#         driver = webdriver.Firefox(service=s)
        # driver.maximize_window()
        # driver.fullscreen_window()
#     else:
#         s = Service(executable_path="D:\SDET\LearnHybridFrameworkDesign\driver\chromedriver.exe")
#         driver = webdriver.Chrome(service=s)
        # driver.maximize_window()
        # driver.fullscreen_window()
#     return driver


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

import pytest
from driverutil.browser import Browser


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driverinit(request):
    webdriver = Browser().getbrowser(request.param)
    request.cls.driver = webdriver
    yield
    webdriver.close()

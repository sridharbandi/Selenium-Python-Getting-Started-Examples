import pytest
from driverutil.Browser import Browser


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    webdriver = Browser().getbrowser(request.param)
    request.cls.driver = webdriver
    yield
    webdriver.close()

''' Just a simple example of Selenium tests.
To run: python3 -m pytest ta_calc_unhrc.py'''
from selenium import webdriver
import pytest
import requests

r = requests.get('http://checkip.amazonaws.com')
public_url = r.text.strip()
URL = f"http://{public_url}:8081/"


@pytest.fixture()
def setup(request):
    service = webdriver.chrome.service.Service('/usr/bin/chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    driver = webdriver.Remote(service.service_url, options=options)
    request.instance.driver = driver

    yield
    driver.close()


@pytest.mark.usefixtures("setup")
class TestURL:
    def test_url_name(self):
        self.driver.get(URL)
        assert self.driver.title == "Calculator"

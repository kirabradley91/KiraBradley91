import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

expected_title = 'Wikipedia'
base_url = 'https://www.wikipedia.org'
title2 = 'World War II - Wikipedia'


@pytest.fixture()
def env_setup():
    global driver
    global baseUrl
    # we will use Google Chrome in this test. Specify the location of your chromedriver.exe
    driver = webdriver.Chrome("C:\\Users\\Kira\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # maximize browser window to full screen
    driver.maximize_window()
    # wait for 10 seconds till the web page will load
    driver.implicitly_wait(10)
    yield
    # when test is done, close ALL windows of the browser
    driver.quit()

def test_title(env_setup):
    driver.get(base_url)
    assert driver.title == expected_title
    driver.find_element_by_id('js-link-box-en').click()
    WebDriverWait(driver, 10).until(expected_conditions.title_contains('Wikipedia, the free encyclopedia'))
    driver.back()
    driver.find_element_by_id('searchInput').send_keys('World war 2')
    driver.find_element_by_xpath("//button[@class='pure-button pure-button-primary-progressive']").click()
    assert driver.title == title2
    driver.find_element_by_id('n-contents').click()
    driver.find_element_by_id('n-featuredcontent').click()
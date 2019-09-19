import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


expected_title = 'Google'
base_url = 'https://www.google.com/'
search_title = 'kingsford recipes - Google Search'
page_title = 'Kingsford® | Learn everything about grilling with Kingsford Charcoal, get premium BBQ culture from the long trusted brand.'


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
    # driver.quit()

def test_title(env_setup):
    driver.get(base_url)
    assert driver.title == expected_title
    search_field = driver.find_element_by_name('q')
    search_field.send_keys('kingsford recipes')
    search_field.send_keys(Keys.ENTER)
    driver.find_element_by_class_name('sA5rQ').click()
    assert driver.title == page_title
    driver.find_element_by_id('nav-open-btn').click()
    driver.find_element_by_partial_link_text("https://www.kingsford.com/country/").click()
    driver.find_element_by_class_name('btn-outline white').send_keys(Keys.ENTER)
    blah blah blah





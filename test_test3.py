import pytest
from selenium import webdriver

expected_title = 'Facebook - Log In or Sign Up'
base_url = 'https://www.facebook.com/'



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

def test_search(env_setup):
    driver.get(base_url)
    assert driver.title == expected_title
    driver.find_element_by_id('email').send_keys("kira-kiseleva@mail.ru")
    driver.find_element_by_id('pass').send_keys("Kiss19Kira91")
    driver.find_element_by_id("u_0_2").click()
    driver.find_element_by_xpath('//*[@id="u_a_2"]/input[2]').send_keys("yuriy kolomiytsev")
    driver.find_element_by_xpath('//*[@id="js_1g"]/form/button/i').click()

import pytest
from selenium import webdriver

expected_title = 'HomePro, Inc'
base_url = 'https://homepro.herokuapp.com/'
search_title = 'HomePro, Inc'


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
    driver.get('https://homepro.herokuapp.com/quote.php')
    assert driver.title == search_title
    driver.find_element_by_name('first_name').send_keys('first_name')
    driver.find_element_by_name('email').send_keys('blah@gmail.com')
    driver.find_element_by_name('phone').send_keys('123456')
    driver.find_element_by_name('comments').send_keys('remodeling')
    checkbox = driver.find_element_by_name('subscription').is_selected()
    if checkbox is False:
        driver.find_element_by_name('subscription').click()
    assert checkbox == True
    driver.find_element_by_xpath('//tr[6]//td[1]//input[1]').click()

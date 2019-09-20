import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# expected_title = 'Demo Table for practicing Selenium Automation'
base_url = 'http://52.41.129.106/andrewd/homePro_v2/index.php'
expected_error = "Homepro System" + "____________________________________________________"+ "You did not enter a value in Name.  This is a Mandatory field.  Please enter it now."


@pytest.fixture()
def env_setup():
    global driver
    global baseUrl
    # we will use Google Chrome in this test. Specify the location of your chromedriver.exe
    driver = webdriver.Chrome("/Users/yuriyfromrussia/Downloads/chromedriver_77")
    # wait for 10 seconds till the web page will load
    driver.implicitly_wait(10)
    # maximize browser window to full screen
    driver.maximize_window()
    yield
    # when test is done, close ALL windows of the browser
    # driver.quit()


def test_title(env_setup):
    # navigate to Amazon.com home page
    driver.get(base_url)
    # verify that website title is Amazon.com
    # assert expected_title == driver.title

    driver.get("http://52.41.129.106/andrewd/homePro_v2/quote.php")

    driver.find_element_by_name("first_name").send_keys("first_name")
    driver.find_element_by_name("phone").send_keys("232425353")


    driver.find_element_by_xpath("//input[@value='Send']").click()

    # success_message = driver.find_element_by_xpath("//div[@id='contact']")
    #
    # print(success_message.text)

    success_message = driver.find_element_by_xpath("//div[contains(text(), 'Thank you!')]")

    print(success_message.text)
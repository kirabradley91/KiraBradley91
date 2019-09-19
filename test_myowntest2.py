import pytest
from selenium import webdriver

expected_title = 'TripAdvisor: Read Reviews, Compare Prices & Book'
base_url = 'https://www.tripadvisor.com/'
search_title = 'Search results: Cancun, Mexico - TripAdvisor'


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
    driver.find_element_by_xpath("//*[@id='component_10']/div/div/div/div/div/div[2]/div[5]/div").send_keys("Cancun, Mexico")
    ("//a[@id='native_dropdown_selected_size_name_8']")
    driver.find_element_by_id("MAIN_SEARCH_CONTAINER").click()
    assert driver.title == search_title
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

expected_title = 'The Internet'
base_url = 'http://the-internet.herokuapp.com/tables'


@pytest.fixture()
def env_setup():
    global driver
    global baseUrl
    driver = webdriver.Chrome("C:\\Users\\Kira\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_title(env_setup):
    driver.get(base_url)
    assert driver.title == expected_title

    table = driver.find_element_by_id('table1')
    rows = table.find_elements(By.TAG_NAME, "tr")
    all_cells = table.find_elements(By.TAG_NAME, "td")
    for row in rows:
        print(row.text)

    table2 = driver.find_element_by_id('table2')
    rows2 = table2.find_elements(By.TAG_NAME, "tr")
    all_cells2 = table2.find_elements(By.TAG_NAME, "td")
    for row in rows2:
        print(row.text)


    assert rows[0] == rows2[0]
    assert rows[1] == rows2[1]
    assert rows[2] == rows2[2]
    assert rows[3] == rows2[3]
    assert rows[4] == rows2[4]

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

expected_title = 'DataTables | Table plug-in for jQuery'
base_url = 'https://datatables.net/'


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
    table = driver.find_element_by_id('example')
    rows = table.find_elements_by_tag_name('tr')
    cells = table.find_elements_by_tag_name('td')
    for row in rows:
        print(row.text)
    for cell in cells:
        print(cell.text)
    print(cells[5].text)
    # assert 'Charde Marshall' == cells[5].text
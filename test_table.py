import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

expected_title = 'Demo Table for practicing Selenium Automation'
base_url = 'https://www.toolsqa.com/automation-practice-table/'


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
    driver.quit()


def test_title(env_setup):
    # navigate to Amazon.com home page
    driver.get(base_url)
    # verify that website title is Amazon.com
    assert expected_title == driver.title

    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element_by_id('content'))
    actions.perform()

    table = driver.find_element_by_xpath("//table[@class='tsc_table_s13']/tbody")

    rows = table.find_elements(By.TAG_NAME, "tr")

    all_cells = table.find_elements(By.TAG_NAME, "td")

    print(all_cells[13].text)

    # for row in rows:
    #     print(row.text)

    # print(rows[0].text)

    row_2 = driver.find_element_by_xpath("//table[@class='tsc_table_s13']/tbody/tr[3]")

    cells = row_2.find_elements(By.TAG_NAME, "td")

    # print(cells[0].text)

    assert "Taiwan" == cells[0].text
    assert "Taipei" == cells[1].text
    assert "509m" == cells[2].text
    assert "2004" == cells[3].text
    assert "3" == cells[4].text

    # for row in rows:
    #     print(row.text)

    # print(rows[2].text)
    #
    # print(cell[10].text)

    # cell_data = rows[1].find_elements(By.TAG_NAME, "td")


    #
    # for cell in cell_data:
    #     print(cell.text)
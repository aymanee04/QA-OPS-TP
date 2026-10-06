from selenium import webdriver

def test_open_browser(driver):
    driver.get("https://formy-project.herokuapp.com/")

    assert "Formy" in driver.title
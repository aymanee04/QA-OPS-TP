from selenium import webdriver

def test_open_browser():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    print(driver.title)
    assert "Formy" in driver.title
    
    driver.quit()
from pages.formy_page import FormyPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def test_formy_homepage(driver):
    page = FormyPage(driver)

    page.open_page()

    assert "Formy" in driver.title


def test_fill_form(driver):
    page = FormyPage(driver)

    page.open_form()

    page.enter_first_name("Aymane")
    page.enter_last_name("Jemmaa")
    page.enter_job_title("Full Stack Developer")

    assert driver.find_element(
        *page.FIRST_NAME
    ).get_attribute("value") == "Aymane"

    assert driver.find_element(
        *page.LAST_NAME
    ).get_attribute("value") == "Jemmaa"

    assert driver.find_element(
        *page.JOB_TITLE
    ).get_attribute("value") == "Full Stack Developer"


def test_radio_button(driver):
    page = FormyPage(driver)

    page.open_radio()
    page.select_radio()

    assert driver.find_element(
        *page.RADIO_BUTTON_1
    ).is_selected()


def test_dropdown(driver):
    page = FormyPage(driver)

    page.open_dropdown()
    page.select_dropdown("0-1")

    selected = Select(
        driver.find_element(*page.SELECT_MENU)
    ).first_selected_option

    assert selected.text == "0-1"

def test_alert(driver):
    page = FormyPage(driver)

    page.open_alert()
    page.trigger_alert()

    alert = driver.switch_to.alert

    assert "Hello! I am an alert box!" in alert.text

    alert.accept()


def test_iframe(driver):
    page = FormyPage(driver)

    page.open_iframe()

    iframe = driver.find_element(*page.IFRAME)
    driver.switch_to.frame(iframe)

    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("Aymane Jemmaa")

    assert name_input.get_attribute("value") == "Aymane Jemmaa"

    driver.switch_to.default_content()
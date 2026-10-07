import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.formy_page import FormyPage


@allure.epic("QAOps - UI Testing")
@allure.feature("Formy UI Tests")
class TestFormy:

    @allure.story("Homepage")
    @allure.title("Verify Formy homepage loads successfully")
    @allure.description(
        "Verify that the Formy homepage is accessible and "
        "the page title contains 'Formy'."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_formy_homepage(self, driver):

        page = FormyPage(driver)

        with allure.step("Open Formy homepage"):
            page.open_page()

        with allure.step("Verify page title"):
            assert "Formy" in driver.title


    @allure.story("Complete Web Form")
    @allure.title("Verify user can fill the complete web form")
    @allure.description(
        "Verify that first name, last name and job title "
        "can be entered successfully."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_form(self, driver):

        page = FormyPage(driver)

        with allure.step("Open complete web form"):
            page.open_form()

        with allure.step("Enter first name"):
            page.enter_first_name("Aymane")

        with allure.step("Enter last name"):
            page.enter_last_name("Jemmaa")

        with allure.step("Enter job title"):
            page.enter_job_title("Full Stack Developer")

        with allure.step("Verify first name"):
            assert driver.find_element(
                *page.FIRST_NAME
            ).get_attribute("value") == "Aymane"

        with allure.step("Verify last name"):
            assert driver.find_element(
                *page.LAST_NAME
            ).get_attribute("value") == "Jemmaa"

        with allure.step("Verify job title"):
            assert driver.find_element(
                *page.JOB_TITLE
            ).get_attribute("value") == "Full Stack Developer"


    @allure.story("Radio Button")
    @allure.title("Verify radio button selection")
    @allure.description(
        "Verify that the first radio button can be selected."
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_radio_button(self, driver):

        page = FormyPage(driver)

        with allure.step("Open radio button page"):
            page.open_radio()

        with allure.step("Select first radio button"):
            page.select_radio()

        with allure.step("Verify radio button is selected"):
            assert driver.find_element(
                *page.RADIO_BUTTON_1
            ).is_selected()


    @allure.story("Dropdown")
    @allure.title("Verify dropdown selection")
    @allure.description(
        "Verify that an option can be selected from the dropdown."
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_dropdown(self, driver):

        page = FormyPage(driver)

        with allure.step("Open dropdown page"):
            page.open_dropdown()

        with allure.step("Select 0-1 from dropdown"):
            page.select_dropdown("0-1")

        with allure.step("Verify selected option"):
            selected = Select(
                driver.find_element(*page.SELECT_MENU)
            ).first_selected_option

            assert selected.text == "0-1"


    @allure.story("JavaScript Alert")
    @allure.title("Verify JavaScript alert can be handled")
    @allure.description(
        "Verify Selenium can detect and accept a JavaScript alert."
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_javascript_alert(self, driver):

        page = FormyPage(driver)

        with allure.step("Open Formy homepage"):
            page.open_page()

        with allure.step("Create JavaScript alert"):
            driver.execute_script(
                "window.alert('QAOps Test Alert');"
            )

        with allure.step("Wait for alert"):
            alert = WebDriverWait(driver, 10).until(
                EC.alert_is_present()
            )

        with allure.step("Verify alert message"):
            assert alert.text == "QAOps Test Alert"

        with allure.step("Accept alert"):
            alert.accept()

        with allure.step("Verify alert is closed"):
            WebDriverWait(driver, 10).until_not(
                EC.alert_is_present()
            )
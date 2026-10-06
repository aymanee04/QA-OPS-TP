from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class FormyPage(BasePage):

    BASE_URL = "https://formy-project.herokuapp.com"

    # Pages
    HOME_URL = f"{BASE_URL}/"
    FORM_URL = f"{BASE_URL}/form"
    RADIO_URL = f"{BASE_URL}/radiobutton"

    # Form
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, "job-title")

    # Radio
    RADIO_BUTTON_1 = (By.ID, "radio-button-1")

    # Dropdown
    SELECT_MENU = (By.ID, "select-menu")

    def open_page(self):
        self.open(self.HOME_URL)

    def open_form(self):
        self.open(self.FORM_URL)

    def open_radio(self):
        self.open(self.RADIO_URL)

    def open_dropdown(self):
        self.open(self.FORM_URL)

    def enter_first_name(self, value):
        self.write(self.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.write(self.LAST_NAME, value)

    def enter_job_title(self, value):
        self.write(self.JOB_TITLE, value)

    def select_radio(self):
        self.click(self.RADIO_BUTTON_1)

    def select_dropdown(self, value):
        element = self.driver.find_element(*self.SELECT_MENU)
        Select(element).select_by_visible_text(value)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    title_label = (By.XPATH, "//span[@data-test='title']")
    first_name_txt = (By.ID, 'first-name')
    last_name_txt = (By.ID, 'last-name')
    postal_code_txt = (By.ID, 'postal-code')
    continue_btn = (By.ID, 'continue')

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path='checkout-step-one.html')

    def get_title(self):
        return self.get_text(locator=self.title_label)

    def fill_payment_details(self, first_name: str, last_name: str, postal_code: str):
        self.type_text(locator=self.first_name_txt, text=first_name)
        self.type_text(locator=self.last_name_txt, text=last_name)
        self.type_text(locator=self.postal_code_txt, text=postal_code)

    def go_to_next_step(self):
        self.click(locator=self.continue_btn)

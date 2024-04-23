from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.cart_page import BasePage


class CheckoutCompletePage(BasePage):
    title_label = (By.XPATH, "//span[@data-test='title']")
    complete_header_label = (By.XPATH, "//*[@data-test='complete-header']")
    complete_label = (By.XPATH, "//*[@data-test='complete-text']")
    back_btn = (By.ID, 'back-to-products')

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path='checkout-complete.html')

    def get_title(self):
        return self.get_text(locator=self.title_label)

    def get_complete_header_text(self):
        return self.get_text(locator=self.complete_header_label)

    def get_complete_label_text(self):
        return self.get_text(locator=self.complete_label)

    def back(self):
        self.click(locator=self.back_btn)

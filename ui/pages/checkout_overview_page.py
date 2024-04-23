from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    title_label = (By.XPATH, "//span[@data-test='title']")
    payment_info_label = (By.XPATH, "//div[@data-test='payment-info-value']")
    shipping_info_label = (By.XPATH, "//div[@data-test='shipping-info-value']")
    price_subtotal_label = (By.XPATH, "//div[@data-test='subtotal-label']")
    price_tax_label = (By.XPATH, "//div[@data-test='tax-label']")
    price_total_label = (By.XPATH, "//div[@data-test='total-label']")
    finish_btn = (By.ID, 'finish')

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path='checkout-step-two.html')

    def get_title(self):
        return self.get_text(locator=self.title_label)

    def get_payment_info(self):
        return self.get_text(locator=self.payment_info_label)

    def get_shipping_info(self):
        return self.get_text(locator=self.shipping_info_label)

    def get_price_subtotal(self):
        return self.get_text(locator=self.price_subtotal_label)

    def get_price_tax(self):
        return self.get_text(locator=self.price_tax_label)

    def get_price_total(self):
        return self.get_text(locator=self.price_total_label)

    def finish_payment(self):
        self.click(locator=self.finish_btn)

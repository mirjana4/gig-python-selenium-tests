from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage


class CartPage(BasePage):
    item_list = (By.XPATH, "//div[@data-test='inventory-item']")
    checkout_btn = (By.ID, 'checkout')

    qty_label = (By.XPATH, "//div[contains(text(), '{product_name}')]/ancestor::div[@data-test='inventory-item']"
                           "//div[@data-test='item-quantity']")
    price_label = (By.XPATH, "//div[contains(text(), '{product_name}')]/ancestor::div[@data-test='inventory-item']"
                             "//div[@data-test='inventory-item-price']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path='cart.html')

    def items_count(self):
        items = self.find_elements(locator=self.item_list)
        return len(items)

    def get_item_quantity(self, product_name: str):
        by, locator = self.qty_label
        locator = locator.format(product_name=product_name)
        qty: str = self.get_text(locator=(by, locator))
        return int(qty) if qty else 0

    def get_item_price(self, product_name: str):
        by, locator = self.price_label
        locator = locator.format(product_name=product_name)
        return self.get_text(locator=(by, locator))

    def go_to_next_step(self):
        self.click(locator=self.checkout_btn)

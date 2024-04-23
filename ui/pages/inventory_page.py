from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    item_list = (By.XPATH, "//div[@data-test='inventory-item']")
    add_to_cart_btn = (By.XPATH, "//div[contains(text(), '{product_name}')]/ancestor::div[@data-test='inventory-item']"
                                 "//button[starts-with(@data-test, 'add-to-cart')]")
    price_label = (By.XPATH, "//div[contains(text(), '{product_name}')]/ancestor::div[@data-test='inventory-item']"
                             "//div[@data-test='inventory-item-price']")
    cart_link = (By.XPATH, "//a[@data-test='shopping-cart-link']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path='inventory.html')

    def add_to_cart(self, product_name: str):
        by, locator = self.add_to_cart_btn
        locator = locator.format(product_name=product_name)
        self.click(locator=(by, locator))

    def items_count(self):
        items = self.find_elements(locator=self.item_list)
        return len(items)

    def get_item_price(self, product_name: str):
        by, locator = self.price_label
        locator = locator.format(product_name=product_name)
        return self.get_text(locator=(by, locator))

    def go_to_cart(self):
        self.click(locator=self.cart_link)

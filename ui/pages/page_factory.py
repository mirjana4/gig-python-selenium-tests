from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage
from ui.pages.checkout_overview_page import CheckoutOverviewPage
from ui.pages.checkout_complete_page import CheckoutCompletePage


class PageFactory:
    login_page: LoginPage
    inventory_page: InventoryPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    checkout_complete_page: CheckoutCompletePage
    checkout_overview_page: CheckoutOverviewPage

    def __init__(self, driver: WebDriver):
        self.login_page = LoginPage(driver=driver)
        self.inventory_page = InventoryPage(driver=driver)
        self.cart_page = CartPage(driver=driver)
        self.checkout_page = CheckoutPage(driver=driver)
        self.checkout_overview_page = CheckoutOverviewPage(driver=driver)
        self.checkout_complete_page = CheckoutCompletePage(driver=driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    username_txt = (By.ID, 'user-name')
    password_txt = (By.ID, 'password')
    login_btn = (By.ID, 'login-button')

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def login(self, username: str, password: str):
        self.type_text(locator=self.username_txt, text=username)
        self.type_text(locator=self.password_txt, text=password)
        self.click(locator=self.login_btn)


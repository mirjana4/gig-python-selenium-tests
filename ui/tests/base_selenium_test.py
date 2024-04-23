from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.page_factory import PageFactory


class BaseSeleniumTest(TestCase):
    driver: WebDriver
    pages: PageFactory

    def setUp(self) -> None:
        super().setUp()

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.pages = PageFactory(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

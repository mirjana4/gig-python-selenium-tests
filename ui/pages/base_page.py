from typing import List, Tuple

from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    _driver: WebDriver
    _wait: WebDriverWait

    _base_url: str
    _page_url: str

    def __init__(self, driver: WebDriver, url_path: str = None):
        self._driver = driver
        self._wait = WebDriverWait(driver, 5)

        self._base_url = 'https://www.saucedemo.com/'
        self._page_url = f'{self._base_url}{url_path}' if url_path else self._base_url

    def get_url(self):
        return self._page_url

    def open(self) -> None:
        if self._page_url:
            self._driver.get(url=self._page_url)

    def wait_for_element_visibility(self, locator: Tuple[str, str]):
        message: str = f'Element not visible: by={locator[0]}, locator={locator[1]}'
        self._wait.until(method=expected_conditions.visibility_of_element_located(locator), message=message)

    def wait_for_element_clickable(self, locator: Tuple[str, str]):
        message: str = f'Element not clickable: by={locator[0]}, locator={locator[1]}'
        self._wait.until(method=expected_conditions.element_to_be_clickable(locator), message=message)

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self._driver.find_element(*locator)

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        try:
            self.wait_for_element_visibility(locator)
            return self._driver.find_elements(*locator)
        except TimeoutException:
            return []

    def click(self, locator: Tuple[str, str]) -> None:
        self.wait_for_element_clickable(locator=locator)
        self.find_element(locator=locator).click()

    def type_text(self, locator: Tuple[str, str], text: str) -> None:
        self.wait_for_element_visibility(locator=locator)
        self.find_element(locator=locator).send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        self.wait_for_element_visibility(locator=locator)
        return self.find_element(locator=locator).text

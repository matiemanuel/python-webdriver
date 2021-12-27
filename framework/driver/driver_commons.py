from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.driver.driver import Driver


class DriverCommons:
    # Commons functionalities for WebDriver and WebElement objects

    DEFAULT_TIMEOUT = 60
    DEFAULT_IMPLICIT_TIMEOUT = 8

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.DEFAULT_IMPLICIT_TIMEOUT)
        self.wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT)

    # Commons functionalities
    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def type(self, element, text: str):
        if not self.__is_web_element(element):
            element = self.find_element(element)
        element.send_keys(text)

    def click(self, element):
        if not self.__is_web_element(element):
            element = self.find_element(element)
        element.click()

    def upload_file_on_input(self, input_element, filepath):
        if not self.__is_web_element(input_element):
            input_element = self.find_element(input_element)
        input_element.send_keys(filepath)

    # Wait functionalities
    def wait_for_element(self, locator: tuple):
        return self.wait.until(expected_conditions.presence_of_element_located(*locator))

    def wait_for_invisibility_of_element(self, locator: tuple):
        return self.wait.until(expected_conditions.invisibility_of_element(*locator))

    def wait_for_element_contain_text(self, locator: tuple, text):
        return self.wait.until(expected_conditions.text_to_be_present_in_element(*locator, text))

    def wait_for_element_to_be_clickable(self, locator: tuple):
        return self.wait.until(expected_conditions.element_to_be_clickable(*locator))

    def wait_for_url_contains(self, text: str):
        return self.wait.until(expected_conditions.url_contains(text))

    # WebDriver functionalities

    def navigate_to(self, url: str):
        self.__get_driver_instance().get(url)

    def get_tab_title(self):
        return self.__get_driver_instance().title

    def switch_to_tab(self, index: int):
        driver = self.__get_driver_instance()
        driver.switch_to.window(driver.window_handles[index])

    def refresh_page(self):
        self.__get_driver_instance().refresh()

    def delete_cookies(self):
        self.__get_driver_instance().delete_all_cookies()

    @staticmethod
    def __is_web_element(element):
        return type(element) is WebElement

    @staticmethod
    def __get_driver_instance():
        return Driver.get_driver_instance()

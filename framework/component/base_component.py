from selenium.webdriver.remote.webelement import WebElement

from framework.driver.driver_commons import DriverCommons


class BaseComponent(DriverCommons):

    def __init__(self, container: WebElement):
        super().__init__(container)

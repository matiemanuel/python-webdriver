from selenium import webdriver as selenium_web_driver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from framework.driver.driver import Driver


class BaseTest:
    driver = Driver()

    def setup(self):
        chrome_options = selenium_web_driver.ChromeOptions()
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument("--incognito")
        self.driver.set_driver_instance(Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options))

    def teardown(self):
        self.driver.get_driver_instance().close()

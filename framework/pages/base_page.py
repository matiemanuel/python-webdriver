from framework.driver.driver_commons import DriverCommons
from framework.driver.driver import Driver


class BasePage(DriverCommons):

    def __init__(self):
        super().__init__(Driver().get_driver_instance())

class Driver:
    DRIVER = None

    @classmethod
    def set_driver_instance(cls, driver):
        cls.DRIVER = driver

    @classmethod
    def get_driver_instance(cls):
        if cls.DRIVER is None:
            raise Exception("WebDriver instance is not instantiated")
        return cls.DRIVER

from selenium import webdriver


class GetDriver:
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls, url):
        if cls.driver is None:
            cls.driver = webdriver.Edge()
            cls.driver.maximize_window()
            cls.driver.get(url)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
        cls.driver = None


if __name__ == '__main__':
    GetDriver().get_driver()

    GetDriver().quit_driver()

    print(GetDriver().driver)

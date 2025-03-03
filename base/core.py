import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("http://zhjw.scu.edu.cn/login")

    # 查找元素方法
    def base_find_element(self, loc, timeout=10, poll=1):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(EC.element_to_be_clickable(loc))  # 在这里不再需要解包，而且必须要是clickable

    # 点击元素方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入元素方法
    def base_input(self, loc, value):
        self.base_find_element(loc).send_keys(value)

    # 获取元素文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./img/{}.png".format(time.strftime("%Y%m%d-%H%M%S")))

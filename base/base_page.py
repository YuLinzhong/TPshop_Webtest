import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, loc, timeout=10):
        ele = WebDriverWait(self.driver, timeout=timeout).until(
            EC.element_to_be_clickable(loc)
        )
        return ele

    # 输入
    def send_keys(self, loc, value):
        self.find_element(loc).send_keys(value)

    # 点击
    def click(self, loc):
        self.find_element(loc).click()

    # 获取文本内容
    def get_text(self, loc):
        return self.find_element(loc).text

    # 删除
    def clear(self, loc):
        self.find_element(loc).clear()

    # 截图
    def get_screenshot(self, reason):
        self.driver.get_screenshot_as_file("../image/{}-{}".format(time.strftime("%Y-%m-%d %H:%M:%S"), reason))

    # 元素是否存在
    def element_exist(self, loc):
        try:
            self.find_element(loc, 3)
            return True
        except:
            return False

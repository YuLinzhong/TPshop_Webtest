from base.base_page import BasePage
from .page_login_locators import *


class PageLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 打开登录页面
    def page_login_open(self):
        self.driver.get(URL)

    # 输入用户名
    def page_input_username(self, username):
        self.send_keys(USERNAME_INPUT, username)

    # 输入密码
    def page_input_password(self, password):
        self.send_keys(PASSWORD_INPUT, password)

    # 输入验证码
    def page_input_verifycode(self, verifycode):
        self.send_keys(VERIFYCODE_INPUT, verifycode)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.click(LOGIN_BUTTON)

    # 判断安全退出是否存在（判断是否登录成功）
    def page_check_login(self):
        return self.element_exist(HEADER_LOGOUT_BUTTON)

    # 判断登录按钮是否存在（判断是否退出成功）
    def page_check_logout(self):
        return self.element_exist(HEADER_LOGIN_BUTTON)

    # 获取登录错误的提示信息
    def page_login_failed_info(self):
        return self.get_text(LOGIN_ERROR_INFO)

    # 登陆失败后点击确认
    def page_login_failed_confirm(self):
        self.find_element(LOGIN_ERROR_CONFIRM)

    # 登录成功后点击退出登录
    def page_login_success_logout(self):
        self.click(HEADER_LOGOUT_BUTTON)

    # 封装登录操作
    def page_login(self, username, password, verifycode):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verifycode(verifycode)
        self.page_click_login_btn()

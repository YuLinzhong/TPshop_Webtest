import unittest

from parameterized import parameterized

from base.get_driver import GetDriver
from page.user.page_login import PageLogin
from page.user.page_login_locators import *
from tool.read_json import read_json


def get_data():
    login_case = []
    for i in read_json(LOGIN_CASE).values():
        login_case.append((i["username"], i["password"], i["verifycode"], i["msg"]))
    return login_case


class TestLogin(unittest.TestCase):
    login = None

    @classmethod
    def setUpClass(cls):
        cls.login = PageLogin(GetDriver().get_driver(URL))

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, password, verifycode, msg):
        self.login.page_login_open()
        self.login.page_login(username, password, verifycode)
        # 正向测试
        if msg == "success!":
            try:
                # 判断登录是否成功
                self.assertEqual(self.login.page_check_login(), True)
            except AssertionError:
                self.login.get_screenshot("login failed")
                raise
            try:
                self.login.page_login_success_logout()
                # 判断退出是否成功
                self.assertEqual(self.login.page_check_logout(), True)
            except AssertionError:
                self.login.get_screenshot("logout failed")
                raise
        # 逆向测试
        else:
            try:
                self.assertEqual(self.login.page_login_failed_info(), msg)
            except AssertionError:
                self.login.get_screenshot("info error")
                raise
            self.login.page_login_failed_confirm()

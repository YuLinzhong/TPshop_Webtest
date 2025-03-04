from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "username")
PASSWORD_INPUT = (By.ID, "password")
VERIFYCODE_INPUT = (By.ID, "verify_code")
LOGIN_BUTTON = (By.CLASS_NAME, "J-login-submit")
HEADER_LOGOUT_BUTTON = (By.PARTIAL_LINK_TEXT, "安全退出")
HEADER_LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, "登录")
LOGIN_ERROR_INFO = (By.CSS_SELECTOR, ".layui-layer-content.layui-layer-padding")
LOGIN_ERROR_CONFIRM = (By.CSS_SELECTOR, ".layui-layer-btn0")
URL = "https://hmshop-test.itheima.net/Home/user/login.html"
LOGIN_CASE = "../data/login.json"

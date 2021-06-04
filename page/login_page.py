"""
登录页面
"""
from time import sleep
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class LoginPage(BasePage):
    """定位页面所有元素"""

    def __init__(self):
        super().__init__()  # 获取基类浏览器对象

        self.back = (By.CLASS_NAME, "pt-fanhui")
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_button = (By.CLASS_NAME, "login-btn")


class LoginHandle(BasePage):
    """所有元素对应的操作方法"""

    def __init__(self):
        super().__init__()
        self.login_page = LoginPage()  # 获取元素定位对象

    def chick_back_button(self):  # 点击切换登录方式方法
        self.click_button('切换登录方式', self.login_page.back)

    def input_username(self, username):  # 输入用户名方法
        self.input_text('用户名框', self.login_page.username, username)

    def input_password(self, password):  # 输入密码方法
        self.input_text("密码框", self.login_page.password, password)

    def click_login_button(self):  # 点击登录方法
        self.click_button("登录按钮", self.login_page.login_button)


class LoginMission(object):
    """登录业务"""

    def __init__(self):
        self.login_mission = LoginHandle()  # 获取对象

    def login_func(self, username, password):
        try:
            self.login_mission.chick_back_button()  # 切换登录方式
        except:
            pass
        self.login_mission.input_username(username)  # 输入用户名
        self.login_mission.input_password(password)  # 输入密码
        self.login_mission.click_login_button()  # 点击登录


if __name__ == '__main__':
    LoginMission().login_func('350203196505264042', '1')
    sleep(20)

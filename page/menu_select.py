"""
菜单栏页面
"""

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from page.login_page import LoginMission


class MenuPage(BasePage):
    """定位菜单元素"""

    def __init__(self):
        super().__init__()  # 获取基类浏览器对象

        # self.menu = (By.XPATH, f"//li[@text={menu}]")

    def menu(self, menu):
        menu = (By.XPATH, f"//li[@text={menu}]")
        return menu


class MenuHandle(BasePage):
    """点击菜单"""

    def __init__(self):
        super().__init__()
        self.login_page = MenuPage()  # 获取元素定位对象

    def chick_menu_func(self, menu):  # 点击菜单方法
        self.click_button(menu, self.login_page.menu(menu))


class MenuMission(object):
    """点击菜单进入各个业务"""

    def __init__(self):
        self.menu_mission = MenuHandle()

    def click_zhzh_whlr_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户维护'")

    def click_zhzh_whsh_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户审核'")

    def click_zhzh_whsh_szs_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户审核(省终审)'")

    def click_zhzh_whba_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户备案'")

    def click_zhzh_zxlr_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户注销录入'")

    def click_zhzh_zxsh_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户注销审核'")

    def click_zhzh_zxba_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户注销备案'")

    def click_zhzh_yhlr_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户移户录入'")

    def click_zhzh_yhsh_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户移户审核'")

    def click_zhzh_yhba_menu(self):
        self.menu_mission.chick_menu_func("'财政专户管理'")
        self.menu_mission.chick_menu_func("'专户账户移户备案'")


if __name__ == '__main__':
    LoginMission().login_func('350203196505264042', '1')
    MenuMission().click_zhzh_whlr_menu()
    MenuMission().click_zhzh_yhlr_menu()
    MenuMission().click_zhzh_zxlr_menu()

"""
专户账户审核页面
"""
from time import sleep
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from page.login_page import LoginMission
from page.menu_select import MenuMission


class ZhZhShPage(BasePage):
    """定位元素"""

    def __init__(self):
        super().__init__()

        self.iframe = (By.XPATH, '//body/div[1]/div[2]/div[1]/div[2]/iframe[1]')

        """未审核页签"""
        self.wsh = (By.XPATH, "//a[contains(text(),'未审核')]")
        self.wsh_tg = (By.XPATH, "//tbody/tr/td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='通过'][1]")
        self.wsh_th = (By.XPATH, "//tbody/tr/td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='退回'][1]")
        self.wsh_plcz_select = (By.XPATH, "//tbody/tr/td/span[@title='{}'][1]/../preceding-sibling::td[3]/input")
        self.wsh_pltg = (By.XPATH, "//button[contains(text(),'批量通过')]")
        self.wsh_plth = (By.XPATH, "//button[contains(text(),'批量退回')]")
        self.wsh_tgyj = (By.XPATH, "//div[@class='layui-layer-content']/textarea")

        self.wsh_alert_qd = (By.XPATH, "//a[contains(text(),'确定')]")  # 弹窗确定
        self.wsh_alert_qx = (By.XPATH, "//a[contains(text(),'取消')]")  # 弹窗取消
        self.wsh_tgyj_qd = (By.XPATH, "//div[contains(text(),'信息')]/following-sibling::div[2]/a")  # 输入通过意见点击确定后的弹窗确定

        """已审核页签"""
        self.ysh = (By.XPATH, "//a[contains(text(),'已审核')]")
        self.ysh_cx = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='撤销送审'][1]")
        self.ysh_zz = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='追踪'][1]")


class ZhZhShHandle(BasePage):
    """操作方法"""

    def __init__(self):
        super().__init__()
        self.zhzhsh_page = ZhZhShPage()

    def enter_iframe(self):
        self.switch_to('首层frame', self.zhzhsh_page.iframe)

    def click_alert_qd(self):
        self.click_button('弹窗确定按钮', self.zhzhsh_page.wsh_alert_qd)

    def click_alert_qx(self):
        self.click_button('弹窗取消按钮', self.zhzhsh_page.wsh_alert_qx)

    def click_tgyj_qd(self):
        sleep(2)
        self.click_button('通过意见弹窗确定按钮', self.zhzhsh_page.wsh_tgyj_qd)

    """未审核页面"""

    def click_wsh(self):
        self.click_button('未审核页签', self.zhzhsh_page.wsh)

    def click_wsh_tg(self, name):
        self.click_button(f'{name}所在数据的审核通过按钮', (self.zhzhsh_page.wsh_tg[0], self.zhzhsh_page.wsh_tg[1].format(name)))

    def click_wsh_th(self, name):
        self.click_button(f'{name}所在数据的退回按钮', (self.zhzhsh_page.wsh_th[0], self.zhzhsh_page.wsh_th[1].format(name)))

    def click_wsh_pltg(self):
        self.click_button('批量通过按钮', self.zhzhsh_page.wsh_pltg)

    def click_wsh_plth(self):
        self.click_button('批量退回按钮', self.zhzhsh_page.wsh_plth)

    def input_tgyj(self):
        self.input_text('通过意见', self.zhzhsh_page.wsh_tgyj, '自动化测试通过意见')

    """已审核页面"""

    def click_ysh(self):
        self.click_button('已审核页签', self.zhzhsh_page.ysh)

    def click_ysh_cx(self, name):
        self.click_button(f'{name}所在数据的撤销按钮', (self.zhzhsh_page.ysh_cx[0], self.zhzhsh_page.ysh_cx[1].format(name)))

    def click_ysh_zz(self, name):
        self.click_button(f'{name}所在数据的追踪按钮', (self.zhzhsh_page.ysh_zz[0], self.zhzhsh_page.ysh_zz[1].format(name)))


class ZhZhShMission(object):
    """审核岗操作"""

    def __init__(self):
        self.zhzhsh_mission = ZhZhShHandle()

    def zhzhwsh_tg_func(self, name):  # 通过
        self.zhzhsh_mission.enter_iframe()
        self.zhzhsh_mission.click_wsh_tg(name)
        self.zhzhsh_mission.input_tgyj()
        self.zhzhsh_mission.click_alert_qd()
        sleep(1)
        self.zhzhsh_mission.click_tgyj_qd()
        self.zhzhsh_mission.click_ysh()
        self.zhzhsh_mission.switch_out()

    def zhzhwsh_pltg_func(self):  # 批量通过
        self.zhzhsh_mission.enter_iframe()
        self.zhzhsh_mission.click_wsh_pltg()
        self.zhzhsh_mission.switch_out()

    def zhzhwsh_th_func(self, name):  # 退回
        self.zhzhsh_mission.enter_iframe()
        self.zhzhsh_mission.click_wsh_th(name)
        self.zhzhsh_mission.switch_out()

    def zhzhwsh_plth_func(self):  # 批量退回
        self.zhzhsh_mission.enter_iframe()
        self.zhzhsh_mission.click_wsh_plth()
        self.zhzhsh_mission.switch_out()

    def zhzhysh_cx_func(self, name):  # 已审核撤销
        self.zhzhsh_mission.enter_iframe()
        self.zhzhsh_mission.click_ysh()
        self.zhzhsh_mission.click_ysh_cx(name)
        self.zhzhsh_mission.click_alert_qd()
        self.zhzhsh_mission.click_alert_qd()
        self.zhzhsh_mission.switch_out()

    def zhzhysh_zz_func(self, name):  # 已审核追踪
        self.zhzhsh_mission.enter_iframe()
        self.zhzhsh_mission.click_ysh()
        self.zhzhsh_mission.click_ysh_zz(name)
        self.zhzhsh_mission.switch_out()


if __name__ == '__main__':
    LoginMission().login_func('430528198611270043', '1')
    MenuMission().click_zhzh_whsh_menu()
    ZhZhShMission().zhzhwsh_tg_func('于宏健自动化测试')
    ZhZhShMission().zhzhysh_cx_func('于宏健自动化测试')

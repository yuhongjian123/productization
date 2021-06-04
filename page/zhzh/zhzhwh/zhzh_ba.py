"""
专户账户备案页面
"""
from time import sleep
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from page.login_page import LoginMission
from page.menu_select import MenuMission


class ZhZhBaPage(BasePage):

    def __init__(self):
        super().__init__()
        self.iframe = (By.XPATH, '//body/div[1]/div[2]/div[1]/div[2]/iframe[1]')

        """未备案"""
        self.wba = (By.XPATH, "//a[contains(text(),'未备案')]")
        self.wba_ba = (By.XPATH, "//tbody/tr/td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='备案'][1]")

        self.baxq_alert_qd = (By.XPATH, "//a[contains(text(),'确定')]")  # 弹窗确定
        self.baxq_alert_qx = (By.XPATH, "//a[contains(text(),'取消')]")  # 弹窗取消
        self.baxq_iframe = (By.XPATH, "//iframe[@allowtransparency='true']")
        self.baxq_qr = (By.XPATH, "//button[contains(text(),'确 认')]")
        self.baxq_qx = (By.XPATH, "//button[contains(text(),'取 消')]")
        self.baxq_khxkzhzh = (By.ID, '111014')
        self.baxq_zh = (By.ID, '111017')
        self.baxq_khyh = (By.XPATH, "//span[contains(text(), '开户银行:')]/following-sibling::span[1]/span/input")
        self.baxq_khyh_select = (By.XPATH, "//span[contains(text(),'{}')]")
        self.baxq_czzhzhdm = (By.XPATH, "//input[@id='111024']")

        """已备案"""
        self.yba = (By.XPATH, "//a[contains(text(),'已备案')]")
        self.yba_name = (By.XPATH, "//td/span[@title='{}']")


class ZhZhBaHandle(BasePage):

    def __init__(self):
        super().__init__()
        self.zhzhba_page = ZhZhBaPage()

    def enter_iframe(self):
        self.switch_to('首层frame', self.zhzhba_page.iframe)

    """未备案页面"""

    def click_wba(self):
        sleep(1)
        self.click_button('未备案页签', self.zhzhba_page.wba)

    def click_wba_ba(self, name):
        sleep(1)
        self.click_button(f'{name}所在数据的备案按钮', (self.zhzhba_page.wba_ba[0], self.zhzhba_page.wba_ba[1].format(name)))

    def enter_baxq_iframe(self):
        self.switch_to('备案详情页frame', self.zhzhba_page.baxq_iframe)

    def click_baxq_qr(self):
        self.click_button('备案详情页确认按钮', self.zhzhba_page.baxq_qr)

    def click_baxq_qx(self):
        self.click_button('备案详情页取消按钮', self.zhzhba_page.baxq_qx)

    def input_khxkzhzh(self, khxkzhzh):
        self.input_text('开户许可证核准号', self.zhzhba_page.baxq_khxkzhzh, khxkzhzh)

    def input_baxq_zh(self, account):
        self.input_text('帐号', self.zhzhba_page.baxq_zh, account)

    def click_baxq_khyh(self):
        self.click_button('开户银行', self.zhzhba_page.baxq_khyh)

    def click_baxq_khyh_select(self, khyh):
        self.click_button('开户银行选择',
                          (self.zhzhba_page.baxq_khyh_select[0], self.zhzhba_page.baxq_khyh_select[1].format(khyh)))

    def input_baxq_czzhzhdm(self, czzhzhdm):
        self.input_text('财政专户账户代码', self.zhzhba_page.baxq_czzhzhdm, czzhzhdm)

    def click_baxq_alert_qd(self):
        sleep(1)
        self.click_button('弹窗确定按钮', self.zhzhba_page.baxq_alert_qd)

    def click_baxq_alert_qx(self):
        sleep(1)
        self.click_button('弹窗取消按钮', self.zhzhba_page.baxq_alert_qx)

    """已备案页面"""

    def click_yba(self):
        self.click_button('已备案页签', self.zhzhba_page.yba)

    def click_yba_name(self, name):
        self.click_button(f'{name}', (self.zhzhba_page.yba_name[0], self.zhzhba_page.yba_name[1].format(name)))


class ZhZhBaMission(object):

    def __init__(self):
        self.zhzhba_mission = ZhZhBaHandle()

    def zhzh_ba_func(self, name, khxkzhzh, account, khyh, czzhzhdm):  # 备案操作
        self.zhzhba_mission.enter_iframe()
        self.zhzhba_mission.click_wba_ba(name)
        self.zhzhba_mission.enter_baxq_iframe()
        self.zhzhba_mission.input_khxkzhzh(khxkzhzh)
        self.zhzhba_mission.input_baxq_zh(account)
        self.zhzhba_mission.click_baxq_khyh()
        self.zhzhba_mission.click_baxq_khyh_select(khyh)
        self.zhzhba_mission.input_baxq_czzhzhdm(czzhzhdm)
        self.zhzhba_mission.click_baxq_qr()
        self.zhzhba_mission.click_baxq_alert_qd()
        self.zhzhba_mission.switch_out()
        self.zhzhba_mission.switch_out()

    def zhzh_ba_yba(self, name):
        self.zhzhba_mission.enter_iframe()
        self.zhzhba_mission.click_yba_name(name)


if __name__ == '__main__':
    LoginMission().login_func('350203196505264042', '1')
    MenuMission().click_zhzh_whba_menu()
    ZhZhBaMission().zhzh_ba_func('yhj测试专户账户050701', '123', '111', "1030602 中国农业银行桂林建干路支行", '123')

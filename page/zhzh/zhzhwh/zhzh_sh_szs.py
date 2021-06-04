"""
专户账户审核-省终审页面
"""
from time import sleep
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from page.login_page import LoginMission
from page.menu_select import MenuMission


class ZhZhShSzsPage(BasePage):
    """定位元素"""

    def __init__(self):
        super().__init__()

        self.iframe = (By.XPATH, '//body/div[1]/div[2]/div[1]/div[2]/iframe[1]')

        """未审核页签"""
        self.wsh = (By.XPATH, "//a[contains(text(),'未审核')]")
        self.wsh_tg = (By.XPATH, "//tbody/tr/td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='通过'][1]")
        self.wsh_th = (By.XPATH, "//tbody/tr/td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='退回'][1]")
        self.wsh_alert_qd = (By.XPATH, "//a[contains(text(),'确定')]")  # 弹窗确定
        self.wsh_alert_qx = (By.XPATH, "//a[contains(text(),'取消')]")  # 弹窗取消

        self.wsh_xq_iframe = (By.XPATH, "//iframe[@allowtransparency='true']")
        self.wsh_xq_tg = (By.XPATH, "//button[contains(text(),'通 过')]")
        self.wsh_xq_qx = (By.XPATH, "//button[contains(text(),'取 消')]")
        self.wsh_xq_khxkehzh = (By.ID, "111214")
        self.wsh_xq_spyj = (By.XPATH, "//textarea[@placeholder='请填写审批意见']")
        self.wsh_xq_spfjsc = (By.XPATH, "//span[@title='审批附件上传']/following-sibling::span[1]/div[1]/div[1]/button")
        self.wsh_xq_alert_qd = (By.XPATH, "//div[contains(text(),'信息')]/following-sibling::div[2]/a")

        """已审核页签"""
        self.ysh = (By.XPATH, "//td[contains(text(),'已审核')]")
        self.ysh_zz = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='追踪'][1]")


class ZhZhShSzsHandle(BasePage):
    """操作方法"""

    def __init__(self):
        super().__init__()
        self.zhzhshszs_page = ZhZhShSzsPage()

    def enter_iframe(self):
        self.switch_to('首层frame', self.zhzhshszs_page.iframe)

    def click_alert_qd(self):
        self.click_button('弹窗确定按钮', self.zhzhshszs_page.wsh_alert_qd)

    def click_alert_qx(self):
        self.click_button('弹窗取消按钮', self.zhzhshszs_page.wsh_alert_qx)

    """未审核页面"""

    def click_wsh(self):
        self.click_button('未审核页签', self.zhzhshszs_page.wsh)

    def click_wsh_tg(self, name):
        self.click_button(f'{name}所在数据的审核通过按钮',
                          (self.zhzhshszs_page.wsh_tg[0], self.zhzhshszs_page.wsh_tg[1].format(name)))

    def click_wsh_th(self, name):
        self.click_button(f'{name}所在数据的退回按钮',
                          (self.zhzhshszs_page.wsh_th[0], self.zhzhshszs_page.wsh_th[1].format(name)))

    def enter_xq_iframe(self):
        self.switch_to('详情页面frame', self.zhzhshszs_page.wsh_xq_iframe)

    def click_wsh_xq_tg(self):
        self.click_button('审核详情页面通过按钮', self.zhzhshszs_page.wsh_xq_tg)

    def click_wsh_xq_qx(self):
        self.click_button('审核详情页面取消按钮', self.zhzhshszs_page.wsh_xq_qx)

    def input_wsh_xq_khxkehzh(self):
        self.input_text('开户许可证核准号', self.zhzhshszs_page.wsh_xq_khxkehzh, '自动化流程测试')

    def input_spyj(self):
        self.input_text('审批意见', self.zhzhshszs_page.wsh_xq_spyj, '自动化测试通过意见')

    def click_wsh_xq_spfjsc(self):
        self.click_button('审批附件上传按钮', self.zhzhshszs_page.wsh_xq_spfjsc)

    def uplod_spfjsc(self, url):
        self.uplode(url)

    def click_wsh_xq_alert_qd(self):
        self.click_button('审核通过信息确定', self.zhzhshszs_page.wsh_xq_alert_qd)

    """已审核页面"""

    def click_ysh(self):
        self.click_button('已审核页签', self.zhzhshszs_page.ysh)

    def click_ysh_zz(self, name):
        self.click_button(f'{name}所在数据的追踪按钮',
                          (self.zhzhshszs_page.ysh_zz[0], self.zhzhshszs_page.ysh_zz[1].format(name)))


class ZhZhShSzsMission(object):
    """终审岗操作"""

    def __init__(self):
        self.zhzhshszs_mission = ZhZhShSzsHandle()

    def zhzhszswsh_tg_func(self, name, url):  # 通过
        self.zhzhshszs_mission.enter_iframe()
        self.zhzhshszs_mission.click_wsh_tg(name)
        self.zhzhshszs_mission.enter_xq_iframe()
        self.zhzhshszs_mission.input_spyj()
        self.zhzhshszs_mission.click_wsh_xq_spfjsc()
        self.zhzhshszs_mission.uplod_spfjsc(url)
        self.zhzhshszs_mission.click_wsh_xq_tg()
        self.zhzhshszs_mission.click_wsh_xq_alert_qd()
        self.zhzhshszs_mission.switch_out()
        self.zhzhshszs_mission.switch_out()

    def zhzhwshszs_th_func(self, name):  # 退回
        self.zhzhshszs_mission.enter_iframe()
        self.zhzhshszs_mission.click_wsh_th(name)
        self.zhzhshszs_mission.switch_out()

    def zhzhyshszs_zz_func(self, name):  # 已审核追踪
        self.zhzhshszs_mission.enter_iframe()
        self.zhzhshszs_mission.click_ysh()
        self.zhzhshszs_mission.click_ysh_zz(name)
        self.zhzhshszs_mission.switch_out()


if __name__ == '__main__':
    LoginMission().login_func('350583198909091018', '1')
    MenuMission().click_zhzh_whsh_szs_menu()
    ZhZhShSzsMission().zhzhszswsh_tg_func('于宏健自动化测试', r"C:\Users\于宏健\Desktop\测试.pdf")

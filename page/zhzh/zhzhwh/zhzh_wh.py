"""
专户账户维护页面
"""

from selenium.webdriver.common.by import By
from time import sleep
from common.base_page import BasePage
from page.login_page import LoginMission
from page.menu_select import MenuMission
from common.Driver_tool import DriverTool
from common.logger import Log


class ZhZhWhPage(BasePage):
    """定位元素"""

    def __init__(self):
        super().__init__()

        self.iframe = (By.XPATH, '//body/div[1]/div[2]/div[1]/div[2]/iframe[1]')

        """待送审页签"""
        self.dss = (By.XPATH, "//a[contains(text(),'待送审')]")  # 待送审页签
        self.dss_kh_button = (By.ID, 'add_acc')  # 开户按钮
        self.dss_name = (By.XPATH, "//td/span[@title='{}']")  # 账户名称超链接
        self.dss_ss = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='送 审'][1]")  # 送审按钮
        self.dss_sc = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='删除'][1]")  # 删除按钮
        self.dss_dy = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='打印预览'][1]")  # 打印按钮

        self.dss_alert_qd = (By.XPATH, "//a[contains(text(),'确定')]")  # 弹窗确定
        self.dss_alert_qx = (By.XPATH, "//a[contains(text(),'取消')]")  # 弹窗取消
        self.kh_alert_qd = (By.XPATH, "//div[contains(text(),'信息')]/following-sibling::div[2]/a")

        self.kh_iframe = (By.XPATH, "//iframe[@allowtransparency='true']")
        self.kh_save = (By.XPATH, "//button[contains(text(),'保 存')]")
        self.kh_qx = (By.XPATH, "//button[contains(text(),'取 消')]")
        self.kh_name = (By.XPATH, "//span[contains(text(), '账户名称:')]/following-sibling::span[1]/input")  # 账户姓名
        self.kh_czqh = (By.XPATH, "//span[contains(text(), '财政区划代码:')]/following-sibling::span[1]/span/input")  # 财政区划
        self.kh_czqh_select = (By.XPATH, "//span[contains(text(),'{}')]")  # 财政区划选择
        self.kh_zhlbdm = (
            By.XPATH, "//span[contains(text(), '账户类别代码:')]/following-sibling::span[1]/span/input")  # 账户类别代码
        self.kh_zhlbdm_select = (By.XPATH, "//span[contains(text(),'{}')]/preceding-sibling::span[1]")  # 账户类别代码选择
        self.kh_xz = (By.XPATH, "//span[contains(text(), '险种:')]/following-sibling::span[1]/span/input")  # 险种
        self.kh_xz_select = (By.XPATH, "//span[contains(text(),'{}')]")
        self.kh_hsnr = (By.ID, '110113')  # 核算内容
        self.kh_splxdm = (By.ID, '110120')  # 审批类型代码
        self.kh_splxdm_select = (By.XPATH, "//select[@id='110120']/option[@value='{}']")  # 1 核准类  2 备案类
        self.kh_khyh = (By.ID, '110107')  # 开户银行
        self.kh_khyh_select = (By.XPATH, "//option[contains(text(),'竞争性方式')]")  # 1 竞争性方式 2 集体决策方式 3 按照国家政策确定 9 其他
        self.kh_dwdm = (By.ID, '110119')  # 单位代码
        self.kh_khyj = (By.ID, '110114')  # 开户依据

        """已送审页签"""
        self.yss = (By.XPATH, "//a[contains(text(),'已送审')]")
        self.yss_name = (By.LINK_TEXT, '{}')  # 账户名称超链接
        self.yss_cx = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='撤销送审'][1]")
        self.yss_zz = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='追踪'][1]")
        self.yss_dy = (By.XPATH, "//td/span[@title='{}'][1]/../following-sibling::td[6]/a[@title='打印预览'][1]")
        self.yss_alert_qd = (By.XPATH, "//a[contains(text(),'确定')]")  # 弹窗确定
        self.yss_alert_qx = (By.XPATH, "//a[contains(text(),'取消')]")  # 弹窗取消

        """专户账户库页签"""
        self.zhk = (By.XPATH, "//a[contains(text(),'专户账户库')]")
        self.zhk_name = (By.LINK_TEXT, '{}')  # 账户名称超链接


class ZhZhWhHandle(BasePage):
    """封装操作方法"""

    def __init__(self):
        super().__init__()
        self.zhzhwh_page = ZhZhWhPage()

    def enter_iframe(self):
        self.switch_to('首层frame', self.zhzhwh_page.iframe)

    """待送审页面操作"""

    def click_dss(self):  # 点击待送审页签
        self.click_button('待送审页签', self.zhzhwh_page.dss)

    def click_dss_name(self, name):  # 点击对应名称的数据账户名称
        self.click_button(f'{name}', (self.zhzhwh_page.dss_name[0], self.zhzhwh_page.dss_name[1].format(name)))

    def click_dss_ss(self, name):  # 对应名称的数据点击送审
        self.click_button(f'{name}所在数据的送审按钮', (self.zhzhwh_page.dss_ss[0], self.zhzhwh_page.dss_ss[1].format(name)))

    def click_dss_sc(self, name):  # 对应名称的数据点击删除
        self.click_button(f'{name}所在数据的删除按钮', (self.zhzhwh_page.dss_sc[0], self.zhzhwh_page.dss_sc[1].format(name)))

    def click_dss_dy(self, name):  # 对应名称的数据点击打印
        self.click_button(f'{name}所在数据的打印按钮', (self.zhzhwh_page.dss_dy[0], self.zhzhwh_page.dss_dy[1].format(name)))

    def click_alert_qd(self):
        self.click_button('弹窗确定按钮', self.zhzhwh_page.dss_alert_qd)

    def click_alert_qx(self):
        self.click_button('弹窗取消按钮', self.zhzhwh_page.dss_alert_qx)

    """开户详情页"""

    def click_kh_button(self):
        self.click_button('开户详情按钮', self.zhzhwh_page.dss_kh_button)

    def enter_kh_iframe(self):
        self.switch_to('开户详情页面frame', self.zhzhwh_page.kh_iframe)

    def click_save(self):
        self.click_button('开户详情页保存按钮', self.zhzhwh_page.kh_save)

    def click_kh_qx(self):
        self.click_button('开户详情页取消按钮', self.zhzhwh_page.kh_qx)

    def click_kh_alert(self):
        sleep(2)
        self.click_button('录入保存后的提示框确定', self.zhzhwh_page.kh_alert_qd)

    def input_name(self, name):
        self.input_text('帐号名称', self.zhzhwh_page.kh_name, name)

    def select_czqh(self, czqhdm):
        self.click_button('财政区划代码', self.zhzhwh_page.kh_czqh)
        self.click_button('财政区划代码选择',
                          (self.zhzhwh_page.kh_czqh_select[0], self.zhzhwh_page.kh_czqh_select[1].format(czqhdm)))

    def select_zhlbdm(self, zhlbdm):
        self.click_button('账户类别代码', self.zhzhwh_page.kh_zhlbdm)
        self.click_button('账户类别代码',
                          (self.zhzhwh_page.kh_zhlbdm_select[0], self.zhzhwh_page.kh_zhlbdm_select[1].format(zhlbdm)))

    def select_xz(self, xz):
        self.click_button('险种', self.zhzhwh_page.kh_xz)
        self.click_button('险种', (self.zhzhwh_page.kh_xz_select[0], self.zhzhwh_page.kh_xz_select[1].format(xz)))

    def input_hsnr(self, hsnr):
        self.input_text('核算内容', self.zhzhwh_page.kh_hsnr, hsnr)

    def select_splxdm(self, splxdm):
        self.click_button('审批类型代码', self.zhzhwh_page.kh_splxdm)
        self.click_button('审批类型代码',
                          (self.zhzhwh_page.kh_splxdm_select[0], self.zhzhwh_page.kh_splxdm_select[1].format(splxdm)))

    def select_khyh(self, khyh):
        self.click_button('开户银行选择方式', self.zhzhwh_page.kh_khyh)
        self.click_button('开户银行选择方式',
                          (self.zhzhwh_page.kh_khyh_select[0], self.zhzhwh_page.kh_khyh_select[1].format(khyh)))

    def input_dwdm(self, dwdm):
        self.input_text('单位代码', self.zhzhwh_page.kh_dwdm, dwdm)

    def input_khyj(self, khyj):
        self.input_text('单位代码', self.zhzhwh_page.kh_khyj, khyj)

    """已送审页面操作"""

    def click_yss(self):
        self.click_button('已送审', self.zhzhwh_page.yss)

    def click_yss_cx(self, name):
        self.click_button(f'{name}所在数据的撤销按钮', (self.zhzhwh_page.yss_cx[0], self.zhzhwh_page.yss_cx[1].format(name)))

    def click_yss_zz(self, name):
        self.click_button(f'{name}所在数据的追踪按钮', (self.zhzhwh_page.yss_zz[0], self.zhzhwh_page.yss_zz[1].format(name)))

    def click_yss_dy(self, name):
        self.click_button(f'{name}所在数据的打印按钮', (self.zhzhwh_page.yss_dy[0], self.zhzhwh_page.yss_dy[1].format(name)))

    """专户账户库页面操作"""

    def click_zhk(self):
        self.click_button('专户账户库', self.zhzhwh_page.zhk)

    def click_zhk_name(self, name):
        self.click_button(f'{name}', (self.zhzhwh_page.zhk_name[0], self.zhzhwh_page.zhk_name[1].format(name)))


class ZhZhWhMission(object):
    """专户账户维护业务"""

    def __init__(self):
        self.zhzhwh_mission = ZhZhWhHandle()
        self.log = Log()

    """待送审页面"""

    def zhzh_kh_func(self, name, czqhdm, zhlbdm, xz, hsnr, splxdm, kuyh, dwdm, khyj):  # 开户录入流程
        self.zhzhwh_mission.enter_iframe()
        self.zhzhwh_mission.click_dss()
        self.zhzhwh_mission.click_kh_button()
        self.zhzhwh_mission.enter_kh_iframe()
        self.zhzhwh_mission.input_name(name)
        self.zhzhwh_mission.select_czqh(czqhdm)
        self.zhzhwh_mission.select_zhlbdm(zhlbdm)
        self.zhzhwh_mission.select_xz(xz)
        self.zhzhwh_mission.input_hsnr(hsnr)
        self.zhzhwh_mission.select_splxdm(splxdm)
        self.zhzhwh_mission.select_khyh(kuyh)
        self.zhzhwh_mission.input_dwdm(dwdm)
        self.zhzhwh_mission.input_khyj(khyj)
        self.zhzhwh_mission.click_save()
        self.zhzhwh_mission.click_kh_alert()
        self.zhzhwh_mission.switch_out()
        self.zhzhwh_mission.switch_out()

    def zhzhdss_ss_func(self, name):  # 送审操作
        self.zhzhwh_mission.enter_iframe()
        self.zhzhwh_mission.click_dss()
        sleep(2)
        self.zhzhwh_mission.click_dss_ss(name)
        self.zhzhwh_mission.click_alert_qd()
        self.zhzhwh_mission.switch_out()

    def zhzhdss_sc_func(self, name):  # 删除操作
        self.zhzhwh_mission.enter_iframe()
        self.zhzhwh_mission.click_dss()
        self.zhzhwh_mission.click_dss_sc(name)
        self.zhzhwh_mission.switch_out()

    """已送审页面"""

    def zhzhyss_cx_func(self, name):  # 撤销
        self.zhzhwh_mission.enter_iframe()
        self.zhzhwh_mission.click_yss()
        self.zhzhwh_mission.click_yss_cx(name)
        self.zhzhwh_mission.switch_out()

    def zhzhyss_zz_func(self, name):  # 追踪
        self.zhzhwh_mission.enter_iframe()
        self.zhzhwh_mission.click_yss()
        self.zhzhwh_mission.click_yss_zz(name)
        self.zhzhwh_mission.switch_out()

    """专户账户库页面"""

    def check_zhzhk_func(self, name):
        self.zhzhwh_mission.enter_iframe()
        self.zhzhwh_mission.click_zhk()
        self.zhzhwh_mission.click_zhk_name(name)
        self.zhzhwh_mission.switch_out()


if __name__ == '__main__':
    LoginMission().login_func('350203196505264042', '1')
    MenuMission().click_zhzh_whlr_menu()
    ZhZhWhMission().zhzh_kh_func('于宏健自动化测试', '450100000 南宁市', "31 社保基金财政专户", "1101 企业职工基本养老保险基金", '核算内容', '1', '9',
                                 '单位代码', '开户依据')
    ZhZhWhMission().zhzhdss_ss_func('于宏健自动化测试')
    ZhZhWhMission().zhzhyss_zz_func('于宏健自动化测试')
    BasePage().log_out()
    DriverTool().quit_driver()

"""
冒烟测试用例
"""
from common.base_page import BasePage
from page.login_page import LoginMission
from page.menu_select import MenuMission
from page.zhzh.zhzhwh.zhzh_ba import ZhZhBaMission
from page.zhzh.zhzhwh.zhzh_sh_szs import ZhZhShSzsMission
from page.zhzh.zhzhwh.zhzh_wh import ZhZhWhMission
from page.zhzh.zhzhwh.zhzh_sh import ZhZhShMission
from common.read_data_func import read_zhzhwh_smoke_data, read_zhzhzx_smoke_data
from common.Driver_tool import DriverTool

from parameterized import parameterized
import unittest


class TestZhZhSmoke(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverTool.get_driver()
        cls.login_mission = LoginMission()
        cls.menu_mission = MenuMission()
        cls.zhzhwh_mission = ZhZhWhMission()
        cls.zhzhsh_mission = ZhZhShMission()
        cls.zhzhshszs_mission = ZhZhShSzsMission()
        cls.zhzhba_mission = ZhZhBaMission()
        cls.base_page = BasePage()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverTool.quit_driver()

    @parameterized.expand(read_zhzhwh_smoke_data())
    def test_zhzhwh_smoke(self, name, czqhdm, zhlbdm, xz, hsnr, splxdm, khyhxzfs, dwdm, khyj, khxkzhzh, account, khyh,
                        czzhzhdm):
        """录入送审"""
        self.login_mission.login_func('350203196505264042', '1')
        self.menu_mission.click_zhzh_whlr_menu()
        self.zhzhwh_mission.zhzh_kh_func(name, czqhdm, zhlbdm, xz, hsnr, splxdm, khyhxzfs, dwdm, khyj)
        self.zhzhwh_mission.zhzhdss_ss_func(name)
        self.base_page.log_out()
        """审核"""
        self.login_mission.login_func('430528198611270043', '1')
        self.menu_mission.click_zhzh_whsh_menu()
        self.zhzhsh_mission.zhzhwsh_tg_func(name)
        self.base_page.log_out()
        """省终审"""
        self.login_mission.login_func('350583198909091018', '1')
        self.menu_mission.click_zhzh_whsh_szs_menu()
        self.zhzhshszs_mission.zhzhszswsh_tg_func(name, r"C:\Users\于宏健\Desktop\测试.pdf")
        self.base_page.log_out()
        """备案"""
        self.login_mission.login_func('350203196505264042', '1')
        self.menu_mission.click_zhzh_whba_menu()
        self.zhzhba_mission.zhzh_ba_func(name, khxkzhzh, account, khyh, czzhzhdm)
        self.base_page.log_out()

    # @parameterized.expand(read_zhzhzx_smoke_data())
    # def test_zhzhzx(self):
    #     ...


if __name__ == '__main__':
    unittest.main()

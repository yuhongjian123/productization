"""
封装所有方法
"""
from datetime import datetime
from time import sleep
import win32con
import win32gui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
from common.Driver_tool import DriverTool
from common.logger import Log


class BasePage(object):
    """封装方法"""

    def __init__(self):
        self.driver = DriverTool.get_driver()
        self.log = Log()

    def find_element_func(self, img_desc, location):  # location 元素定位信息
        """元素定位方法"""
        try:
            element = self.driver.find_element(location[0], location[1])  # 定位元素方法
            self.log.info("'{}'{}元素定位成功".format(img_desc, location))
            return element
        except Exception as e:
            self.log.warning("'{}'{}元素定位失败，报错信息为：{}".format(img_desc, location, e))
            try:
                element = self.driver.find_element(location[0], location[1])  # 定位元素方法
                self.log.info("'{}'{}元素定位成功".format(img_desc, location))
                return element
            except Exception as e:
                self.log.warning("'{}'{}元素再次定位失败，报错信息为：{}".format(img_desc, location, e))

    def input_text(self, img_desc, element, text):
        """输入内容方法"""
        try:
            self.find_element_func(img_desc, element).clear()
            self.log.info("{}清除成功".format(img_desc))
            self.find_element_func(img_desc, element).send_keys(text)
            self.log.info("在{}中输入{}成功".format(img_desc, text))
        except:
            self.log.warning("在{}中输入{}失败".format(img_desc, text))

    def get_text(self, img_desc, element, a):
        try:
            text = self.find_element_func(img_desc, element).get_attribute(a)
            self.log.info("获取{}中{}属性的值成功，值为{}".format(img_desc, a, text))
            return text
        except:
            self.log.warning("没有获取到{}中{}属性的值".format(img_desc, a))

    def click_button(self, img_desc, element):
        """点击按钮方法"""
        try:
            self.find_element_func(img_desc, element).click()
            self.log.info("点击{}成功".format(img_desc))
        except:
            self.log.warning("点击{}失败".format(img_desc))

    def move_to_element(self, img_desc, element):
        """鼠标悬停方法"""
        try:
            ActionChains(self.driver).move_to_element(self.find_element_func(img_desc, element)).perform()
            self.log.info(f'鼠标悬停到{img_desc}成功')
        except:
            self.log.warning(f'鼠标悬停到{img_desc}失败')

    def move_to_element_click(self, img_desc, element):
        """鼠标点击方法"""
        try:
            ActionChains(self.driver).move_to_element(self.find_element_func(img_desc, element)).click().perform()
            self.log.info(f'鼠标点击{img_desc}成功')
        except:
            self.log.warning(f'鼠标点击{img_desc}失败')

    def uplode(self, path):
        """上传附件方法"""
        try:
            sleep(2)
            dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path)  # 往输入框输入绝对地址
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
            sleep(1)
            self.log.info('上传附件成功')
        except:
            self.log.warning('上传附件失败')

    def save_screenshot(self, img_description):
        """截图方法"""
        now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        img_name = "{}_{}.png".format(img_description, now)
        base_path = os.path.dirname(os.path.dirname(__file__))   # 当前项目的绝对路径
        out_put_path = os.path.join(base_path, "OutPut", "img")
        img_path = os.path.join(out_put_path, img_name)
        try:
            self.driver.save_screenshot(img_path)
            self.log.info("截图成功，截图放在：{}".format(img_path))
        except:
            self.log.warning("当前页面截图失败")

    def switch_to(self, img_desc, element):
        """进入iframe方法"""
        try:
            self.driver.switch_to.frame(self.find_element_func(img_desc, element))
            self.log.info("进入frame{}成功".format(element))
        except:
            self.log.warning("进入frame{}失败".format(img_desc))

    def switch_out(self):
        """跳出iframe方法"""
        try:
            switch_out = self.driver.switch_to.default_content()
            self.log.info(f'跳出frame成功')
            return switch_out
        except:
            self.log.warning(f'跳出frame失败')

    # def get_all_handle(self):
    #     """获取所有句柄"""
    #     return self.driver.window_handles

    # def switch_to_handle(self, handle):
    #     self.driver.switch_to.window(handle)

    def switch_alert(self):
        """"""
        alert = self.driver.switch_to.alert
        alert.accept()

    # def get_list(self, element):
    #     """获取列表方法"""
    #     self.driver.find_elements(self.find_element_func(element))

    def log_out(self):
        """退出当前账号登录"""
        try:
            self.switch_out()
            self.driver.find_element(By.CLASS_NAME, 'pt-yonghu').click()
            self.driver.find_element(By.CLASS_NAME, 'pt-tuichudenglu').click()
            self.driver.find_element(By.XPATH, "//span[contains(text(),'确定')]").click()
            self.log.info('成功退出当前用户')
        except:
            self.log.warning('退出当前用户失败')

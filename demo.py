from selenium import webdriver
import time
import win32con
import win32gui

driver = webdriver.Chrome()
driver.get("http://172.16.101.21:15001/login")
# 窗口最大化
driver.maximize_window()
# 以防跳转加载不出来，等待5s
driver.implicitly_wait(5)
# 鼠标点击事件，跳转到登录界面
driver.find_element_by_class_name("login-tab-user").click()
# 登录账号和密码
driver.find_element_by_id('username').send_keys('350203196505264042')
driver.find_element_by_id('password').send_keys('1')
# 点击“登录”按钮
driver.find_element_by_xpath('//*[@id="portalLoginForm"]/div[6]/button').click()
# 打开左侧菜单列表
driver.find_element_by_xpath('//*[@id="menu-list-id1860701"]/ul/li[8]/a/span[1]').click()
driver.find_element_by_xpath('//*[@id="menu-list-id1860701"]/ul/li[8]/ul/li[1]/a/span[1]').click()
# 点击【专户账户维护】
driver.find_element_by_link_text('专户账户维护').click()
# 点击开户
# 点击"开户"按钮，开户按钮在一个iframe里面，所以先定义一个iframe
driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/iframe'))
time.sleep(3)
driver.find_element_by_xpath('//*[@id="add_acc"]').click()
# 填写账户名称
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="layui-layer-iframe100001"]'))
driver.find_element_by_id('110102').send_keys('zdd测试专户开户0531001')
# 填写财政区划代码 #选择南宁市
driver.find_element_by_xpath('//*[@id="_easyui_textbox_input2"]').click()
driver.find_element_by_xpath('//*[@id="_easyui_tree_4"]/span[4]').click()
# //span[text()='450100000 南宁市']

# 账户类别代码
driver.find_element_by_xpath('//*[@id="_easyui_textbox_input4"]').click()
driver.find_element_by_xpath("//span[text()='31 社保基金财政专户']").click()
# 险种
driver.find_element_by_xpath('//*[@id="_easyui_textbox_input6"]').click()
driver.find_element_by_xpath('//*[@id="_easyui_tree_72"]/span[4]').click()
# 核算内容
driver.find_element_by_id('110113').send_keys('zdd测试专户开户0531001')
# 审批类型代码
driver.find_element_by_id('110120').click()
driver.find_element_by_xpath('//*[@id="110120"]/option[2]').click()
# 开户银行选择方式
driver.find_element_by_id('110107').click()
driver.find_element_by_xpath('//*[@id="110107"]/option[2]').click()
# 单位代码
driver.find_element_by_id('110119').send_keys('101001')
# 开户依据
driver.find_element_by_id('110114').send_keys('测试专用')
time.sleep(2)

# 添加附件
driver.find_element_by_xpath('//*[@id="floor_2"]/ul/form[1]/li/div/span[2]/div/div[1]/button').click()
time.sleep(3)
dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
time.sleep(3)
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r"C:\Users\于宏健\Desktop\测试.pdf")  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

# #点击保存
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/span[2]/button[1]').click()
# #点击确定
# driver.find_element_by_xpath('//*[@id="layui-layer100002"]/div[3]/a').click()

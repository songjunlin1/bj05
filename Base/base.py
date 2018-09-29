"""
    Base：类封装所有公用的方法
            解释： 只要有两个要面以上要使用的相同的方法，都可以理解为公共用的方法
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver=driver
    # 找元素  给谁用？？？ 给以下需要用到的方法使用；
    def base_get_element(self,loc,timeout=30,poll=0.5):
        """
        :param loc: 一定是一个元祖格式，谁调用，谁给我！！！
        :return:
        """
        driver=self.driver
        # 显示等待
        return WebDriverWait(driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 点击方法 封装
    def base_click(self,loc):
        # 调用 自己封装的查找元素方法，获取到元素后，进行点击
        self.base_get_element(loc).click()
    # 输入方法 封装
    def base_input(self,loc,text):
        # 调用 自己封装的查找元素方法，获取到元素后，输入指定内容
        """
        :param loc: 谁调用谁把元祖给我
        :param text: 要输的内容告诉我
        """
        el=self.base_get_element(loc)
        # 输入内容之前先执行清除
        el.clear()
        # 输入内容
        el.send_keys(text)
    # 封装driver
    def base_get_driver(self,package,activity):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # 设置中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # app的信息
        desired_caps['appPackage'] = package
        desired_caps['appActivity'] = activity

        # 声明我们的driver对象
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
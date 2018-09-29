import os,sys
sys.path.append(os.getcwd())
import pytest
from Base.get_driver import get_driver
from Page.page_in import PageIn
from Base.read_yaml import ReadYAML
# 测试封装的读取工具类方法
def get_data():
    return ReadYAML("read_setting_yaml.yaml").read_yaml()
class TestSetting():
    # setup_class
    def setup_class(self):
        # 获取driver
        self.driver=get_driver()
        # 实例化PageIn
        self.page=PageIn(self.driver)
        # 获取PageSetting实例化对象 为什么要拿到setting对象？？？
        self.setting=self.page.page_get_page_setting()
    # teardown_class
    def teardown_class(self):
        # 关闭驱动对象
        self.driver.quit()
    # 测试方法
    @pytest.mark.parametrize("text",get_data())
    def test_search(self,text):
        """按照操作步骤完成"""
        # 点击搜索按钮
        self.setting.page_click_search()
        # 输入信息
        self.setting.page_input(text)
        # 点击返回按钮
        self.setting.page_click_back_btn()
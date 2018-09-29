"""
    Page页面：如何编写？？？
            说明：
                1. 根据测试用例内操作步骤进行编写
                2. 暂时我们把没每一步操作单独放为一个函数

"""
from Base.base import Base
import Page
"""
    说明：通过包名.方式 可以获取到包内的__init__.py文件内的属性和方法
    如： Page.setting_search_btn
"""

class PageSetting(Base):
    # 点击搜索按钮
    def page_click_search(self):
        self.base_click(Page.setting_search_btn)
    # 输入内容
    def page_input(self,text):
        self.base_input(Page.setting_input_search,text)
    # 点击返回按钮
    def page_click_back_btn(self):
        self.base_click(Page.setting_back_btn)
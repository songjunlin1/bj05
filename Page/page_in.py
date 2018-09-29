from Page.page_setting import PageSetting
"""
    page_in：统一入口类
        说明：
            1. 解决多个page页面，实例化引用问题
            2. 无论多少个page页面，我们只需要导入PageIn就可以
        
"""
class PageIn():
    # driver 谁实例化PageIn谁给我driver
    def __init__(self,driver):
        self.driver=driver
    # 返回 page_setting实例
    def page_get_page_setting(self):
        return PageSetting(self.driver)
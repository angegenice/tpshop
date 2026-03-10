import pytest
from utils import DriverUtils,build_data,get_el_text
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
import time
class TestLogin:

    def setup_class(self):
        """每次测试前打开一次浏览器"""
        self.driver = DriverUtils.get_driver()

    def teardown_class(self):
        """所有测试用例结束关闭浏览器"""
        DriverUtils.quit_driver()
    
    def setup_method(self):
        """每个方法的起点-回到首页开始"""
        self.driver.get("http://localhost/index.php")

    @pytest.mark.parametrize(("username","password","code","expect"),build_data("tp_login_data"))
    def test_login(self,username,password,code,expect):
        # 找到首页的登录按钮
        DriverUtils.get_driver().find_element(By.XPATH,"//*[text()='登录']").click()
        # 调用page对象
        LoginPage().tp_login(username,password,code)
        time.sleep(2)
        # 读取提示信息
        msg = get_el_text("//*[@class='layui-layer-content layui-layer-padding']")
        # 断言
        assert expect in msg
        


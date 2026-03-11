import pytest
from utils import build_data,DriverUtils
from page.register_page import RegisterPage
from selenium.webdriver.common.by import By
import time
class TestRegister():

    def setup_class(self):
        """类级别，整个测试类中仅执行一次"""
        self.driver = DriverUtils.get_driver()
    def teardown_class(self):
        """所有测试用例结束关闭浏览器"""
        DriverUtils.quit_driver()

    def setup_method(self):
        """方法级别，每个测试方法执行前都会执行。"""
        self.driver.get("http://localhost/index.php/Home/User/reg")

    @pytest.mark.parametrize(("tel","verify_code","code","password","password2","invite"),build_data("tp_register_data"))
    def test_register(self,tel,verify_code,code,password,password2,invite):
        reg = RegisterPage()
        reg.tp_register(tel,verify_code,code,password,password2,invite)
        # 找到按钮点击
        reg.find_el((By.XPATH,"//a[@class='regbtn J_btn_agree']")).click()
        time.sleep(1)
        reg.find_el((By.XPATH,"//*[@class='layui-layer-btn0']")).click()


from utils import DriverUtils,build_data,get_el_text
from page.admin_login_page import AdminLoginPage
from selenium.webdriver.common.by import By
import pytest
import time
class TestAdminLogin():

    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    @classmethod
    def teardown_class(self):
        DriverUtils.quit_driver()
        print("is coming ?")

    def setup_method(self):
        self.driver.get("http://localhost/index.php?m=Admin&c=Admin&a=login")
        self.driver.delete_all_cookies() # 强制清除登录状态
        self.driver.refresh()
    

    @pytest.mark.parametrize(("username","password","code","expect"),build_data("tp_admin_login_data"))
    def test_admin_login(self,username,password,code,expect):
        admin = AdminLoginPage()
        # 找到页面登录按钮
        btn = admin.find_el((By.NAME,"submit"))
        admin.tp_admin_login(username,password,code)
        time.sleep(1)
        btn.click()
        # 找到返回提示
        if admin.find_el((By.XPATH,"//*[@class='error']")) is None:
            msg = ""
        else:
            msg = get_el_text("//*[@class='error']")
        assert expect in msg
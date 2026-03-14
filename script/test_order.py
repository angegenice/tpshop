from utils import DriverUtils
from page.login_page import LoginPage
from page.search_page import SearchPage
from page.order_page import OrderPage
import time
class TestOrder():

    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    def setup_method(self):
        # 从登录页面开始：login-search-add_cat-enter_order_page-order
        self.driver.get("http://localhost/Home/user/login")

    def teardown_class(self):
        DriverUtils.quit_driver()

    def test_order(self):
        # login
        login = LoginPage()
        login.tp_login("13817996547","123456","8888")
        time.sleep(0.5)
        # search eg:衣服
        search = SearchPage()
        search.tp_search_to_add("手机")
        time.sleep(0.5)
        search.tp_click_cat_btn()
        # order
        oder = OrderPage()
        time.sleep(0.5)
        oder.tp_click_order_btn()
        time.sleep(4)
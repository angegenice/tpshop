from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By

class AdminLoginPage(BasePage):

    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.username = (By.NAME,"username")
        self.password = (By.NAME,"password")
        self.code = (By.NAME,"vertify")

    def tp_admin_login(self,username,pwd,code):
        self.input_text(self.find_el(self.username),username)
        self.input_text(self.find_el(self.password),pwd)
        self.input_text(self.find_el(self.code),code)
        



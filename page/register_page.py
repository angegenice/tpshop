from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.username = (By.ID,"username")
        self.verify_code = (By.NAME,"verify_code")
        self.code = (By.ID,"code")
        self.password = (By.ID,"password")
        self.password2 = (By.ID,"password2")
        self.invite = (By.NAME,"invite")

    def tp_register(self,username,verify_code,code,password,password2,invite):
        self.input_text(self.find_el(self.username),username)
        self.input_text(self.find_el(self.verify_code),verify_code)
        self.input_text(self.find_el(self.code),code)
        self.input_text(self.find_el(self.password),password)
        self.input_text(self.find_el(self.password2),password2)
        self.input_text(self.find_el(self.invite),invite)


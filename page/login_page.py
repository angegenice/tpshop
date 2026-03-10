from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils import DriverUtils

class LoginPage(BasePage):
    def __init__(self):
        # 获得驱动s
        self.driver = DriverUtils.get_driver()
        self.username = (By.ID,"username")
        self.password = (By.ID,"password")
        self.verify_code = (By.ID,"verify_code")
        self.login_btn = (By.XPATH,"//*[@class='login_bnt']/a")
    
    def tp_login(self,user,pwd,code):
        """"
        user:str 文本
        pwd:str
        code:str
        """
        self.input_text(self.find_el(self.username),user)
        self.input_text(self.find_el(self.password),pwd)
        self.input_text(self.find_el(self.verify_code),code)
        # 点击登录
        self.find_el(self.login_btn).click()

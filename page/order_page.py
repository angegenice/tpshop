from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By
class OrderPage(BasePage):
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        # 购物车按钮
        self.order_btn = (By.XPATH,"//a[@class='paytotal']")
        self.order_upload_btn = (By.XPATH,"//button[@id='submit_order']")
    
    def tp_click_order_btn(self):
        self.find_el(self.order_btn).click()
        # 点击js alert弹出框
        self.driver.switch_to.alert.accept()
        # 订单页提交订单按钮
        self.find_el(self.order_upload_btn).click()
        

    


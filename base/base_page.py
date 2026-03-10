import logging

from selenium.webdriver.support.wait import WebDriverWait

from utils import DriverUtils

class BasePage():
    def __init__(self):
        self.driver = DriverUtils.get_driver()
    
    # location = (BY.xxx,"xxx")
    def find_el(self,location:tuple):
        """定位元素方法，return el"""
        try:
            el = WebDriverWait(self.driver,10,1).until(lambda x : x.find_element(*location))
            logging.info(f"find {location} success！")
        except Exception as e:
            el = None
            logging.error(f"find {location} failed！")
        return el
    
    def input_text(self,element,text):
        """元素输入内容"""
        try:
            element.clear()
            element.send_keys(text)
            logging.info(f"input {text} success!")
        except Exception as e:
            logging.error(f"input {text} failed")
            

    # frame切换
    def switch_frame(self, i_el):
        try:
            self.driver.switch_to.frame(i_el)
            logging.info(f"switch iframe success!")
        except Exception as e:
            logging.error(f"switch iframe failed!")

    # 窗口切换
    def switch_window(self, n):
        try:
            # 1.获取所有句柄信息
            handles = self.driver.window_handles
            # 2.切换到指定窗口
            self.driver.switch_to.window(handles[n])
            logging.info(f"switch window success!")
        except Exception as e:
            logging.error(f"switch window failed!")


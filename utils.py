from selenium import webdriver
from selenium.webdriver.common.by import By
# 等待
from selenium.webdriver.support.wait import WebDriverWait
import logging
import json
import os
import time

class DriverUtils:
    # 私有属性
    __driver = None

    @classmethod
    def get_driver(cls):
        """
        cls: 类方法，表示类本身
        获取浏览器驱动
        """
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            # 隐式等待30 「智能等待」，不是必须等满 30 秒，找到元素就立即执行
            cls.__driver.implicitly_wait(30)
        return cls.__driver
    
    @classmethod
    def quit_driver(cls):
        """关闭浏览器对象"""
        if cls.__driver is not None:
            time.sleep(2)
            cls.__driver.quit()
            # 设为空
            cls.__driver = None
    
"""函数方法"""


def get_el_text(xpath_str):
    """获取元素文本"""
    try:
        msg = WebDriverWait(DriverUtils.get_driver(),10,1).\
        until(lambda x:x.find_element(By.XPATH,xpath_str)).text
    except Exception as e:
        logging.error(f"没有获取到{xpath_str}的元素对象文本!")
        msg = None
    return msg

def el_is_exist_by_text(key_text):
    """根据文本判断页面是否存在元素"""
    try:
        is_suc = WebDriverWait(DriverUtils.get_driver(),10,1).\
        until(lambda x : x.find_element(By.XPATH,f"//*[text()='{key_text}']"))
    except Exception as e:
        is_suc = False
        DriverUtils.get_driver().get_screenshot_as_file(f"{key_text}未找到.png")
        logging.error(f"未找到文本为{key_text}的元素对象!")
    # 返回是否找到结果
    return is_suc

"""
{
  "登录成功用例": {
    "用户名": "admin",
    "密码": "123456",
    "预期结果": "跳转到首页",
    "状态码": 200
  },
  "密码错误用例": {
    "用户名": "admin",
    "密码": "654321",
    "预期结果": "提示密码错误",
    "状态码": 400
  },
  "用户名为空用例": {
    "用户名": "",
    "密码": "123456",
    "预期结果": "提示用户名不能为空",
    "状态码": 400
  }
}
"""
# [["15801010202","123456","8888","账号不存在"],["15800000001", "error", "8888","密码错误"]]
def build_data(file_name):
    """读取数据文件"""
    file_path = os.path.dirname(__file__) + f"/data/{file_name}.json"
    case_data = []
    with open(file_path,"r",encoding="utf-8") as f:
        all_data = json.load(f)
    for i in all_data.values():
        case_data.append(list(i.values()))
    return case_data

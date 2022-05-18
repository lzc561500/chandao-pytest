# -*- coding:utf8 -*-
from selenium.webdriver.support.wait import WebDriverWait
class InputValue:
    def __init__(self,driver):
        self.driver = driver

    def input_value(self,tagName,value,direction="后",index=1):
        try:
            if direction == "后":
                ele = WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element_by_xpath(
                    "//*[normalize-space(text())='{0}']/following::input[{1}]".format(tagName,index)))
                ele.click()
                ele.clear()
                ele.send_keys(value)
            elif direction == "前":
                ele = WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element_by_xpath(
                    "//*[normalize-space(text())='{0}']/preceding::input[{1}]".format(tagName,index)))
                ele.click()
                ele.clear()
                ele.send_keys(value)
        except Exception:
            raise Exception("未找到{0}{1}面第{2}个输入框".format(tagName,direction,index))





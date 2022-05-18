# -*- coding:utf8 -*-
from selenium.webdriver.support.wait import WebDriverWait
class ButtonClick:
    def __init__(self,driver):
        self.driver = driver

    def button_click(self,tagName,index=1):
        try:
            eles = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements_by_xpath(
                "//*[normalize-space(text())='{0}']".format(tagName)))
            if len(eles) == 1:
                ele = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(
                "//*[normalize-space(text())='{0}']".format(tagName)))
            elif len(eles) > 1:
                ele = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(
                "//*[normalize-space(text())='{0}']".format(tagName)))
            ele.click()
        except Exception:
            raise Exception("未找到名为{0}的按钮")


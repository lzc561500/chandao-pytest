# -*- coding:utf8 -*-
import re
from selenium import webdriver
class CheckValue:
    def __init__(self,driver):
        self.driver = driver

    def check_taget_value(self,value):
        #获取HTML页面源码第一种方法
        page = self.driver.find_element_by_xpath("//*").get_attribute("outerHTML")
        #获取HTML页面源码第二种方法
        #page = self.driver.page_source
        list_value = re.findall(value,page)
        if len(list_value) == 0:
           raise Exception("在当前页面中未找到{0}".format(value))



# -*- coding:utf8 -*-
from selenium import webdriver
from base.chandaologin import LoginChanDao,ButtonClick,InputValue,CheckValue
import allure
import time
@allure.feature("添加公司名称")
class TestAddCompany:

    @allure.story("打开谷歌浏览器并输入禅道网址")
    def setup_class(self):
        url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    @allure.story("登录后添加公司信息")
    def test_addCompany(self):
        with allure.step("登录"):
            LoginChanDao(self.driver).login()
        time.sleep(3)
        with allure.step("进入首页点击组织"):
            ButtonClick(self.driver).button_click("组织")
        time.sleep(2)
        with allure.step("点击公司"):
            ButtonClick(self.driver).button_click("公司")
        time.sleep(2)
        with allure.step("点击编辑"):
            ButtonClick(self.driver).button_click("编辑")
        time.sleep(2)
        with allure.step("切换到ifram"):
            self.driver.switch_to.frame("modalIframe")
        time.sleep(2)
        with allure.step("输入公司名称"):
            InputValue(self.driver).input_value("公司名称","浦发银行","后")
        time.sleep(2)
        with allure.step("输入公司联系电话"):
            InputValue(self.driver).input_value("联系电话","021-4567891","后")
        time.sleep(2)
        with allure.step("输入通讯地址"):
            InputValue(self.driver).input_value("通讯地址","上海市长宁区凯旋路5881号","后")
        time.sleep(2)
        with allure.step("是否允许匿名登录"):
            ButtonClick(self.driver).button_click("不允许")
        time.sleep(2)
        with allure.step("点击保存"):
            ButtonClick(self.driver).button_click("保存")
        time.sleep(2)
        with allure.step("检查是否编辑成功"):
            CheckValue(self.driver).check_taget_value("浦发银行")

    @allure.story("清除cookies并关闭浏览器")
    def teardown_class(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


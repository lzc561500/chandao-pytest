# -*- coding:utf8 -*-
from selenium import webdriver
from base.input import InputValue
from base.buttonClick import ButtonClick
from base.checkValue import CheckValue
from data.read_data_excel import Data
from base.isexiteAlert import IsAlert
import time
import pytest
import allure

@allure.feature("禅道登录用例")
class TestLogin:
    @allure.story("打开谷歌浏览器并输入禅道网址")
    def setup_class(self):
        url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    @allure.story("输入用户名和密码")
    @pytest.mark.parametrize("data", Data("./data/data.xls", "登录").readData())
    def test_sc_login(self,data):
        login_input = InputValue(self.driver)
        with allure.step("输入登录名"):
            userName = data["用户名"]
            login_input.input_value("用户名", "{}".format(userName))
            # picture= Screen(self.driver).screenshot_element("用户名")
            # allure.attach(picture,attachment_type=allure.attachment_type.PNG)
        time.sleep(1)
        with allure.step("输入密码"):
            psw = data["密码"]
            login_input.input_value("密码", "{}".format(psw))
            # picture = Screen(self.driver).screenshot_element("密码")
            # allure.attach(picture, attachment_type=allure.attachment_type.PNG)
        with allure.step("点击保持登录"):
            ButtonClick(self.driver).button_click("保持登录")
            # picture = Screen(self.driver).screenshot_element("保持登录")
            # allure.attach(picture, attachment_type=allure.attachment_type.PNG)
        with allure.step("点击登录按钮"):
            ButtonClick(self.driver).button_click("登录")
        time.sleep(1)
        with allure.step("是否有alert弹窗"):
            IsAlert(self.driver).isExiteAlert()
        time.sleep(4)
        with allure.step("检查是否登录成功"):
            CheckValue(self.driver).check_taget_value("退出")
            # picture = Screen(self.driver).screenshot_element("退出")
            # allure.attach(picture, attachment_type=allure.attachment_type.PNG)

    def teardown(self):
        time.sleep(2)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @allure.story("关闭浏览器")
    def teardown_class(self):
        self.driver.quit()
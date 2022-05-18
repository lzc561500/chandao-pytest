# -*- coding:utf8 -*-
from data.read_data_excel import Data
from base.input import InputValue
from base.checkValue import CheckValue
from base.buttonClick import ButtonClick
import time
class LoginChanDao:

    def __init__(self,driver):
        self.driver = driver

    def login(self,index=1):
        data = Data("./data/data.xls","登录1").readData()
        userName = data[index-1]["用户名"]
        psw = data[index-1]["密码"]
        InputValue(self.driver).input_value("用户名",userName,"后")
        InputValue(self.driver).input_value("密码", psw, "后")
        ButtonClick(self.driver).button_click("登录")
        time.sleep(5)
        CheckValue(self.driver).check_taget_value("退出")




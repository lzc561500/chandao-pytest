# -*- coding:utf8 -*-
import time
class IsAlert:

    def __init__(self,driver):
        self.driver = driver

    def isExiteAlert(self):
        try:
            a = self.driver.switch_to.alert
            a.text
            a.accpet()
        except Exception:
            return ""

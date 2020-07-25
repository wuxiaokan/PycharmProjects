# -*- encoding: utf-8 -*-
'''
@File    :   emailMergerRulePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/4 0004 16:52   dmk      1.0         None
'''

import time
import random
from selenium.webdriver.common.by import By
from .emailSettingPage import emailSettingPage


class emailMergerRulePage(emailSettingPage):
    #归并规则设置按钮
    mergerRuleSettingBtn_loc = (By.XPATH,"//span[text()='归并规则']")
    #立即归并按钮
    instantlyMerger_loc = (By.XPATH,'//div[@class="merger_check"]//label')
    #所有的设置列表项
    allSetting_loc = (By.XPATH,'//ul[@class="setting-menu el-menu align-center"]/li')

    def __init__(self,driver):
        super(emailMergerRulePage,self).__init__(driver)
        self.find_element(self.mergerRuleSettingBtn_loc).click()

    def run_instantlyMergerSave_case(self):
        #判断立即归并是否勾选
        time.sleep(1)
        if "is-checked" in self.find_element(self.instantlyMerger_loc).get_attribute("class"):
            self.find_element(self.instantlyMerger_loc).click()
            time.sleep(1)
            self.find_element(self.instantlyMerger_loc).click()
        else:
            self.find_element(self.instantlyMerger_loc).click()

        #切换到其他tab
        self.find_element(self.allSetting_loc,index=random.randint(1,10)).click()
        #再次切到归并规则
        time.sleep(0.5)
        self.find_element(self.mergerRuleSettingBtn_loc).click()
        time.sleep(1)
        if "is-checked" not in self.find_element(self.instantlyMerger_loc).get_attribute("class"):
            raise Exception("立即归并设置后，切换其他tab，没有保存成功")
# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 16:12   dmk      1.0         None
'''
import time,traceback
from pageObject.basePage import Action
from pageObject.seniorSearchMailPage.seniorSearchMailPage_loc import seniorSearchMailPageLoc


class seniorSearchMailPage(Action,seniorSearchMailPageLoc):

    def __init__(self,driver):
        super(seniorSearchMailPage,self).__init__(driver)
        try:
            self.switch_mainPage()
            self.find_element(self.seniorSearchMailPage_seniorSearchBtn_loc).click()
        except Exception:
            traceback.print_exc()
        finally:
            self.switch_frame(self.mainFrame_loc)

    #根据是否包含附件进行搜索
    def searchMailByAttach(self,is_attach):
        time.sleep(0.5)
        if is_attach:
            self.find_element(self.seniorSearchMailPage_hasAttchBtn_loc).click()
        else:
            self.find_element(self.seniorSearchMailPage_hasNoAttchBtn_loc).click()
    #点击确定搜索按钮
    def click_searchBtn(self):
        self.find_element(self.seniorSearchMailPage_sureBtn_loc).click()




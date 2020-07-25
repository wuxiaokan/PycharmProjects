# -*- encoding: utf-8 -*-
'''
@File    :   relatedBusinessPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/14 0014 13:53   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from pageObject.supplierInfoShowPage.supplierInfoShowPage import supplierInfoShowPage
from pageObject.customerInfoShowPage.relatedBusinessPage_loc import relatedBusinessPageLoc


class relatedBusinessPage(supplierInfoShowPage,relatedBusinessPageLoc):

    def __init__(self,driver):
        super(relatedBusinessPage,self).__init__(driver)
        self.click_ele(self.relatedBusinessPage_relatedBusinessBtn_loc,key="点击相关业务按钮")



    #过滤相关业务
    def run_filterRelatedBusiness_case(self,data):
        with allure.step("点击更多条件按钮"):
            self.click_ele(self.relatedBusinessPage_moreConditionBtn_loc,key="点击更多条件按钮")
        time.sleep(0.5)
        with allure.step("选中：{}".format(data["condition"])):
            conditionBtn_loc = (By.XPATH,self.relatedBusinessPage_moreConditionListBtn_loc[1].replace("跟进",data["condition"]))
            self.click_ele(conditionBtn_loc,key="选中：{}".format(data["condition"]))
        with allure.step("获取更多条件文本"):
            moreCondition_text = self.get_elementText(self.relatedBusinessPage_moreConditionBtn_loc)
        assert moreCondition_text == data["condition"]
        with allure.step("点击联系人按钮"):
            self.click_ele(self.relatedBusinessPage_allContactBtn_loc)
        time.sleep(0.5)
        with allure.step("点击第一个联系人"):
            firstContactEle = self.find_element(self.relatedBusinessPage_contactList_loc,index=1)
            firstContact = firstContactEle.text
            firstContactEle.click()
        with allure.step("获取显示的联系人"):
            showContact = self.get_elementText(self.relatedBusinessPage_allContactBtn_loc)
        assert firstContact == showContact
        # with allure.step("点击商机下拉框按钮"):
        #     self.click_ele(self.relatedBusinessPage_selectBusinessBtn_loc)
        # time.sleep(0.5)
        # with allure.step("点击第一个商机"):
        #     firstBusinessEle = self.find_element(self.relatedBusinessPage_businessList_loc)
        #     firstBusiness = firstBusinessEle.text
        #     firstBusinessEle.click()
        # with allure.step("获取显示的商机"):
        #     showBusiness = self.get_elementText(self.relatedBusinessPage_selectBusinessBtn_loc)
        # assert firstBusiness == showBusiness
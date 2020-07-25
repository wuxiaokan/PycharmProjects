# -*- encoding: utf-8 -*-
'''
@File    :   emailInsertSitePage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/3 0003 15:02   dmk      1.0         None
'''

import time
from utils.generator import *
from selenium.webdriver.common.by import By
from .emailWriteMailPage import emailWriteMailPage

class emailInsertSitePage(emailWriteMailPage):
    #插入营销网站
    insertSite_loc = (By.XPATH,"//div[@class='tool']//li[text()='营销网站']")
    #营销网站分组,根据index判断是第几个
    siteGroup_loc = (By.XPATH,"//div[@class='el-tree line32 el-tree--highlight-current']/div")
    #营销网站信息
    siteInfo_loc = (By.XPATH,"//div[@class='product-info fl']")

    def __init__(self,driver):
        super(emailInsertSitePage,self).__init__(driver)
        self.find_element(self.insertSite_loc).click()

    #营销网站各分组数量
    def run_siteInfoByGroup_case(self):
        #获取全部分组的网站信息
        time.sleep(1)
        allSiteInfo = self.get_elementText(self.siteInfo_loc,index="all")
        #切换到第一个分组
        self.find_element(self.siteGroup_loc).click()
        time.sleep(0.5)
        if self.is_element_exist(self.siteInfo_loc[1]):
            firstGroupSiteInfo = self.get_elementText(self.siteInfo_loc,index="all")
            if allSiteInfo == firstGroupSiteInfo:
                raise Exception("营销网站第一分组：{}，数据与全部分组一致，请排查".format(self.find_element(self.siteGroup_loc).text))
        #切换到第二个分组
        self.find_element(self.siteGroup_loc,index=1).click()
        time.sleep(0.5)
        if self.is_element_exist(self.siteInfo_loc[1]):
            secondGroupSiteInfo = self.get_elementText(self.siteInfo_loc,index="all")
            if allSiteInfo == secondGroupSiteInfo:
                raise Exception("营销网站第二分组：{}，数据与全部分组一致，请排查".format(self.find_element(self.siteGroup_loc,index=1).text))
        # #切换到第三个分组
        # self.find_element(self.siteGroup_loc,index=2).click()
        # time.sleep(0.5)
        # if self.is_element_exist(self.siteInfo_loc[1]):
        #     thirdGroupSiteInfo = self.get_elementText(self.siteInfo_loc,index="all")
        #     if allSiteInfo == thirdGroupSiteInfo:
        #         raise Exception("营销网站第三分组：{}，数据与全部分组一致，请排查".format(self.find_element(self.siteGroup_loc,index=2).text))
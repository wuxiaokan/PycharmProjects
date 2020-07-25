# -*- encoding: utf-8 -*-
'''
@File    :   unArchivesContactPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/17 0017 16:43   dmk      1.0         None
'''

import allure,time,traceback
from selenium.webdriver.common.by import By
from pageObject.basePage import Action


class unArchivesContactPage(Action):
    #未建档联系人页面，未建档联系人图标
    unArchivesContactPage_unArchivesContactIcon_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg" and contains(@style,"color: rgb(92, 107, 119);")]')
    #未建档联系人页面，添加联系人按钮
    unArchivesContactPage_addContactBtn_loc = (By.XPATH,'//button[@class="el-button m-l-10 btn-small el-button--default"]')
    #未建档联系人页面，供应商tab
    unArchivesContactPage_supplierTab_loc = (By.XPATH,'//li[@class="el-menu-item" and text()="供应商"]')
    #未建档联系人页面，尾页按钮
    unArchivesContactPage_lastPageBtn_loc = (By.XPATH,'//div[contains(@class,"addContacts ")]//button[@class="btn-next"]')
    #未建档联系人页面，业务员是云基础列
    unArchivesContactPage_salesmanColumn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF addContacts align-center"]//div[text()="云基础"]')
    #未建档联系人页面，业务员是管理员列
    unArchivesContactPage_adminColumn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF addContacts align-center"]//div[text()="管理员"]')
    #未建档联系人页面，供应商行
    unArchivesContactPage_supplierRow_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF addContacts align-center"]//tbody//tr')
    #未建档联系人页面，联系人邮箱
    unArchivesContactPage_contactEmailAccount_loc = (By.XPATH,'//span[@class="cursor0"]//span[@class="contact_names"]')
    #未建档联系人页面，确定按钮
    unArchivesContactPage_sureBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF addContacts align-center"]//button[@class="el-button small el-button--primary"]')
    #客户模块，添加联系人页面，客户名称input
    customerMoudel_addContactPageCustomerNameInput_loc = (By.XPATH,'//li[@data-name="客户名称"]//input')
    #客户模块，添加联系人页面，联系人邮箱input
    customerMoudel_addContactPageContactAccountInput_loc = (By.XPATH,'//span[text()="邮箱"]/../..//span[@class="el-input__inner"]')
    #客户模块，添加联系人页面，联系人邮箱input,供应商
    customerMoudel_addContactPageContactAccountInput_supplier_loc = (By.XPATH,'//div[contains(@class,"panel-supplier-contact-info")]//td[@data-name="邮箱"]//input')
    #供应商模块，添加联系人页面，客户名称input
    supplierMoudel_addContactPageCustomerNameInput_loc = (By.XPATH,'//li[@data-name="供应商名称"]//input')
    #客户编辑frame
    customerEditFrame_loc = (By.XPATH,'//iframe[@name="customer-edit"]')


    def __init__(self,driver):
        super(unArchivesContactPage,self).__init__(driver)
        #找到一个未建档联系人，并点击icon
        time.sleep(1)
        self.get_unArchivesContactAndClick()


    def get_unArchivesContactAndClick(self):
        with allure.step("找到一个未建档联系人，并点击icon"):
            if self.is_element_exist(self.unArchivesContactPage_unArchivesContactIcon_loc[1]):
                self.find_element(self.unArchivesContactPage_unArchivesContactIcon_loc).click()
            else:
                self.find_element(self.nextPageBtn_loc).click()
                self.find_element(self.unArchivesContactPage_unArchivesContactIcon_loc).click()


    #未建档添加联系人
    def run_unArchivesContactPageAddContact_case(self,type,operator):
        """type,1:客户，2：供应商,operator,0:所有，1：云基础，2：管理员"""
        with allure.step("获取联系人邮箱"):
            time.sleep(0.5)
            contactEmailAccount = self.find_element(self.unArchivesContactPage_contactEmailAccount_loc).text.split("<")[1].split(">")[0]
        with allure.step("点击添加联系人按钮"):
            self.find_element(self.unArchivesContactPage_addContactBtn_loc).click()
        time.sleep(0.2)
        # with allure.step("点击最后一页按钮，跳转到最后一页"):
        #     self.find_element(self.unArchivesContactPage_lastPageBtn_loc).click()
        # time.sleep(0.3)
        if type == "2":
            with allure.step("点击供应商tab"):
                self.find_element(self.unArchivesContactPage_supplierTab_loc).click()
            time.sleep(0.2)
            with allure.step("点击第一行，第一个供应商"):
                self.find_element(self.unArchivesContactPage_supplierRow_loc).click()
        else:
            if operator == "1":
                with allure.step("点击云基础客户"):
                    self.find_element(self.unArchivesContactPage_salesmanColumn_loc).click()
            elif operator == "2":
                with allure.step("点击管理员客户"):
                    self.find_element(self.unArchivesContactPage_adminColumn_loc).click()
        with allure.step("点击确定按钮"):
            self.find_element(self.unArchivesContactPage_sureBtn_loc).click()
        return contactEmailAccount

    #切换句柄，获取带入的联系人邮箱
    def get_takedEmailAccount(self,type):
        all_handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        try:
            if type == "2":
                with allure.step("切换到跳转的句柄"):
                    self.driver.switch_to.window(all_handles[1])
                    # if type == "1":
                    #     self.switch_frame(self.customerEditFrame_loc)
            with allure.step("获取联系人邮箱"):
                if type == "1":
                    return self.get_elementText(self.customerMoudel_addContactPageContactAccountInput_loc).strip()
                else:
                    time.sleep(3)
                    self.screenshotImg(key="添加供应商联系人")
                    return self.find_element(self.customerMoudel_addContactPageContactAccountInput_supplier_loc,index=1).get_attribute("value")
        except Exception as e:
            traceback.print_exc()
        finally:
            if type == "2":
                self.driver.close()
                self.driver.switch_to.window(current_handle)
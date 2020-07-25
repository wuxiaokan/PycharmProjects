# -*- encoding: utf-8 -*-
'''
@File    :   generalAddCustomerPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 0016 9:42   dmk      1.0         None
'''

import allure,time,os
from random import randint
from selenium.webdriver.common.by import By
from utils.generator import *
from utils.config import ATTACH_PATH
from pageObject.basePage import Action
from pageObject.generalAddCustomerPage.generalAddCustomerCommon import generalAddCustomerCommon
from pageObject.generalAddCustomerPage.generalAddCustomerPage_loc import generalAddCustomerPageLoc
from pageObject.customerDetailPage.customerDetailPage_loc import customerDetailPageLoc
from pageObject.customerPage.customerPage_loc import customerPageLoc
from pageObject.customerDetailPage.customerDetailPageCommon import customerDetailPageCommon
from pageObject.fastAddCustomerPage.fastAddCustomerPage_loc import fastAddCustomerPageLoc


class generalAddCustomerPage(Action,generalAddCustomerPageLoc,customerDetailPageLoc,customerPageLoc,fastAddCustomerPageLoc):

    def __init__(self,driver):
        super(generalAddCustomerPage,self).__init__(driver)
        self.generalAddCustomerCommon = generalAddCustomerCommon(driver)
        self.customerDetailPageCommon = customerDetailPageCommon(driver)


    def run_generalAddCustomer_case(self,is_add,customer_sendKeys,customer_selectKeys):
        self.screenshotImg(key="客户")
        self.generalAddCustomerCommon.is_addCustomer(is_add)
        time.sleep(1)
        with allure.step("点击联系人展开按钮"):
            #self.find_element(self.generalAddCustomerPage_showOrHideContactBtn_loc).click()
            self.click_ele(self.generalAddCustomerPage_showOrHideContactBtn_loc)
        for data in customer_sendKeys:
            key = list(data.keys())[0]
            value = list(data.values())[0]
            with allure.step("输入：{}".format(key)):
                self.generalAddCustomerCommon.sendKeys_customer(xpath=key,key=value)
        for data in customer_selectKeys:
            key = list(data.keys())[0]
            value = list(data.values())[0]
            with allure.step("选择：{}".format(key)):
                self.generalAddCustomerCommon.selectKeys_customer(xpath=key, key=value)
        with allure.step("点击保存按钮"):
            self.find_element(self.generalAddCustomerPage_saveCustomerBtn_loc).click()
        time.sleep(1)
        with allure.step("判断客户详情信息"):
            with allure.step("全部展开客户信息"):
                customerInfoShowBtnEles = self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index="all")
                for customerInfoShowBtnEle in customerInfoShowBtnEles:
                    customerInfoShowBtnEle.click()
                    time.sleep(0.5)
            with allure.step("展开联系人信息"):
                self.find_element(self.customerDetailPage_contactInfoShowBtn_loc).click()
            for data in customer_sendKeys:
                key = list(data.keys())[0]
                value = list(data.values())[0]
                if key != "姓名" and key != "职务":
                    with allure.step("获取：{}的信息，并判断".format(key)):
                        info = self.customerDetailPageCommon.get_customerInfo(xpath=key)
                        if key == "邮箱":
                            if value not in info:
                                raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key,value,info))
                        else:
                            if str(value) != info:
                                raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key,value,info))
                elif key == "姓名":
                    with allure.step("获取联系人的姓名，并判断是否正确"):
                        contactName = self.find_element(self.customerDetailPage_contactName_loc).text
                        if value != contactName:
                            raise Exception("输入的客户联系人姓名：{}，与客户详情里面的联系人姓名：{}，不一致".format(value,contactName))
                elif key == "职务":
                    with allure.step("获取联系人的职务，并判断是否正确"):
                        contactJob = self.find_element(self.customerDetailPage_contactJob_loc).text
                        if value != contactJob:
                            raise Exception("输入的客户联系人的职务：{}，与客户详情里面的联系人职务：{}，不一致".format(value,contactJob))
            for data in customer_selectKeys:
                key = list(data.keys())[0]
                value = list(data.values())[0]
                with allure.step("获取：{}的信息，并判断".format(key)):
                    info = self.customerDetailPageCommon.get_customerInfo(xpath=key)
                    if key == "国家/地区":
                        if value not in info:
                            raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key, value, info))
                    else:
                        if value != info:
                            raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key, value, info))


    def run_addAndEditMinorCustomerInfo_case(self,caseid,data):
        if data["is_add"]:
            operate = "新增"
        else:
            operate = "编辑"
        self.generalAddCustomerCommon.is_addCustomer(data["is_add"])
        time.sleep(2)
        if data["is_add"]:
            if caseid != 1 and caseid != 2:
                with allure.step("输入客户编码"):
                    customerInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("客户代码")
                    self.find_element(customerInput_loc).send_keys(random_number(20))
            with allure.step("输入客户名称"):
                customerName = random_name()+str(random_number(3)) + "测试，可删除"
                self.find_element(self.generalAddCustomerPage_customerNameInput_loc).send_keys(customerName)
            with allure.step("点击客户类型一级选择框"):
                customerType_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("客户类型")
                self.find_element(customerType_loc).click()
                time.sleep(0.3)
            with allure.step("选择第一个客户类型"):
                customerType_loc = self.generalAddCustomerCommon.generateXpathByCountryList("合作客户")
                self.find_element(customerType_loc).click()
                with allure.step("输入联系人姓名"):
                    contactNameInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("姓名")
                    self.find_element(contactNameInput_loc).send_keys("联系人测试")
        if caseid == 1 or caseid == 2:
            customerCode = self.generalAddCustomerCommon.generate_customerCode()
            print(customerCode)
        elif caseid == 3 or caseid == 4:
            with allure.step("点击主营产品一级选择框"):
                mainProductInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("主营产品")
                print(mainProductInput_loc)
                self.mouseClick(mainProductInput_loc)
            time.sleep(0.5)
            with allure.step("选择一个未被选中的主营产品"):
                self.find_element(self.generalAddCustomerPage_unSelectedMainProductList_loc).click()
            time.sleep(0.2)
            with allure.step("获取被选中的主营产品列表"):
                mailProductList = self.get_elementText(self.generalAddCustomerPage_selectedMainProductList_loc,index="all")
                print(mailProductList)
        elif caseid == 5 or caseid == 6:
            with allure.step("输入注释"):
                customerComment = random_text().replace("\n","")
                self.find_element(self.generalAddCustomerPage_commentTextarea_loc).clear()
                self.find_element(self.generalAddCustomerPage_commentTextarea_loc).send_keys(customerComment)
        elif caseid == 7 or caseid == 8:
            with allure.step("点击扩展信息里面的是否按钮"):
                self.find_element(self.generalAddCustomerPage_extendInfoIsBtn_loc).click()
            time.sleep(0.3)
            with allure.step("判断扩展信息里面的是否按钮是否被选中"):
                is_select = 0
                if "is-checked" in self.find_element(self.generalAddCustomerPage_extendInfoIsBtn_loc).get_attribute("class"):
                    is_select = 1
        elif caseid == 9 or caseid == 10:
            with allure.step("点击自定义数据字典里面的自定义按钮"):
                self.scroll_element(self.generalAddCustomerPage_extendInfoCustomBtn_loc)
                self.mouseClick(self.generalAddCustomerPage_extendInfoCustomBtn_loc)
        elif caseid == 11 or caseid == 12:
            with allure.step("点击自定义数据字典里面的字典按钮"):
                self.scroll_element(self.generalAddCustomerPage_extendInfoDictBtn_loc)
                self.mouseClick(self.generalAddCustomerPage_extendInfoDictBtn_loc)
        elif caseid == 13 or caseid == 14:
            with allure.step("点击日历按钮"):
                customer_pickerBtn_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("日期")
                self.mouseClick(customer_pickerBtn_loc)
            time.sleep(0.3)
            with allure.step("随机选中一个时间"):
                random_day = str(randint(10,20))
                customer_pickerDay_loc = (By.XPATH,self.generalAddCustomerPage_pickerDayBtn_loc[1].replace("26",random_day))
                self.mouseClick(customer_pickerDay_loc)
        elif caseid == 15 or caseid == 16:
            with allure.step("选择性别-男按钮"):
                self.scroll_element(self.generalAddCustomerPage_contactInfoMaleBtn_loc)
                self.mouseClick(self.generalAddCustomerPage_contactInfoMaleBtn_loc)
        elif caseid == 17 or caseid == 18:
            with allure.step("选择性别-女按钮"):
                self.scroll_element(self.generalAddCustomerPage_contactInfoFemaleBtn_loc)
                self.mouseClick(self.generalAddCustomerPage_contactInfoFemaleBtn_loc)
        elif caseid in (19,20):
            with allure.step("点击日历按钮"):
                customerContact_pickerBtn_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("生日")
                self.scroll_element(customerContact_pickerBtn_loc)
                self.mouseClick(customerContact_pickerBtn_loc)
                time.sleep(0.3)
                with allure.step("随机选中一个时间"):
                    random_day = str(randint(10, 20))
                    customerContact_pickerDay_loc = (
                    By.XPATH, self.generalAddCustomerPage_pickerDayBtn_loc[1].replace("26", random_day))
                    self.mouseClick(customerContact_pickerDay_loc)
        elif caseid == 21:
            with allure.step("点击业务员下拉框"):
                operatorBtn_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("业务员")
                self.mouseClick(operatorBtn_loc)
            time.sleep(0.3)
            with allure.step("选择云基础业务员"):
                cloudBaseOperator_loc = self.generalAddCustomerCommon.generateXpathByCountryList("云基础(dmktest_001)")
                print(cloudBaseOperator_loc)
                self.mouseClick(cloudBaseOperator_loc)
        elif caseid in (22,23):
            with allure.step("输入一个邮箱"):
                random_emailAccount = random_email()
                emailAccountInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("邮箱")
                self.find_element(emailAccountInput_loc).clear()
                self.find_element(emailAccountInput_loc).send_keys(random_emailAccount)
            with allure.step("点击联系人信息展开按钮"):
                self.find_element(self.generalAddCustomerPage_showOrHideContactBtn_loc).click()
            with allure.step("点击联系人启禁用按钮"):
                self.scroll_element(self.generalAddCustomerPage_contactStatusBtn_loc)
                self.mouseClick(self.generalAddCustomerPage_contactStatusBtn_loc)
            time.sleep(0.5)
            with allure.step("获取启禁用的状态"):
                contactStatus_attribute = self.find_element(self.generalAddCustomerPage_contactStatusBtn_loc).get_attribute("class")
        elif caseid in (24,25):
            with allure.step("上传一个附件"):
                attach_path = os.path.join(ATTACH_PATH,"5648215.jpg")
                print(attach_path)
                self.find_element_byPresence(self.generalAddCustomerPage_uploadAttachInput_loc).send_keys(attach_path)
                time.sleep(1)
        with allure.step("点击保存按钮"):
            self.find_element(self.generalAddCustomerPage_saveCustomerBtn_loc).click()
        time.sleep(2)
        if caseid == 1 or caseid == 2:
            with allure.step("判断新增或者重新编辑后的客户代码是否正确"):
                customerDetail_customerCode = self.find_element(self.customerDetailPage_customerCodeDetail_loc).text
                print(customerDetail_customerCode)
        elif caseid == 3 or caseid == 4:
            with allure.step("获取客户详情里面的主营产品"):
                customerDetail_mainProductList = []
                customerDetail_mainProduct_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("主营产品")
                customerDetail_mainProductText = self.find_element(customerDetail_mainProduct_loc).text
                if "," in customerDetail_mainProductText:
                    customerDetail_mainProductList = customerDetail_mainProductText.split(",")
                else:
                    customerDetail_mainProductList.append(customerDetail_mainProductText)
            with allure.step("判断主营产品是否一致"):
                if customerDetail_mainProductList != mailProductList:
                    raise Exception("客户详情里面的主营产品：{}，与{}时候选中的主营产品：{}，不一致".format(customerDetail_mainProductList,operate,mailProductList))
        elif caseid == 5 or caseid == 6:
            with allure.step("获取客户详情里面的注释"):
                customerDetail_comment_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("备注")
                customerDetail_comment = self.find_element(customerDetail_comment_loc).text
            with allure.step("判断备注是否一致"):
                if customerDetail_comment != customerComment:
                    raise Exception("客户详情里面的备注：{}，与{}时候，的备注：{}，不一致".format(customerDetail_comment,operate,customerComment))
        elif caseid == 7 or caseid == 8:
            with allure.step("点击扩展信息，以展开"):
                self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index=2).click()
            with allure.step("获取扩展信息里面的是否文本"):
                extendInfo_isOrNot_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("是否")
                print(extendInfo_isOrNot_loc)
                extendInfo_isOrNot_text = self.find_element(extendInfo_isOrNot_loc).text
            with allure.step("判断扩展信息里面的是否文本是否一致"):
                if is_select == 0:
                    if extendInfo_isOrNot_text != "否":
                        raise Exception("客户详情里面的是否文本：{}，与{}操作里面的勾选情况：{}，不一致".format(extendInfo_isOrNot_text,operate,is_select))
                else:
                    if extendInfo_isOrNot_text != "是":
                        raise Exception("客户详情里面的是否文本：{}，与{}操作里面的勾选情况：{}，不一致".format(extendInfo_isOrNot_text,operate,is_select))
        elif caseid == 9 or caseid == 10:
            with allure.step("点击扩展信息，以展开"):
                self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index=2).click()
            with allure.step("获取自定义数据字典里面的文本"):
                customerDetail_customData_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("自定义数据字典")
                customerDetail_customData_text = self.find_element(customerDetail_customData_loc).text
            with allure.step("判断选择的自定义数据字典是否一致"):
                if customerDetail_customData_text != "自定义":
                    raise Exception("客户详情里面的自定义数据字典文本：{}，与{}操作时候，选择的自定义按钮，不一致".format(customerDetail_customData_text,operate))
        elif caseid == 11 or caseid == 12:
            with allure.step("点击扩展信息，以展开"):
                self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index=2).click()
            with allure.step("获取自定义数据字典里面的文本"):
                customerDetail_customData_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("自定义数据字典")
                customerDetail_customData_text = self.find_element(customerDetail_customData_loc).text
            with allure.step("判断选择的自定义数据字典是否一致"):
                if customerDetail_customData_text != "字典":
                    raise Exception("客户详情里面的自定义数据字典文本：{}，与{}操作时候，选择的字典按钮，不一致".format(customerDetail_customData_text,operate))
        elif caseid == 13 or caseid == 14:
            with allure.step("点击扩展信息，以展开"):
                self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index=2).click()
            with allure.step("获取扩展信息里面的日期"):
                extendInfo_pickDay_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("日期")
                customerDetail_pickDay_text = self.find_element(extendInfo_pickDay_loc).text
            with allure.step("判断扩展信息里面的日期是否一致"):
                customer_pickerDate = time.strftime("%Y-%m-")+random_day
                if customerDetail_pickDay_text != customer_pickerDate:
                    raise Exception("客户详情里面的日期：{}，与{}操作时候，选中的日期：{}，不一致".format(customerDetail_pickDay_text,operate,customer_pickerDate))
        elif caseid in (15,16,17,18,19,20):
            with allure.step("点击联系人展开按钮"):
                self.find_element(self.customerDetailPage_contactInfoShowBtn_loc).click()
            if caseid in (15, 16, 17, 18):
                with allure.step("获取联系人信息里面的性别"):
                    customerDetail_contactGender_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("性别")
                    customerDetail_contactGender_text = self.find_element(customerDetail_contactGender_loc).text
                    if caseid == 15 or caseid == 16:
                        with allure.step("判断联系人的性别是否是男"):
                            if customerDetail_contactGender_text != "男":
                                raise Exception("客户详情里面的性别：{}，与{}操作时候选择的性别,男，不一致".format(customerDetail_contactGender_text,operate))
                    elif caseid == 17 or caseid == 18:
                        with allure.step("判断联系人的性别是否是男"):
                            if customerDetail_contactGender_text != "女":
                                raise Exception("客户详情里面的性别：{}，与{}操作时候选择的性别,男，不一致".format(customerDetail_contactGender_text,operate))
            elif caseid in (19,20):
                with allure.step("获取扩展信息里面的日期"):
                    contactInfo_pickDay_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("生日")
                    customerDetail_ontact_pickDay_text = self.find_element(contactInfo_pickDay_loc).text
                with allure.step("判断扩展信息里面的日期是否一致"):
                    customer_pickerDate = time.strftime("%Y-%m-") + random_day
                    if customerDetail_ontact_pickDay_text != customer_pickerDate:
                        raise Exception("客户联系人详情里面的日期：{}，与{}操作时候，选中的日期：{}，不一致".format(customerDetail_ontact_pickDay_text, operate,customer_pickerDate))
        elif caseid == 21:
            with allure.step("展开管理信息tab"):
                self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index=1).click()
            with allure.step("获取业务员信息文本"):
                customerDetail_companyInfoOperator_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("业务员")
                customerDetail_companyInfoOperator_text = self.get_elementText(customerDetail_companyInfoOperator_loc)
            with allure.step("判断客户详情里面的业务员信息是否正确"):
                if customerDetail_companyInfoOperator_text != "云基础":
                    raise Exception("客户详情里面的业务员：{}，与编辑时候的业务员：云基础，不一致".format(customerDetail_companyInfoOperator_text))
        elif caseid in (22,23):
            with allure.step("展开联系人信息"):
                self.find_element(self.customerDetailPage_contactInfoShowBtn_loc).click()
            with allure.step("获取联系人状态"):
                contactStatus_loc = self.customerDetailPageCommon.generateXpathByCustomerCodeDetail("状态")
                contactStatus_text = self.find_element(contactStatus_loc).text
            with allure.step("判断联系人状态是否正确"):
                if "is-checked" in contactStatus_attribute:
                    if contactStatus_text != "启用":
                        raise Exception("客户详情里面，联系人的状态：{}，与{}操作时候选择的状态：{}，不一致".format(contactStatus_text,operate,contactStatus_attribute))
                    with allure.step("点击写邮件"):
                        self.find_element(self.customerDetailPage_writeMailBtn_loc).click()
                    time.sleep(1)
                    with allure.step("获取写邮件页面的收件人"):
                        recepient_text = self.find_element(self.customerDetailPage_recipent_loc).text
                    with allure.step("判断收件人是否被带到写信页面"):
                        if random_emailAccount not in recepient_text:
                            raise Exception("联系人邮箱未带到写信页面")
                else:
                    if contactStatus_text != "停用":
                        raise Exception("客户详情里面，联系人的状态：{}，与{}操作时候选择的状态：{}，不一致".format(contactStatus_text,operate,contactStatus_attribute))
                    time.sleep(1)
                    with allure.step("点击写邮件"):
                        self.find_element(self.customerDetailPage_writeMailBtn_loc).click()
                    with allure.step("获取toast提示"):
                        toast_text = self.find_element(self.toast_loc).text
                    with allure.step("判断toast提示是否正确"):
                        if toast_text != "没有联系人邮箱，或已禁用":
                            raise Exception("禁用联系人邮箱后，点击写邮件后的toast：{}，提示不对".format(toast_text))
        elif caseid in (24,25):
            with allure.step("点击文件按钮"):
                self.find_element(self.customerDetailPage_fileBtn_loc).click()
            with allure.step("获取所有的附件名"):
                allAttachNames = self.get_elementText(self.customerDetailPage_attachName_loc,index="all")
            with allure.step("判断上传的附件是否在客户详情里面"):
                if "5648215.jpg" not in allAttachNames:
                    raise Exception("客户详情里面的附件：{}，不包含{}操作时候，上传的附件:5648215.jpg".format(allAttachNames))


    def run_addCustomerContact_case(self,data):
        self.generalAddCustomerCommon.is_addCustomer(data["is_add"])
        if data["is_add"]:
            self.generalAddCustomerCommon.write_needfulCustomerInfo()
        with allure.step("点击联系人新增按钮"):
            self.scroll_element(self.generalAddCustomerPage_addContactBtn_loc)
            time.sleep(0.3)
            # self.find_element(self.generalAddCustomerPage_addContactBtn_loc).click()
            self.mouseClick(self.generalAddCustomerPage_addContactBtn_loc)
        with allure.step("输入联系人姓名"):
            random_contactName = random_name()+"测试"
            contactNameInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("姓名")
            self.find_element(contactNameInput_loc).send_keys(random_contactName)
        with allure.step("点击保存按钮"):
            self.find_element(self.generalAddCustomerPage_saveCustomerBtn_loc).click()
        time.sleep(1)
        with allure.step("判断新增的联系人是否在客户详情中"):
            with allure.step("获取客户详情里面的联系人姓名"):
                allCustomerNames_customerDetail = self.get_elementText(self.customerDetailPage_contactName_loc,index="all")
            with allure.step("判断新增的联系人姓名是否在客户详情中"):
                if random_contactName not in allCustomerNames_customerDetail:
                    raise Exception("客户详情的联系人姓名中：{}，没有新增的联系人姓名：{}".format(allCustomerNames_customerDetail,random_contactName))

    #del_num,0,删除当前单个，1，删除选中的多个，2，删除全部
    def run_delCustomerContact_case(self,data):
        self.generalAddCustomerCommon.is_addCustomer(data["is_add"])
        with allure.step("判断联系人个数是否大于1"):
            with allure.step("获取联系人个数"):
                customerContactEle = self.find_element_byPresence(self.generalAddCustomerPage_contactCard_loc,index="all")
            if len(customerContactEle) == 1:
                with allure.step("新增一个联系人"):
                    self.scroll_element(self.generalAddCustomerPage_addContactBtn_loc)
                    time.sleep(0.5)
                    self.find_element(self.generalAddCustomerPage_addContactBtn_loc).click()
                with allure.step("输入联系人姓名"):
                    random_contactName = random_name()+"测试"
                    contactNameInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("姓名")
                    self.find_element_byPresence(contactNameInput_loc).send_keys(random_contactName)
                with allure.step("点击保存按钮"):
                    self.find_element(self.generalAddCustomerPage_saveCustomerBtn_loc).click()
                time.sleep(1)
                with allure.step("点击编辑按钮"):
                    self.find_element(self.customerDetailPage_customerEditBtn_loc).click()
        if data["del_num"] == 2:
            with allure.step("点击全选按钮"):
                self.scroll_element(self.generalAddCustomerPage_selectAllContactCheckboxBtn_loc)
                time.sleep(0.5)
                self.mouseClick(self.generalAddCustomerPage_selectAllContactCheckboxBtn_loc)
            with allure.step("点击删除按钮"):
                self.find_element(self.generalAddCustomerPage_delSeveralContactBtn_loc).click()
            with allure.step("点击确定删除按钮"):
                self.find_element(self.generalAddCustomerPage_sureDelContactBtn_loc).click()
            with allure.step("获取联系人卡片的数量,并判断"):
                customerContactEle = self.find_element_byPresence(self.generalAddCustomerPage_contactCard_loc,index="all")
                if len(customerContactEle) != 1:
                    with allure.step("新增一个联系人"):
                        raise Exception("全部删除之后，有多于1个联系人卡片存在")
            with allure.step("输入联系人姓名"):
                random_contactName = random_name() + "测试"
                contactNameInput_loc = self.generalAddCustomerCommon.generateXpathByCustomerName("姓名")
                self.find_element_byPresence(contactNameInput_loc).send_keys(random_contactName)
        elif data["del_num"] == 1:
            with allure.step("获取最后一个联系人姓名"):
                singleDel_contactName = self.find_element_byPresence(self.generalAddCustomerPage_customerNameInput_loc,index=-1).get_attribute("value")
            with allure.step("选中最后一个联系人卡片"):
                self.scroll_element(self.generalAddCustomerPage_contactCard_loc)
                time.sleep(0.3)
                self.find_element(self.generalAddCustomerPage_contactCard_loc,index=-1).click()
            with allure.step("点击删除按钮"):
                self.find_element(self.generalAddCustomerPage_delSeveralContactBtn_loc).click()
            with allure.step("点击确定删除按钮"):
                self.find_element(self.generalAddCustomerPage_sureDelContactBtn_loc).click()
        else:
            with allure.step("获取第一个联系人姓名"):
                singleDel_contactName = self.find_element_byPresence(self.generalAddCustomerPage_customerNameInput_loc,index=-1).get_attribute("value")
            with allure.step("悬浮第一个联系人卡片"):
                self.scroll_element(self.generalAddCustomerPage_contactCard_loc)
                time.sleep(0.3)
                self.mouseHover(self.generalAddCustomerPage_contactCard_loc)
            with allure.step("点击删除按钮"):
                self.mouseClick(self.generalAddCustomerPage_delCurrentContactBtn_loc)
            with allure.step("点击确定删除按钮"):
                self.find_element(self.generalAddCustomerPage_sureDelContactBtn_loc).click()
        with allure.step("点击保存按钮"):
            self.find_element(self.generalAddCustomerPage_saveCustomerBtn_loc).click()
        time.sleep(1)
        with allure.step("获取所有客户详情里面的联系人姓名"):
            allcustomerName_customerDetail = self.get_elementText(self.customerDetailPage_contactName_loc,index="all")
        if data["del_num"] == 2:
            with allure.step("判断客户详情里面的联系人是不是只有一个"):
                contactNames = []
                contactNames.append(random_contactName)
                if allcustomerName_customerDetail != contactNames:
                    raise Exception("客户详情中的联系人姓名：{}，与全部删除后，重新添加的联系人姓名：{}，不一致".format(allcustomerName_customerDetail,random_contactName))
        else:
            with allure.step("判断删除的联系人是否还在客户详情中"):
                if singleDel_contactName in allcustomerName_customerDetail:
                    raise Exception("客户详情的联系人：{}，包含了删除的联系人：{}".format(allcustomerName_customerDetail,singleDel_contactName))


    #is_save,1,保存并新建，2，取消保存弹窗，是，3，取消保存弹窗，否.4，取消保存弹窗，取消
    def run_saveAndAddCustomer_case(self,data):
        self.generalAddCustomerCommon.is_addCustomer(data["is_add"])
        if data["is_add"]:
            self.generalAddCustomerCommon.write_needfulCustomerInfo()
        else:
            with allure.step("重新输入客户名称"):
                self.find_element(self.generalAddCustomerPage_customerNameInput_loc).clear()
                time.sleep(0.3)
                self.find_element(self.generalAddCustomerPage_customerNameInput_loc).send_keys(random_name()+str(random_number(3))+"测试，可删除")
        with allure.step("获取客户名称"):
            _customerName = self.find_element(self.generalAddCustomerPage_customerNameInput_loc).get_attribute("value")
        if data["is_save"] == 1:
            with allure.step("点击保存并新建按钮"):
                self.find_element(self.generalAddCustomerPage_saveAndAddCustomerBtn_loc).click()
            with allure.step("获取客户名称,查看是否清空"):
                _new_customerName = self.find_element(self.generalAddCustomerPage_customerNameInput_loc).get_attribute("value")
                if _new_customerName:
                    raise Exception("点击保存并新建后，客户信息：{}，没有清空".format(_new_customerName))
        else:
            with allure.step("点击取消按钮"):
                self.find_element(self.generalAddCustomerPage_cancelSaveCustomerBtn_loc).click()
            if data["is_save"] == 2:
                self.find_element(self.fastAddCustomerPage_isSaveBtn_loc).click()
            elif data["is_save"] == 3:
                self.find_element(self.fastAddCustomerPage_notSaveBtn_loc).click()
            elif data["is_save"] == 4:
                self.find_element(self.fastAddCustomerPage_cancelSaveBtn_loc).click()
        time.sleep(1)
        with allure.step("切换到客户tab"):
            self.find_element(self.generalAddCustomerPage_customerTabBtn_loc).click()
        with allure.step("点击更多按钮"):
            self.find_element(self.customerPage_moreBtn_loc).click()
        time.sleep(0.5)
        with allure.step("点击刷新按钮"):
            self.find_element(self.customerPage_refreshBtn_loc).click()
        with allure.step("获取所有的客户名"):
            _allCustomerNames = self.get_elementText(self.customerPage_customerName_loc, index="all")
        if data["is_save"] in (1,2):
            with allure.step("判断保存的客户是否在列表中"):
                if _customerName not in _allCustomerNames:
                    raise Exception("客户列表中：{}，没有保存的客户：{}".format(_allCustomerNames, _customerName))
        else:
            with allure.step("判断保存的客户是否在列表中"):
                if _customerName in _allCustomerNames:
                    raise Exception("客户列表中：{}，有未保存的客户：{}".format(_allCustomerNames, _customerName))
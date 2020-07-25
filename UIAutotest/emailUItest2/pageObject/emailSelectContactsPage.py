# -*- encoding: utf-8 -*-
'''
@File    :   emailSelectContactsPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/30 0030 19:41   dmk      1.0         None
'''

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .emailWriteMailPage import emailWriteMailPage

class emailSelectContactsPage(emailWriteMailPage):
    #添加收件人按钮
    addReceiptBtn_loc = (By.XPATH,"//div[@class='addressee_input_item b_line i_item addressee']//div[@class='addIcon']")
    #客户tab
    customerTab_loc = (By.XPATH,"//div[@id='tab-first']")
    #供应商tab
    supplierTab_loc = (By.XPATH,"//div[@id='tab-second']")
    #内部联系人tab
    internalContactTab_loc = (By.XPATH,"//div[@id='tab-third']")
    #用户组按钮
    userGroup_loc = (By.XPATH,"//div[@id='pane-third']//label[@tabindex='-1']")
    #用户组列表
    userGroupList_loc = (By.XPATH,'//div[@class="inner-panel"]//div[@class="e_l_item"]')
    #内部联系人搜索框
    internalContactSearchInput_loc = (By.XPATH,"//div[@id='pane-third']//input[@placeholder='联系人姓名、账号']")
    #内部联系人搜索按钮
    internalContactSearchBtn_loc = (By.XPATH,"//div[@id='pane-third']//span[@class='el-input__suffix-inner']")
    #内部联系人列表
    internalContactList_loc = (By.XPATH,"//div[@id='pane-third']//tbody//tr")
    #公海客户
    public_loc = (By.XPATH,"//label[text()='搜索范围']/following-sibling::div//label[2]")
    #共享按钮
    shareBtn_loc = (By.XPATH,"//label[text()='是否含共享']/following-sibling::div//label[1]")
    #客户名称
    customerName_loc = (By.XPATH,"//input[@placeholder='请输入客户名称']")
    #联系人名称
    customerReleatedName_loc = (By.XPATH,"//div[@id='pane-first']//input[@placeholder='请输入联系人名称']")
    #未联系天数
    unreleated_loc = (By.XPATH,"//div[@title='未联系天数']//input")
    #最近7天
    latelySevenDays_loc = (By.XPATH,"//span[text()='最近七天']")
    #跟进阶段
    followStatus_loc = (By.XPATH,"//div[@title='跟进阶段']//input")
    #签订协议
    signAggrement_loc = (By.XPATH,"//span[text()='产品推广']")
    #供应商名称
    supplierName_loc = (By.XPATH,"//input[@placeholder='请输入供应商名称']")
    #供应商类型
    supplierType_loc = (By.XPATH,"//div[@title='供应商类型']//input")
    #代理商
    agency_loc = (By.XPATH,"//span[text()='代理商']")
    #供应商标签
    supplierTag_loc = (By.XPATH,"//div[@title='供应商标签']//input")
    #红色
    blue_loc = (By.XPATH,"//span[text()='红色']")
    #供应商搜索按钮
    supplierSearchBtn_loc = (By.XPATH,"//div[@id='pane-second']//button[@class='el-button el-button--primary el-button--mini']")
    #客户搜索按钮
    customerSearchBtn_loc = (By.XPATH,"//div[@id='pane-first']//button[@class='el-button el-button--primary el-button--mini']")
    #重新搜索
    researchBtn_loc = (By.XPATH,"//span[@class='a_fc01 f12 again-search']")
    #供应商重置按钮
    supplierReSettingSearchBtn_loc = (By.XPATH,"//div[@id='pane-second']//button[@class='el-button el-button--default el-button--mini']")
    #客户重置按钮
    customerReSettingSearchBtn_loc = (By.XPATH,"//div[@id='pane-first']//button[@class='el-button el-button--default el-button--mini']")
    #联系人数量
    releatedTotalNum_loc = (By.XPATH,"//div[@id='pane-first']//span[@class='el-pagination__total']")
    #供应商联系人数量
    supplierReleatedTotalNum_loc = (By.XPATH,"//div[@id='pane-second']//span[@class='el-pagination__total']")
    #客户联系人数量
    customerReleatedTotalNum_loc = (By.XPATH,"//div[@id='pane-first']//span[@class='el-pagination__total']")
    #客户联系人邮箱账号列表
    customerAccountList_loc = (By.XPATH,"//div[@id='pane-first']//tbody//tr/td[3]")
    #供应商联系人邮箱账号列表
    supplierAccountList_loc = (By.XPATH,"//div[@id='pane-second']//tbody//tr/td[3]")
    #内部联系人邮箱账号列表
    internalAccountList_loc = (By.XPATH,"//div[@id='pane-third']//tbody//tr/td[2]")
    #选中的收件人列表
    selectedReceiptList_loc = (By.XPATH,'//span[@class="li-name"]')

    def __init__(self,driver):
        super(emailSelectContactsPage,self).__init__(driver)
        # # 点击新增收件人按钮
        self.find_element(self.addReceiptBtn_loc).click()
        # self.screenshotImg(key="联系人搜索")

    def run_resettingSearch_case(self):
        #输入客户名字
        self.find_element(self.customerName_loc).send_keys("test")
        #点击搜索
        self.find_element(self.customerSearchBtn_loc).click()
        #点击重新搜索
        time.sleep(0.5)
        print(self.find_element(self.researchBtn_loc,index="all"))
        self.find_element(self.researchBtn_loc).click()
        #点击重置按钮
        self.find_element(self.customerReSettingSearchBtn_loc).click()
        #点击联系天数
        self.find_element(self.unreleated_loc).click()
        #判断是否有最近7天的标签
        time.sleep(0.5)
        if self.is_element_exist(self.latelySevenDays_loc[1]):
            self.find_element(self.latelySevenDays_loc).click()
        else:
            raise Exception("重置条件之后。最近联系天数下拉框没有最近联系7天选项")
        #点击跟进阶段
        time.sleep(0.5)
        self.find_element(self.followStatus_loc).click()
        if self.is_element_exist(self.signAggrement_loc[1]):
            self.find_element(self.signAggrement_loc).click()
            self.find_element(self.customerSearchBtn_loc).click()
        else:
            raise Exception("重置条件之后。跟进阶段下拉框没有产品推广选项")


        #点击供应商tab
        self.find_element(self.supplierTab_loc).click()
        #输入供应商名字
        self.find_element(self.supplierName_loc).send_keys("测试")
        #点击搜索
        self.find_element(self.supplierSearchBtn_loc).click()
        #点击重新搜索
        time.sleep(0.5)
        print(self.find_element(self.researchBtn_loc,index="all"))
        self.find_element(self.researchBtn_loc).click()
        #点击重置
        self.find_element(self.supplierReSettingSearchBtn_loc).click()
        #点击供应商标签
        # self.find_element(self.supplierTag_loc).click()
        # if self.is_element_exist(self.blue_loc[1]):
        #     self.find_element(self.blue_loc).click()
        # else:
        #     raise Exception("重置条件之后。供应商标签下拉框没有红色选项")
        #点击供应商类型
        self.find_element(self.supplierType_loc).click()
        if self.is_element_exist(self.agency_loc[1]):
            self.find_element(self.agency_loc).click()
            self.find_element(self.supplierSearchBtn_loc).click()
        else:
            raise Exception("重置条件之后。供应商类型下拉框没有代理商选项")


    def run_customerSearch_case(self,casename,is_public,is_send,is_select,sendInput,key,selectTag,option,is_click,click_btn):
        #首先判断是否是公海搜索
        if is_public:
            self.find_element(self.public_loc).click()
        #点击搜索按钮，获取全部的用户联系人数量
        self.find_element(self.customerSearchBtn_loc).click()
        time.sleep(0.2)
        customerTotalNum = self.find_element(self.customerReleatedTotalNum_loc).text
        print(customerTotalNum)
        #点击重新搜索
        self.find_element(self.researchBtn_loc).click()
        if is_public:
            self.find_element(self.public_loc).click()
        if is_send:
            sendInput = ('xpath',str(sendInput))
            self.find_element(sendInput).send_keys(key)
        if is_select:
            selectTag = ('xpath',str(selectTag))
            option = ('xpath', str(option))
            self.scroll_element(selectTag)
            time.sleep(0.2)
            self.find_element(selectTag).click()
            time.sleep(0.5)
            self.find_element(option).click()
            self.find_element(self.customerTab_loc).click()
        if is_click:
            time.sleep(1)
            click_btn = ('xpath',str(click_btn))
            # self.find_element(click_btn).send_keys(Keys.ENTER)
            ele = self.find_element(click_btn)
            js = "arguments[0].scrollIntoView();"
            self.driver.execute_script(js,ele)
            time.sleep(1)
            ele.click()
        #再次点击搜索，获取联系人数量
        self.find_element(self.customerSearchBtn_loc).click()
        time.sleep(1)
        if self.is_element_exist(self.releatedTotalNum_loc[1]):
            reSearchCustomerTotalNum = self.find_element(self.releatedTotalNum_loc).text
            if reSearchCustomerTotalNum == customerTotalNum:
                raise Exception("按照这个条件：{}，搜索客户联系人无效！".format(casename))


    def run_supplieerSearch_case(self,casename,is_send,is_select,sendInput,key,selectTag,option,is_click,click_btn):
        #点击进入供应商tab
        self.find_element(self.supplierTab_loc).click()
        #点击搜索按钮，获取全部的用户联系人数量
        self.find_element(self.supplierSearchBtn_loc).click()
        supplierTotalNum = self.find_element(self.supplierReleatedTotalNum_loc).text
        print(supplierTotalNum)
        #点击重新搜索
        self.find_element(self.researchBtn_loc,index="all")[-1].click()
        if is_send:
            sendInput = ('xpath',str(sendInput))
            self.find_element(sendInput).send_keys(key)
        if is_select:
            selectTag = ('xpath',str(selectTag))
            option = ('xpath', str(option))
            self.find_element(selectTag).click()
            time.sleep(0.5)
            self.find_element(option).click()
            time.sleep(0.5)
            #判断下拉框是否消失，不消失，强制消失
            if self.is_element_exist(option[1]):
                print("下拉框没有消失")
                self.find_element(self.supplierTab_loc).click()
        if is_click:
            time.sleep(1)
            click_btn = ('xpath',str(click_btn))
            # self.find_element(click_btn).send_keys(Keys.ENTER)
            ele = self.find_element(click_btn)
            js = "arguments[0].scrollIntoView();"
            self.driver.execute_script(js,ele)
            time.sleep(1)
            ele.click()
        #再次点击搜索，获取联系人数量
        self.find_element(self.supplierSearchBtn_loc).click()
        time.sleep(1)
        if self.is_element_exist(self.supplierReleatedTotalNum_loc[1]):
            reSearchCustomerTotalNum = self.find_element(self.supplierReleatedTotalNum_loc).text
            print(reSearchCustomerTotalNum)
            if reSearchCustomerTotalNum == supplierTotalNum:
                raise Exception("按照这个条件：{}，搜索供应商联系人无效！".format(casename))


    def run_internalContactSearch_case(self,is_userGroup,key):
        #点击内部联系人tab
        self.find_element(self.internalContactTab_loc).click()
        #判断是否是用户组还是联系人
        time.sleep(0.5)
        if is_userGroup:
            self.find_element(self.userGroup_loc).click()
        #搜索框输入关键词
        self.find_element(self.internalContactSearchInput_loc).send_keys(key)
        time.sleep(1)
        self.find_element(self.userGroupList_loc).click()
        internalContactLists = self.is_element_exist(self.internalContactList_loc[1])
        if internalContactLists:
            for internalContactList in internalContactLists:
                print(internalContactList.text)
                if key not in internalContactList.text:
                    raise Exception("内部联系人搜索结果异常，搜索结果:{},不包含关键词：{}".format(internalContactList.text,key))


    #客户，供应商，内部联系人选中与取消选中
    def run_internalContactSelectAndCancelSelect_case(self,contact_type):
        #根据联系人类型来选择联系人
        if contact_type == "1":
            #点击客户搜索按钮
            self.find_element(self.customerSearchBtn_loc).click()
            #获取第一个客户联系人,并点击
            time.sleep(0.5)
            firstCustomerContactElement = self.find_element(self.customerAccountList_loc)
            firstCustomerContactAccount = firstCustomerContactElement.text
            print(firstCustomerContactAccount)
            firstCustomerContactElement.click()
            #获取右侧收件人列表是否有选中的联系人
            if firstCustomerContactAccount != self.find_element(self.selectedReceiptList_loc).text:
                self.screenshotImg(key="选中一个客户联系人")
                raise Exception("选中的客户联系人：{}，没有带到右边的收件人列表".format(firstCustomerContactAccount))
            #再次点击第一个客户联系人
            self.find_element(self.customerAccountList_loc).click()
            time.sleep(0.5)
            if EC.visibility_of_any_elements_located(self.selectedReceiptList_loc)(self.driver):
                self.screenshotImg(key="取消选中一个客户联系人")
                raise Exception("取消选中客户联系人:{}，右边的收件人列表中依然存在".format(firstCustomerContactAccount))
        elif contact_type == "2":
            #点击供应商tab
            time.sleep(0.5)
            self.find_element(self.supplierTab_loc).click()
            #点击客户搜索按钮
            self.find_element(self.supplierSearchBtn_loc).click()
            #获取第一个客户联系人,并点击
            time.sleep(0.5)
            firstCustomerContactElement = self.find_element(self.supplierAccountList_loc)
            firstCustomerContactAccount = firstCustomerContactElement.text
            firstCustomerContactElement.click()
            #获取右侧收件人列表是否有选中的联系人
            if firstCustomerContactAccount != self.find_element(self.selectedReceiptList_loc).text:
                self.screenshotImg(key="选中一个供应商联系人")
                raise Exception("选中的供应商联系人：{}，没有带到右边的收件人列表".format(firstCustomerContactAccount))
            #再次点击第一个客户联系人
            self.find_element(self.supplierAccountList_loc).click()
            time.sleep(0.5)
            if EC.visibility_of_any_elements_located(self.selectedReceiptList_loc)(self.driver):
                self.screenshotImg(key="取消选中一个供应商联系人")
                raise Exception("取消选中供应商联系人:{}，右边的收件人列表中依然存在".format(firstCustomerContactAccount))
        elif contact_type == "3":
            #点击内部联系人tab
            time.sleep(0.5)
            self.find_element(self.internalContactTab_loc).click()
            #获取第一个内部联系人,并点击
            time.sleep(0.5)
            # firstCustomerContactElement = self.find_element(self.internalAccountList_loc)
            # firstCustomerContactAccount = firstCustomerContactElement.text
            # firstCustomerContactElement.click()
            firstCustomerContactAccount = self.get_elementText(self.internalAccountList_loc)
            self.click_ele(self.internalAccountList_loc)
            #获取右侧收件人列表是否有选中的联系人
            if "管理员<fttx222@aliyun.com>" != self.find_element(self.selectedReceiptList_loc).text:
                self.screenshotImg(key="选中一个内部联系人")
                raise Exception("选中的内部联系人：{}，没有带到右边的收件人列表".format(firstCustomerContactAccount))
            #再次点击第一个客户联系人
            self.find_element(self.internalAccountList_loc).click()
            time.sleep(0.5)
            if EC.visibility_of_any_elements_located(self.selectedReceiptList_loc)(self.driver):
                self.screenshotImg(key="取消选中一个内部联系人")
                raise Exception("取消选中内部联系人:{}，右边的收件人列表中依然存在".format(firstCustomerContactAccount))
# -*- encoding: utf-8 -*-
'''
@File    :   emailAccountSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 10:57   dmk      1.0         None
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .emailSettingPage import emailSettingPage


class emailAccountSettingPage(emailSettingPage):
    #添加账号按钮
    addAcount_loc = (By.XPATH,"//button[@class='el-button add_account el-button--primary']")
    #账号输入框
    accountInput_loc = (By.XPATH,"//input[@placeholder='请输入E-mail地址']")
    #密码输入框
    passwordInput_loc = (By.XPATH,"//input[@placeholder='请输入邮箱密码或授权码']")
    #保存账号按钮
    saveAccount_loc = (By.XPATH,"//div[@class='el-form-item__content']//button[3]")
    #再次保存账号按钮
    reSaveAccount_loc = (By.XPATH,"//div[@class='btnWrap']//button[@class='el-button el-button--primary']")
    #账号列表
    accountList_loc = (By.XPATH,"//span[@class='account']")
    #手动设置
    manualSetting_loc = (By.XPATH,"//span[text()='手动设置']")
    #删除按钮
    delAccont_loc = (By.XPATH,"//li[contains(@class,'cursorMove active')]//span[@class='icon-btn']/span")
    # 确定删除按钮
    sureDelBtn_loc = (By.XPATH,"//button[@class='el-button el-button--default el-button--small el-button--primary ']")
    #确定删除toast文本
    sureDelToast_loc = (By.XPATH,"//div[@class='el-message-box__message']//p")
    #账号已默认按钮
    defaultedActBtn_loc = (By.XPATH,"//span[@class='i-default visible']")
    #默认发件人
    defaultSender_loc = (By.XPATH,"//input[@placeholder='请选择发件人']")
    #发件人昵称
    senderNick_loc = (By.XPATH,"//input[@placeholder='请输入发件用昵称']")
    #人员信息
    showOperator_loc = (By.XPATH,"//div[@class='sale-select']//input")
    l = (By.XPATH,"//span[text()='fangwang@hotmail.com']/../following-sibling::span[2]/span[2]")
    #收件服务器
    receiptServerInput_loc = (By.XPATH,'//div[@class="el-form-item item-popPort"]//label')
    #收件服务器端口
    receiptServerPort_loc = (By.XPATH,'//div[@class="el-form-item item-popPort"]//div[@class="JOINF el-input"]//input')
    #发件服务器
    sendServerInput_loc = (By.XPATH,"//div[contains(@class,'is-required') and contains(@class,'item-smtpPort')]//label")
    #发件服务器端口
    sendServerPort_loc = (By.XPATH,'//div[contains(@class,"is-required") and contains(@class,"item-smtpPort")]//div[@class="JOINF el-input"]//input')



    def runcase(self,username,password):
        #进入设置页面
        self.click_settingBtn()
        self.screenshotImg(key="初次进入设置页面")
        #点击添加账号按钮
        time.sleep(1)
        self.find_element(self.addAcount_loc).click()
        #输入账号
        time.sleep(0.5)
        self.find_element(self.accountInput_loc).send_keys(username)
        #输入密码
        self.find_element(self.passwordInput_loc).send_keys(password)
        # #点击保存
        self.find_element(self.saveAccount_loc).click()
        #再次保存
        self.find_element(self.reSaveAccount_loc).click()


    #获取账号列表
    def get_accountList(self):
        time.sleep(1)
        # if EC.invisibility_of_element_located(self.manualSetting_loc)(driver):
        return self.get_elementText(self.accountList_loc,index="all")

    def del_account(self,username):
        # 添加的账号
        addedAccount_loc = (By.XPATH,"//ul[@class='account-list']//span[text()='{}']".format(username))
        #悬浮新增的账号
        self.mouseHover(addedAccount_loc)
        #点击删除
        time.sleep(0.2)
        self.mouseClick(self.delAccont_loc)
        #点击确定
        self.find_element(self.sureDelBtn_loc).click()

    def run_defaultAccount_case(self,caseid,account):
        #进入设置页面
        self.click_settingBtn()
        #判断当前是否有默认账号
        self.accountList = self.get_accountList()
        if caseid == "1":
            if self.is_element_exist(self.defaultedActBtn_loc[1]):
                self.find_element(self.defaultedActBtn_loc).click()
        else:
            #设置默认账号
            loc = (By.XPATH,"//ul[@class='account-list']//span[text()='{}']".format(account))
            print(loc)
            # 账号设置默认按钮
            defaultActBtn_loc = (By.XPATH, "//ul[@class='account-list']//span[text() = '{}'] /../ following-sibling::span[1]".format(account))
            print(defaultActBtn_loc)
            self.mouseHover(loc)
            self.find_element(defaultActBtn_loc).click()
        #切换到邮件首页，进入写信页面
        self.find_element(self.emailHomePage_loc).click()
        #进入写信页面
        self.find_element(self.writeEmail_loc).click()
        if caseid == "2":
            return account
        else:
            return self.accountList[0]


    #获取写信页面的默认的发件账号
    def get_defaultSender(self):
        time.sleep(2)
        if self.is_element_exist("//button[@class='el-button item send f12 el-button--primary']"):
            print("页面加载完成")
            return self.find_element(self.defaultSender_loc).get_attribute("value")
        else:
            time.sleep(2)
            print("等待2s在获取元素")
            return self.find_element(self.defaultSender_loc).get_attribute("value")

    def run_emailAccountNickName_case(self,username,password,has_nick,nick_name):
        #进入设置页面
        self.click_settingBtn()
        #点击添加账号按钮
        time.sleep(1)
        self.find_element(self.addAcount_loc).click()
        #输入账号
        time.sleep(0.5)
        self.find_element(self.accountInput_loc).send_keys(username)
        #输入密码
        self.find_element(self.passwordInput_loc).send_keys(password)
        # #点击保存
        self.find_element(self.saveAccount_loc).click()
        if has_nick:
            self.find_element(self.senderNick_loc).send_keys(nick_name)
            self.find_element(self.reSaveAccount_loc).click()

    #获取写信页面的发件账号
    def get_sender(self,username,has_nick,nick_name):
        #切换到邮件首页，进入写信页面
        self.find_element(self.emailHomePage_loc).click()
        #进入写信页面
        self.find_element(self.writeEmail_loc).click()
        time.sleep(3)
        #点击发件人
        self.find_element(self.defaultSender_loc).click()
        #判断是否有昵称
        if has_nick:
            username = nick_name + "<" + username + ">"
        else:
            nick = username.split("@")[0]
            username = nick + "<" + username + ">"
        #获取发件账号
        loc = ("//div[@x-placement='top-start']//span[text()='{}']".format(username))
        loc_xpath = (By.XPATH,loc)
        if self.is_element_exist(loc):
            return self.find_element(loc_xpath).text
        else:
            print("没有找到该发件账号：{}".format(username))
            return False

    def run_operatorShow_case(self):
        #进入设置页面
        self.click_settingBtn()
        #获取人员信息
        time.sleep(2)
        return self.find_element(self.showOperator_loc).get_attribute("value")

    def run_delAccount_case(self):
        #删除选中的账号
        username = "fangwang@hotmail.com"
        addedAccount_loc = (By.XPATH,"//ul[@class='account-list']//span[text()='{}']".format(username))
        #悬浮指定的账号
        self.mouseHover(addedAccount_loc)
        delBtn_loc = (By.XPATH,"//span[text()='{}']/../following-sibling::span[3]".format(username))
        #点击删除
        self.find_element(delBtn_loc).click()
        delAccountToast = self.find_element(self.sureDelToast_loc).text
        #点击确定删除
        self.find_element(self.sureDelBtn_loc).click()
        accountList = self.get_accountList()
        return delAccountToast,accountList

    def run_accountSSLPort_case(self,emailHost,receiptPort_ssl,receiptPort,sendPort_ssl,sendPort):
        #根据邮箱域名判断
        time.sleep(1)
        self.screenshotImg(key="账号设置页面")
        accountListElements = self.find_element(self.accountList_loc,index="all")
        for accountListElement in accountListElements:
            if emailHost in accountListElement.text:
                accountListElement.click()
                self.screenshotImg(key="{}账号的截图".format(accountListElement.text))
                break
        time.sleep(1)
        #判断ssl是否勾选
        receiptServerInput = self.find_element(self.receiptServerInput_loc)
        sendServerInput = self.find_element(self.sendServerInput_loc)
        if "is-checked" in receiptServerInput.get_attribute("class"):
            if self.find_element(self.receiptServerPort_loc).get_attribute("value") != receiptPort_ssl:
                raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(self.find_element(self.receiptServerPort_loc).get_attribute("value"),receiptPort_ssl))
            self.find_element(self.receiptServerInput_loc).click()
            time.sleep(1)
            if "is-checked" in self.find_element(self.receiptServerInput_loc).get_attribute("class"):
                raise Exception("SSL收件服务器未勾选，不应该有is-checked属性")
            else:
                if self.find_element(self.receiptServerPort_loc).get_attribute("value") != receiptPort:
                    raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(
                        self.find_element(self.receiptServerPort_loc).get_attribute("value"),receiptPort))
        else:
            if self.find_element(self.receiptServerPort_loc).get_attribute("value") != receiptPort:
                raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(self.find_element(self.receiptServerPort_loc).get_attribute("value"),receiptPort))
            self.find_element(self.receiptServerInput_loc).click()
            time.sleep(1)
            if "is-checked" not in self.find_element(self.receiptServerInput_loc).get_attribute("class"):
                raise Exception("SSL收件服务器已勾选，但是没有is-checked属性")
            else:
                if self.find_element(self.receiptServerPort_loc).get_attribute("value") != receiptPort_ssl:
                    raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(
                        self.find_element(self.receiptServerPort_loc).get_attribute("value"),receiptPort_ssl))

        if "is-checked" in sendServerInput.get_attribute("class"):
            if self.find_element(self.sendServerPort_loc).get_attribute("value") != sendPort_ssl:
                raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(self.find_element(self.receiptServerPort_loc).get_attribute("value"),sendPort_ssl))
            self.find_element(self.sendServerInput_loc).click()
            time.sleep(1)
            if "is-checked" in self.find_element(self.sendServerInput_loc).get_attribute("class"):
                raise Exception("SSL收件服务器未勾选，不应该有is-checked属性")
            else:
                if self.find_element(self.sendServerPort_loc).get_attribute("value") != sendPort:
                    raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(
                        self.find_element(self.sendServerPort_loc).get_attribute("value"),sendPort))
        else:
            if self.find_element(self.sendServerPort_loc).get_attribute("value") != sendPort:
                raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(self.find_element(self.sendServerPort_loc).get_attribute("value"),sendPort))
            self.find_element(self.sendServerInput_loc).click()
            time.sleep(1)
            if "is-checked" not in self.find_element(self.sendServerInput_loc).get_attribute("class"):
                raise Exception("SSL收件服务器已勾选，但是没有is-checked属性")
            else:
                if self.find_element(self.sendServerPort_loc).get_attribute("value") != sendPort_ssl:
                    raise Exception("aliyun邮箱SSL收件服务端口：{}有误，应该是{}".format(
                        self.find_element(self.sendServerPort_loc).get_attribute("value"),sendPort_ssl))





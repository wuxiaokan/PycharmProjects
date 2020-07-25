# -*- encoding: utf-8 -*-
'''
@File    :   emailTagPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/3 0003 10:46   dmk      1.0         None
'''
import time
from utils.generator import *
from selenium.webdriver.common.by import By
from .basePage import Action

class emailTagPage(Action):
    #标签按钮
    tagBtn_loc = (By.XPATH,"//div[@class='email_module_list_vue data']//span[@class='tag']//*[name()='svg']")
    #新建标签
    addTag_loc = (By.XPATH,"//div[@class='btn new_btn el-icon-plus']")
    #标签名称输入框
    tagInput_loc = (By.XPATH,"//div[@class='t-flex-row']//input[@placeholder='标签名称']")
    #确定按钮
    sureAddTagBtn_loc = (By.XPATH,"//div[@class='el-dialog__wrapper JOINF add-new-tags']//button[@class='el-button el-button--primary']")
    #确定删除按钮
    sureDelBtn_loc = (By.XPATH,"//button[@class='el-button el-button--default el-button--small el-button--primary ']")
    #确认打标
    sureMarkTag_loc = (By.XPATH,"//div[@class='btn sure']")
    #取消选中标签
    cancelTag_loc = (By.XPATH,"//div[@class='btn cancel_btn']")
    #标签列表
    tagList_loc = (By.XPATH,"//div[@class='tag_picker']//li//label")
    #邮件标签
    emailTag_loc = (By.XPATH,"//div[@class='email_module_list_vue data']//tbody[1]//tr[1]//span[@class='tag']//li")


    def __init__(self,driver):
        super(emailTagPage,self).__init__(driver)
        time.sleep(0.5)
        self.mouseHover(self.tagBtn_loc)
        time.sleep(1)
        self.find_element(self.tagBtn_loc).click()


    #获取标签列表
    def get_tagList(self):
        return self.get_elementText(self.tagList_loc,index="all")

    def run_addTag_case(self):
        newTag_name = random_name()+"标签测试可删除"
        #点击新建标签
        self.find_element(self.addTag_loc).click()
        #输入标签名
        self.find_element(self.tagInput_loc).send_keys(newTag_name)
        #点击确定按钮
        self.find_element(self.sureAddTagBtn_loc).click()
        time.sleep(0.5)
        tagListText = self.get_tagList()
        if newTag_name not in tagListText:
            raise Exception("新增标签{}，不在标签列表中：{}".format(newTag_name,tagListText))

    def run_editTag_case(self):
        editTag_name = random_name()+"编辑标签可删除"
        #遍历所有标签，查找含有可删除的标签
        tagLists = self.get_tagList()
        for tag in tagLists:
            if "可删除" in tag:
                currentTag_loc = (By.XPATH,"//div[@class='tag_picker']//span[text()='{}']".format(tag))
                currentTagEditBtn_loc = (By.XPATH,"//div[@class='tag_picker']//span[text()='{}']/../../following-sibling::div/span[@class='iconfont iconbianji fc01']".format(tag))
                break
        #悬浮该标签
        self.scroll_element(currentTag_loc)
        self.mouseHover(currentTag_loc)
        #点击编辑按钮
        time.sleep(0.5)
        self.mouseClick(currentTagEditBtn_loc)
        #输入新的标签名
        self.find_element(self.tagInput_loc).clear()
        self.find_element(self.tagInput_loc).send_keys(editTag_name)
        #点击确定
        self.find_element(self.sureAddTagBtn_loc).click()
        #获取所有标签
        time.sleep(1)
        editAllTagListText = self.get_tagList()
        if editTag_name not in editAllTagListText:
            raise Exception("新增标签{}，不在标签列表中：{}".format(editTag_name,editAllTagListText))


    def run_delTag_case(self):
        #遍历所有标签，查找含有可删除的标签
        tagLists = self.get_tagList()
        for tag in tagLists:
            if "可删除" in tag:
                delTag_name = tag
                print(delTag_name)
                currentTag_loc = (By.XPATH,"//div[@class='tag_picker']//span[text()='{}']".format(tag))
                currentTagDelBtn_loc = (By.XPATH,"//div[@class='tag_picker']//span[text()='{}']/../../following-sibling::div/span[@class='iconfont iconshanchu fc01']".format(tag))
                break

        #悬浮该标签
        self.scroll_element(currentTag_loc)
        self.mouseHover(currentTag_loc)
        #点击编辑按钮
        time.sleep(0.5)
        self.mouseClick(currentTagDelBtn_loc)
        #点击确定
        self.find_element(self.sureDelBtn_loc).click()
        #获取所有标签
        self.mouseHover(self.tagBtn_loc)
        time.sleep(1)
        self.find_element(self.tagBtn_loc).click()
        delAllTagListText = self.get_tagList()
        if delTag_name in delAllTagListText:
            raise Exception("删掉的标签：{}，仍然在标签列表中：{}".format(delTag_name,delAllTagListText))


    def run_markTag_case(self):
        #取消选中所有标签
        self.find_element(self.cancelTag_loc).click()
        #点击选中第一个标签
        firstTagElement = self.find_element(self.tagList_loc)
        firstTagText = firstTagElement.text
        firstTagElement.click()
        #点击确定，打标
        self.find_element(self.sureMarkTag_loc).click()
        #获取邮件上面的标签内容
        # self.mouseHover(self.tagBtn_loc)
        # time.sleep(1)
        # self.find_element(self.tagBtn_loc).click()
        firstEmailTagText = self.find_element(self.emailTag_loc).text
        if firstTagText != firstEmailTagText:
            raise Exception("邮件打标:{},之后，邮件上显示：{}，结果不一致".format(firstTagText,firstEmailTagText))
        #取消选中
        self.mouseHover(self.tagBtn_loc)
        time.sleep(1)
        self.find_element(self.tagBtn_loc).click()
        self.find_element(self.cancelTag_loc).click()
        self.find_element(self.sureMarkTag_loc).click()
        time.sleep(0.5)
        if self.is_element_exist(self.emailTag_loc[1]):
            raise Exception("取消选中标签之后，不生效，依然显示标签:{}".format(self.find_element(self.emailTag_loc).text))




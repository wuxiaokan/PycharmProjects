# -*- encoding: utf-8 -*-
'''
@File    :   queryBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/21 0021 14:41   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class queryBoxPageLoc:

    #新增查询箱按钮
    queryBoxPage_addQueryBoxBtn_loc = (By.XPATH,'//ul[@class="search-menu el-menu"]//span[text()="查询箱"]/../div')
    #查询箱列表
    queryBoxPage_queryBoxList_loc = (By.XPATH,'//div[@class="list-group"]//li')
    #可删除的查询箱列表
    queryBoxPage_canDelQueryBoxList_loc = (By.XPATH,'//div[@class="list-group"]//li//span[contains(text(),"可删除")]/../..')
    #查询箱名字输入框
    queryBoxPage_queryBoxNameInput_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//div[@class="item_input_one JOINF el-input"]//input')
    #确定按钮
    queryBoxPage_sureBtn_loc = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="确定"]/..')
    #查询箱更多操作按钮
    queryBoxPage_queryBoxMoreOperateBtn_loc = (By.XPATH,'//span[@class="right-box-btn"]')
    #修改查询箱按钮
    queryBoxPage_editQueryBoxBtn_loc = (By.XPATH,'//ul[@x-placement="top" or @x-placement="bottom"]//li[text()="修改此查询箱"]')
    #删除查询箱按钮
    queryBoxPage_delQueryBoxBtn_loc = (By.XPATH,'//ul[@x-placement="top" or @x-placement="bottom"]//li[text()="删除此查询箱"]')
    #确认删除按钮
    queryBoxPage_sureDelQueryBoxBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    #主题输入框
    queryBoxPage_subjectInput_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="主题"]/..//div[contains(@class,"el-input")]//input')
    #包含按钮
    queryBoxPage_containsBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="主题"]/..//span[text()="包含"]/..')
    #等于按钮
    queryBoxPage_equalBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="主题"]/..//span[text()="等于"]/..')
    #几天内，发件按钮
    queryBoxPage_servalDaysSendBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="几天内"]/..//span[text()="发件"]/..')
    #标签列表
    queryBoxPage_markList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li[not(contains(@class,"is-disabled"))]')
    #不限附件按钮
    queryBoxPage_unLimitBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="附件"]/..//label[@role="radio"][1]')
    #不包含附件按钮
    queryBoxPage_unContainAttachBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="附件"]/..//label[@role="radio"][2]')
    #包含附件按钮
    queryBoxPage_containAttachBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="附件"]/..//label[@role="radio"][3]')
    #附件单选按钮
    queryBoxPage_attachRadioBtn_loc = (By.XPATH,'//div[contains(@aria-label,"查询箱")]//label[text()="附件"]/..//label[@role="radio"]')
    #主营产品，电器
    queryBoxPage_mainProductelEctrical_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//li//span[text()="电器"]/..')
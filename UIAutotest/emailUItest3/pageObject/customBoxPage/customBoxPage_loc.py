# -*- encoding: utf-8 -*-
'''
@File    :   customBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/18 0018 10:02   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class customBoxPageLoc:

    #添加自定义箱按钮
    customBoxPage_addCustomBoxBtn_loc = (By.XPATH,'//ul[@class="search-menu el-menu"]//span[text()="自定义箱"]/../div')
    #自定义箱名字输入框
    customBoxPage_addCustomBoxNameInput_loc = (By.XPATH,'//div[contains(@class,"menu-tree-input")]//input')
    #确定新增自定义箱按钮
    customBoxPage_sureAddCustomBoxBtn_loc = (By.XPATH,'//div[contains(@class,"menu-tree-input")]//*[name()="svg"][1]')
    #自定义箱子列表
    customBoxPage_customBoxList_loc = (By.XPATH,'//span[@class="custom-tree-node"]')
    #父级自定义箱子列表
    customBoxPage_parentCustomBoxList_loc = (By.XPATH,'//div[@class="el-tree el-tree--highlight-current"]/div[@class="el-tree-node is-expanded is-focusable"]')
    #可删除的父级自定义箱子列表
    customBoxPage_canCancelParentCustomBoxList_loc = (By.XPATH,'//div[@class="el-tree el-tree--highlight-current"]/div[@class="el-tree-node is-expanded is-focusable"]//span[contains(text(),"可删除") and not(contains(@class,"level2"))]')
    #可删除的子级自定义箱子列表
    customBoxPage_canCancelChildCustomBoxList_loc = (By.XPATH,'//div[@class="el-tree el-tree--highlight-current"]/div[@class="el-tree-node is-expanded is-focusable"]//span[contains(text(),"可删除") and contains(@class,"level2")]')
    #子自定义箱子列表
    customBoxPage_childCustomBoxList_loc = (By.XPATH,'//div[@class="el-tree-node__children"]/div[@class="el-tree-node is-expanded is-focusable"]')
    #自定义箱子更多操作按钮
    customBoxPage_customBoxMoreOperateBtn_loc = (By.XPATH,'//span[@class="custom-tree-node"]//span[@class="right-box-btn"]')
    #新增下级自定义箱按钮
    customBoxPage_addChildCustomBoxBtn_loc = (By.XPATH,'//ul[@x-placement="top" or @x-placement="bottom"]//li[text()="新增下级自定义箱"]')
    #确认删除自定义箱子
    customBoxPage_sureDelCustomBoxBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    #移动到收件箱按钮
    customBoxPage_moveToRecipientBoxBtn_loc = (By.XPATH,'//ul[@x-placement="top" or @x-placement="bottom"]//div[contains(@class,"show-left")]//li[contains(text(),"收件箱")]')
    #移动全部邮件按钮
    customBoxPage_moveAllEmailBtn_loc = (By.XPATH,'//ul[@x-placement="top" or @x-placement="bottom"]//li[@class="el-dropdown-menu__item has-child custom-all-email"]')
    #新建自定义箱名输入框
    customBoxPage_addCustomBoxPage_customBoxNameInput_loc = (By.XPATH,'//div[@aria-label="新建自定义箱"]//div[@class="JOINF el-input"]//input')
    #新建自定义箱保存按钮
    customBoxPage_addCustomBoxPage_saveCustomBoxBtn_loc = (By.XPATH,'//button[@class="el-button small el-button--primary"]//span[text()="保存"]/..')
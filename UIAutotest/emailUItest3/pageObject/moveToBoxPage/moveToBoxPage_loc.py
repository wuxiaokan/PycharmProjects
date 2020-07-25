# -*- encoding: utf-8 -*-
'''
@File    :   moveToBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/18 0018 19:11   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class moveToBoxPageLoc:

    #客户箱，供应商箱子列表
    moveToBoxPage_customerBoxList_loc = (By.XPATH,'//div[@class="treeBox customerTree"]//div[@class="el-tree-node is-focusable"]')
    #内部联系人箱子列表
    moveToBoxPage_innerBoxList_loc = (By.XPATH,'//div[@class="el-table dialog_table el-table--fit el-table--enable-row-hover el-table--enable-row-transition"]//tbody//div[@class="cell"]')
    #自定义箱子列表
    moveToBoxPage_customBoxList_loc = (By.XPATH,'//div[@class="treeBox"]//span[@class="one-line"]')
    #移动页面，可删除的自定义箱子列表
    moveToBoxPage_canDelCustomBoxList_loc = (By.XPATH,'//div[@class="treeBox"]//span[contains(text(),"可删除")]/..')
    #确认移动按钮
    moveToBoxPage_sureMoveBtn_loc = (By.XPATH,'//button[@class="el-button small el-button--primary"]//span[text()="确认"]/..')
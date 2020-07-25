# -*- encoding: utf-8 -*-
'''
@File    :   addFollowPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/14 0014 19:39   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class addFollowPageLoc:
    # 选择商机按钮
    addFollowPage_selectBusinessBtn_loc = (By.XPATH, '//div[@class="form-group m-t-10 businessList"]//span[@class="sel"]')
    # 商机列表
    addFollowPage_businessList_loc = (By.XPATH, '//div[@class="form-group m-t-10 businessList"]//div[@class="dropdown-selectBox"]//li')
    #跟进内容输入框
    addFollowPage_followContentInput_loc = (By.XPATH,'//div[@class="col-md-9  contactContent"]//textarea')
    #保存跟进按钮
    addFollowPage_saveFollowBtn_loc = (By.XPATH,'//button[@class="btn btn-primary edit-save"]')
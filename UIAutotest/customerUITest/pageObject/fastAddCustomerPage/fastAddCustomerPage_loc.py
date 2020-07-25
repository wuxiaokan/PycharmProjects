# -*- encoding: utf-8 -*-
'''
@File    :   fastAddCustomerPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/23 0023 9:26   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class fastAddCustomerPageLoc:

    #快速新建按钮
    fastAddCustomerPage_fastAddCustomerBtn_loc = (By.XPATH,'//div[contains(@class,"fast-new")]//button[1]')
    #客户名称输入框
    fastAddCustomerPage_customerNameInput_loc = (By.XPATH,'//div[contains(@class,"customer_edit_add_vue")]//span[text()="客户名称"]/../following-sibling::div//input')
    #联系人备注
    fastAddCustomerPage_contactComment_loc = (By.XPATH,'//div[contains(@class,"customer_edit_add_vue")]//span[text()="备注"]/../following-sibling::div//textarea')
    #客户类型列表
    fastAddCustomerPage_customerTypeList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li//span[text()="新客户"]')
    #附件上传input框
    fastAddCustomerPage_attachInput_loc = (By.XPATH,'//div[@class="my-uploader file-list"]//input')
    #保存按钮
    fastAddCustomerPage_saveBtn_loc = (By.XPATH,'//div[@class="btn_group"]//button//span[text()="保存"]/..')
    #全屏按钮
    fastAddCustomerPage_fullScreenBtn_loc = (By.XPATH,'//div[@class="btn"]//i[@class="btn_box"][1]')
    #关闭按钮
    fastAddCustomerPage_cloaseBtn_loc = (By.XPATH,'//div[@class="btn"]//i[@class="btn_box"][2]')
    #关闭提示里面的是按钮
    fastAddCustomerPage_isSaveBtn_loc = (By.XPATH,'//div[@class="el-dialog__footer"]//span[text()="是"]/..')
    #关闭提示里面的否按钮
    fastAddCustomerPage_notSaveBtn_loc = (By.XPATH,'//div[@class="el-dialog__footer"]//span[text()="否"]/..')
    #关闭提示里面的取消按钮
    fastAddCustomerPage_cancelSaveBtn_loc = (By.XPATH,'//div[@class="el-dialog__footer"]//span[text()="否"]/../preceding-sibling::button')
    #快速新建页面，head
    fastAddCustomerPage_fastAddHeader_loc = (By.XPATH,'//div[contains(@class,"customer_edit_add_vue")]//div[contains(text(),"快速新建")]')
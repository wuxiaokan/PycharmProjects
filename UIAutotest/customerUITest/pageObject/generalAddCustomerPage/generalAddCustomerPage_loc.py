# -*- encoding: utf-8 -*-
'''
@File    :   generalAddCustomerPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 0016 9:42   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class generalAddCustomerPageLoc:

    #客户tab按钮
    generalAddCustomerPage_customerTabBtn_loc = (By.XPATH,'//div[@class="tabs_nav"]//div[text()="客户"]')
    #普通新建客户下拉按钮
    generalAddCustomerPage_addCustomerDropDownBtn_loc = (By.XPATH,'//button[contains(@class,"el-dropdown__caret-button")]')
    #普通新建客户按钮
    generalAddCustomerPage_generalAddCustomerBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[text()="普通新建"]')
    #客户代码二维码按钮
    generalAddCustomerPage_customerQRcodeBtn_loc = (By.XPATH,'//div[@class="customer_edit_add_vue"]//i[contains(@class,"iconerweima ")]')
    #编码国家一级选择框
    generalAddCustomerPage_customerCode_firstDropBoxOfCountry_loc = (By.XPATH,"//label[contains(text(),'国家')]/following-sibling::div")
    #国家列表
    generalAddCustomerPage_customerCode_countryList_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//li//span[text()="阿富汗"]')
    #编码sku一级选择框
    generalAddCustomerPage_customerCode_firstDropBoxOfSku_loc = (By.XPATH,"//label[contains(text(),'sku')]/following-sibling::div")
    #编码列表
    generalAddCustomerPage_customerCodeList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li')
    #申请编码按钮
    generalAddCustomerPage_appplyCustomerCodeBtn_loc = (By.XPATH,'//button//span[text()="申请编码"]')
    #客户名称输入框
    generalAddCustomerPage_customerNameInput_loc = (By.XPATH,'//div[@class="customer_edit_add_vue"]//span[text()="客户名称"]/../following-sibling::div//input')
    #国家地区一级下拉框
    generalAddCustomerPage_countryDropDownBtn_loc = (By.XPATH,'//div[@class="customer_edit_add_vue"]//span[contains(text(),"国家/地区")]/../following-sibling::div//input')
    #客户主要信息里面的备注
    generalAddCustomerPage_commentTextarea_loc = (By.XPATH,'//div[contains(@class,"base-info")]//span[text()="备注"]/../following-sibling::div//textarea')
    #已选中的主营产品列表
    generalAddCustomerPage_selectedMainProductList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li[contains(@class,"selected")]')
    #未被选中的主营产品列表
    generalAddCustomerPage_unSelectedMainProductList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li[@class="el-select-dropdown__item"]')
    #扩展信息里面的是否按钮
    generalAddCustomerPage_extendInfoIsBtn_loc = (By.XPATH,'//div[contains(@class,"base-info")]//span[text()="是否"]/../following-sibling::div//label')
    #扩展信息里面的自定义按钮
    generalAddCustomerPage_extendInfoCustomBtn_loc = (By.XPATH,'//div[contains(@class,"base-info")]//span[text()="自定义数据字典"]/../following-sibling::div//label[1]/span[1]')
    #扩展信息里面的字典按钮
    generalAddCustomerPage_extendInfoDictBtn_loc = (By.XPATH,'//div[contains(@class,"base-info")]//span[text()="自定义数据字典"]/../following-sibling::div//label[2]')
    #日历弹框某一天按钮
    generalAddCustomerPage_pickerDayBtn_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//table[@class="el-date-table"]//span[contains(text(),"26")]')
    #联系人性别男按钮
    generalAddCustomerPage_contactInfoMaleBtn_loc = (By.XPATH,'//ul[contains(@class,"contact_item")]//span[text()="性别"]/../following-sibling::div//label[1]')
    #联系人性别女按钮
    generalAddCustomerPage_contactInfoFemaleBtn_loc = (By.XPATH,'//ul[contains(@class,"contact_item")]//span[text()="性别"]/../following-sibling::div//label[2]')
    #联系人状态
    generalAddCustomerPage_contactStatusBtn_loc = (By.XPATH,'//ul[contains(@class,"contact_item")]//span[text()="状态"]/../following-sibling::div/div')
    #联系人收起展开按钮
    generalAddCustomerPage_showOrHideContactBtn_loc = (By.XPATH,'//span[@class="d_btn f12 fc01 no-sel pointer"]')
    #客户保存按钮
    generalAddCustomerPage_saveCustomerBtn_loc = (By.XPATH,'//div[@class="customer_edit_add_vue"]//button//span[text()="保存"]')
    #保存并新建按钮
    generalAddCustomerPage_saveAndAddCustomerBtn_loc = (By.XPATH,'//span[text()="保存并新建"]/..')
    #取消保存按钮
    generalAddCustomerPage_cancelSaveCustomerBtn_loc = (By.XPATH,'//div[@class="customer_edit_add_vue"]//span[text()="取消"]/..')
    #上传附件input
    generalAddCustomerPage_uploadAttachInput_loc = (By.XPATH,'//div[@class="my-uploader file-list"]//input')
    #联系人全选按钮
    generalAddCustomerPage_selectAllContactCheckboxBtn_loc = (By.XPATH,'//dd[@class="contact-info-content"]//span[text()="全选"]/..')
    #新增联系人按钮
    generalAddCustomerPage_addContactBtn_loc = (By.XPATH,'//dd[@class="contact-info-content"]//button[contains(@class,"primary")]')
    #删除多个联系人按钮
    generalAddCustomerPage_delSeveralContactBtn_loc = (By.XPATH,'//dd[@class="contact-info-content"]//button[contains(@class,"default")]')
    #联系人卡片
    generalAddCustomerPage_contactCard_loc = (By.XPATH,'//div[@class="contact-cards"]//div[contains(@class,"card-item")]')
    #联系人默认按钮
    generalAddCustomerPage_defaultContactBtn_loc = (By.XPATH,'//div[@class="default_btn no-sel pointer"]//div[text()="默认"]')
    #删除当前联系人按钮
    generalAddCustomerPage_delCurrentContactBtn_loc = (By.XPATH,'//div[@class="del_btn no-sel pointer"]')
    #确认删除联系人按钮
    generalAddCustomerPage_sureDelContactBtn_loc = (By.XPATH,'//span[@class="dialog-footer"]//span[text()="是"]/..')
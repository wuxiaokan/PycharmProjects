# -*- encoding: utf-8 -*-
'''
@File    :   writeMailPageInsertFastTextPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/8 0008 10:08   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class writeMailPageInsertFastTextPageLoc:
    # 写信页面插入快速文本按钮
    writeMailPage_insertFastTextBtn_loc = (By.XPATH, '//a[@class="cke_button cke_button__shortcut cke_button_off"]')
    # 选择快速文本页面新增快速文本按钮
    writeMailPageInsertFastTextPage_addFastTextBtn_loc = (By.XPATH, '//button[@id="addNewText"]')
    # 选择快速文本页面，插入按钮
    writeMailPageInsertFastTextPage_insertFastTextBtn_loc = (By.XPATH, '//button[@id="insertText"]')
    # 选择快速文本页面，搜索输入框
    writeMailPageInsertFastTextPage_searchFastTextInput_loc = (By.XPATH, '//input[@class="searchBox el-input__inner"]')
    # 选择快速文本页面，搜索按钮
    writeMailPageInsertFastTextPage_searchFastTextBtn_loc = (By.XPATH, '//i[@class="el-icon-search"]')
    # 选择快速文本页面，新增文本主题输入框
    writeMailPageInsertFastTextPage_addFastTextTitleInput_loc = (By.XPATH, '//input[@class="subject"]')
    # 选择快速文本页面，新增文本主题输入框
    writeMailPageInsertFastTextPage_addFastTextBodyInput_loc = (By.XPATH, '//textarea[@placeholder="请输入文本内容"]')
    # 选择快速文本页面，保存新增文本按钮
    writeMailPageInsertFastTextPage_saveAddFastTextBtn_loc = (By.XPATH, '//button[@class="el-button small el-button--primary el-button--mini"]//span[text()="保存"]')
    # 选择快速文本页面，快速文本列表
    writeMailPageInsertFastTextPage_fastTextList_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr')
    # 选择快速文本页面，快速文本单选框
    writeMailPageInsertFastTextPage_fastTextCheckBox_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr//label')
    # 选择快速文本页面，快速文本全选框
    writeMailPageInsertFastTextPage_fastTextAllCheckBox_loc = (By.XPATH, '//table[@id="select-email-text"]//thead/tr//label')
    # 选择快速文本页面，快速文本主题
    writeMailPageInsertFastTextPage_fastTextTitle_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr//td[2]')
    # 选择快速文本页面，快速主题包含可删除的主题
    writeMailPageInsertFastTextPage_fastTextTitleContainsDel_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr//td[2]//span[contains(text(),"可删除")]')
    # 选择快速文本页面，快速文本内容
    writeMailPageInsertFastTextPage_fastTextBody_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr//td[3]')
    # 选择快速文本页面，编辑文本按钮
    writeMailPageInsertFastTextPage_editFastTextBtn_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr//td[4]/i[contains(@class,"icons_edit")]')
    # 选择快速文本页面，删除文本按钮
    writeMailPageInsertFastTextPage_delFastTextBtn_loc = (By.XPATH, '//table[@id="select-email-text"]//tbody/tr//td[4]/i[contains(@class,"icons_del")]')
    # 选择快速文本页面，确定删除按钮
    writeMailPageInsertFastTextPage_sureDelFastTextBtn_loc = (By.XPATH, '//button[@class="el-button small el-button--primary el-button--mini"]//span[text()="确定"]')
    # 选择快速文本页面，换行显示按钮
    writeMailPageInsertFastTextPage_newLineShowBtn_loc = (By.XPATH, '//div[@class="el-dialog dialog-fast-text"]//div[@class="el-dialog__footer"]//label')
    # 选择快速文本页面，关闭选择快速文本页面按钮
    writeMailPageInsertFastTextPage_closeSelectFastTextPageBtn_loc = (By.XPATH, '//div[@class="el-dialog dialog-fast-text"]//button[@class="el-dialog__headerbtn"]')
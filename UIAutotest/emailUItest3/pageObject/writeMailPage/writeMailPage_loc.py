# -*- encoding: utf-8 -*-
'''
@File    :   writeMailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/19 0019 20:51   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class writeMailPageLoc:
    # 写信页面插入签名按钮
    writeMailPage_insertSignatureBtn_loc = (By.XPATH, '//span[contains(@class,"insert_signature")]')
    # 写信页面新建签名按钮
    writeMailPage_addSignatureBtn_loc = (By.XPATH, "//ul[@x-placement='bottom-end']//span[contains(text(),'新建签名')]/..")
    # 设置页面选中的项
    settingPage_selectedOption_loc = (By.XPATH, '//li[@class="el-menu-item is-active"]')
    # 邮件编辑器内的文本
    emailBodyInEmailEdit_loc = (By.XPATH, '/html/body')
    # 邮件编辑器内的图片
    emailBodyImgInEmailEdit_loc = (By.XPATH, '/html/body/p/img')
    #写信页面，邮件文本
    writeMailPage_emailBody_loc = (By.XPATH,'//p[@class="joinfEmailBody setting"]')
    # 写信页面，发送按钮
    writeMailPage_sendEmailBtn_loc = (By.XPATH, '//button[@class="el-button item send f12 el-button--primary"]')
    #写信页面，保存草稿按钮
    writeMailPage_saveDraftBtn_loc = (By.XPATH,'//span[text()="存草稿"]')
    # 写信页面，抄送按钮
    writeMailPage_ccSendEmailBtn_loc = (By.XPATH, '//ul[@class="d_operation"]//li[text()="抄送"]')
    # 写信页面，密送按钮
    writeMailPage_bcSendEmailBtn_loc = (By.XPATH, '//ul[@class="d_operation"]//li[text()="密送"]')
    # 写信页面，收件人输入框
    writeMailPage_recipientInput_loc = (By.XPATH, '//div[@class="addressee_input_item b_line i_item addressee"]//input')
    #写信页面，删除收件人按钮
    writeMailPage_delRecipientBtn_loc = (By.XPATH,'//div[@class="addressee"]//li[contains(@class,"addressee_tag_vue")]//div[contains(@class,"close_btn")]')
    #写信页面，收件人列表
    writeMailPage_recipientList_loc = (By.XPATH,'//div[@class="addressee"]//p[@class="show_txt f12 fc02 no-sel"]')
    # 写信页面，最近联系人列表
    writeMailPage_recentContactList_loc = (By.XPATH, '//div[@class="recentContact_list_box"]//li//div[@class="contact f12 fc02"]')
    # 写信页面，抄送人输入框
    writeMailPage_ccInput_loc = (By.XPATH, '//div[@class="addressee_input_item b_line i_item copy"]//input')
    # 写信页面，密送人输入框
    writeMailPage_bcInput_loc = (By.XPATH, '//div[@class="addressee_input_item b_line i_item secret_send"]//input')
    #写信页面，抄送人
    writeMailPage_cc_loc = (By.XPATH,'//div[@class="addressee_input_item b_line i_item copy"]//p[contains(@class,"show_txt")]')
    #写信页面，密送人
    writeMailPage_bc_loc = (By.XPATH,'//div[@class="addressee_input_item b_line i_item secret_send"]//p[contains(@class,"show_txt")]')
    # 写信页面，主题输入框
    writeMailPage_emailSubjectInput_loc = (By.XPATH, '//div[@class="b_line i_item subject"]//input')
    # 写信页面，发件人选择框
    writeMailPage_senderInput_loc = (By.XPATH, '//div[@class="sender-select"]//input')
    #写信页面，发件人
    writeMailPage_sender_loc = (By.XPATH,'//div[@x-placement="top-start" or @x-placement="bottom-start"]//span[contains(text(),"126")]')
    #写信页面，提交审批按钮
    writeMailPage_submitApprovalBtn_loc = (By.XPATH,'//div[@class="el-dialog__footer"]//span[text()="提交审批"]')
    #写信页面，不审，发送按钮
    writeMailPage_noApprovalBtn_loc = (By.XPATH,'//div[@class="el-dialog__footer"]//span[text()="不审，发送"]')
    #写信页面，提交审批输入框
    writeMailPage_submitApprovalInput_loc = (By.XPATH,'//div[@class="el-dialog__body"]//textarea')
    #写信页面，纯文本选择框
    writeMailPage_pureTextBtn_loc = (By.XPATH,'//span[text()="纯文本"]/..')
    #写信页面，取消纯文本按钮
    writeMailPage_cancelPureTextBtn_loc = (By.XPATH,'//button[@class="el-button small el-button--default"]')
    #写信页面，确定纯文本按钮
    writeMailPage_surePureTextBtn_loc = (By.XPATH,'//button[@class="el-button small"]')
    #写信页面，纯文本编辑框
    writeMailPage_pureTextEdit_loc = (By.XPATH,'//textarea[@class="el-textarea__inner"]')
    #写信页面，添加附件input框
    writeMailPage_addAttachInput_loc = (By.XPATH,'//div[@class="tool"]//span[text()="添加附件"]/following-sibling::input')
    #写信页面，附件向下下拉按钮
    writeMailPage_attachPullDownBtn_loc = (By.XPATH,'//span[@class="el-dropdown-link a_fc03 f12 el-dropdown-selfdefine"]')
    #写信页面，普通附件input框
    writeMailPage_smallAttachInput_loc = (By.XPATH,'//ul[@x-placement="bottom-end" or @x-placement="top-end"]//span[contains(text(),"普通附件")]/following-sibling::input')
    #写信页面，大附件input框
    writeMailPage_bigAttachInput_loc = (By.XPATH,'//ul[@x-placement="bottom-end" or @x-placement="top-end"]//span[contains(text(),"超大附件")]/following-sibling::input')
    #写信页面，附件名
    writeMailPage_attachName_loc = (By.XPATH,'//div[@class="attachment_list"]//p[contains(@class,"text1")]')
    # writeMailPage_attachName_loc = (By.XPATH,'//li[@class="attachment_upload attachment"]//p[contains(@class,"text1")]')
    #写信页面，大附件名
    writeMailPage_bigAttachName_loc = (By.XPATH,'//div[@class="attachment_list"]//span[text()="7天有效"]/../../preceding-sibling::p')
    #写信页面，报价单附件名
    writeMailPage_quoteAttachName_loc = (By.XPATH,'//div[@class="attachment_list"]//p[starts-with(text(),"quotation")]')
    #写信页面，订单附件名
    writeMailPage_orderAttachName_loc = (By.XPATH,'//div[@class="attachment_list"]//p[starts-with(text(),"pi")]')
    #写信页面，插入产品按钮
    writeMailPage_insertProductBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="产品"]')
    #写信页面，产品选择框里面的产品列表
    writeMailPage_productSelectList_loc = (By.XPATH,'//ul[@class="product-list clearfix"]//li[1]')
    #写信页面，产品选择框里面的图片
    writeMailPage_productSelectImg_loc = (By.XPATH,'//ul[@class="product-list clearfix"]//div[contains(@class,"product-img")]')
    #写信页面，产品选择框里面的产品编码
    writeMailPage_productSelectCode_loc = (By.XPATH,'//ul[@class="product-list clearfix"]//p[contains(@class,"product-id")]')
    #写信页面，编辑器里面的产品图片
    writeMailPage_edit_productImg_loc = (By.XPATH,'//table[@class="mce-item-table cke_show_border"]//tr[1]/td[1]/img')
    #写信页面，编辑器里面的产品编码
    writeMailPage_edit_productCode_loc = (By.XPATH,'//table[@class="mce-item-table cke_show_border"]//tr[1]/td[3]')
    #写信页面，产品选择框
    writeMailPage_productCheckbox_loc = (By.XPATH,'//ul[contains(@class,"product-list")]//li[contains(@class,"clearfix fl")]/label')
    #写信页面，确定插入产品按钮
    writeMailPage_sureInsertProductBtn_loc = (By.XPATH,'//div[@class="email-product"]//button[contains(@class,"el-button--primary")]')
    #写信页面，插入报价按钮
    writeMailPage_insertQuoteBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="报价"]')
    #写信页面，报价订单对话框页面
    writeMailPage_orderSelectdialog_loc = (By.XPATH,'//div[contains(@class,"orderSelectdialog")]')
    #写信页面，报价单号
    writeMailPage_quoteCode_loc = (By.XPATH,'//div[@aria-label="插入报价单"]//tbody//tr/td[2]//div[@class="cell"]')
    #写信页面，插入PDF报价按钮
    writeMailPage_insertPDFQuoteBtn_loc = (By.XPATH,'//div[@aria-label="插入报价单"]//button//span[contains(text(),"插入PDF")]')
    #写信页面，确定插入报价订单按钮
    writeMailPage_sureInsertQuoteOrderBtn_loc = (By.XPATH,'//div[@class="el-message-box__wrapper"]//button[contains(@class,"el-button--primary")]')
    #写信页面，插入订单按钮
    writeMailPage_insertOrderBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="订单"]')
    #写信页面，订单单号
    writeMailPage_orderCode_loc = (By.XPATH,'//div[@aria-label="插入订单"]//tbody//tr/td[2]//div[@class="cell"]')
    #写信页面，插入EXCEL订单按钮
    writeMailPage_insertEXCELOrderBtn_loc = (By.XPATH,'//div[@aria-label="插入订单"]//button//span[contains(text(),"插入EXCEL")]')
    #写信页面，插入营销网站按钮
    writeMailPage_insertSiteBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="营销网站"]')
    #营销网站对话框
    writeMailPage_siteSelectdialog_loc = (By.XPATH,'//div[contains(@class,"product-select")]')
    #写信页面，插入营销网站快照按钮
    writeMailPage_insertSiteSnapshotBtn_loc = (By.XPATH,'//div[contains(@class,"product-select")]//button//span[text()="插入营销网站首页快照"]')
    #写信页面，编辑器内的营销网站快照
    writeMailPage_siteSnapshot_edit_loc = (By.XPATH,'//span[@class="market-product-wrapper"]//a')
    #写信页面，插入云文件按钮
    writeMailPage_insertDishFileBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="云文件"]')
    #写信页面，云文件列表
    writeMailPage_dishFileList_loc = (By.XPATH,'//div[contains(@class,"dishfile-list")]//div[contains(@class,"el-col")][1]')
    #写信页面，云文件选择框
    writeMailPage_dishFileCheckBox_loc = (By.XPATH,'//div[contains(@class,"dishfile-list")]//div[contains(@class,"el-col")]//label[@class="el-checkbox"]')
    #写信页面，云文件名字
    writeMailPage_dishFileName_loc = (By.XPATH,'//div[contains(@class,"dishfile-list")]//div[contains(@class,"el-col")]//div[@class="item_name"]')
    #写信页面，确定插入云文件按钮
    writeMailPage_sureInsertDishFileBtn_loc = (By.XPATH,'//div[contains(@class,"dishfile-select")]//button[contains(@class,"el-button--primary")]')
    #写信页面，插入邮件模板按钮
    writeMailPage_insertMailTemplateBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="邮件模板"]')
    #写信页面，邮件模板对话框
    writeMailPage_templateSelectdialog_loc = (By.XPATH,'//div[contains(@class,"template-select")]')
    #写信页面，系统模板按钮
    writeMailPage_systemMailTemplateBtn_loc = (By.XPATH,'//div[contains(@class,"template-select")]//li[text()="系统"]')
    #写信页面，系统模板列表
    writeMailPage_systemMailTemplateList_loc = (By.XPATH,'//div[contains(@class,"template-select")]//div[contains(@class,"el-col")]')
    #写信页面，插入模板到指定位置
    writeMailPage_insertMailTemplateToLocationBtn_loc = (By.XPATH,'//div[contains(@class,"template-select")]//button//span[text()="追加到指定位置"]')
    #写信页面，tab关闭按钮
    writeMailPage_closeTabBtn_loc = (By.XPATH,'//div[@class="tabs_nav"]//i[contains(@class,"el-icon-close")]')
    #写信tab
    writeMailPage_writeMailTabBtn_loc = (By.XPATH,'//div[@class="tabs_nav"]//div[text()="写邮件"]')
    #写信页面，需要回执按钮
    writeMailPage_needReceiptBtn_loc = (By.XPATH,'//span[text()="需要回执"]/..')
    #写信页面，标签按钮
    writeMailPage_markBtn_loc = (By.XPATH,'//div[@class="email_write"]//div[@class="tags f12"]//*[name()="svg"]')
    #写信页面，标签列表
    writeMailPage_markList_loc = (By.XPATH,'//div[@class="email_write"]//div[@class="tag_list"]//li')
    #写信页面，确定插入标签按钮
    writeMailPage_sureInsertMarkBtn_loc = (By.XPATH,'//div[@class="email_write"]//div[@class="btn sure"]/..')
    #写信页面，已插入标签列表
    writeMailPage_insertedMarkList_loc = (By.XPATH,'//div[@class="email_write"]//ul[@class="tag_list li3"]//li')
    #写信页面，定时发送按钮
    writeMailPage_timedSendBtn_loc = (By.XPATH,'//li[contains(@class,"b_timed_sending")]')
    #写信页面，确认定时发送按钮
    writeMailPage_sureTimedSendBtn_loc = (By.XPATH,'//div[@aria-label="设置定时发送"]//button[contains(@class,"el-button--primary")]')
    #设置定时页面，设置的定时文本
    writeMailPage_setTimePage_settedTime_loc = (By.XPATH,'//div[@aria-label="设置定时发送"]//div[contains(@class,"text")]//span[contains(@class,"nor_break")]')
    #写信页面，设置的定时文本
    writeMailPage_settedTime_loc = (By.XPATH,'//li[contains(@class,"b_timed_sending")]//span')
    #写信页面，取消定时按钮
    writeMailPage_cancelTimedSendBtn_loc = (By.XPATH,'//li[contains(@class,"cancel_timed_sending")]')
    #消息通知里面的时间文本
    writeMailPage_notifyTime_loc = (By.XPATH,'//div[@class="el-dialog notifyDialog"]//div[@class="tips"]//strong')
    #写信页面，内部转发按钮
    writeMailPage_innerForwardBtn_loc = (By.XPATH,'//div[@class="o_bar"]//li[text()="内部转发"]')
    #写信页面，群发单显按钮
    writeMailPage_massSendBtn_loc = (By.XPATH,'//div[@class="o_bar"]//li[text()="群发单显"]')
    #内部转发页面，内部联系人
    writeMailPage_innerForwardPage_innerList_loc = (By.XPATH,'//div[@aria-label="内部转发"]//div[@class="tree-left"]//li')
    #内部转发页面，转发意见输入框
    writeMailPage_innerForwardPage_forwardIdeaInput_loc = (By.XPATH,'//div[@aria-label="内部转发"]//textarea')
    #内部转发页面，确定转发按钮
    writeMailPage_innerForwardPage_sureForwadrBtn_loc = (By.XPATH,'//div[@aria-label="内部转发"]//button[contains(@class,"el-button--primary")]')
    #插入宏按钮
    writeMailPage_insertMacroBtn_loc = (By.XPATH,'//a[@title="插入宏"]')
    #宏列表
    writeMailPage_macroList_loc = (By.XPATH,'//div[@id="Modal-Select-Macro"]//li')
    #确定插入宏按钮
    writeMailPage_sureInsertMacroBtn_loc = (By.XPATH,'//div[@class="el-dialog__footer"]//button[@class="el-button el-button--primary small el-button--mini"]')
    #邮件追踪按钮
    writeMailPage_emailTraceBtn_loc = (By.XPATH,'//div[@class="email_write"]//span[text()="邮件追踪"]/..')
    #邮件正文
    writeMailPage_emailContent_loc = (By.XPATH,'//p[@class="joinfEmailBody setting"]//span')
    #插入图片按钮
    writeMailPage_insertImgBtn_loc = (By.XPATH,'//a[@class="cke_button cke_button__myimage cke_button_off"]')
    #商机页面，发送邮件按钮
    businessPage_sendEmailBtn_loc = (By.XPATH,'//div[@class="el-table__fixed-right"]//i[contains(@class,"iconfasongyoujian")]')
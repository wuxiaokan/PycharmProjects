# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 16:12   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class emailDetailPageLoc():
    #转发下拉按钮
    emailDetailPage_forwardDropDownBtn_loc = (By.XPATH,'//div[@class="icon_group"]//div[@class="icon el-dropdown"][3]')
    #转发按钮
    emailDetailPage_forwardBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="转发"]')
    #内部转发按钮
    emailDetailPage_innerForwardBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="内部转发"]')
    #作为附件转发按钮
    emailDetailPage_forwardAsAttachBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="作为附件转发"]')
    #详情页面，更多操作按钮
    emailDetailPage_moreOperateBtn_loc = (By.XPATH,'//div[@class="ti"]//div[@class=" b_l_bar f0"]//div[@class="icon_group"]/div[@class="el-tooltip icon el-dropdown"][2]')
    #更多操作标记按钮
    emailDetailPage_moreOperateMarkBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//p[contains(text(),"标记为")]')
    #更多操作，标记功能列表
    emailDetailPage_moreOperateList_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//div[@class="dropdown-children show-left"]//li')
    #更多操作，未读按钮
    emailDetailPage_moreOperateUnReadBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[contains(text(),"未读")]')
    #更多操作，归并按钮
    emailDetailPage_mergerBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[contains(text(),"归并")]')
    #详情页面，附件列表
    emailDetailPage_attachList_loc = (By.XPATH,'//div[@class="attachment"]//p[contains(@class,"text1")]/span[1]')
    #详情页面，附件名
    emailDetailPage_attachName_loc = (By.XPATH,'//div[@class="attachment"]//p[contains(@class,"text1")]/span[1]')
    #详情页面，附件大小
    emailDetailPage_attachSize_loc = (By.XPATH,'//div[@class="attachment"]//p[@class="text1 a_fc02 f12"]/span[2]')
    #详情页面，邮件主题
    emailDetailPage_subject_loc = (By.XPATH,'//div[contains(@class,"subject ")]//span')
    #详情页面，确定按钮
    emailDetailPage_sureBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    #详情页面，自动回执选择框
    emailDetailPage_autoReceiptBtn_loc = (By.XPATH,'//span[text()="自动发送回执"]/..')
    #详情页面,发送回执按钮
    emailDetailPage_sendReceiptBtn_loc = (By.XPATH,'//div[@aria-label="邮件回执"]//button[contains(@class,"el-button--primary")]')
    #详情页面,不发送回执按钮
    emailDetailPage_notSendReceiptBtn_loc = (By.XPATH,'//div[@aria-label="邮件回执"]//button[contains(@class,"el-button--default")]')
    #发件人
    emailDetailPage_sender_loc = (By.XPATH,'//div[@class="main-content"]//span[@class="contact_names fc01"]')
    #收件人
    emailDetailPage_recipient_loc = (By.XPATH,'//div[@class="main-content"]//div[contains(@class,"d_info")]//span[contains(@class,"compact")]//span[@class="contact_names"]')
    #抄送人
    emailDetailPage_cc_loc = (By.XPATH,'//div[@class="mail_read window"]//span[text()="抄送人"]/..//span[@class="contact_names"]')
    #产品图片地址
    emailDetailPage_productImg_loc = (By.XPATH,'//table[@class="mce-item-table cke_show_border"]//tr[1]//td[1]//img')
    #产品编码
    emailDetailPage_productCode_loc = (By.XPATH,'//table[@class="mce-item-table cke_show_border"]//tr[1]//td[3]')
    #营销快照图片地址
    emailDetailPage_siteImg_loc = (By.XPATH,'//span[@class="market-product-wrapper"]//a')
    #邮件内容
    emailDetailPage_emailContent_loc = (By.XPATH,'//p[contains(@class,"joinfEmailBody")]')
    # #大附件名
    # emailDetailPage_bigAttachName_loc = (By.XPATH,'//span[contains(text(),"Reserved to")]/preceding-sibling::span')
    #大附件名
    emailDetailPage_bigAttachName_loc = (By.XPATH,'//span[contains(text(),"Reserved to")]/..//*[1]')
    #回复下拉按钮
    emailDetailPage_replyDropDownBtn_loc = (By.XPATH,'//div[@class="icon_group"]//div[@class="icon el-dropdown"][1]')
    #回复带附件按钮
    emailDetailPage_replyContainAttachBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="回复（带附件）"]')
    #内部人员
    emailDetailPage_innerPerson_loc = (By.XPATH,'//div[contains(@class,"d_info")]//span[text()="内部人员"]/preceding-sibling::div')
    #转发，分发意见按钮
    emailDetailPage_forwardIdeaBtn_loc = (By.XPATH,'//div[contains(@class,"status_info")]//span[text()="转发/分发意见"]')
    #转发，分发文本
    emailDetailPage_forwardIdeaText_loc = (By.XPATH,'//div[contains(@class,"m_r_d_f_popover")]//div[@class="f12 fc02"]')
    #内部转发，云基础联系人
    emailDetailPage_innerForwardPage_inner_loc = (By.XPATH,'//div[contains(@class,"email-inner-forward")]//span[text()="云基础"]')
    #内部转发，转发意见输入框
    emailDetailPage_innerForwardPage_forwardIdeaInput_loc = (By.XPATH,'//div[contains(@class,"email-inner-forward")]//textarea')
    #内部转发，确定按钮
    emailDetailPage_innerForwardPage_sureBtn_loc = (By.XPATH,'//div[contains(@class,"el-dialog__wrapper JOINF")]//span[text()="确定"]/..')
    #移动按钮
    emailDetailPage_moveBtn_loc = (By.XPATH,'//div[@class="ti"]//div[@class=" b_l_bar f0"]//div[@class="el-tooltip icon el-dropdown"][1]')
    #已发箱按钮
    emailDetailPage_moveToHasSendBoxBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="已发箱"]')
    #客户箱列表
    emailDetailPage_moveToCustomerBoxList_loc = (By.XPATH,'//div[@class="treeBox customerTree"]//div[@class="el-tree-node is-focusable"]')
    #内部联系人箱子列表
    emailDetailPage_moveToInnerBoxList_loc = (By.XPATH,'//div[@aria-label="移动到"]//tbody//tr')
    #自定义箱子列表
    emailDetailPage_moveToCustomBoxList_loc = (By.XPATH,'//div[@class="treeBox"]//div[@class="el-tree-node is-focusable"]')
    #移动到箱子，确定按钮
    emailDetailPage_sureMoveBtn_loc = (By.XPATH,'//div[@aria-label="移动到"]//span[text()="确认"]/..')
    #详情页面，左翻页按钮
    emailDetailPage_leftTurnPageBtn_loc = (By.XPATH,'//div[@class="icon_group"]//*[name()="svg" and contains(@class,"iconzuofanye")]')
    #详情页面，有翻页按钮
    emailDetailPage_rightTurnPageBtn_loc = (By.XPATH,'//div[@class="icon_group"]//*[name()="svg" and contains(@class,"iconyoufanye")]')
    #详情页面，邮件日志
    emailDetailPage_emailLog_loc = (By.XPATH,'//div[@aria-label="邮件日志"]//tbody//tr')
    #详情页面，删除按钮
    emailDetailPage_delBtn_loc = (By.XPATH,'//div[@class="ti"]//li[text()="客户箱"]/../../following-sibling::div[1]')
    #详情页面，确认删除按钮
    emailDetailPage_sureDelBtn_loc = (By.XPATH,'//div[@aria-label="提示"]//span[contains(text(),"确认")]/..')
    #详情页面，翻译frame
    emailDetailPage_transFrame_loc = (By.XPATH,'//iframe[contains(@src,"fanyi.baidu")]')
    #详情页面，翻译文本框
    emailDetailPage_transInput_loc = (By.XPATH,'//div[@class="trans-left"]//textarea')
    #邮件详情页面，保存模板按钮
    emailDetailPage_saveTemplateBtn_loc = (By.XPATH,'//div[contains(@class,"tranferSaveTemplate")]//span[text()="保存"]/..')
    #详情页面，详情tab按钮
    emailDetailPage_detailTabBtn_loc = (By.XPATH,'//div[@class="text closable"]')
    #PDF预览按钮
    emailDetailPage_previewPDFBtn_loc = (By.XPATH,'//div[@class="attachment"]//li//p[contains(@title,"pdf")]/following-sibling::div//span[text()="预览"]/..')
    #EXCEL预览按钮
    emailDetailPage_previewEXCELBtn_loc = (By.XPATH,'//div[@class="attachment"]//li//p[contains(@title,"xlsx")]/following-sibling::div//span[text()="预览"]/..')
    #png预览按钮
    emailDetailPage_previewPNGBtn_loc = (By.XPATH,'//div[@class="attachment"]//li//p[contains(@title,"png")]/following-sibling::div//span[text()="预览"]/..')
    #预览之后的图片
    emailDetailPage_previewedImg_loc = (By.XPATH,'//div[@class="vue-lb-figure"]//img')
    #相关邮件列表
    emailDetailPage_relatedEmailList_loc = (By.XPATH,'//div[@class="el-table table_email table_email_body el-table--fit el-table--enable-row-hover el-table--enable-row-transition"]//tr')
    #相关邮件tab按钮
    emailDetailPage_relatedEmailBtn_loc = (By.XPATH,'//div[text()="相关邮件"]')
    #下载按钮
    emailDetailPage_downloadSmallAttachBtn_loc = (By.XPATH,'//div[@class="attachment"]//li//span[text()="下载"]/..')
    #批量下载按钮
    emailDetailPage_downloadAllBtn_loc = (By.XPATH,'//div[@class="attachment"]//div[@class="download"]/span[1]')
    #详细信息按钮
    emailDetailPage_detailInfoBtn_loc = (By.XPATH,'//div[contains(@class,"status_info")]//div[contains(text(),"详细信息")]')

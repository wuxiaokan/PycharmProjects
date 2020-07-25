# -*- encoding: utf-8 -*-
'''
@File    :   recipientBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/20 0020 10:38   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class recipientBoxPageLoc:
    #用户顶部导航
    userNav_loc = (By.XPATH,'//div[@class="navbar-user focus-outside"]')
    #用户文本
    userText_loc = (By.XPATH,'//div[@class="user-text fl"]')
    #未读邮件的主题
    recipientBoxPage_unReadEmailSubject_loc = (By.XPATH,'//div[@title="点击标记已读"]/ancestor::tr//div[contains(@class,"sub_item")]')
    #邮件主题
    # recipientBoxPage_subject_loc = (By.XPATH,'//div[@class="sub_item"]//div[contains(@class,"sub_info info3")]/span/span[not(contains(@class,"fc05"))]')
    recipientBoxPage_subject_loc = (By.XPATH,'//div[@class="sub_item"]//div[contains(@class,"sub_info info3")]/span/span[not(contains(@class,"fc05")) and not(contains(@class,"boxName"))]')
    #收件箱页面，收件箱按钮
    recipientBoxPage_recipientBoxBtn_loc = (By.XPATH,'//div[@id="pane-email" or @id="pane-customer" or @id="pane-supplier" or @id="pane-inner"]//span[text()="收件箱"]/../..')
    #收件箱页面，已发箱按钮
    recipientBoxPage_hasSendBoxBtn_loc = (By.XPATH,'//ul[contains(@class,"search-menu")]//span[text()="已发箱"]')
    #收件箱页面，待发箱按钮
    recipientBoxPage_waitSendBoxBtn_loc = (By.XPATH,'//span[text()="待发箱"]')
    #收件箱页面，审批箱按钮
    recipientBoxPage_approvalBoxBtn_loc = (By.XPATH,'//span[text()="审批箱"]')
    #收件箱页面，审批箱邮件数量
    recipientBoxPage_approvalBoxNum_loc = (By.XPATH,'//span[text()="审批箱"]/following-sibling::span')
    #邮件主题
    recipientBoxPage_emailSubject_loc = (By.XPATH,'//div[contains(@class,"sub_info")]')
    #收件箱页面，过滤按钮
    recipientBoxPage_filterBtn_loc = (By.XPATH,'//div[@class="icon_group"]/div[1]')
    #收件箱页面，过滤列表中待审批按钮
    recipientBoxPage_filterListWaitApprovalBtn_loc = (By.XPATH,'//ul[@x-placement="bottom" or @x-placement="top"]//li[text()="待审批"]')
    #收件箱页面，待审批按钮
    recipientBoxPage_waitapprovalBtn_loc = (By.XPATH,'//tr[@class="el-table__row"]//span[@title="待审批"]')
    #收件箱页面，审批通过按钮
    recipientBoxPage_approvalPassBtn_loc = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="审批通过"]')
    #收件箱页面，审批驳回按钮
    recipientBoxPage_approvalRejectBtn_loc = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="审批驳回"]')
    #收件箱页面，设置tab
    recipientBoxPage_settingTabBtn_loc = (By.XPATH,'//div[@class="text closable"]')
    #收件箱页面，查询箱
    recipientBoxPage_queryBoxBtn_loc = (By.XPATH,'//ul[contains(@class,"search-menu")]//span[text()="主题包含重构，勿动"]')
    #收件箱页面，邮件选择框
    recipientBoxPage_emailCheckBoxBtn_loc = (By.XPATH,'//tbody//div[@class="cell"]//label')
    #收件箱页面，自定义箱按钮
    recipientBoxPage_customBoxListBtn_loc = (By.XPATH,'//div[@class="menu-tree"]//span[text()="自定义箱测试，勿动"]')
    #邮箱主tab
    recipientBoxPage_emailBoxBtn_loc = (By.XPATH,'//div[@id="tab-email"]')
    #收件箱页面，客户箱按钮
    recipientBoxPage_customerBoxBtn_loc = (By.XPATH,'//div[@id="tab-customer"]')
    #收件箱页面，供应商箱按钮
    recipientBoxPage_supplierBoxBtn_loc = (By.XPATH,'//div[@id="tab-supplier"]')
    #收件箱页面，内部联系人箱按钮
    recipientBoxPage_innerBoxBtn_loc = (By.XPATH,'//div[@id="tab-inner"]')
    #收件箱页面，刷新按钮
    recipientBoxPage_refreshBtn_loc = (By.XPATH,'//div[@class="operate_button_vue el-tooltip icon"]')
    #收件箱页面，全部选择框
    recipientBoxPage_selectAllCheckBox_loc = (By.XPATH,'//div[contains(@class,"email_module_list_vue")]//div[@class="plugins"]//label')
    #收件箱页面，移动按钮
    recipientBoxPage_moveBtn_loc = (By.XPATH,'//div[@class="icon_group"]//div[@class="el-tooltip el-dropdown"][2]')
    #收件箱页面，移动到收件箱按钮
    recipientBoxPage_moveToRecipientBoxBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="收件箱"]')
    #移动页面，可删除的自定义箱子列表
    recipientBoxPage_movePage_canDelCustomBoxList_loc = (By.XPATH,'//div[@class="treeBox"]//span[contains(text(),"可删除")]/..')
    #移动页面，确认按钮
    recipientBoxPage_movePage_sureMoveBtn_loc = (By.XPATH,'//button[@class="el-button small el-button--primary"]//span[text()="确认"]/..')
    #收件箱页面，未读箱邮件数量
    recipientBoxPage_unReadEmailNum_loc = (By.XPATH,'//div[@class="side-bar"]//span[text()="未读邮件"]//following-sibling::span[@class="receipt-num"]')
    #收件箱页面，星标邮件数量
    recipientBoxPage_starEmailNum_loc = (By.XPATH,'//div[@class="side-bar"]//span[text()="星标邮件"]//following-sibling::span[@class="receipt-num"]')
    #收件箱页面，分页按钮
    recipientBoxPage_pageBtn_loc = (By.XPATH,'//div[@class="el-select el-select--mini"]//input')
    #分页页数按钮
    recipientBoxPage_pageNumBtn_loc = (By.XPATH,'//ul[@class="el-pager"]//li')
    #收件箱页面，200每页按钮
    recipientBoxPage_200PageBtn_loc = (By.XPATH,'//div[@x-placement="top-start"]//span[text()="200条/页"]/..')
    #免回复标签
    recipientBoxPage_freeReplyBtn_loc = (By.XPATH,'//div[@class="operater_status"]//span[@title="免回复"]')
    #已回复icon
    recipientBoxPage_replyedIconBtn_loc = (By.XPATH,'//div[@class="operater_status"]//span[@title="已回复"]')
    #已转发icon
    recipientBoxPage_forwardIconBtn_loc = (By.XPATH,'//div[@class="operater_status"]//span[@title="已转发"]')
    #已读icon
    recipientBoxPage_readIconBtn_loc = (By.XPATH,'//div[@class="operater_status"]//div[@title="点击标记未读"]')
    #未读icon
    recipientBoxPage_unReadIconBtn_loc = (By.XPATH,'//div[@class="operater_status"]//div[@title="点击标记已读"]')
    #内部转发icon
    recipientBoxPage_innerForwardIconBtn_loc = (By.XPATH,'//div[@class="sub_item"]//a[@title="内部转发出"]')
    #追踪icon
    recipientBoxPage_traceIconBtn_loc = (By.XPATH,'//div[@class="el-tooltip attach_item"]')
    #已经标记星标icon
    recipientBoxPage_markStarIconBtn_loc = (By.XPATH,'//div[@title="点击取消星标"]')
    #未标记星标icon
    recipientBoxPage_unMarkStarIconBtn_loc = (By.XPATH,'//div[@title="点击设置星标"]')
    #右上角提示框关闭按钮
    recipientBoxPage_closeRightTopNotifyBtn_loc = (By.XPATH,'//div[@class="el-dialog notifyDialog"]//button[@class="el-dialog__headerbtn"]')
    #所有邮件标签列表
    recipientBoxPage_emailMarksList_loc = (By.XPATH,'//span[@class="tag"]//ul//li')
    #每封邮件的标签集合
    recipientBoxPage_everyEmailMarks_loc = (By.XPATH,'//span[@class="tag"]//ul')
    #发件人
    recipientBoxPage_sender_loc = (By.XPATH,'//span[not(contains(@class,"compact"))]//span[@class="contact_names"]')
    #收件人
    recipientBoxPage_recipient_loc = (By.XPATH,'//span[contains(@class,"compact")]//span[@class="contact_names"]')
    #日期
    recipientBoxPage_date_loc = (By.XPATH,'//tbody//tr//div[@class="cell"]//div[@class="el-tooltip" or @class="el-tooltip f_w_bold"]')
    #邮件所在箱子名
    recipientBoxPage_emailBoxName_loc = (By.XPATH,'//div[@class="sub_item"]//span[@class="boxName"]')
    #附件icon标志
    recipientBoxPage_attachIconBtn_loc = (By.XPATH,'//tbody//tr//div[@class="attach_item"]')
    #未建档icon标志
    recipientBoxPage_unArchiverIconBtn_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg" and contains(@style,"color: rgb(92, 107, 119)")]')

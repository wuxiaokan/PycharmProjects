# -*- encoding: utf-8 -*-
'''
@File    :   test_emailAccountSetting.py
@Contact :   fttxtest<fttxtest@163.com>
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 11:22   dmk      1.0         None
'''

import pytest
from pageObject.emailSelectContactsPage import emailSelectContactsPage

customerSearch_datas = [(1,"根据客户名称搜索",0,1,0,0,0,"//input[@placeholder='请输入客户名称']","test",0,0),(2,"根据联系人名称搜索",0,1,0,0,0,"//div[@id='pane-first']//input[@placeholder='请输入联系人名称']","交易",0,0),(3,"根据客户简称名称搜索",0,1,0,0,0,"//div[@id='pane-first']//input[@placeholder='请输入客户简称']","科技",0,0),(4,"根据联系人邮箱搜索",0,1,0,0,0,"//div[@id='pane-first']//input[@placeholder='请输入联系人邮箱']","qq.com",0,0),(5,"根据客户代码搜索",0,1,0,0,0,"//div[@id='pane-first']//input[@placeholder='请输入客户代码']","33333",0,0),(6,"根据未联系天数搜索",0,0,1,0,0,0,0,"//div[@title='未联系天数']//input","//span[text()='最近七天']"),(7,"根据跟进阶段搜索",0,0,1,0,0,0,0,"//div[@title='跟进阶段']//input","//div[@x-placement='bottom-start']//span[text()='产品推广']"),(8,"根据国家地区搜索",0,0,1,0,0,0,0,"//div[@title='国家地区']//input","//div[@x-placement='bottom-start']//span[text()='阿富汗']"),(9,"根据主营产品搜索",0,0,1,0,0,0,0,"//div[@title='主营产品']//input","//div[@x-placement='bottom-start']//span[text()='电器']"),(10,"根据客户类型搜索",0,0,1,0,0,0,0,"//div[@title='客户类型']//input","//div[@x-placement='bottom-start']//span[text()='潜在客户']"),(11,"根据客户等级搜索",0,0,1,0,0,0,0,"//div[@title='客户等级']//input","//div[@x-placement='bottom-start']//span[text()='一般']"),(12,"根据客户来源搜索",0,0,1,0,0,0,0,"//div[@title='客户来源']//input","//div[@x-placement='bottom-start']//span[text()='互联网']"),(13,"根据业务类型搜索",0,0,1,0,0,0,0,"//div[@title='业务类型']//input","//div[@x-placement='bottom-start']//span[text()='采购商']")]


internalContactSelectAndCancelSelect_datas = [("1","客户联系人选择","1"),("2","供应商联系人选择","2"),("3","内部联系人选择","3")]

class TestCustomerSearchEmailContacts():

    @pytest.mark.parametrize("caseid,casename,is_public,is_send,is_select,is_click,click_btn,sendInput,key,selectTag,option",customerSearch_datas)
    def test_customerSearchEmailContacts(self,caseid,casename,is_public,is_send,is_select,is_click,click_btn,sendInput,key,selectTag,option,login):
        self.is_public = is_public
        self.is_send = is_send
        self.is_select = is_select
        self.is_click = is_click
        self.click_btn = click_btn
        self.sendInput = sendInput
        self.key = key
        self.selectTag = selectTag
        self.option = option
        self.driver = emailSelectContactsPage(login)
        self.driver.run_customerSearch_case(casename,is_public,is_send,is_select,sendInput,key,selectTag,option,is_click,click_btn)


    @pytest.mark.parametrize("caseid,casename,contact_type",internalContactSelectAndCancelSelect_datas)
    def test_internalContactSelectAndCancelSelect(self,caseid,casename,contact_type,login):
        self.driver = emailSelectContactsPage(login)
        self.driver.run_internalContactSelectAndCancelSelect_case(contact_type)


if __name__ == '__main__':
    pytest.main(["-v","test_customerSearchEmailContacts.py"])

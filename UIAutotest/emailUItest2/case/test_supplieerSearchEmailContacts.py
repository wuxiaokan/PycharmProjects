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

customerSearch_datas = [(1,"根据供应商名称搜索",1,0,0,0,"//input[@placeholder='请输入供应商名称']","test",0,0),(2,"根据联系人名称搜索",1,0,0,0,"//div[@id='pane-second']//input[@placeholder='请输入联系人名称']","公司",0,0),(3,"根据供应商编码搜索",1,0,0,0,"//div[@id='pane-second']//input[@placeholder='请输入供应商编码']",22222,0,0),(4,"根据联系人邮箱搜索",1,0,0,0,"//div[@id='pane-second']//input[@placeholder='请输入联系人邮箱']","aliyun.com",0,0),(5,"根据供应商简称搜索",1,0,0,0,"//div[@id='pane-second']//input[@placeholder='请输入供应商简称']","科技",0,0),(6,"根据主营产品搜索",0,1,0,0,0,0,"//div[@id='pane-second']//div[@title='主营产品']//input","//div[@x-placement='bottom-start']//span[text()='电器']"),(7,"根据供应商类型搜索",0,1,0,0,0,0,"//div[@id='pane-second']//div[@title='供应商类型']//input","//div[@x-placement='bottom-start']//span[text()='加工商']"),(8,"根据供应商标签搜索",0,1,0,0,0,0,"//div[@id='pane-second']//div[@title='供应商标签']//input","//div[@x-placement='bottom-start']//span[text()='蓝色']")]


class TestSupplieerSearchEmailContacts():

    @pytest.mark.parametrize("caseid,casename,is_send,is_select,is_click,click_btn,sendInput,key,selectTag,option",customerSearch_datas)
    def test_supplieerSearchEmailContacts(self,caseid,casename,is_send,is_select,is_click,click_btn,sendInput,key,selectTag,option,login):
        self.is_send = is_send
        self.is_select = is_select
        self.is_click = is_click
        self.click_btn = click_btn
        self.sendInput = sendInput
        self.key = key
        self.selectTag = selectTag
        self.option = option
        self.driver = emailSelectContactsPage(login)
        self.driver.run_supplieerSearch_case(casename,is_send,is_select,sendInput,key,selectTag,option,is_click,click_btn)

if __name__ == '__main__':
    pytest.main(["-v","test_supplieerSearchEmailContacts.py"])

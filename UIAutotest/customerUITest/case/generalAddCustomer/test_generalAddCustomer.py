# -*- encoding: utf-8 -*-
'''
@File    :   test_generalAddCustomer.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 0016 10:24   dmk      1.0         None
'''

import pytest,allure
from utils.generator import *
from pageObject.generalAddCustomerPage.generalAddCustomerPage import generalAddCustomerPage


generalAddCustomer_datas = [(1,"普通新建客户-主链路",1,[{"客户代码": random_phone_number()+random_str(3,8)},{"客户名称": random_name() +str(random_number(3))+ "测试，可删除"}, {"客户简称": random_name() + "测试"},{"企业网站": random_url()}, {"固定电话": random_phone_number()},{"传真": random_number(8)}, {"银行账号": random_creditCardNumber()}, {"联系地址": random_address()},{"邮编": random_postcode()},{"Facebook公司主页": random_url()}, {"Twitter公司主页": random_url()}, {"字符": random_str(1,3)},{"百分比": str(random_pyfloat(2,1))}, {"整数": random_number(2)}, {"小数": str(random_pyfloat(0,1))},{"姓名": random_name()}, {"邮箱": random_email()}, {"手机": random_phone_number()},  {"职务": random_job()}, {"Facebook账号": random_phone_number()}, {"Facebook个人主页": random_url()}, {"Twitter账号": random_str(6,12)}, {"Twitter个人主页": random_url()}, {"Linkedin": random_number(7)}, {"WhatsApp": random_str(4,9)}, {"Skype": random_str(3,6)+str(random_number(3))}, {"QQ": random_number(8)}, {"微信": random_str(3,5)+str(random_number(5))},{"联系人整数": random_number(3)},{"联系人小数": str(random_pyfloat(0,1))},{"联系人字符": random_str(2,4)}, {"联系人百分比": str(random_pyfloat(2,1))}],[{"国家/地区":"阿富汗"},{"客户类型":"大客户"},{"开户银行":"中国工商银行"},{"客户等级":"非常重要"},{"客户来源":"互联网"},{"业务类型":"贸易公司"},{"跟进阶段":"资料获得"},{"系统数据类型":"武汉"}]),(2,"编辑客户-主链路",0,[{"客户代码": random_phone_number()+random_str(3,8)},{"客户名称": random_name() +str(random_number(3))+ "测试，可删除"}, {"客户简称": random_name() + "测试"},{"企业网站": random_url()}, {"固定电话": random_phone_number()},{"传真": random_number(8)}, {"银行账号": random_creditCardNumber()}, {"联系地址": random_address()},{"邮编": random_postcode()},{"Facebook公司主页": random_url()}, {"Twitter公司主页": random_url()}, {"字符": random_str(1,3)},{"百分比": str(random_pyfloat(2,1))}, {"整数": random_number(2)}, {"小数": str(random_pyfloat(0,1))},{"姓名": random_name()}, {"邮箱": random_email()}, {"手机": random_phone_number()},  {"职务": random_job()}, {"Facebook账号": random_phone_number()}, {"Facebook个人主页": random_url()}, {"Twitter账号": random_str(6,12)}, {"Twitter个人主页": random_url()}, {"Linkedin": random_number(7)}, {"WhatsApp": random_str(4,9)}, {"Skype": random_str(3,6)+str(random_number(3))}, {"QQ": random_number(8)}, {"微信": random_str(3,5)+str(random_number(5))},{"联系人整数": random_number(3)},{"联系人小数": str(random_pyfloat(0,1))},{"联系人字符": random_str(2,4)}, {"联系人百分比": str(random_pyfloat(2,1))}],[{"国家/地区":"安道尔"},{"客户类型":"意向客户"},{"开户银行":"中国农业银行"},{"客户等级":"一般"},{"客户来源":"客户推荐"},{"业务类型":"采购商"},{"跟进阶段":"商务洽谈"},{"系统数据类型":"fttxtest@sina.cn"}])]


addAndEditMinorCustomerInfo_datas = [(1,"新增客户，申请编码",{"is_add":1}),(2,"编辑客户，申请编码",{"is_add":0}),(3,"新增客户，选择主营产品",{"is_add":1}),(4,"编辑客户，选择主营产品",{"is_add":0}),(5,"新增客户，添加注释",{"is_add":1}),(6,"编辑客户，添加注释",{"is_add":0}),(7,"新增客户，点击扩展信息里面的是否按钮",{"is_add":1}),(8,"编辑客户，点击扩展信息里面的是否按钮",{"is_add":0}),(9,"新增客户，选择自定义数据字典-自定义",{"is_add":1}),(11,"新增客户，选择自定义数据字典-字典",{"is_add":1}),(10,"编辑客户，选择自定义数据字典-自定义",{"is_add":0}),(12,"编辑客户，选择自定义数据字典-字典",{"is_add":0}),(13,"新增客户，选择一个日期",{"is_add":1}),(14,"编辑客户，选择一个日期",{"is_add":0}),(15,"新增客户，选择性别-男",{"is_add":1}),(17,"新增客户，选择性别-女",{"is_add":1}),(16,"编辑客户，选择性别-男",{"is_add":0}),(18,"编辑客户，选择性别-女",{"is_add":0}),(19,"新增客户，设置生日",{"is_add":1}),(20,"编辑客户，设置生日",{"is_add":0}),(21,"编辑客户，设置其他业务员",{"is_add":0}),(22,"新增客户，启禁用联系人",{"is_add":1}),(23,"编辑客户，启禁用联系人",{"is_add":0}),(24,"新建客户，上传附件",{"is_add":1}),(25,"编辑客户，上传附件",{"is_add":0})]


addCustomerContact_datas = [(1,"新增客户，新增联系人",{"is_add":1}),(1,"编辑客户，新增联系人",{"is_add":0})]

delCustomerContact_datas = [(1,"编辑客户，删除全部联系人",{"is_add":0,"del_num":2}),(2,"编辑客户，删除多个联系人",{"is_add":0,"del_num":1}),(3,"编辑客户，删除当前的一个联系人",{"is_add":0,"del_num":0})]

saveAndAddCustomer_datas = [(1,"新增客户，保存并新建",{"is_add":1,"is_save":1}),(2,"编辑客户，保存并新建",{"is_add":0,"is_save":1}),(3,"新增客户，取消弹窗-点击是",{"is_add":1,"is_save":2}),(4,"编辑客户，取消弹窗-点击是",{"is_add":0,"is_save":2}),(5,"新增客户，取消弹窗-点击否",{"is_add":1,"is_save":3}),(6,"编辑客户，取消弹窗-点击否",{"is_add":0,"is_save":3}),(7,"新增客户，取消弹窗-点击取消",{"is_add":1,"is_save":3}),(8,"编辑客户，取消弹窗-点击取消",{"is_add":0,"is_save":3})]

@allure.feature("普通新建客户相关功能")
class TestGeneralAddCustomer:

    @allure.story("普通新建客户")
    @pytest.mark.parametrize("caseid,casename,is_add,customer_sendKeys,customer_selectKeys",generalAddCustomer_datas)
    def test_generalAddAndEditCustomer_mainFlow(self,caseid,casename,is_add,customer_sendKeys,customer_selectKeys,login):
        self.driver = generalAddCustomerPage(login)
        self.driver.run_generalAddCustomer_case(is_add,customer_sendKeys,customer_selectKeys)


    @allure.story("新建和编辑客户，填充编码，附件等信息")
    @pytest.mark.parametrize("caseid,casename,data",addAndEditMinorCustomerInfo_datas)
    def test_addAndEditMinorCustomerInfo(self,caseid,casename,data,login):
        if caseid == 1:
            self.driver = generalAddCustomerPage(login)
            self.driver.run_addAndEditMinorCustomerInfo_case(caseid,data)


    @allure.story("新增客户联系人")
    @pytest.mark.parametrize("caseid,casename,data",addCustomerContact_datas)
    def test_addCustomerContact(self,caseid,casename,data,login):
        self.driver = generalAddCustomerPage(login)
        self.driver.run_addCustomerContact_case(data)


    @allure.story("删除联系人相关功能")
    @pytest.mark.parametrize("caseid,casename,data",delCustomerContact_datas)
    def test_delCustomerContact(self,caseid,casename,data,login):
        self.driver = generalAddCustomerPage(login)
        self.driver.run_delCustomerContact_case(data)


    @allure.story("保存新建和取消保存相关功能")
    @pytest.mark.parametrize("caseid,casename,data",saveAndAddCustomer_datas)
    def test_saveAndAddCustomer(self,caseid,casename,data,login):
        self.driver = generalAddCustomerPage(login)
        self.driver.run_saveAndAddCustomer_case(data)



if __name__ == '__main__':
    pytest.main(["-s","test_generalAddCustomer.py"])
# -*- encoding: utf-8 -*-
'''
@File    :   test_customBox.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/18 0018 10:32   dmk      1.0         None
'''

import allure,pytest
from pageObject.customBoxPage.customBoxPage import customBoxPage

addCustomBox_datas = [(1,"新增不重名的一级自定义箱",{"is_parent":1,"is_repeat":0,"expect_toast":"操作成功！"}),(2,"新增重名的一级自定义箱",{"is_parent":1,"is_repeat":1,"expect_toast":"箱子名称已存在"}),(3,"新增不重名的二级自定义箱",{"is_parent":0,"is_repeat":0,"expect_toast":"操作成功！"}),(4,"新增重名的二级自定义箱",{"is_parent":0,"is_repeat":1,"expect_toast":"箱子名称已存在"})]

editCustomBox_datas = [(1,"编辑不重名的一级自定义箱",{"is_parent":1,"is_repeat":0,"expect_toast":"操作成功！"}),(2,"编辑重名的一级自定义箱",{"is_parent":1,"is_repeat":1,"expect_toast":"箱子名称已存在"}),(3,"编辑不重名的二级自定义箱",{"is_parent":0,"is_repeat":0,"expect_toast":"操作成功！"}),(4,"编辑重名的二级自定义箱",{"is_parent":0,"is_repeat":1,"expect_toast":"箱子名称已存在"})]

delCustomBox_datas = [(1,"删除一级自定义箱子",{"is_parent":1,"expect_toast":"删除成功"}),(2,"删除二级自定义箱子",{"is_parent":0,"expect_toast":"删除成功"})]


moveAllEmail_datas = [(1,"移动全部邮件到收件箱",{"boxCategory":"收件箱"}),(2,"移动全部邮件到已发箱",{"boxCategory":"已发箱"}),(3,"移动全部邮件到群发箱",{"boxCategory":"群发箱"}),(4,"移动全部邮件到客户箱",{"boxCategory":"客户箱"}),(5,"移动全部邮件到供应商箱",{"boxCategory":"供应商箱"}),(6,"移动全部邮件到内部联系人箱",{"boxCategory":"内部联系人箱"}),(7,"移动全部邮件到自定义箱",{"boxCategory":"自定义箱"})]


@allure.feature("自定义箱相关功能")
class TestCustomBox:

    @allure.story("新增自定义箱相关功能")
    @pytest.mark.parametrize("caseid,casename,data",addCustomBox_datas)
    def test_addCustomBox(self,caseid,casename,data,login):
        if caseid == 3:
            self.driver = customBoxPage(login)
            self.driver.run_addCustomBox_case(data)


    @allure.story("编辑自定义箱子相关功能")
    @pytest.mark.parametrize("caseid,casename,data",editCustomBox_datas)
    def test_editCustomBox(self,caseid,casename,data,login):
        self.driver = customBoxPage(login)
        self.driver.run_editCustomBox_case(data)


    @allure.story("删除自定义箱子功能")
    @pytest.mark.parametrize("caseid,casename,data",delCustomBox_datas)
    def test_delCustomBox(self,caseid,casename,data,login):
        self.driver = customBoxPage(login)
        self.driver.run_delCustomBox_case(data)


    @allure.story("清空自定义箱子")
    def test_clearCustomBox(self,login):
        self.driver = customBoxPage(login)
        self.driver.run_clearCustomBox_case()


    @allure.story("移到全部邮件相关功能")
    @pytest.mark.parametrize("caseid,casename,data",moveAllEmail_datas)
    def test_moveAllEmail(self,caseid,casename,data,login):
        self.driver = customBoxPage(login)
        self.driver.run_moveAllEmail_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_customBox.py"])
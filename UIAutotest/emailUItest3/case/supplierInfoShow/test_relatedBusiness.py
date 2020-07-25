# -*- encoding: utf-8 -*-
'''
@File    :   test_relatedBusiness.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 10:57   dmk      1.0         None
'''

import allure,pytest
from pageObject.supplierInfoShowPage.relatedBusinessPage import relatedBusinessPage


filterRelatedBusiness_datas = [(1,"过滤日志",{"condition":"日志"}),(2,"过滤跟进",{"condition":"跟进"})]


@allure.feature("相关业务相关功能")
class TestRelatedBusiness:

    @allure.story("相关业务过滤功能")
    @pytest.mark.parametrize("caseid,casename,data",filterRelatedBusiness_datas)
    def test_filterRelatedBusiness(self,caseid,casename,data,login):
        self.driver = relatedBusinessPage(login)
        self.driver.run_filterRelatedBusiness_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_relatedBusiness.py"])
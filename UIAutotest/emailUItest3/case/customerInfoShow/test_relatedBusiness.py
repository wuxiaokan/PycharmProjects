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
from pageObject.customerInfoShowPage.relatedBusinessPage import relatedBusinessPage

filterRelatedBusiness_datas = [(1,"过滤日志",{"condition":"日志"}),(2,"过滤迁移信息",{"condition":"迁移信息"}),(3,"过滤商机",{"condition":"商机"}),(4,"过滤跟进",{"condition":"跟进"}),(5,"过滤edm",{"condition":"edm"}),(6,"过滤订单",{"condition":"订单"}),(7,"过滤报价",{"condition":"报价"})]


@allure.feature("相关业务相关功能")
class TestRelatedBusiness:

    @allure.story("相关业务过滤功能")
    @pytest.mark.parametrize("caseid,casename,data",filterRelatedBusiness_datas)
    def test_filterRelatedBusiness(self,caseid,casename,data,login):
        self.driver = relatedBusinessPage(login)
        self.driver.run_filterRelatedBusiness_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_relatedBusiness.py"])
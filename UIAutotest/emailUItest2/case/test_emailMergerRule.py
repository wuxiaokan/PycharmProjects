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
from pageObject.emailMergerRulePage import emailMergerRulePage

@pytest.fixture(scope="function")
def resotreInstantlyMerger(login):
    driver = login
    yield
    #取消立即归并
    ele = driver.find_element_by_xpath('//div[@class="merger_check"]//label')
    if "is-checked" in ele.get_attribute("class"):
        ele.click()

class TestEmailMergerRule():

    def test_instantlyMergerSave(self,login,resotreInstantlyMerger):
        self.driver = emailMergerRulePage(login)
        self.driver.run_instantlyMergerSave_case()


if __name__ == '__main__':
    pytest.main(["-v","test_emailMergerRule.py"])

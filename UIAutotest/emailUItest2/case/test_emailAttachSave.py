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
from pageObject.emailAttachSavePage import emailAttachSavePage

singleSaveAttach_datas = [("1","单个转存到共享",1,0),("2","单个转存到个人",0,0),("3","批量转存到共享",0,1),("4","批量转存到个人",1,1)]

class TestEmailAttachSave():

    @pytest.mark.parametrize("caseid,casename,is_share,is_multiple",singleSaveAttach_datas)
    def test_saveEmailAttach(self,caseid,casename,is_share,is_multiple,login):
        if caseid == "1":
            self.driver = emailAttachSavePage(login)
            self.driver.run_saveEmailAttach_case(casename,is_share,is_multiple)


if __name__ == '__main__':
    pytest.main(["-v","test_emailAttachSave.py"])

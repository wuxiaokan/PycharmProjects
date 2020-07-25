# -*- encoding: utf-8 -*-
'''
@File    :   test_emailSignatureSwitch.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 19:41   dmk      1.0         None
'''

import pytest
from pageObject.emailReceiptBoxPage import emailReceiptBoxPage

datas = [("1","新邮件签名","fttx666<fttx666@aliyun.com>","fttx888<fttx888@aliyun.com>",['新邮件签名fttx666@aliyun.com'],['新邮件签名fttx888@aliyun.com']),("2","回复签名","fttx666<fttx666@aliyun.com>","fttx888<fttx888@aliyun.com>",['回复邮件签名fttx666@aliyun.com'],['回复邮件签名fttx888@aliyun.com']),("3","转发邮件签名","fttx666<fttx666@aliyun.com>","fttx888<fttx888@aliyun.com>",['转发邮件签名fttx666@aliyun.com'],['转发邮件签名fttx888@aliyun.com'])]

class TestEmailSignatureSwitch():

    @pytest.mark.parametrize("caseid,case_name,default_account,purpose_account,default_signature,purpose_signature", datas)
    def test_newEmailSignature(self,caseid,case_name,default_account,purpose_account,default_signature,purpose_signature,login001):
        self.caseid = caseid
        self.default_account = default_account
        self.purpose_account = purpose_account
        self.default_signature = default_signature
        self.purpose_signature = purpose_signature

        self.driver1 = emailReceiptBoxPage(login001)
        if self.caseid == "1":
            self.driver1.enterWriteEmail()
        else:
            self.driver1.enter_email()
            if self.caseid == "2":
                self.driver1.reply_email()
            else:
                self.driver1.forword_email()
        self.send_account = self.driver1.switch_sender(self.default_account,self.purpose_account)
        self.signatureContent = self.driver1.get_signatureContent()
        if self.send_account == self.default_account:
            assert self.signatureContent == self.default_signature
        else:
            assert self.signatureContent == self.purpose_signature


if __name__ == '__main__':
    pytest.main(["-v","test_emailSignatureSwitch.py"])
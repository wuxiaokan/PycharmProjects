# -*- encoding: utf-8 -*-
'''
@File    :   emailDetailPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/31 0031 16:45   dmk      1.0         None
'''

import time,allure
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc


class emailDetailPageCommon(Action,emailDetailPageLoc):

    #获取邮件详情里面的主题
    def get_subjectOfEmailDetail(self):
        return self.get_elementText(self.emailDetailPage_subject_loc,key="获取邮件主题")

    # 获取邮件详情里面的收件人
    def get_recipientOfEmailDetail(self):
        return self.get_elementText(self.emailDetailPage_recipient_loc, index="all")

    # 获取邮件详情里面的发件人
    def get_senderOfEmailDetail(self):
        return self.get_elementText(self.emailDetailPage_sender_loc)

    #获取邮件详情里面的抄送人
    def get_ccOfEmailDetail(self,index=0):
        if self.is_element_exist(self.emailDetailPage_detailInfoBtn_loc[1]):
            self.click_ele(self.emailDetailPage_detailInfoBtn_loc)
        return self.get_elementText(self.emailDetailPage_cc_loc,index=index)

    # 获取邮件详情里面的所有小附件
    def get_allSmallAttachNamesOfEmailDetail(self):
        time.sleep(3)
        return self.get_elementText(self.emailDetailPage_attachName_loc, index="all")

    # 获取邮件详情里面的产品图片地址
    def get_allProductImgUrlsOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            allProductImgEles = self.find_element(self.emailDetailPage_productImg_loc, index="all")
            allProductImgurls = []
            for productImgEle in allProductImgEles:
                allProductImgurls.append(productImgEle.get_attribute("src").split("?")[0].split("/")[-1])
            allProductImgCodes = self.get_elementText(self.emailDetailPage_productCode_loc, index="all")
            return allProductImgurls, allProductImgCodes
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    # 获取邮件详情里面的快照地址
    def get_allSiteUrlsOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            allSiteImgEles = self.find_element(self.emailDetailPage_siteImg_loc, index="all")
            allSiteImgurls = []
            for siteImgEle in allSiteImgEles:
                allSiteImgurls.append(siteImgEle.get_attribute("href"))
            return allSiteImgurls
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    # 获取邮件详情里面的邮件文本
    def get_emailTextOfEmailDetail(self,index=0):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            return self.get_elementText(self.emailDetailPage_emailContent_loc,index=index)
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    # 获取邮件详情里面的大附件名
    def get_allBigAttachNamesOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            bigAttachNames = []
            bigAttachNames_tmp = self.get_elementText(self.emailDetailPage_bigAttachName_loc, index="all",key="获取大附件")
            for name in bigAttachNames_tmp:
                bigAttachNames.append(name.split("(")[0])
            return bigAttachNames
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()


    #点击要移动的箱子类型
    def clickBoxCategory_toMove(self,boxCategory):
        boxCategory_loc = (By.XPATH,self.emailDetailPage_moveToHasSendBoxBtn_loc[1].replace("已发箱",boxCategory))
        self.click_ele(boxCategory_loc,key="点击{}".format(boxCategory))

    #获取翻译框里面的文本
    def get_textOfTransInput(self):
        try:
            self.switch_frame(self.emailDetailPage_transFrame_loc)
            transText = self.find_element(self.emailDetailPage_transInput_loc,key="获取翻译框文本").get_attribute("value")
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()
        return transText

    #邮件详情内，点击更多按钮
    def clickMoreOperateBtn(self):
        self.click_ele(self.emailDetailPage_moreOperateBtn_loc, key="点击更多操作按钮")

    #邮件详情内，点击更多里面的按钮
    def clickBtn_moreOperate(self,btn_text):
        relatedEmailBtn_loc = (By.XPATH, self.emailDetailPage_mergerBtn_loc[1].replace("归并", btn_text))
        self.click_ele(relatedEmailBtn_loc, key="点击{}按钮".format(btn_text))
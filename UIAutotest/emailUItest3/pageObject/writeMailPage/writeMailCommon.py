# -*- encoding: utf-8 -*-
'''
@File    :   writeMailCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/6 0006 16:07   dmk      1.0         None
'''

import allure,time,os
from random import randint
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.config import ATTACH_PATH
from utils.generator import *
from pageObject.basePage import Action
from pageObject.writeMailPage.writeMailPage_loc import writeMailPageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc


class writeMailCommon(Action,writeMailPageLoc,recipientBoxPageLoc,emailDetailPageLoc):


    def __init__(self,driver):
        super(writeMailCommon,self).__init__(driver)


    #上传附件
    def upload_attach(self,smallAttach,bigAttach):
        with allure.step("上传附件"):
            with allure.step("点击附件下拉按钮"):
                self.find_element(self.writeMailPage_attachPullDownBtn_loc).click()
            time.sleep(0.2)
            with allure.step("上传普通附件"):
                for small in smallAttach:
                    smallAttachPath = os.path.join(ATTACH_PATH,small)
                    self.find_element_byPresence(self.writeMailPage_smallAttachInput_loc).send_keys(smallAttachPath)
            with allure.step("上传超大附件"):
                for big in bigAttach:
                    bigAttachPath = os.path.join(ATTACH_PATH,big)
                    self.find_element_byPresence(self.writeMailPage_bigAttachInput_loc).send_keys(bigAttachPath)
            time.sleep(3)
            with allure.step("判断上传附件是否成功"):
                with allure.step("获取所有的附件名"):
                    allAttachNames = self.get_elementText(self.writeMailPage_attachName_loc,index="all")
                with allure.step("遍历小附件"):
                    for small in smallAttach:
                        if small not in allAttachNames:
                            self.screenshotImg(key="普通附件上传不成功")
                            raise Exception("该小附件：{}，上传不成功，上传之后的附件列表：{}".format(small,allAttachNames))
                with allure.step("遍历大附件"):
                    for big in bigAttach:
                        if big not in allAttachNames:
                            self.screenshotImg(key="大附件上传不成功")
                            raise Exception("该大附件：{}，上传不成功，上传之后的附件列表：{}".format(big,allAttachNames))
            with allure.step("判断大附件是否有7天有效标识"):
                with allure.step("根据7天有效标识获取附件名"):
                    allBigAttachNames = self.get_elementText(self.writeMailPage_bigAttachName_loc,index="all")
                with allure.step("遍历大附件"):
                    for big in bigAttach:
                        if big not in allBigAttachNames:
                            self.screenshotImg(key="大附件上传之后没有7天标识")
                            raise Exception("该大附件：{}，上传之后没有7天标识".format(big))

    #插入产品
    def insert_product(self):
        with allure.step("插入产品"):
            with allure.step("点击产品按钮"):
                self.find_element(self.writeMailPage_insertProductBtn_loc).click()
            allProductImgs = []
            allProductCodes = []
            with allure.step("点击产品选择框,并获取产品图片和编码"):
                for i in range(randint(1,3)):
                    productImgEle = self.find_element(self.writeMailPage_productSelectImg_loc,index=i)
                    productImg = productImgEle.value_of_css_property("background-image").split("?")[0].split("/")[-1]
                    allProductImgs.append(productImg)
                    allProductCodes.append(self.get_elementText(self.writeMailPage_productSelectCode_loc,index=i))
                    self.mouseHover((By.XPATH,self.writeMailPage_productSelectList_loc[1].replace("1",str(i+1))))
                    time.sleep(0.2)
                    self.find_element(self.writeMailPage_productCheckbox_loc).click()
            with allure.step("点击插入按钮"):
                self.find_element(self.writeMailPage_sureInsertProductBtn_loc).click()
            with allure.step("获取toast提示，并断言"):
                toast_text = self.find_element(self.toast_loc).text
                if toast_text != "插入成功":
                    raise Exception("插入产品后，提示语：{}不对".format(toast_text))
            allProductCodes_edit = []
            allProductImgs_edit = []
            with allure.step("判断插入编辑器的产品，图片，编码是否正确"):
                try:
                    with allure.step("切换到编辑器frame"):
                        self.switch_frame(self.emailEditFrame_loc)
                    with allure.step("获取所有的产品图片"):
                        productImgEles_edit = self.find_element(self.writeMailPage_edit_productImg_loc,index="all")
                        for productImgEle_edit in productImgEles_edit:
                            productImg_edit = productImgEle_edit.get_attribute("src").split("?")[0].split("/")[-1]
                            allProductImgs_edit.append(productImg_edit)
                    with allure.step("获取所有的产品编码"):
                        allProductCodes_edit = self.get_elementText(self.writeMailPage_edit_productCode_loc,index="all")
                except Exception as e:
                    print(e)
                finally:
                    self.switch_parentFrame()
            with allure.step("断言插入前后的产品编码是否一致"):
                if sorted(allProductCodes_edit) != sorted(allProductCodes):
                    raise Exception("插入前的产品编码：{}，与插入后的产品编码：{}，不一致".format(allProductCodes,allProductCodes_edit))
            with allure.step("断言插入前后的产品图片是否一致"):
                if sorted(allProductImgs) != sorted(allProductImgs_edit):
                    raise Exception("插入前的产品图片：{}，与插入后的产品图片：{}，不一致".format(allProductImgs,allProductImgs_edit))
            return allProductImgs,allProductCodes

    #插入报价
    def insert_quote(self):
        with allure.step("插入报价"):
            with allure.step("点击插入报价按钮"):
                self.find_element(self.writeMailPage_insertQuoteBtn_loc).click()
            allQuoteNames = []
            allQuoteNames_inserted = []
            with allure.step("选中报价单，并获取报价单编码"):
                for i in range(randint(1,3)):
                    allQuoteNames.append(self.get_elementText(self.writeMailPage_quoteCode_loc,index=i))
                    self.find_element(self.writeMailPage_quoteCode_loc,index=i).click()
            with allure.step("点击插入PDF按钮"):
                self.find_element(self.writeMailPage_insertPDFQuoteBtn_loc).click()
            with allure.step("判断是否有确定按钮，有的话就点击"):
                time.sleep(1)
                if self.is_element_exist(self.writeMailPage_sureInsertQuoteOrderBtn_loc[1]):
                    self.find_element(self.writeMailPage_sureInsertQuoteOrderBtn_loc).click()
            with allure.step("获取插入之后的报价单编码"):
                num = 1
                while num < 7:
                    orderSelectdialogEle = self.find_element_byPresence(self.writeMailPage_orderSelectdialog_loc)
                    orderSelectdialogEleAttr = orderSelectdialogEle.get_attribute("style")
                    print("num:{},orderSelectdialogEleAttr:{}".format(num,orderSelectdialogEleAttr))
                    if "display" in orderSelectdialogEleAttr:
                        break
                    else:
                        num = num + 1
                        time.sleep(3)
                    if num == 7:
                        raise Exception("已经过了18s，仍然在插入报价")
                allQuoteNames_inserted = self.get_elementText(self.writeMailPage_quoteAttachName_loc,index="all")
            with allure.step("判断插入的报价单是否正确"):
                allQuoteNames_inserted_tmp = []
                for quoteName_inserted in allQuoteNames_inserted:
                    allQuoteNames_inserted_tmp.append(quoteName_inserted.split("_")[-1].split(".")[0])
                for quoteName in allQuoteNames:
                    if quoteName not in allQuoteNames_inserted_tmp:
                        raise Exception("插入前的报价单编码：{}，不在插入后的报价单编码中：{}，插入前的报价编码：{}，插入后的编码截取结果：{}".format(quoteName,allQuoteNames_inserted,allQuoteNames,allQuoteNames_inserted_tmp))
            with allure.step("删除带入的收件人"):
                self.find_element(self.writeMailPage_delRecipientBtn_loc).click()
            return allQuoteNames_inserted

    #插入订单
    def insert_order(self):
        with allure.step("插入订单"):
            with allure.step("点击插入订单按钮"):
                self.find_element(self.writeMailPage_insertOrderBtn_loc).click()
            allOrderNames = []
            allOrderNames_inserted = []
            with allure.step("选中报价单，并获取报价单编码"):
                for i in range(randint(1,3)):
                    allOrderNames.append(self.get_elementText(self.writeMailPage_orderCode_loc,index=i))
                    self.find_element(self.writeMailPage_orderCode_loc,index=i).click()
            with allure.step("点击插入EXCEL按钮"):
                self.find_element(self.writeMailPage_insertEXCELOrderBtn_loc).click()
            with allure.step("判断是否有确定按钮，有的话就点击"):
                time.sleep(1)
                if self.is_element_click(self.writeMailPage_sureInsertQuoteOrderBtn_loc):
                    self.find_element(self.writeMailPage_sureInsertQuoteOrderBtn_loc).click()
            with allure.step("获取插入之后的订单编码"):
                num = 1
                while num < 7:
                    if "display" in self.find_element_byPresence(self.writeMailPage_orderSelectdialog_loc).get_attribute("style"):
                        break
                    else:
                        num = num + 1
                        time.sleep(3)
                if num == 7:
                    raise Exception("已经过了18s，仍然在插入订单")
                allOrderNames_inserted = self.get_elementText(self.writeMailPage_orderAttachName_loc,index="all")
            with allure.step("判断插入的订单是否正确"):
                allOrderNames_inserted_tmp = []
                for quoteName_inserted in allOrderNames_inserted:
                    allOrderNames_inserted_tmp.append(quoteName_inserted.split("_")[-1].split(".")[0])
                for orderName in allOrderNames:
                    if orderName not in allOrderNames_inserted_tmp:
                        raise Exception("插入前的报价单编码：{}，不在插入后的报价单编码中：{}，插入前的订单编码：{}，插入后的订单编码截取结果：{}".format(orderName,allOrderNames_inserted,allOrderNames,allOrderNames_inserted_tmp))
            with allure.step("删除带入的收件人"):
                self.find_element(self.writeMailPage_delRecipientBtn_loc).click()
            return allOrderNames_inserted

    #插入营销网站
    def insert_site(self):
        with allure.step("插入营销网站"):
            with allure.step("点击插入营销网站按钮"):
                self.find_element(self.writeMailPage_insertSiteBtn_loc).click()
            time.sleep(1)
            with allure.step("选中营销网站"):
                site_num = randint(1,3)
                for i in range(site_num):
                    self.mouseHover((By.XPATH,self.writeMailPage_productSelectList_loc[1].replace("1",str(i+1))))
                    self.find_element(self.writeMailPage_productCheckbox_loc).click()
            with allure.step("点击插入快照按钮"):
                self.find_element(self.writeMailPage_insertSiteSnapshotBtn_loc).click()
            with allure.step("判断营销网站对话框是否在18s内消失"):
                num = 1
                while num < 7:
                    if "display" in self.find_element_byPresence(self.writeMailPage_siteSelectdialog_loc).get_attribute("style"):
                        break
                    else:
                        num = num + 1
                        time.sleep(3)
                if num == 7:
                    self.screenshotImg(key="插入营销网站快照中...")
                    raise Exception("已经过了18s，仍然在插入营销网站快照")
            with allure.step("获取编辑器内的营销网站地址"):
                allSiteUrls = []
                try:
                    self.switch_frame(self.emailEditFrame_loc)
                    allSiteEles = self.find_element(self.writeMailPage_siteSnapshot_edit_loc,index="all")
                    for siteEle in allSiteEles:
                        allSiteUrls.append(siteEle.get_attribute("href"))
                except Exception as e:
                    print(e)
                finally:
                    self.switch_parentFrame()
            with allure.step("判断插入的快照个数是否正确"):
                if len(allSiteUrls) != 1:
                    raise Exception("实际插入到编辑器的网站个数：{}，不是1个".format(site_num,len(allSiteUrls)))
            with allure.step("判断插入的网站地址是否正确"):
                for siteUrl in allSiteUrls:
                    if "joinf.com" not in siteUrl:
                        raise Exception("插入的营销网站快照地址：{}，不正确".format(siteUrl))
            return allSiteUrls


    #插入云文件
    def insert_dishFile(self):
        with allure.step("插入云文件"):
            with allure.step("点击插入云文件按钮"):
                self.find_element(self.writeMailPage_insertDishFileBtn_loc).click()
            with allure.step("选中云文件，并获取云文件名"):
                dishFile_num = randint(1,5)
                allDishFileNames = []
                for i in range(dishFile_num):
                    self.mouseHover((By.XPATH,self.writeMailPage_dishFileList_loc[1].replace("1",str(i+1))))
                    allDishFileNames.append(self.get_elementText(self.writeMailPage_dishFileName_loc,index=i))
                    self.find_element(self.writeMailPage_dishFileCheckBox_loc).click()
            with allure.step("点击插入按钮"):
                self.find_element(self.writeMailPage_sureInsertDishFileBtn_loc).click()
            time.sleep(1)
            with allure.step("获取插入后的云文件名"):
                allDishFileNames_inserted = self.get_elementText(self.writeMailPage_attachName_loc,index="all")
            with allure.step("判断插入前后的云文件是否一致"):
                for dishFile in allDishFileNames:
                    if dishFile not in allDishFileNames_inserted:
                        raise Exception("插入前的云文件：{}，不在插入后的文件中：{}，插入前的所有云文件：{}".format(dishFile,allDishFileNames_inserted,allDishFileNames))
            return allDishFileNames


    #插入模板
    def insert_template(self):
        with allure.step("插入模板"):
            with allure.step("点击邮件模板按钮"):
                self.find_element(self.writeMailPage_insertMailTemplateBtn_loc).click()
            time.sleep(5)
            with allure.step("点击系统按钮"):
                self.find_element(self.writeMailPage_systemMailTemplateBtn_loc).click()
            time.sleep(10)
            with allure.step("随机选中一个模板"):
                # self.find_element(self.writeMailPage_systemMailTemplateList_loc,index=randint(0,9)).click()
                self.click_ele(self.writeMailPage_systemMailTemplateList_loc,index=randint(0,9),key="插入系统模板")
            with allure.step("点击追加到指定位置"):
                self.find_element(self.writeMailPage_insertMailTemplateToLocationBtn_loc).click()

    #输入邮件文本
    def send_emailContent(self):
        with allure.step("输入随机文本"):
            emain_text = random_text().replace("\n","")
            try:
                self.switch_frame(self.emailEditFrame_loc)
                self.find_element((By.XPATH,'/html/body')).send_keys(emain_text)
            except Exception as e:
                print(e)
            finally:
                self.switch_parentFrame()
            return emain_text

    #插入图片
    def insert_img(self,file):
        with allure.step("点击插入图片按钮"):
            self.click_ele(self.writeMailPage_insertImgBtn_loc,key="点击插入图片按钮")
        time.sleep(2)
        with allure.step("选择图片，并上传"):
            file_path = os.path.join(ATTACH_PATH,file)
            self.upload_file(filePath=file_path)
            self.screenshotImg(key="上传一张图片")


    #选择发件人
    def select_sender(self,sender="fttxtest@126.com"):
        with allure.step("选择发件人"):
            with allure.step("点击发件人选择框"):
                self.find_element(self.writeMailPage_senderInput_loc).click()
            time.sleep(0.5)
            with allure.step("选择:{},作为发件人".format(sender)):
                sender_loc = (By.XPATH,self.writeMailPage_sender_loc[1].replace("126",sender))
                self.click_ele(sender_loc)

    #接收邮件并点击
    def click_emailBySubject(self,subject):
        time.sleep(3)
        num = 0
        while num < 20:
            with allure.step("获取所有的邮件主题"):
                allEmailSubjects = self.get_elementText(self.recipientBoxPage_subject_loc, index="all")
            with allure.step("遍历主题，查看是否包含要找的主题"):
                if subject in allEmailSubjects:
                    subject_loc = (By.XPATH,'//div[@class="sub_item"]//span[text()="{}"]'.format(subject))
                    self.scroll_element(subject_loc)
                    time.sleep(0.3)
                    self.mouseClick(subject_loc)
                    time.sleep(3)
                    break
                else:
                    time.sleep(30)
                    num = num + 1
                    with allure.step("点击收件箱，再次收取"):
                        self.find_element(self.recipientBoxPage_recipientBoxBtn_loc).click()
                        time.sleep(3)


    #获取主题输入框内的主题
    def get_emailSubjectInSubjectInput(self):
        return self.find_element(self.writeMailPage_emailSubjectInput_loc,key="写信页面主题输入框").get_attribute("value")

    #获取写信页面所有的附件
    def get_allAttachNamesOfWriteEmailPage(self):
        return self.get_elementText(self.writeMailPage_attachName_loc,index="all")

    #获取写信页面的收件人
    def get_recipientsOfWriteEmailPage(self):
        return self.get_elementText(self.writeMailPage_recipientList_loc,index="all",key="获取所有的收件人")

    #获取写信页面的发件人
    def get_sendersOfWriteEmailPage(self):
        return self.find_element(self.writeMailPage_senderInput_loc,key="获取发件人").get_attribute("value")

    #获取写信页面的邮件文本
    def get_emailBodyOfWriteEmailPage(self):
        try:
            self.switch_frame(self.emailEditFrame_loc)
            return self.get_elementText(self.writeMailPage_emailBody_loc,index="all",key="获取邮件文本")
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    #获取写信页面的产品图片地址，产品编码
    def get_productInfoOfWriteEmailPage(self):
        try:
            with allure.step("切换到编辑器frame"):
                self.switch_frame(self.emailEditFrame_loc)
            with allure.step("获取所有的产品图片"):
                productImgEles_edit = self.find_element(self.writeMailPage_edit_productImg_loc, index="all")
                allProductImgs_edit = []
                for productImgEle_edit in productImgEles_edit:
                    productImg_edit = productImgEle_edit.get_attribute("src").split("?")[0].split("/")[-1]
                    allProductImgs_edit.append(productImg_edit)
            with allure.step("获取所有的产品编码"):
                allProductCodes_edit = self.get_elementText(self.writeMailPage_edit_productCode_loc, index="all")
            return allProductImgs_edit,allProductCodes_edit
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()


    #获取写=写信页面的营销网站快照地址
    def get_sitesOfWriteEmailPage(self):
        allSiteUrls = []
        try:
            self.switch_frame(self.emailEditFrame_loc)
            allSiteEles = self.find_element(self.writeMailPage_siteSnapshot_edit_loc, index="all")
            for siteEle in allSiteEles:
                allSiteUrls.append(siteEle.get_attribute("href"))
            return allSiteUrls
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()


    # 获取邮件详情里面的大附件名
    def get_allBigAttachNamesOfWriteEmailPage(self):
        try:
            self.switch_frame(self.emailEditFrame_loc)
            bigAttachNames = []
            bigAttachNames_tmp = self.get_elementText(self.emailDetailPage_bigAttachName_loc, index="all")
            for name in bigAttachNames_tmp:
                bigAttachNames.append(name.split(" ")[-1])
            return bigAttachNames
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()


    #获取邮件详情里面的收件人
    def get_recipientOfEmailDetail(self):
        return self.get_elementText(self.emailDetailPage_recipient_loc,index="all",key="获取邮件详情收件人")

    #获取邮件详情里面的发件人
    def get_senderOfEmailDetail(self):
        return self.get_elementText(self.emailDetailPage_sender_loc)

    #获取邮件详情里面的所有小附件
    def get_allSmallAttachNamesOfEmailDetail(self):
        return self.get_elementText(self.emailDetailPage_attachName_loc,index="all")

    #获取邮件详情里面的产品图片地址
    def get_allProductImgUrlsOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            allProductImgEles = self.find_element(self.emailDetailPage_productImg_loc,index="all")
            allProductImgurls = []
            for productImgEle in allProductImgEles:
                allProductImgurls.append(productImgEle.get_attribute("src").split("?")[0].split("/")[-1])
            allProductImgCodes = self.get_elementText(self.emailDetailPage_productCode_loc,index="all")
            return allProductImgurls,allProductImgCodes
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    #获取邮件详情里面的快照地址
    def get_allSiteUrlsOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            allSiteImgEles = self.find_element(self.emailDetailPage_siteImg_loc,index="all")
            allSiteImgurls = []
            for siteImgEle in allSiteImgEles:
                allSiteImgurls.append(siteImgEle.get_attribute("href"))
            return allSiteImgurls
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    #获取邮件详情里面的邮件文本
    def get_emailTextOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            return self.get_elementText(self.emailDetailPage_emailContent_loc)
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    #获取邮件详情里面的大附件名
    def get_allBigAttachNamesOfEmailDetail(self):
        try:
            self.switch_frame(self.emailBodyFrame_loc)
            bigAttachNames = []
            bigAttachNames_tmp = self.get_elementText(self.emailDetailPage_bigAttachName_loc,index="all")
            for name in bigAttachNames_tmp:
                bigAttachNames.append(name.split("(")[0])
            return bigAttachNames
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()

    #点击回复带附件按钮
    def click_replyContainsAttach(self):
        with allure.step("点击回复下拉按钮"):
            self.find_element(self.emailDetailPage_replyDropDownBtn_loc).click()
        time.sleep(0.5)
        with allure.step("点击回复带附件按钮"):
            self.find_element(self.emailDetailPage_replyContainAttachBtn_loc).click()

    #插入标签
    def insert_mark(self):
        with allure.step("点击标签按钮"):
            self.click_ele(self.writeMailPage_markBtn_loc)
        time.sleep(0.3)
        with allure.step("点击第一个标签列表"):
            firstMarkListEle = self.find_element(self.writeMailPage_markList_loc)
            firstMarkListText = firstMarkListEle.text
            firstMarkListEle.click()
        with allure.step("点击确定按钮"):
            self.click_ele(self.writeMailPage_sureInsertMarkBtn_loc)
        time.sleep(0.3)
        with allure.step("获取插入的标签文本"):
            inserted_markText = self.get_elementText(self.writeMailPage_insertedMarkList_loc)
        with allure.step("判断插入前后的标签文本是否一致"):
            if inserted_markText != firstMarkListText:
                raise Exception("插入后的标签文本：{}，与插入前的标签文本：{}，不一致".format(inserted_markText,firstMarkListText))
            return firstMarkListText

    #获取草稿箱中，指定的主题邮件，并点击
    def click_draftBoxEmailBySubject(self,subject):
        time.sleep(2)
        with allure.step("获取所有的邮件主题"):
            allEmailSubjects = self.get_elementText(self.recipientBoxPage_subject_loc, index="all")
            print(allEmailSubjects)
        with allure.step("遍历主题，查看是否包含要找的主题"):
            if subject in allEmailSubjects:
                subject_loc = (By.XPATH,'//div[@class="sub_item"]//span[text()="{}"]'.format(subject))
                self.scroll_element(subject_loc)
                time.sleep(0.3)
                self.mouseClick(subject_loc)
                time.sleep(3)
            else:
                raise Exception("草稿箱中没有主题是：{}的草稿".format(subject))


    #选择内部转发人
    def selectInnerToForward(self,inner,forwardIdea):
        with allure.step("点击内部转发按钮"):
            self.click_ele(self.writeMailPage_innerForwardBtn_loc)
        with allure.step("选择内部联系人-{}".format(inner)):
            allInnerEles = self.find_element(self.writeMailPage_innerForwardPage_innerList_loc,index="all")
            for innerEle in allInnerEles:
                if inner in innerEle.text:
                    innerEle.click()
                    break
        with allure.step("输入转发意见"):
            self.sendKeys(self.writeMailPage_innerForwardPage_forwardIdeaInput_loc,key=forwardIdea)
        with allure.step("点击确定按钮"):
            self.click_ele(self.writeMailPage_innerForwardPage_sureForwadrBtn_loc)


    #插入宏
    def insert_macro(self):
        with allure.step("点击插入宏按钮"):
            self.click_ele(self.writeMailPage_insertMacroBtn_loc)
        with allure.step("全部插入宏列表"):
            time.sleep(1)
            macroLists = self.find_element(self.writeMailPage_macroList_loc,index="all")
            for macroList in macroLists:
                macroList.click()
        with allure.step("点击确定按钮"):
            self.click_ele(self.writeMailPage_sureInsertMacroBtn_loc)

    #发送一封普通邮件
    def send_generalEmail(self,has_recipient=1,recipient=None,subject=None,sender=None):
        if has_recipient:
            with allure.step("输入收件人"):
                if recipient:
                    _recipient = recipient
                else:
                    _recipient = ["hiitboy@aliyun.com"]
                if len(_recipient) > 1:
                    for r in _recipient:
                        self.sendKeys(self.writeMailPage_recipientInput_loc,key=r)
                        self.click_ele(self.writeMailPage_writeMailTabBtn_loc)
                        time.sleep(1)
                else:
                    self.sendKeys(self.writeMailPage_recipientInput_loc,key=_recipient[0])
        with allure.step("输入邮件主题"):
            if subject:
                _subject = subject
            else:
                _subject = random_name() + "--普通发送测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.sendKeys(self.writeMailPage_emailSubjectInput_loc,key=_subject)
        with allure.step("输入邮件文本"):
            self.send_emailContent()
        if sender:
            with allure.step("选择发件人"):
                self.select_sender(sender=sender)
        with allure.step("点击发送按钮"):
            self.click_ele(self.writeMailPage_sendEmailBtn_loc)

    #获取草稿详情中的定时文本时间
    def get_settedTime_writeMailPage(self):
        return self.get_elementText(self.writeMailPage_settedTime_loc)

    #获取写邮件，文本内容的css属性
    def get_writeMail_css(self):
        with allure.step("获取邮件文本元素"):
            try:
                self.switch_frame(self.emailEditFrame_loc)
                emailBodyEle = self.find_element(self.writeMailPage_emailContent_loc,index=-1)
                writeMailPage_emailBody_font = emailBodyEle.value_of_css_property("font-family")
                writeMailPage_emailBody_fontSize = emailBodyEle.value_of_css_property("font-size")
                writeMailPage_emailBody_fontColor = emailBodyEle.value_of_css_property("color")
                return writeMailPage_emailBody_font,writeMailPage_emailBody_fontSize,writeMailPage_emailBody_fontColor
            except Exception as e:
                print(e)
            finally:
                self.switch_parentFrame()


    #获取抄送，密送人
    def get_writeMail_ccAndBc(self):
        with allure.step("点击抄送按钮"):
            self.click_ele(self.writeMailPage_ccSendEmailBtn_loc)
        with allure.step("点击密送按钮"):
            self.click_ele(self.writeMailPage_bcSendEmailBtn_loc)
        with allure.step("获取抄送密送人"):
            if self.is_element_exist(self.writeMailPage_cc_loc[1]):
                cc = self.get_elementText(self.writeMailPage_cc_loc,index="all")
            else:
                cc = []
            if self.is_element_exist(self.writeMailPage_bc_loc[1]):
                bc = self.get_elementText(self.writeMailPage_bc_loc,index="all")
            else:
                bc = []
            return cc,bc


    #商机业务发送邮件
    def sendEmail_businessPage(self,subject,):
        try:
            with allure.step("点击商机模块"):
                self.switch_mainPage()
                self.click_ele(self.sidebar_businessBtn_loc,key="点击侧边栏商机按钮")
                self.switch_frame(self.mainFrame_loc)
                time.sleep(5)
            with allure.step("点击发送邮件按钮"):
                self.click_ele(self.businessPage_sendEmailBtn_loc,key="点击商机页面发送邮件按钮")
            with allure.step("开始发送邮件"):
                self.send_generalEmail(subject=subject,has_recipient=0)
            time.sleep(3)
        except Exception as e:
            logger.info("从商机模块发送邮件发生了报错：{}".format(e))
        finally:
            with allure.step("切换到邮件模块"):
                self.switch_mainPage()
                self.click_ele(self.sidebar_emailBtn_loc,key="点击侧边栏邮件按钮")
                time.sleep(2)
                self.switch_frame(self.mainFrame_loc)
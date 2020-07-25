# -*- encoding: utf-8 -*-
'''
@File    :   conftest.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/31 0031 14:33   dmk      1.0         None
'''

import pytest,os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pageObject.basePage import Action
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon

@pytest.fixture(scope="function",autouse=True)
def auto_switchOperator(login):
    driver = login
    Action(driver).switch_operator()


@pytest.fixture(scope="function",autouse=True)
def auto_refreshBro(login):
    driver = login
    yield
    mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")
    driver.refresh()
    # 判断是否有弹窗
    time.sleep(1)
    alert = EC.alert_is_present()(driver)
    if alert:
        alert.accept()
    time.sleep(3)
    EC.frame_to_be_available_and_switch_to_it(mainFrame_loc)(driver)

# @pytest.fixture(scope="function",autouse=False)
# def auto_refreshBro1(login001):
#     driver1 = login001
#     yield
#     mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")
#     driver1.refresh()
#     # 判断是否有弹窗
#     time.sleep(1)
#     alert = EC.alert_is_present()(driver1)
#     if alert:
#         alert.accept()
#     time.sleep(3)
#     EC.frame_to_be_available_and_switch_to_it(mainFrame_loc)(driver1)


@pytest.fixture(scope="session",autouse=True)
def switchTo200(login):
    driver = login
    recipientBoxPageCommon(driver).switchPageTo200()


# @pytest.fixture(scope="session",autouse=False)
# def switchTo2001(login001):
#     driver1 = login001
#     recipientBoxPageCommon(driver1).switchPageTo200()
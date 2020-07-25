# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageHolidayReplyPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/27 0027 20:52   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class mailSettingPageHolidayReplyPageLoc:

    #节假回复按钮
    mailSettingPageHolidayReplyPage_holidayReplyBtn_loc = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="节假回复"]')
    #回复设置选择框
    mailSettingPageHolidayReplyPage_replySettingCheckbox_loc = (By.XPATH,'//main[@class="el-main"]/label')
    #开始日期选择框
    mailSettingPageHolidayReplyPage_startDateInput_loc = (By.XPATH,'//main[@class="el-main"]//input[@placeholder="开始日期"]')
    #结束日期选择框
    mailSettingPageHolidayReplyPage_endDateInput_loc = (By.XPATH,'//main[@class="el-main"]//input[@placeholder="结束日期"]')
    #当前日期
    mailSettingPageHolidayReplyPage_currentDate_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//td[contains(@class,"available today")]')
    #某一天日期
    mailSettingPageHolidayReplyPage_someDay_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//table[@class="el-date-table"]//span[contains(text(),20)]')
    #当天时间的后一天
    mailSettingPageHolidayReplyPage_currentTodayAfterDay_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//td[contains(@class,"available today")]/following-sibling::td[1]')
    #当天时间的前一天
    mailSettingPageHolidayReplyPage_currentTodayBeforeDay_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//td[contains(@class,"available today")]/preceding-sibling::td[1]')
    #保存按钮
    mailSettingPageHolidayReplyPage_saveBtn_loc = (By.XPATH,'//button[@class="el-button set-save-btn f12 el-button--primary"]')
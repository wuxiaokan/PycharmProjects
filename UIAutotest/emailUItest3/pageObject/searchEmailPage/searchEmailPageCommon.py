# -*- encoding: utf-8 -*-
'''
@File    :   searchEmailPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/1 0001 14:51   dmk      1.0         None
'''

import allure,pytest
from pageObject.basePage import Action
from pageObject.searchEmailPage.searchEmailPage_loc import searchEmailPageLoc

class searchEmailPageCommon(Action,searchEmailPageLoc):
    pass
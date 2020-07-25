#coding: utf-8
import os
from utils.mail import Email

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.getcwd()),"/report/report.html")

    e = Email(title='API自动化测试报告',
              message='这是今天的tms重构ui自动化测试报告，请查收！',
              receiver='fttxtest@126.com',
              server='smtp.163.com',
              sender='fttxtest@163.com',
              password='fttxtest321',
              path=path
              )
    e.send()
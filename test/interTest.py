__author__ = 'WIN7'

# coding:utf8

# import requests
# import json
# ref=requests.post('https://datacn.joinf.com:8080/favorite/addGroupInfo',
#               data={'groupName': "哈哈哈yyy", 'parentId': -1, 'loginUserId': "134114"})
# print(ref.json())
# print(ref.status_code)

# import MySQLdb
#
# conn = MySQLdb.connect(
#   host='118.31.184.136',
#   user='root',
#   passwd='Fttx2018',
#   db='joinf_business_data',
#   charset='utf8'
# )

# 创建游标
# c = conn.cursor()
#
# c.execute('select * from bs_label')
#
# row = c.fetchone()
#
# print(row)

import requests

url = 'https://ceshilogin.joinf.com/login?service=https%3A%2F%2Fceshi.joinf.com%2Frapi%2F%3Fredirect_uri=https%253A%252F%252Fceshi.joinf.com%252Femail%252FmanageEmail'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}

date = {
  'username': 7777,
  'password': 123456
}

s = requests.session()

test1 = s.post(url=url, json=date, headers=headers)
print(test1.status_code)

url1 = 'https://datacn.joinf.com:8080/bs/selectAggregation'
date1 = {
  "countries": ["UNITED STATES"],
  "0": "UNITED STATES",
  "emailFlag": "-1",
  "industries": [],
  "industriesSession": [],
  "keywords": "led",
  "loginUserId": "290782",
  "pageNum": 1,
  "pageSize": 20,
  "searchType": "0",
  "urlFlag": "-1"
}

test2 = s.post(url=url1, json=date1, headers=headers)

print(test2.json())

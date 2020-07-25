
#coding:utf-8

# name = '张三'
# age='10'
# info='名字叫'+name+'年龄为'+age
# print(info)
#换行
#print('hhh'+'\n'+str(111))
# a=3
# b=4
# print(a>b)
#list列表
# classmates=['小黑','小王','小刘','小企鹅']
# print str(classmates).decode('string_escape')
# print('安安')
# classmates.insert(0,'阿萨德')
# print(len(classmates))


import random
a=random.sample(range(1,100),20)
print(a)
i=0
sum=0
l= []
while i<20:
    if(a[i]%2==0):
        sum=sum+a[i]#偶数相加
    else:
        l.append(a[i])#把奇数放入list
    i=i+1
print(sum,l)










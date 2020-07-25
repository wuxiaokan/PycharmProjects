__author__ = 'WIN7'
#coding:utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.taobao.com")
time.sleep(3)
#截屏  路径+文件名+格式
driver.get_screenshot_as_file("C:\\Users\\WIN7\\Desktop\\a.png")
driver.quit()

# class Person:
#     def __init__(self,age):
#         self.age=age
#     def run(self):
#         print('run run run')
#
#
# class Student(Person):
#     def __init__(self,age,score):
#       Person.__init__(self,age)
#       self.score=score
#     def say(self):
#         print("%s,%s"%(self.age,self.score))
#         Person.run(self)
#
# class Person:
#     @staticmethod
#     def run(age):
#         print('年龄：',age)
#
# class Student(Person):
#     @staticmethod
#     def say(score):
#         Person.run(22)
#         print(score)
#
# S=Student()
# S.say(60)
#
# A=Person(20)
# A.run()
# B=Student(100,1)
# B.say()
#
# class Father(object):
#     def __init__(self, name):
#         self.name=name
#       #  print ( "name: %s" %( self.name) )
#     def getName(self):
#         return 'Father ' + self.name
#
# class Son(Father):
#     def getName(self):
#         return 'Son '+self.name
#
#
# son=Son('runoob')
# print ( son.getName() )
#
#
# class Person:
#     @staticmethod
#     def run(age):
#         print("年龄:", age)
#
#
# class Student(Person):
#     @staticmethod
#     def say(score):
#         Person.run(15)
#         print("成绩：", score)
#
#
# Student.say(95)
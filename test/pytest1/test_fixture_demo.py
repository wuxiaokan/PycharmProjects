
#coding:utf-8
#
# import pytest
#
# # 不带参数时默认scope="function"
# @pytest.fixture()
# def login():
#     print("输入账号，密码先登录")
#
# def test_s1(login):
#     print("用例1：登录之后其它动作111")
#
# def test_s2():  # 不传login
#     print("用例2：不需要登录，操作222")
#
# def test_s3(login):
#     print("用例3：登录之后其它动作333")
#
# if __name__ == "__main__":
#     pytest.main(["-s", "test_fixture_demo.py"])
#
# 新建一个文件test_f1.py

import pytest
# '''
# ** 作者：上海-悠悠 QQ交流群：588402570**
# '''
#
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_fixture_demo.py"])


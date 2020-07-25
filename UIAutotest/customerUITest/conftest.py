#coding: utf-8
import sys
import os
rootPath = os.path.dirname(os.getcwd())
# rootPath = os.path.split(curPath)[0]
# print(curPath,rootPath)
sys.path.append(rootPath)


import pytest,allure
import os, sys
from selenium import webdriver
from utils.config import DRIVER_PATH
from utils.config import Config
from utils.common import *
from utils.mail import Email

mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")

_system = sys.platform

print("操作系统：{}".format(_system))
if "win" in _system:
    driver_path = os.path.join(DRIVER_PATH,"chromedriver.exe")
elif "linux" in _system:
    driver_path = "chromedriver"
else:
    raise Exception("操作系统：{}，不对".format(_system))

print(driver_path)

def signin(request,username,password,url):
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
    option.add_argument('lang=zh_CN')
    try:
        global driver
        driver = webdriver.Chrome(driver_path,chrome_options=option)
        driver.implicitly_wait(30)
        driver.get(url)
        driver.set_window_size(1920,1080)
        driver.maximize_window()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("loginID"))
        driver.find_element_by_id("loginID").send_keys(username)
        driver.find_element_by_id("loginPassword").send_keys(password)
        driver.find_element_by_id("loginBtn").click()
        time.sleep(3)
        try:
            # 关掉活动模态框
            activitiesSeasonBtnOneElement = getElementById(driver, "activitiesSeasonBtnOne")
            clickElement(activitiesSeasonBtnOneElement)
            time.sleep(1)
            activitiesSeasonBtnTwoElement = getElementById(driver, "activitiesSeasonBtnTwo")
            clickElement(activitiesSeasonBtnTwoElement)
        except Exception as e:
            print("没有查找到活动模态框元素：{}".format(e))
        time.sleep(1)
        EC.frame_to_be_available_and_switch_to_it(mainFrame_loc)(driver)
        def quitbro():
            print("关闭浏览器")
            #driver.quit()
        request.addfinalizer(quitbro)
        print("driver:{}".format(driver))
        return driver
    except Exception as e:
        print("发生错误：{}".format(e))
        print("-----------")




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    out = yield
    rep = out.get_result()
    #we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope="session")
def login(request,geturl):
    username = "dmktest"
    password = "123456"
    return signin(request,username,password,geturl)


@pytest.fixture(scope="function",autouse=True)
def auto_refreshBro(login):
    driver = login
    yield
    driver.refresh()
    # 判断是否有弹窗
    time.sleep(1)
    alert = EC.alert_is_present()(driver)
    if alert:
        alert.accept()
    time.sleep(3)
    EC.frame_to_be_available_and_switch_to_it(mainFrame_loc)(driver)


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="pro", help="my option: type1 or type2"
    )

@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture(scope="session")
def geturl(cmdopt):
    if cmdopt == "ali_dev":
        test_url = Config().get("ali_dev_url")
        return test_url
    elif cmdopt == "hw_dev":
        test_url = Config().get("hw_dev_url")
        return test_url
    elif cmdopt == "pro":
        test_url = Config().get("pro_url")
        return test_url
    else:
        print("你输入的命令行参数是：{}，请输入dev或者pro".format(cmdopt))
        raise ValueError("请输入有效的命令行参数")


@pytest.fixture(scope="session",autouse=True)
def foo():
    print("用例开始执行")
    logger.info("用例开始执行```````````````````````````")

    yield

    print("yield············用例全部执行完毕")
    logger.info("yield·······用例全部执行完毕```````````````````````````")
    # send_report()
    logger.info("-----测试报告已发送-------")

#发送邮件
def send_report():
    path = os.path.join(os.path.dirname(os.getcwd()),"report","report.html")

    e = Email(title='API自动化测试报告',
              message='这是今天的tms重构UI自动化测试报告，请查收！',
              receiver='fttxtest@126.com',
              server='smtp.163.com',
              sender='fttxtest@163.com',
              password='fttxtest321',
              path=path
              )
    e.send()
#coding: utf-8
import sys
import os

from selenium.webdriver.chrome.options import Options

rootPath = os.path.dirname(os.getcwd())
# rootPath = os.path.split(curPath)[0]
# print(curPath,rootPath)
sys.path.append(rootPath)


import pytest,allure,traceback
import os, time
from selenium import webdriver
from utils.config import DRIVER_PATH
from utils.config import IMAGE_PATH
from utils.config import Config
from utils.common import *
from utils.mail import Email
from selenium.webdriver.common.action_chains import ActionChains




@pytest.fixture(scope="session")
def login(request):
    username = "dmktest"
    password = "123456"
    return signin(request,username,password)

@pytest.fixture(scope="session")
def login001(request):
    username = "ffy_001"
    password = "123456"
    return signin(request,username,password)

@pytest.fixture(scope="session")
def login005(request):
    username = "ffy_005"
    password = "123456"
    return signin(request,username,password)

@pytest.fixture(scope="session")
def login002(request):
    username = "ffy_002"
    password = "123456"
    return signin(request,username,password)

@pytest.fixture(scope="session")
def login003(request):
    username = "ffy_003"
    password = "123456"
    return signin(request,username,password)

@pytest.fixture(scope="session")
def login_pro(request):
    username = "fttx037"
    password = "test001"
    return signin(request,username,password)



# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#     hook pytest失败
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         # pic_info = adb_screen_shot()
#         with allure.step('添加失败截图...'):
#             allure.attach(driver.get_screenshot_as_png(), "失败截图,driver:{}".format(driver), allure.attachment_type.PNG)






def signin(request,username,password):
    if "ffy" in username or "test" in username:
        url = "https://ceshilogin.joinf.com/login?service=https%3A%2F%2Fceshi.joinf.com%2Femail%2Findex"
    else:
        url = "https://pre.joinf.com/login?service=https%3A%2F%2Fcrm.pre.joinf.com%2Femail%2Findex"
    # global driver
    driver_path = os.path.join(DRIVER_PATH, "chromedriver.exe")
    # 加启动配置
    logger.info("添加启动配置")
    chrome_option = Options()
    chrome_option.add_argument('disable-infobars')
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    chrome_option.add_argument('--lang=zh-CN')
    try:
        driver = webdriver.Chrome(driver_path,options=chrome_option)
        driver.implicitly_wait(20)
        driver.set_window_size(1920,1080)
        driver.maximize_window()
        driver.get(url)
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("loginID"))
        driver.find_element_by_id("loginID").send_keys(username)
        driver.find_element_by_id("loginPassword").send_keys(password)
        logger.info(driver.title)
        # loginBtnEle = driver.find_element_by_id("loginBtn")
        loginBtnEle = driver.find_element_by_xpath('//div[@class="login-buttons"]')
        # logger.info(loginBtnEle)
        # logger.info(loginBtnEle.get_attribute("class"))
        # logger.info(loginBtnEle.text)
        loginBtnEle.click()
        # ActionChains(driver).click(loginBtnEle).perform()
        time.sleep(1)
        logger.info("切换frame")
        driver.switch_to.frame("businessList")
        # try:
        #     # 关掉活动模态框
        #     activitiesSeasonBtnOneElement = getElementById(driver, "activitiesSeasonBtnOne")
        #     clickElement(activitiesSeasonBtnOneElement)
        #     time.sleep(1)
        #     activitiesSeasonBtnTwoElement = getElementById(driver, "activitiesSeasonBtnTwo")
        #     clickElement(activitiesSeasonBtnTwoElement)
        # except Exception as e:
        #     print("没有查找到活动模态框元素：{}".format(e))
        # WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('//*[@id="activitiesSeasonBtnOne"]')).click()
        def quitbro():
            print("关闭浏览器")
            driver.quit()
        request.addfinalizer(quitbro)
        return driver
    except Exception as e:
        print("发生错误：{}".format(e))
        logger.info("发生错误了：{}".format(e))
        logger.info("发生错误：{}".format(traceback.print_exc()))


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="dev", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture(scope="function",autouse=True)
def geturl(cmdopt):
    if cmdopt == "dev":
        test_url = Config().get("dev_url")
        return test_url
    elif cmdopt == "pro":
        test_url = Config().get("pro_url")
        return test_url
    else:
        print("你输入发命令行参数是：{}，请输入dev或者pro".format(cmdopt))
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
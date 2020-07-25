#coding:utf-8
import time,traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.config import IMAGE_PATH
from utils.log import logger


#通过xpath获取元素
def getElementByXpath(driver,loc):
    return WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(loc))

#通过css选择器获取元素
def queryCssSelector(driver,path):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_css_selector(path))

#通过class获取元素
def getElementsByClassName(driver,path,time=10):
    return WebDriverWait(driver,time).until(lambda x:x.find_elements_by_class_name(path))

#通过id获取元素
def getElementById(driver,path,index=0):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_id(path))[index]

#通过xpath获取元素
def getElementsByXpath(driver,path):
    try:
        return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_xpath(path))
    except Exception:
        traceback.print_exc()

#通过contains获取元素
def getElementByContains(driver,path,tag,attr="id"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[contains(@{},'{}')]".format(tag,attr,path)))

#通过contains文本获取元素
def getElementByContainsText(driver,key,tag="*"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[contains(text(),'{}')]".format(tag,key)))

#通过文本获取元素
def getElementByText(driver,key,path=None,tag=None):
    if path:
        elements = WebDriverWait(driver,10).until(lambda x:x.find_elements_by_class_name(path))
    else:
        elements = WebDriverWait(driver, 20).until(lambda x: x.find_elements_by_tag_name(tag))
    num = 0
    for element in elements:
        if element.text == key:
            num = 1
            return element

    if num == 0:
        print("未获取元素：{}--{}".format(tag,key))


#通过starts-with获取元素
def getElementByStartsWith(driver,path,tag,attr="id"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[starts-with(@{},'{}')]".format(tag,attr,path)))

#通过contains获取元素
def getElementByStartsEnd(driver,path,tag,attr="id"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[starts-end(@{},'{}')]".format(tag,attr,path)))

#点击元素
def clickElement(element):
    element.click()

#输入文本
def sendKeys(element,key,is_clear=1):
    if is_clear:
        element.clear()
    element.send_keys(key)

#鼠标悬停操作
def mouseHover(driver,element):
    ActionChains(driver).move_to_element(element).perform()

#鼠标点击操作
def mouseClick(driver,element):
    ActionChains(driver).click(element).perform()

#鼠标双击操作
def mouseDoubleClick(driver,element):
    ActionChains(driver).double_click(element).perform()

#鼠标拖动操作
def mouseDrag(driver,element,target):
    # ActionChains(driver).click_and_hold(element).drag_and_drop_by_offset(element,10,20).perform()
    # ActionChains(driver).click_and_hold(element).move_by_offset(x, y).release().perform()
    ActionChains(driver).drag_and_drop(element,target).perform()

#点击下拉菜单
def clickMenu(driver,path,key):
    path = eval(path)
    btn = getElementsByXpath(driver,path[0])
    clickElement(btn)
    #选中对应的菜单
    time.sleep(1)
    elements = WebDriverWait(driver,10).until(lambda x:x.find_elements_by_class_name(path[1]))
    num = 0
    for element in elements:
        if element.text == key:
            num = num + 1
            print(element.text)
            element.click()
            break
    if num == 0:
        raise Exception("key：{}未找到".format(key))


#截图
def screenshotImg(driver,key=None):
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    logger.info("保存的图片：{}/{}-{}.png".format(IMAGE_PATH,nowTime,key))
    driver.get_screenshot_as_file("{}/{}-{}.png".format(IMAGE_PATH,nowTime,key))


#公共断言
def publicAssert(excepted,actual,key):
    if excepted == actual:
        print("{}断言通过".format(key))
    else:
        print("{}断言不通过".format(key))
        print("{}-----{}".format(excepted,actual))


#颠倒联系人顺序
def reverse_contact(str):
    str = str.split("，")
    print(str)
    string = ","
    return string.join(reversed(str))

#coding:utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


#通过css选择器获取元素
def queryCssSelector(driver,path):
    return WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector(path))

#通过class获取元素
def getElementsByClassName(driver,path):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_class_name(path))

#通过id获取元素
def getElementById(driver,path):
    return WebDriverWait(driver,10).until(lambda x:x.find_element_by_id(path))

#通过xpath获取元素
def getElementsByXpath(driver,path):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath(path))

#通过contains获取元素
def getElementByContains(driver,path,tag,attr="id"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[contains(@{},{})]".format(tag,attr,path)))

#通过contains文本获取元素
def getElementByContains(driver,key,tag):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[contains(text(),{})]".format(tag,key)))

#通过starts-with获取元素
def getElementByStartsWith(driver,path,tag,attr="id"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[starts-with(@{},'{}')]".format(tag,attr,path)))

#通过contains获取元素
def getElementByStartsEnd(driver,path,tag,attr="id"):
    return WebDriverWait(driver,10).until(lambda x:x.find_elements_by_xpath("//{}[starts-end(@{},{})]".format(tag,attr,path)))

#点击元素
def clickElement(element):
    element.click()

#输入文本
def sendKeys(driver,path,key):
    element = driver.find_element_by_css_selector(path)
    element.send_keys(key)

#鼠标悬停操作
def mouseHover(driver,element):
    ActionChains(driver).move_to_element(element).perform()

#鼠标点击操作
def mouseClick(driver,element):
    ActionChains(driver).click(element).perform()

#点击下拉菜单
def clickMenu(driver,path,key):
    path = eval(path)
    btn = queryCssSelector(driver,path[0])
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



def clickEle(driver,path):
    element = driver.find_element_by_css_selector(path)
    element.click()
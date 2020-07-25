# -*- encoding: utf-8 -*-
'''
@File    :   basePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 10:24   dmk      1.0         None
'''



import time,traceback,allure
import win32gui
import win32con
import win32api
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,TimeoutException,StaleElementReferenceException
from utils.log import logger
from utils.config import IMAGE_PATH

class Action(object):

    def __init__(self,driver):
        # 主frame
        self.mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")
        #邮件主体frame
        self.emailBodyFrame_loc = (By.XPATH,"//iframe[@class='mail_iframe_vue']")
        #邮件编辑器
        self.emailEditFrame_loc = (By.XPATH,"//iframe[@class='cke_wysiwyg_frame cke_reset']")
        # 邮件首页
        self.emailHomePage_loc = (By.XPATH, "//div[text()='邮件首页']")
        # 写邮件按钮
        self.writeEmailBtn_loc = (By.XPATH, "//button[@class='el-button el-tooltip item email_write_btn f12 el-button--primary']")
        #收件箱
        self.receiptBox_loc = (By.XPATH,"//span[text()='收件箱']")
        #草稿箱
        self.draftBox_loc = (By.XPATH,"//span[text()='草稿箱']")
        # 群发箱
        self.massBox_loc = (By.XPATH, "//span[text()='群发箱']")
        # toast提示
        self.toast_loc = (By.XPATH, "//p[@class='el-message__content']")
        #下一页按钮
        self.nextPageBtn_loc = (By.XPATH,'//button[@class="btn-next"]')
        #邮件主题
        self.recipientBoxPage_emailSubject_loc = (By.XPATH,'//div[@class="sub_item"]//div[contains(@class,"sub_info info3")]/span/span[not(contains(@class,"boxName"))][1]')
        #导航栏上面的用户名
        self.navUserName_loc = (By.XPATH,'//p[@class="w64 text-white f-s-10 text-ellipsis"]')
        #用户中心用户名
        self.userInfo_userName_loc = (By.XPATH,'//ul[@id="systemMenu"]//div[@class="user-text fl"]')
        #用户列表，dmktest
        self.userList_dmktest_loc = (By.XPATH,'//ul[@id="userChangeSelect"]//div[@class="user-text fl"]//div[text()="dmktest"]/..')
        #用户列表，dmktest001
        self.userList_dmktest001_loc = (By.XPATH,'//ul[@id="userChangeSelect"]//div[@class="user-text fl"]//div[text()="dmktest_001"]/..')
        #关闭tab按钮
        self.closeTabBtn = (By.XPATH,'//div[@class ="tabs_nav"]//i[contains( @class ,"el-icon-close")]')
        #侧边栏，邮件模块按钮
        self.sidebar_emailBtn_loc = (By.XPATH,'//div[@id="sidebar"]//li//i[contains(text(),"邮件")]/..')
        #侧边栏，商机模块按钮
        self.sidebar_businessBtn_loc = (By.XPATH,'//div[@id="sidebar"]//li//i[contains(text(),"商机")]/..')
        #邮件总数量
        self.emailNumTotal_loc = (By.XPATH,'//span[@class="el-pagination__total"]')


        self.driver = driver
        self.timeout = 15
        self.t = 0.5
        # try:
        #     self.switch_frame(self.mainFrame_loc)
        # except Exception as e:
        #     traceback.print_exc()


    def find_element(self,*loc,index=0,key=None):
        wait = WebDriverWait(self.driver, self.timeout, self.t)
        try:
            if isinstance(index,int):
                return wait.until(EC.visibility_of_any_elements_located(*loc))[index]
            else:
                return wait.until(EC.visibility_of_any_elements_located(*loc))
        except TimeoutException as t:
            logger.info('error: found "{}" timeout!'.format(*loc), t)
            self.screenshotImg(key=key)
            return False
        except NoSuchElementException as e:
            logger.info('error: no such "{}"'.format(*loc), e)
            self.screenshotImg(key=key)
            return False
        except StaleElementReferenceException as e:
            logger.info('error: element is not attached to the page document "{}"'.format(*loc), e)
            time.sleep(3)
            if isinstance(index,int):
                return wait.until(EC.visibility_of_any_elements_located(*loc))[index]
            else:
                return wait.until(EC.visibility_of_any_elements_located(*loc))
        except Exception as e:
            self.screenshotImg(key=key)
            raise e


    def find(self,*loc,key):
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.visibility_of_any_elements_located(*loc))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(*loc), t)
            self.screenshotImg(key=key)
            return False
        except NoSuchElementException as e:
            print('error: no such "{}"'.format(*loc), e)
        except Exception as e:
            self.screenshotImg(key=key)
            raise e
        else:
            return ele

    def find_element_byPresence(self,*loc,index=0,key=None):
        wait = WebDriverWait(self.driver, self.timeout, self.t)
        try:
            if isinstance(index,int):
                return wait.until(EC.presence_of_all_elements_located(*loc))[index]
            else:
                return wait.until(EC.presence_of_all_elements_located(*loc))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(*loc), t)
            self.screenshotImg(key=key)
            return False
        except NoSuchElementException as e:
            print('error: no such "{}"'.format(*loc), e)
            self.screenshotImg(key=key)
            return False
        except StaleElementReferenceException as e:
            logger.info('error: element is not attached to the page document "{}"'.format(*loc), e)
            time.sleep(3)
            if isinstance(index,int):
                return wait.until(EC.visibility_of_any_elements_located(*loc))[index]
            else:
                return wait.until(EC.visibility_of_any_elements_located(*loc))
        except Exception as e:
            self.screenshotImg(key=key)
            raise e



    #判断元素是否可见
    def is_visible(self,*loc,visibility=True):
        if visibility:
            return WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(*loc))
        else:
            return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(*loc))

    #获取元素文本
    def get_elementText(self,*loc,index=0,key=None):
        # 先滚动元素
        self.scroll_element(*loc,key=key)
        time.sleep(0.5)
        elements = self.find_element(*loc,index="all",key=key)
        if isinstance(index,int):
            return elements[index].text
        else:
            text = []
            for element in elements:
                text.append(element.text)
            return text

    # 点击元素
    def click_ele(self, *loc,index=0,key=None):
        # 先滚动元素
        self.scroll_element(*loc,key=key)
        time.sleep(0.5)
        self.find_element(*loc,index=index,key=key).click()
        #self.find(*loc,key=key).click()

    # 输入内容
    def sendKeys(self, *loc, key, clear=1):
        # 先滚动元素
        self.scroll_element(*loc)
        time.sleep(0.5)
        # 默认清空输入框
        ele = self.find_element(*loc)
        if clear:
            ele.clear()
        time.sleep(0.3)
        ele.send_keys(key)


    #文件上传
    def upload_file(self,filePath,browser_type="chrome"):
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""

        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        #
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮


    #鼠标悬浮操作
    def mouseHover(self,*loc,index=0):
        ele = self.find_element_byPresence(*loc,index=index)
        ActionChains(self.driver).move_to_element(ele).perform()

    #鼠标悬浮操作
    def mouseHover_visibleEle(self,*loc):
        ele = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    #鼠标点击操作
    def mouseClick(self,*loc):
        self.scroll_element(*loc)
        ele = self.find_element(*loc)
        ActionChains(self.driver).click(ele).perform()

    # 鼠标双击操作
    def mouseDoubleClick(self, *loc):
        self.scroll_element(*loc)
        ele = self.find_element(*loc)
        ActionChains(self.driver).double_click(ele).perform()

    #切换frame
    def switch_frame(self,*loc):
        # return EC.frame_to_be_available_and_switch_to_it(*loc)(self.driver)
        WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it(*loc))


    #切回父frame
    def switch_parentFrame(self):
        print("切回父frame")
        self.driver.switch_to.parent_frame()

    #切回主文档
    def switch_mainPage(self):
        print("切回主文档")
        self.driver.switch_to.default_content()

    #刷新浏览器
    def refresh_bro(self,frame=1):
        mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")
        self.driver.refresh()
        #判断是否有弹窗
        time.sleep(1)
        alert = EC.alert_is_present()(self.driver)
        if alert:
            alert.accept()
        if frame == 1:
            EC.frame_to_be_available_and_switch_to_it(mainFrame_loc)(self.driver)

    #判断元素是否存在
    def is_element_exist(self,xpath):
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            print("元素未找到:%s" % xpath)
            return False
        else:
            print("一共找到{}个元素".format(len(s)))
            return s


    #判断元素是否可点击
    def is_element_click(self,*loc):
        try:
            ele = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(*loc))
        except Exception:
            return False
        return ele


    #滚动元素到指定位置，以点击
    def scroll_element(self,*loc,key=None):
        ele = self.find_element_byPresence(*loc,key=key)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)

    #保存截图
    def screenshotImg(self,key=None):
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        logger.info("保存的图片：{}/{}-{}.png".format(IMAGE_PATH, nowTime, key))
        self.driver.get_screenshot_as_file("{}/{}-{}.png".format(IMAGE_PATH, nowTime, key))

    #切换业务员
    def switch_operator(self,operator="dmktest"):
        self.switch_mainPage()
        #判断当前业务员是不是demktest
        operator_text = self.find_element(self.navUserName_loc).text
        print(operator_text)
        if operator_text == operator:
            # 切换进主frame
            self.switch_frame(self.mainFrame_loc)
        else:
            #点击导航栏用户
            self.find_element(self.navUserName_loc).click()
            time.sleep(0.5)
            #点击用户中心里面的管理员，弹出下拉框
            self.find_element(self.userInfo_userName_loc).click()
            time.sleep(0.5)
            #选择弹出的业务员
            if operator == "dmktest":
                self.find_element(self.userList_dmktest_loc).click()
            else:
                self.find_element(self.userList_dmktest001_loc).click()
            time.sleep(2)
            #判断切换后是不是要切换的业务员
            operator_text = self.find_element(self.navUserName_loc).text
            if operator_text != operator:
                raise Exception("切换业务员失败")
            else:
                #切换进主frame
                self.switch_frame(self.mainFrame_loc)

    #替换text，生成xpath
    def generateXpathByInsteadText(self,*loc):
        newXpath_loc = (By.XPATH,loc[1].replace(""))
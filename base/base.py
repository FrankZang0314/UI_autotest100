import allure
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog
log = GetLog.get_logger()

class Base:
    def __init__(self,driver):
        log.info("正在初始化driver:{}".format(driver))
        self.driver=driver

    def base_find(self,loc,timeout=30,poll=0.5):
        # self.driver.find_element()
        log.info("正在查找元素：{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x:x.find_element(*loc)))

    def base_input(self,loc,value):
        el=self.base_find(loc)
        log.info("正在对{}元素进行清空操作".format(loc))
        el.clear
        log.info("正在对{}元素进行输入：{}操作".format(loc,value))
        el.send_keys(value)

    def base_click(self,loc):
        log.info("正在对{}元素进行点击操作".format(loc))
        self.base_find(loc).click

    def base_get_text(self,loc):
        log.info("正在对{}元素获取文本，获取的文本值为{}".format(loc,self.base_find(loc).text))   #如果追求性能测试时，先将base_find(loc)赋予一个变量
        return self.base_find(loc).text

    def base_get_image(self):
        log.error("断言出错，正在执行截图操作！")
        self.driver.get_screenshot_as_file("./image/err1.png")
        # self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错，正在将错误图片写入allure报告   ！")
        self.__base_write_image()

    def __base_write_image(self):
        with open("./image/err1.png","rb") as f:
            # allure.attach("错误原因","图片流","图片类型")
            allure.attach("错误原因", f.read(), allure.attachment_type.PNG)
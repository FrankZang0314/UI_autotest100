from selenium import webdriver


class GetDriver():
    __web_driver = None

    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None

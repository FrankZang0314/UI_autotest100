from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog

log= GetLog.get_logger()

class PageMpLogin(Base):
    def page_input_username(self,username):
        self.base_input(page.mp_username,username)

    def page_input_code(self,code):
        self.base_input(page.mp_code,code)

    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login_btn)

    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # def page_mp_login(self,username,code):
    #     self.page_input_username(username)
    #     self.page_input_code(code)
    #     self.page_click_login_btn()

    def page_mp_login(self,username):
        log.info("正在调用自媒体业务方法，登录的用户名是:{}".format(username))
        self.page_input_username(username)
        # self.page_input_code(code)
        self.page_click_login_btn()
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log=GetLog.get_logger()

class TestMpLogin:
    def setup_class(self):
        driver=GetDriver.get_web_driver(page.url_mp)
        self.mp=PageIn(driver).page_get_PageMpLogin()

    def teardown_cass(self):
        GetDriver.quit_web_driver()

    # @pytest.mark.parametrize("username,code,expect",read_yaml("mp_login.yaml"))    #参数化运行
    # def test_mp_login(self,username,code,expect):
    #     self.mp.page_mp_login(username,code)
    #     # print("\n 获取的昵称为：",self.mp.page_get_nickname())
    #     try:
    #         assert expect ==self.mp.page_get_nickname()
    #     except Exception as e:
    #         # print("错误原因：",e)
    #         self.mp.base_get_image()
    #         raise

    @pytest.mark.parametrize("username,expect", read_yaml("mp_login.yaml"))  # 参数化运行
    def test_mp_login(self, username, expect):
        self.mp.page_mp_login(username)
        # print("\n 获取的昵称为：",self.mp.page_get_nickname())
        try:
            # assert expect == self.mp.page_get_nickname()
            assert expect =="百度一下1"
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            # print("错误原因：",e)
            self.mp.base_get_image()
            raise
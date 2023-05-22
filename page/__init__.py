from selenium.webdriver.common.by import By

url_mp="https://www.baidu.com/"



# mp_username=(By.CSS_SELECTOR,"[placeholder='请输入手机号']")   #[]是属性选择器，属性名无需加@修饰；都是元祖格式，加不加小括号都一样
mp_username=(By.CSS_SELECTOR,".s_ipt")   #[]是属性选择器，属性名无需加@修饰；都是元祖格式，加不加小括号都一样

mp_code=(By.CSS_SELECTOR,"[placeholder='验证码']")

# mp_login_btn=(By.CSS_SELECTOR,".el-button-primary")      #* .为class选择器
mp_login_btn=(By.CSS_SELECTOR,"[id='su']")      #* .为class选择器

mp_nickname=(By.CSS_SELECTOR,".btn self-btn bg s_btn")
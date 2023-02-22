import master
from master import *


driver.maximize_window()


User_email = "harsh.sachan@universityliving.com"
click_x("//span[text()='Login / SignUp']")
entry_i("email","harsh.sachan@universityliving.com")
click_x("//div[text()='Login']")
entry_n("otp0",'1')
entry_n("otp1",'2')
entry_n("otp2",'3')
entry_n("otp3",'4')
entry_n("otp4",'5')
click_x("//div[text()='Continue']")
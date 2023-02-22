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
click_x("(//img[@class='rounded-full'])[1]")
dashboard_email = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section/div[2]/div[1]/div/div/p[2]').text
# click_x("(//p[text()='Personal Information'])[2]")
# personalInfo_email = driver.find_element(By.XPATH,"(//input[@name='email'])[1]").text
click_x("(//p[text()='Profile'])[2]")
profile_email = driver.find_element(By.XPATH,"//div/div[2]/div[2]/p[2]").text

print("dashboard",dashboard_email)
# print("personalInfo",personalInfo_email)
print("profile",profile_email)

if ((dashboard_email == User_email) and (profile_email == User_email)):
    print("Email validation passed")
else:
    print("Email validation Failed")

time.sleep(5)
driver.close()


import master

from master import *

driver.maximize_window()
click_x("//span[text()='Melbourne']")
#driver.switch_to.window(driver.window_handles[1])
click_x("//a[text()='Scape Swanston']")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(3)
click_x("//div[text()='Book Now']")
entry_i("email","harsh.sachan@universityliving.com")
click_x("//div[text()='Login']")
entry_n("otp0",'1')
entry_n("otp1",'2')
entry_n("otp2",'3')
entry_n("otp3",'4')
entry_n("otp4",'5')
click_x("//div[text()='Continue']")
driver.find_element(By.XPATH,"(//input[@placeholder='Select your University'])[2]").click()
click_i("university-search-item-1")
click_x("//span[text()='Yes']")
click_x("(//div[text()='Book Now'])[last()]")
click_x("//span[text()='Male']")
entry_x("//input[@placeholder='address']","Test")
country_drop = driver.find_element(By.NAME,"country")
Select(country_drop).select_by_visible_text("Austria")
entry_x("//input[@placeholder='Select State/Province']","Test")
entry_x("//input[@placeholder='City']","Test")
entry_x("//input[@placeholder='Postal Code']","201304")
nationality = driver.find_element(By.NAME, "nationality")
Select(nationality).select_by_visible_text("Indian")
click_x("//div[text()='Next']")





ascii_art = pyfiglet.figlet_format("Driver exiting.....", font="starwars")
print(ascii_art)
time.sleep(5)
ascii_art = pyfiglet.figlet_format("pass !", font="starwars")
print(ascii_art)
driver.quit()
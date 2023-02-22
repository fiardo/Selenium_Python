import master

from master import *

driver.maximize_window()
click_x("//span[text()='London']")
# driver.switch_to.window(driver.window_handles[1])
click_x("//a[text()='iQ Hoxton']")
driver.switch_to.window(driver.window_handles[1])
click_x("//div[text()='Enquire']")
entry_i("firstName","test")
entry_i("lastName","test")
entry_i("email","harsh.sachan@universityliving.com")
entry_i("contactNumber","8505813979")
entry_i("message","test")
drop = Select(driver.find_element(By.NAME,"visaStatus"))
drop.select_by_index(2)

driver.find_element(By.XPATH,"(//input[@placeholder='Select your University'])[2]").click()
click_i("university-search-item-0")


# click_x("(//input[@placeholder='Select your University'])[2]")
click_x("//div[text()='Submit']")
element = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/h1/span').text
if element == "Test":
    ascii_art = pyfiglet.figlet_format("PASS  😎!", font="starwars")
    print(ascii_art)
else:
    ascii_art = pyfiglet.figlet_format("FAIL  😞!", font="starwars")
    print(ascii_art)


time.sleep(5)
driver.quit()
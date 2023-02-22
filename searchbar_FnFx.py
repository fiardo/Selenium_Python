from master import *

driver.maximize_window()

click_x("//input[@type='text']")
click_x("//li[text()='UK']")
click_x("(//li[text()='Ireland'])[1]")
click_x("(//li[text()='Canada'])[1]")
click_x("(//li[text()='US'])[1]")

entry_x("//input[@type='text']","testers are cool")
if driver.find_element(By.XPATH,"//a[text()='No matches found.']").text == "No matches found.":
    print("no match validation pass.")
else:
    print("no match validation failed.")

driver.close()
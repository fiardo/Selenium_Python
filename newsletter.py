import master

from master import *
import random
import string

driver.maximize_window()
entry_x("//input[@name='email']","test@yopmail.com")
click_x("//div[text()='Subscribe']")
time.sleep(4)
welcome = driver.find_element(By.CLASS_NAME,"my-6").text
if welcome == "You’re already subscribed to UL Newsletter.":
    print("existing email address is entered --> test@yopmail.com")

click_cl("outline-none")

letters = string.ascii_lowercase
a = ( ''.join(random.choice(letters) for i in range(5)) )
new_email = a + '@yopmail.com'


entry_x("//input[@name='email']",new_email)
click_x("//div[text()='Subscribe']")
time.sleep(4)

welcome2 = driver.find_element(By.CLASS_NAME,"my-6").text
if welcome2 == "Welcome onboard, Thank you for subscribing to UL Newsletter.":
    print("new email is entered -->", new_email)

click_cl("outline-none")
time.sleep(3)
driver.close()
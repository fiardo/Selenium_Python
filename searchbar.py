import master

from master import *
driver.maximize_window()

keyword = "london"

entry_x("//input[@type='text']",keyword)
lst = []
items = driver.find_elements(By.XPATH,"(/html/body/div[1]/main/section[1]/div[1]/div/div[1]/div[1]/div[2]/div/a/div/div[1])")
for item in items:
    # if item.text == "Ostuni":
    #     item.click()
    #     break
    lst.append(item.text)

print(lst)
print("total count of listed properties is -->",len(lst))

time.sleep(3)
driver.close()
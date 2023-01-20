import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
import pyfiglet
from colorama import init
init(strip=not sys.stdout.isatty()) 
from pyfiglet import figlet_format



s = Service("/Users/uniliv/Desktop/Data/Automation/chromedriver")

driver = webdriver.Chrome(service=s)
driver.get('https://stg-next.universityliving.com/')


driver.maximize_window()
wait = 1
def click_x(xpath):
    driver.find_element(By.XPATH,xpath).click()
    time.sleep(wait)

def entry_x(xpath,keys):
    driver.find_element(By.XPATH,xpath).send_keys(keys)
    time.sleep(wait)

def click_i(iD):
    driver.find_element(By.ID,iD).click()
    time.sleep(wait)

def entry_i(iD,keys):
    driver.find_element(By.ID,iD).send_keys(keys)
    time.sleep(wait)

def click_n(NamE):
    driver.find_element(By.NAME,NamE).click()
    time.sleep(wait)

def entry_n(NamE,keys):
    driver.find_element(By.NAME,NamE).send_keys(keys)
    time.sleep(wait)


click_x("//span[text()='Login / SignUp']")
entry_i("email","pravin.garg@universityliving.com")
click_x("//div[text()='Login']")
time.sleep(3)
entry_n("otp0",'1')
entry_n("otp1",'2')
entry_n("otp2",'3')
entry_n("otp3",'4')
entry_n("otp4",'5')
click_x("//div[text()='Continue']")

driver.get('https://stg-next.universityliving.com/dashboard?tab=booking')
time.sleep(3)
element = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section/div[2]/div[1]/div/div/p[2]').text
time.sleep(3)
assert element == 'pravin.garg@universityliving.com'

time.sleep(3)
driver.quit()
ascii_art = pyfiglet.figlet_format("PASS!", font="starwars")
print(ascii_art)
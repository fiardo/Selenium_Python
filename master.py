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


ascii_art = pyfiglet.figlet_format("START", font="starwars")
print(ascii_art)
s = Service("C:/Users/TUL/Desktop/cd/cd2.exe")

driver = webdriver.Chrome(service=s)
driver.get('https://www.universityliving.com/')
wait = 1

def click_x(xpath):           # click using xpath
    driver.find_element(By.XPATH,xpath).click()
    time.sleep(wait)

def entry_x(xpath,keys):       # entry using xpath
    driver.find_element(By.XPATH,xpath).send_keys(keys)
    time.sleep(wait)

def click_i(iD):               # click using ID
    driver.find_element(By.ID,iD).click()
    time.sleep(wait)

def entry_i(iD,keys):          # entry using ID
    driver.find_element(By.ID,iD).send_keys(keys)
    time.sleep(wait)

def click_n(NamE):             # click using html name.
    driver.find_element(By.NAME,NamE).click()
    time.sleep(wait)

def entry_n(NamE,keys):        # entry using html name.
    driver.find_element(By.NAME,NamE).send_keys(keys)
    time.sleep(wait)

def click_cl(clss):             # click using class names
    driver.find_element(By.CLASS_NAME,clss).click()
    time.sleep(wait)

def entry_cl(clss,keys):        # entry using class names
    driver.find_element(By.CLASS_NAME,clss).send_keys(keys)
    time.sleep(wait)

def act_chain(chains):
    pass
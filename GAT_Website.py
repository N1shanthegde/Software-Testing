from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
import sys


chromedriver_path = "./chromedriver.exe" 
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid black;');", element)
    time.sleep(1)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

driver.get("https://globalparents.contineo.in/newparentseven/index.php") 
driver.maximize_window()
time.sleep(1)

USN = driver.find_element(By.XPATH, '//*[@id="username"]')
highlight_element(USN)
USN.send_keys(" ")  #enter your user id
time.sleep(1)

day = driver.find_element(By.XPATH, '//*[@id="dd"]')
highlight_element(day)
day.send_keys("10")
time.sleep(1)

month = driver.find_element(By.XPATH, '//*[@id="mm"]')
highlight_element(month)
month.send_keys("mar")
time.sleep(1)

year = driver.find_element(By.XPATH, '//*[@id="yyyy"]')
highlight_element(year)
year.send_keys("2003")
time.sleep(1)

login = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input[1]')
highlight_element(login)
login.click()
time.sleep(1)

#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

attendence = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[4]/a/button')
highlight_element(attendence)
attendence.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

eee62 = driver.find_element(By.XPATH, '//*[@id="tab2"]/a')
highlight_element(eee62)
eee62.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

# eee63 = driver.find_element(By.XPATH, '//*[@id="tab3"]/a')
# highlight_element(eee63)
# eee63.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# eee661 = driver.find_element(By.XPATH, '//*[@id="tab4"]/a')
# highlight_element(eee661)
# eee661.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# eee643 = driver.find_element(By.XPATH, '//*[@id="tab5"]/a')
# highlight_element(eee643)
# eee643.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# eee653 = driver.find_element(By.XPATH, '//*[@id="tab6"]/a')
# highlight_element(eee653)
# eee653.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

Home = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[2]/nav/div/div/ul/li[1]/a')
highlight_element(Home)
Home.click()
time.sleep(1)

cie = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[5]/a/button')
highlight_element(cie)
cie.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

eee62 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/ul/li[2]/a')
highlight_element(eee62)
eee62.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

# eee63 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/ul/li[3]/a')
# highlight_element(eee63)
# eee63.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# eee661 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/ul/li[4]/a')
# highlight_element(eee661)
# eee661.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# eee643 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/ul/li[5]/a')
# highlight_element(eee643)
# eee643.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# eee653 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/ul/li[6]/a')
# highlight_element(eee653)
# eee653.click()
# time.sleep(1)
# #scroll page
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
# for i in range(0,9):
#     driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
#     time.sleep(1)



event = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/nav/div/div/ul/li[2]/a')
highlight_element(event)
event.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

tt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/nav/div/div/ul/li[3]/a')
highlight_element(tt)
tt.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

Prev_Perf = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/nav/div/div/ul/li[4]/a')
highlight_element(Prev_Perf)
Prev_Perf.click()
time.sleep(1)
#scroll page
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,9):
    driver.find_element(by=By.TAG_NAME,value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)
    
    
logout = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/nav/div/div/ul/li[5]/a')
highlight_element(logout)
logout.click()
time.sleep(1)
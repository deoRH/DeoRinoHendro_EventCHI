from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import requests
import re

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.demo.chi.app/")

print("___Welcome to web demo automation___")
time.sleep(5)
try:
    element = driver.find_element(By.XPATH,"//*[contains(text(), 'EventCHI')]")
    print("welcome to", element.text)
except:
    print("not found")

#register number

dropdown = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/img').click()
time.sleep(3)
MX = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div').click()
time.sleep(3)
US_code = "62"
US_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/input')
US_field.clear()
time.sleep(3)
US_field.send_keys(US_code)
time.sleep(3)

phone_number = "81991184560"
phone_number_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/input')
phone_number_field.send_keys(phone_number)
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div').click()
time.sleep(3)


phone_number_id = driver.find_element(By. XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[2]')
print (f"your number is {phone_number_id.text}")
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]').click()
time.sleep(3)

#send otp

otp = "060827"
otp_regis = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div/input')
otp_regis.send_keys(otp)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div').click()
time.sleep(10)
#personal information

first_name = "John"
last_name = "Doe"
date = "01"
month = "06"
year = "1990"
email = "johndoe@test.com"
confirm_email = "johndoe@test.com"

first_name_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/input')
first_name_field.send_keys(first_name)
time.sleep(2)
last_name_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/input')
last_name_field.send_keys(last_name)
time.sleep(2)
date_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/input[1]')
date_field.send_keys(date)
time.sleep(1)
month_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/input[2]')
month_field.send_keys(month)
time.sleep(1)
year_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/input[3]')
year_field.send_keys(year)
time.sleep(1)
country = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div/div[1]').click()
country_field = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div[1]/div/input')
country_field.send_keys("Indonesia")
element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div').click()
time.sleep(5)
email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div/input')
email_field.send_keys(email)
time.sleep(2)
confirm_email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/input')
confirm_email_field.send_keys(confirm_email)
time.sleep(2)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[7]/div[1]/div[1]/div').click()
time.sleep(2)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[2]').click()
time.sleep(2)

# security code 
sec_code = "1234"
sec_code_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[4]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/input')
sec_code_field.send_keys(sec_code)
sec_code_conf_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[4]/div/div/div/div[2]/div[1]/div[3]/div[2]/div/input')
sec_code_conf_field.send_keys(sec_code)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[4]/div/div/div/div[2]/div[2]/div[2]').click()
time.sleep(10)
driver.save_screenshot('homepage.png')

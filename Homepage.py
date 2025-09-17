from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Login_page import login


chrome_options = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://web.demo.chi.app/")

login(driver)

# transaction page
addcard = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div').click()
time.sleep(8)
driver.save_screenshot('transaction.png')
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/img').click()
time.sleep(3)

# QR page
paywithqr = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/a[2]').click()
time.sleep(8)
driver.save_screenshot('qr.png')
time.sleep(3)

# tickets
tickets = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/a[3]/div/div[2]/div/img').click()
time.sleep(8)
driver.save_screenshot('ticket.png')
time.sleep(3)

# wearables
wearables = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/a[4]').click()
time.sleep(8)
driver.save_screenshot('wearables.png')
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[4]/div/div/div/div[3]/div/div[2]').click()

# error
code = 123
field_code = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/input')
field_code.send_keys(code)
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[2]/div').click()
time.sleep(5)
wording = driver.find_element(By.XPATH, "//*[contains(text(), 'Wearable pairing failed')]")
print("Teks ditemukan:", wording.text)
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div').click()
time.sleep(1)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/img').click()
time.sleep(5)

# logout
logout = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[4]/div/div/div/div[1]/div/div[2]/button/div/div/div/div/img').click()
time.sleep(5)

# relogin
phone_number = "81991184560"
phone_number_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/input')
phone_number_field.send_keys(phone_number)
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div').click()
time.sleep(3)

#pin lock

pin = "1234"
pin_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/input')
pin_field.send_keys(pin)
time.sleep(2)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[3]').click()
time.sleep(5)
driver.save_screenshot('homepage.png')

driver.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import requests

def login(driver):

    print("___Welcome to web demo automation___")
    time.sleep(5)
    try:
      element = driver.find_element(By.XPATH,"//*[contains(text(), 'EventCHI')]")
      print("welcome to", element.text)
    except:
      print("not found")

    #login number

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

    #pin lock

    pin = "1234"
    pin_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/input')
    pin_field.send_keys(pin)
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[3]').click()
    time.sleep(5)
    driver.save_screenshot('homepage.png')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import cv2
import numpy as np

username = "" #Write your login here!
password = "" #Write your password here!
url = "https://wsp.kbtu.kz/RegistrationOnline"

def login():
    time.sleep(1)
    driver.get(url)
    time.sleep(5)
    username_input = driver.find_element(By.CSS_SELECTOR, "input.v-filterselect-input[type='text']")
    username_input.send_keys(username)
    time.sleep(1)
    password_input = driver.find_element(By.CSS_SELECTOR, "input.v-textfield[type='password']")
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

def click_itog_buttons():
    for i in range(3):
        time.sleep(1)
        try:
            button = driver.find_element(By.XPATH, "//div[contains(@class, 'v-button') and .//span[text()='Отметиться']]")
            button.click()
            print("Button clicked successfully!")
        except Exception as e:
            print("Error")
        time.sleep(1)
        driver.refresh()


driver = webdriver.Chrome()
login()
time.sleep(5)

while True:
    click_itog_buttons()
    time.sleep(180)
    driver.refresh()

driver.quit()

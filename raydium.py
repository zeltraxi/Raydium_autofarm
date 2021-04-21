# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:26:17 2021

@author: Guillaume
"""

import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import pyautogui, sys
import schedule
from datetime import datetime

def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Time: ", dt_string)
    options = webdriver.ChromeOptions() 
    options.add_argument(r"YOURCHROMEPROFILEPATH") #Path to your chrome profile
    options.add_argument("--start-maximized")#Maximize window
    driver = webdriver.Chrome(r"YOURCHROMEDRIVER.EXE",options=options)
    time.sleep(1)
    driver.get('https://raydium.io/farms/');
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    time.sleep(1)
    #Click Connect
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/header/div/div[1]/button')[0]
    python_button.click()
    #Open Sollet Wallet
    time.sleep(1)
    #Focus on new tab
    python_button = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]')[0]
    python_button.click()
    #Connect Sollet Wallet
    time.sleep(1)
    #pyautogui.click(x=1300, y=10)
    #time.sleep(3)
    pyautogui.click(x=400, y=440)
    time.sleep(1)
    pyautogui.click(x=1300, y=500)
    time.sleep(1)
    pyautogui.click(x=1300, y=500)
    time.sleep(1)
    #Print earn in LP
    print('Value in RAY/USDT : ' + driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[3]/div[1]/div/div/div[2]/div/div/div[2]/div[2]')[0].text)
    print('Value in RAY/ETH : ' + driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[3]/div[1]/div/div/div[9]/div[1]/div/div[2]/div[2]')[0].text)
    #Select Reward RAY / USDT
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[3]/div[1]/div/div/div[2]/div/div/div[2]')[0]
    python_button.click()
    time.sleep(3)
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/button')[0]
    python_button.click()
    #Select Reward RAY / ETH
    time.sleep(3)
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[3]/div[1]/div/div/div[9]/div[1]/div/div[2]')[0]
    python_button.click()
    time.sleep(3)
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[3]/div[1]/div/div/div[9]/div[2]/div/div/div[2]/div/div[2]/button')[0]
    python_button.click()
    #Staking Page
    driver.get('https://raydium.io/staking/');
    #Click Connect
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/header/div/div[1]/button')[0]
    python_button.click()
    #Open Sollet Wallet
    time.sleep(1)
    #Focus on new tab
    python_button = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]')[0]
    python_button.click()
    time.sleep(1)
    #pyautogui.click(x=1300, y=10)
    #time.sleep(3)
    pyautogui.click(x=400, y=440)
    time.sleep(1)
    pyautogui.click(x=1300, y=500)
    time.sleep(1)
    pyautogui.click(x=1300, y=500)
    #Earn Ray
    time.sleep(3)
    print('Ray in staking : ' + driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]')[0].text)
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[2]/div/div/div/div[1]/div/div[2]')[0]
    python_button.click()
    time.sleep(3)
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/button')[0]
    python_button.click()
    time.sleep(3)
    #Staking RAY
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/button[2]')[0]
    python_button.click()
    time.sleep(3)
    #MAX
    python_button = driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/button')[0]
    python_button.click()
    time.sleep(3)
    #Confirm
    python_button = driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/button')[0]
    python_button.click()
    time.sleep(5)
    python_button = driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[2]/div/div/div/div[1]/div/div[2]')[0]
    python_button.click()
    print('Total Value in Staking : ' + driver.find_elements_by_xpath('//*[@id="__layout"]/section/main/div/div[2]/div/div/div/div[1]/div/div[3]/div[2]')[0].text + '\n')
    time.sleep(3)
    driver.quit()
#Every 30 minutes
print("Schedule")
schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
"""
To Check Macro click
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        print('\n')
        time.sleep(1)
except KeyboardInterrupt:
    print('\n')

"""

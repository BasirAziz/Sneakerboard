# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:21:27 2020

@author: BasirAziz
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time
from selenium.webdriver.support.ui import Select
import time, datetime
import logging
import threading
import time
import numpy as np


year_date = input('Enter year: ')
month_date = input('Enter month: ')
datedate = input('Enter date: ')
hourhour = input('hour:')
mints = input('minutes: ')
sec = input('seconds: ')
msec = input('milli seconds: ')

yy = int(year_date) 
mm = int(month_date)
dd = int(datedate)
hh = int(hourhour)
mins = int(mints)
secs = int(sec)
milsecs = int(msec)

sd = datetime.datetime(yy, mm, dd, hh, mins, secs, milsecs)


def first_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\BasirAziz\Desktop\Airus\chromedriver_win32 (87)\chromedriver.exe')
  driver.maximize_window()


  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('itstiafarisha@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('@Nniikkee99')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/air-jordan-1-dark-mocha?size=9&productId=94fc30a5-9916-50d5-8519-8f0903058887")
  time.sleep(6)
  driver.find_element_by_xpath('// *[@id="firstName"]').click()
  time.sleep(2)
  driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('35,Jalan Putra Indah 9/22')  #id="addressLine1"
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Putra Heights,Selangor') # id="addressLine2"  id="postCode"  id="locality"
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47650') 
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Subang Jaya') 
  time.sleep(2)
  select = Select(driver.find_element_by_id('state'))
  select.select_by_visible_text('Kuala Lumpur')
  time.sleep(2)
  driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
  time.sleep(2)
  driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
  time.sleep(2)
  driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  time.sleep(2)   
  driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
  time.sleep(2)
  driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('4283322042240935')   
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1222")         
  time.sleep(2)     
  driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("268")                                
  time.sleep(2)
  driver.switch_to_default_content()
  time.sleep(2)
  driver.find_element_by_xpath('//button[@ class="button-continue"]').click()

  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
  
def second_account():
  driver = webdriver.Chrome(executable_path=r'C:\Users\BasirAziz\Desktop\Airus\chromedriver_win32 (87)\chromedriver.exe')
  driver.maximize_window()



  driver.get("https://www.nike.com/my/launch")
  time.sleep(5)
  driver.find_element_by_xpath('// button[@class="join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b"]').click()
  time.sleep(5)
  driver.find_element_by_xpath('// input[@placeholder="Email address"]').send_keys('tanlt4896@gmail.com')
  time.sleep(3)
  driver.find_element_by_xpath('// input[@placeholder="Password"]').send_keys('Nike1111')
  time.sleep(5)
  driver.find_element_by_xpath('// input[@value="SIGN IN"]').click()
  time.sleep(8)
  driver.get("https://www.nike.com/my/launch/t/air-jordan-1-dark-mocha?size=9&productId=94fc30a5-9916-50d5-8519-8f0903058887")
  time.sleep(6)
  driver.find_element_by_xpath('// *[@id="firstName"]').click()
  time.sleep(2)
  driver.find_element_by_xpath('// *[@id="firstName"]').send_keys('Haziq')
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="lastName"]').send_keys('Razak')
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="addressLine1"]').send_keys('35,Jalan Putra Indah 9/22')  #id="addressLine1"
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="addressLine2"]').send_keys('Putra Heights,Selangor') # id="addressLine2"  id="postCode"  id="locality"
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="postCode"]').send_keys('47650') 
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="locality"]').send_keys('Subang Jaya') 
  time.sleep(2)
  select = Select(driver.find_element_by_id('state'))
  select.select_by_visible_text('Kuala Lumpur')
  time.sleep(2)
  driver.find_element_by_xpath('//input[@placeholder="Phone number"]').send_keys('1165042828') 
  time.sleep(2)
  driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('razhaziq@gmail.com')
  time.sleep(2)
  driver.find_element_by_xpath('//button[@ class="button-continue"]').click()       
  time.sleep(2)   
  driver.switch_to_frame(driver.find_element_by_class_name('newCard'))
  time.sleep(2)
  driver.find_element_by_xpath('//input[@id="cardNumber-input"]').send_keys('4283322042240935')   
  time.sleep(2)
  driver.find_element_by_xpath('// input[@id="cardExpiry-input"]').send_keys("1222")         
  time.sleep(2)     
  driver.find_element_by_xpath('// input[@id="cardCvc-input"]').send_keys("268")                                
  time.sleep(2)
  driver.switch_to_default_content()
  time.sleep(2)
  driver.find_element_by_xpath('//button[@ class="button-continue"]').click()

  while datetime.datetime.now() < sd:  
    time.sleep(1)

  driver.find_element_by_xpath('//button[@ class="button-submit"]').click()
  
t1 = threading.Thread(target=first_account)
t2 = threading.Thread(target=second_account)


t1.start()
t2.start()

t1.join()
t2.join()
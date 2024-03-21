#Encontrar locators e usar no site https://paulocoliveira.github.io/mypages/jobapplication.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://paulocoliveira.github.io/mypages/jobapplication.html')

sleep(3)

#Encontrar o locator do full name e preencher através de CSS
full_name = driver.find_element(By.CSS_SELECTOR, 'form>fieldset>input')
full_name.send_keys('Magda Rocha')

sleep(1)

#Encontrar o locator email e preencher através do XPATH

email= driver.find_element(By.XPATH, '//form//fieldset//input[2]')
email.send_keys('magda.rocha92@gmail.com')

sleep(1)

#Encontrar o locator phone number e preencher através do CSS

phone_number = driver.find_element(By.CSS_SELECTOR, 'form fieldset input:nth-child(11)')
phone_number.send_keys('932345679')

sleep(1)

#Encontrar o locator cargo desejado e preencher através do XPATH (usando a biblioteca
#Select por ser uma dropdownlist)

Select(driver.find_element(By.XPATH, '//form/fieldset/select')).select_by_visible_text('Designer')

sleep(1)

#Encontrar o locator Preferred work location e preencher através do CSS

office = driver.find_element(By.CSS_SELECTOR , 'form fieldset:nth-child(2) input:nth-child(9)')
office.click()

sleep(1)

#Encontrar o locator years of experience e preencher através do XPATH

years_of_experience = driver.find_element(By.XPATH, '//form/fieldset[3]/input')
years_of_experience.send_keys('3')

sleep(1)

#Encontrar o locator skills e preencher através do CSS

skills = driver.find_element(By.CSS_SELECTOR, 'form fieldset:nth-child(3) input:nth-child(9)')
skills.click()

sleep(1)

#Encontrar o locator Submit e preencher através de XPATH

submission = driver.find_element(By.XPATH, '//form/button')
submission.click()

sleep(1)

driver.quit()
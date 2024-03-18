from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

linkedin= webdriver.Chrome()

linkedin.get('https://www.linkedin.com/')

linkedin.maximize_window()

sleep(3)

#1 elemento
#BY ID do campo de colocação do email/nome no linkedin
email = linkedin.find_element(By.ID, 'session_key')

#By name do mesmo elemento
name = linkedin.find_element(By.NAME, 'session_key')

#2 elemento
#By class name do SIGN IN
sign = linkedin.find_element(By.CLASS_NAME, 'btn-md')

#By LINK_TEXT do mesmo elemento
sign1 = linkedin.find_element(By.LINK_TEXT, 'Sign in')

#3 elemento
#By PARTIAL_LINK_TEXT do obter a app
app = linkedin.find_element(By.PARTIAL_LINK_TEXT, 'now')

#By TAG_NAME do mesmo elemento
app1 = linkedin.find_elements(By.TAG_NAME, 'a')

title = linkedin.title

print(title)

linkedin.quit()
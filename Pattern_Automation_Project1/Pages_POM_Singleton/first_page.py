from selenium.webdriver.common.by import By
from Pages_POM_Singleton.base_page import BasePage


class LoginPage(BasePage):
    USER = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login-button')
   
    
    def login(self, username, password):
        self.wait_for_element(self.USER).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()
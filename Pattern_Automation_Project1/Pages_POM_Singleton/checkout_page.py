from selenium.webdriver.common.by import By
from Pages_POM_Singleton.base_page import BasePage

class CheckoutPage(BasePage):
    NAME = (By.CSS_SELECTOR, 'div input:first-child')
    LAST_NAME = (By.CSS_SELECTOR, 'form div div:nth-child(2) input:first-child')
    ZIP_CODE = (By.XPATH, '//form/div/div[3]/input')
    CONTINUE_BUTTON = (By.ID, 'continue')
   
    def fill_form_and_checkout(self, firstname, lastname, zipcode):
        self.driver.find_element(*self.NAME).send_keys(firstname)
        self.driver.find_element(*self.LAST_NAME).send_keys(lastname)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zipcode)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

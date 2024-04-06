from selenium.webdriver.common.by import By
from Pages_POM_Singleton.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT = (By.XPATH, '//div/button[2]')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
   
    def click_checkout(self):
        button_checkout = self.driver.find_element(*self.CHECKOUT)
        button_checkout.click()
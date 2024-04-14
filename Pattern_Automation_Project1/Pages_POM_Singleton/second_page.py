from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from Pages_POM_Singleton.base_page import BasePage
from time import sleep

class ProductPage(BasePage, PageFactory):
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, 'btn_inventory')
    locators = {'add_to_cart_buttons':('CLASS_NAME','btn_inventory'), 
                'cart_badge':('CLASS_NAME','shopping_cart_badge'), 
                'specific_button':('CSS','button:nth-child(2)'),
                'tree_line_menu': ('CSS', 'body div div div div div div div div div button'),
                'logout_button': ('ID', 'logout_sidebar_link')}
    
    def add_to_cart(self, num_click=6):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        number_of_clicks = 0
    
        for button in buttons:
            button.click()
            number_of_clicks += 1
            if number_of_clicks == num_click:
                break

    def remove_item(self):
        self.specific_button.click_button()

    def click_cart(self):
        self.cart_badge.click_button()

    def logout(self):
        self.tree_line_menu.click_button()
        self.logout_button.click_button()
      
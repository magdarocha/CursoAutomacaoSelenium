from Pages_POM_Singleton.base_page import BasePage
from seleniumpagefactory.Pagefactory import PageFactory

class CartPage(BasePage, PageFactory):
    locators = {'checkout':('XPATH','//div/button[2]'), 
                'cart_badge':('CLASS_NAME','shopping_cart_badge')}
   
    def click_checkout(self):
        self.checkout.click_button()
        
from seleniumpagefactory.Pagefactory import PageFactory
from Pages_POM_Singleton.base_page import BasePage

class CheckoutPage(BasePage, PageFactory):
    locators = {'name':('CSS','div input:first-child'), 
                'last_name':('CSS','form div div:nth-child(2) input:first-child'), 
                'zip_code':('XPATH','//form/div/div[3]/input'),
                'continue_button': ('ID', 'continue')}
   
    def fill_form_and_checkout(self, firstname, lastname, zipcode):
        self.name.set_text(firstname)
        self.last_name.set_text(lastname)
        self.zip_code.set_text(zipcode)
        self.continue_button.click_button()
        

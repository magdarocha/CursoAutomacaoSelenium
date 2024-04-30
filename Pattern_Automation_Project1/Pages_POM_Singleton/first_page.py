from Pages_POM_Singleton.base_page import BasePage
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By


class LoginPage(BasePage, PageFactory):
    locators = {'user':('ID','user-name'),
                'password':('ID','password'), 
                'login_button':('ID', 'login-button')}
   
    
    def login(self, username, password):
        self.user.set_text(username)
        self.password.set_text(password)
        self.login_button.click_button()

    def clear_login(self):
        self.user.clear_text()
        self.password.clear_text()

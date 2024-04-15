from Pages_POM_Factory.base_page import BasePage
from seleniumpagefactory.Pagefactory import PageFactory

class InitialPage(BasePage, PageFactory):
    locators = {'username':('XPATH','//body /div /main /section /div /form /div /input'), 
                'search':('XPATH','//body /div /main /section /div /form /div /button')}
   
    def find_github_username(self, username):
        self.username.set_text(username)
        self.search.click_button()
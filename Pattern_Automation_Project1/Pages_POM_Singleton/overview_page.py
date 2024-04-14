from seleniumpagefactory.Pagefactory import PageFactory
from Pages_POM_Singleton.base_page import BasePage

class OverviewPage(BasePage, PageFactory):
    locators = {'finish_button':('ID','finish')}

    def click_finish(self):
        self.finish_button.click_button()
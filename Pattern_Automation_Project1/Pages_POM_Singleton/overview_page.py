from selenium.webdriver.common.by import By
from Pages_POM_Singleton.base_page import BasePage

class OverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, 'finish')
    

    def click_finish(self):
        self.wait_for_element(self.FINISH_BUTTON).click()
from POM.base_page import BasePage
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

#Nesta página o pagefactory não está a ser usado, por causa de querer retornar uma 
#lista de divs e o pagefactory não dá


class ResultPage(BasePage, PageFactory):
    locators = {'product_list_el':('XPATH', '//div[@data-view_id="grid"]//div[contains(@class,"product-layout")]')
                }

    def get_number_of_elements(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@data-view_id='grid']//div[contains(@class,'product-layout')]")
        item_list = len(elements)
        return item_list
    
    def click_product_element(self):
        self.product_list_el.click()

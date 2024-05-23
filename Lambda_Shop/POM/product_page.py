from POM.base_page import BasePage
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class ProductPage(BasePage, PageFactory):
    locators = {'brand_el':('XPATH', "//div[@id='entry_216826']//a"), 'availability_el':('XPATH', "//div[@id='entry_216826']//span[contains(@class, 'badge')]"), 'disabled_el':('XPATH', "//div[@id='entry_216842']//button[contains(@class, 'button-cart')]")
                }
    
    def read_brand_name(self):
        brand_text = self.brand_el.get_text()
        return brand_text
    
    def read_availability(self):
        availability_text = self.availability_el.get_text()
        return availability_text
    
    def check_disabled_button(self):
        disabled_button = self.disabled_el.get_text()
        return not (disabled_button == 'OUT OF STOCK')
    

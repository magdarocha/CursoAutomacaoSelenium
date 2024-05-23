from POM.base_page import BasePage
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from time import sleep

#Nesta página não funciona o locator da lupa para pesquisar, quando se tenta localizar e clicar na lupa
#o código falha. Apenas funciona com um submit pois o botão está dentro de um form


class HomePage(BasePage, PageFactory):
    locators = {'search_bar':('XPATH', '//div[@id="container"]//input[@name="search"]')}

    def search(self, product_name):
        sleep(2)
        self.search_bar.set_text(product_name)
        self.search_bar.submit()


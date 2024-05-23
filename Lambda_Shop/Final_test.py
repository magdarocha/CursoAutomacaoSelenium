import pytest
from POM.base_page import BasePage
from POM.home_page import HomePage
from POM.result_page import ResultPage
from POM.product_page import ProductPage
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from Singleton.Singleton import WebDriverSingleton

# Teste 1: Pesquisar um produto na barra de pesquisa e retornar resultados e 
#contar o número de resultados

@pytest.fixture()
def site_before_test():
    print("Begin Test")
    #driver = WebDriverSingleton.get_instance()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    BasePage(driver).go_to_site()
    yield driver
    print("End Test")

@pytest.fixture(scope="session", autouse=True)
def close_browser():
    yield
    #WebDriverSingleton.quit_instance()
    pass

def test_search_product(site_before_test):
    driver = site_before_test

    home_page = HomePage(driver)
    home_page.search('Iphone')

    result_page = ResultPage(driver)
    itens = result_page.get_number_of_elements()

    assert itens == 4

# Teste 2: Pesquisar um produto em particular, clicar nele e verificar a marca

def test_search_brand_product(site_before_test):
    driver = site_before_test

    home_page = HomePage(driver)
    home_page.search('Iphone')

    result_page = ResultPage(driver)
    result_page.click_product_element()

    brand_page = ProductPage(driver)
    brand = brand_page.read_brand_name()

    assert brand == 'Apple'



# Teste 3: Ao clicar num produto verificar a disponibilidade e se estiver disponivel deve 
# ser possivel adicionar ao carrinho

def test_availability_product(site_before_test):
    """Teste 1
    """
    driver = site_before_test

    home_page = HomePage(driver)
    home_page.search('Iphone')

    result_page = ResultPage(driver)
    result_page.click_product_element()

    brand_page = ProductPage(driver)
    availability = brand_page.read_availability()

    assert availability == 'Out Of Stock'

    enabled_button = brand_page.check_disabled_button()

    assert not enabled_button

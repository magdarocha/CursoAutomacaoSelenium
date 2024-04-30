import pytest
from Pages_POM_Factory.base_page import BasePage
from Pages_POM_Factory.initial_page import InitialPage
from selenium.webdriver.common.by import By
from Singleton.singleton import WebDriverSingleton
from time import time,sleep
import requests

@pytest.fixture()
def site_before_test():
    print("Begin Test")
    driver = WebDriverSingleton.get_instance()
    BasePage(driver).go_to_site()
    yield driver
    print("End Test")

@pytest.fixture(scope="session", autouse=True)
def close_browser():
    yield
    WebDriverSingleton.quit_instance()

# Colocar um user e testar se abre o github na zona inferior
def test_git_hub(site_before_test):
    driver = site_before_test

    name = 'magdarocha'

    user = InitialPage(driver)
    user.find_github_username(name)

    #Verifico se o elemento está na página e se é visivel
    sleep(2)
    follow = driver.find_element(By.XPATH, "//a[contains(@href,'github.com')]")
    link_to_github = follow.get_attribute('href')
    assert link_to_github == 'https://github.com/' + name.lower().strip().replace(' ','' )
    print(' O teste passou. O github user corresponde ao nome')

# Abrir um user git hub, obter o link do user e verificar 
#se é um site válido ou não, usar a biblioteca requests

def test_git_hub_002(site_before_test):
    driver = site_before_test

    name = 'magdarocha'

    user = InitialPage(driver)
    user.find_github_username(name)

    link = user.get_link()
    request_response = requests.head(link)
    status_code = request_response.status_code
    assert status_code != 200
    print('O teste passou, verifica-se que o site não abre')

# Verificar se o número de followers a que se refere em cima corresponde ao número da lista em baixo

def test_git_hub_003(site_before_test):
    driver = site_before_test

    name = 'magdarocha'

    user = InitialPage(driver)
    user.find_github_username(name)

    sleep(1)

    followers = user.get_followers()
    follows_list = str(user.get_followers_num_list())

    assert followers == follows_list
    print('O teste passou, a lista de followers tem o mesmo número de followers')

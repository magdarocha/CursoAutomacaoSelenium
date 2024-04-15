import pytest
from Pages_POM_Factory.base_page import BasePage
from Pages_POM_Factory.initial_page import InitialPage
from selenium.webdriver.common.by import By
from Singleton.singleton import WebDriverSingleton
from time import time,sleep

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

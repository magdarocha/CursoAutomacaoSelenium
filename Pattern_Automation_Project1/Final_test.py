import pytest
from selenium import webdriver
from Pages_POM_Singleton.base_page import BasePage
from Pages_POM_Singleton.first_page import LoginPage
from Pages_POM_Singleton.second_page import ProductPage
from Pages_POM_Singleton.cart_page import CartPage
from Pages_POM_Singleton.overview_page import OverviewPage
from Pages_POM_Singleton.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from time import time 

@pytest.fixture()
def site_before_test():
    print("Begin Test")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)

    BasePage(driver).go_to_site()

    yield driver
    print("End Test")
    driver.quit()

# Fluxo 1
def mtest_all_cicle(site_before_test):
    driver = site_before_test

    # login
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    products_el = driver.find_element(By.CLASS_NAME, 'title')

    #Verifico se o elemento está na página e se é visivel
    assert 'Products' == products_el.text and products_el.is_displayed()

    # Product
    product_page = ProductPage(driver)
    product_page.add_to_cart()

    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    badge_verification = int(cart_badge.text)

    assert badge_verification == 6

    product_page.remove_item()

    badge_verification = int(cart_badge.text)
    assert badge_verification == 5

    product_page.click_cart()

    # Cart

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Checkout

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form_and_checkout('teste', 'lasttest', '4000')

    # Overview

    overview_page = OverviewPage(driver)
    overview_page.click_finish()

    thank_you = driver.find_element(By.CLASS_NAME, 'complete-header')
    assert 'Thank you for your order!' == thank_you.text

#Fluxo 2
def mtest_login_and_logout(site_before_test):    
    driver = site_before_test

    # login
    login_page = LoginPage(driver)
    login_page.login('problem_user', 'secret_sauce')

    products_el = driver.find_element(By.CLASS_NAME, 'title')

    #Verifico se o elemento está na página e se é visivel
    assert 'Products' == products_el.text and products_el.is_displayed()

    logout_page = ProductPage(driver)
    logout_page.logout()

    login_el = driver.find_element(By.ID, 'login-button')
    assert 'Login' == login_el.get_attribute('value')

# Fluxo 3
def mtest_error(site_before_test):
    driver = site_before_test

    login_page = LoginPage(driver)
    login_page.login('locked_out_user', 'secret_sauce')

    message_error_el = driver.find_element(By.XPATH, '//h3')
    assert 'Epic sadface: Sorry, this user has been locked out.' == message_error_el.text

# Fluxo 4
def mtest_fluxo4(site_before_test):
    
    driver = site_before_test

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    products_el = driver.find_element(By.CLASS_NAME, 'title')

    #Verifico se o elemento está na página e se é visivel
    assert 'Products' == products_el.text and products_el.is_displayed()

    # Product
    product_page = ProductPage(driver)
    product_page.add_to_cart(2)

    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    badge_verification = int(cart_badge.text)

    assert badge_verification == 2

    product_page.remove_item()

    badge_verification = int(cart_badge.text)
    assert badge_verification == 1

# Fluxo 5 (orientado ao erro)
def test_login_time(site_before_test):
    
    driver = site_before_test

    initial_time = time()

    login_page = LoginPage(driver)
    login_page.login('performance_glitch_user', 'secret_sauce')
    
    products_el = driver.find_element(By.CLASS_NAME, 'title')
    assert 'Products' == products_el.text

    final_time = time() - initial_time - 2 # 2 sleeps do login
    assert final_time <= 2


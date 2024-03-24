# Foram realizados vários testes de forma incremental, para ir verificando os passos
# No final tem o teste que verifica tudo
# Fluxo 1

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#Função para abrir o site

def open_site():
    '''Esta função abre o site do saucedemo, maximiza e fecha'''
    site = webdriver.Chrome()
    site.get('https://www.saucedemo.com/')

    site.maximize_window()

    sleep(2)
    return site

# Função para fazer login no site

def login(site, username, password):
    '''Esta função faz login no site, coloca o user escolhido, a password e clica no login'''
    user_el = site.find_element(By.ID, 'user-name')
    user_el.send_keys(username)

    sleep(1)

    password_el = site.find_element(By.ID, 'password')
    password_el.send_keys(password)

    sleep(1)

    login_el = site.find_element(By.ID, 'login-button')
    login_el.click()

#Função para fazer logout

def logout(site):
    '''Esta função faz o logout'''
    tree_line_el = site.find_element(By.CSS_SELECTOR, 'body div div div div div div div div div button')
    tree_line_el.click()

    sleep(0.5)

    logout_el = site.find_element(By.ID, 'logout_sidebar_link')
    logout_el.click()


# Função para adicionar compras ao carro

def add_to_cart(site, num_click):
    '''Esta função permite adicionar itens no carro'''
    buttons = site.find_elements(By.CLASS_NAME, 'btn_inventory')
    number_of_clicks = 0
   
    for button in buttons:
        button.click()
        number_of_clicks += 1
        if number_of_clicks == num_click:
            break

# Função para clicar no carro

def click_cart(site):
    '''Esta função clica no carro'''
    cart_badge = site.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    cart_badge.click()

# Função para remover um produto do carro
def remove_item(site):
    '''Esta função remove um item do carro'''
    remove = site.find_element(By.CSS_SELECTOR, 'button:nth-child(2)')
    remove.click()

#Função para fazer o checkout e preencher os dados
def checkout(site, name, last_name, zip_code):
    '''Esta função faz todo o procedimento de checkout com os dados que a pessoa pretender'''
    button_checkout = site.find_element(By.XPATH, '//div/button[2]')
    button_checkout.click()

    name_el = site.find_element(By.CSS_SELECTOR, 'div input:first-child')
    name_el.send_keys(name)

    last_name_el = site.find_element(By.CSS_SELECTOR, 'form div div:nth-child(2) input:first-child')
    last_name_el.send_keys(last_name)

    zip_code_el = site.find_element(By.XPATH, '//form/div/div[3]/input')
    zip_code_el.send_keys(zip_code)

    continue_button = site.find_element(By.ID, 'continue')
    continue_button.click()


#Setup do teste
@pytest.fixture(scope='session')
def setup():
    print('Start')
    yield
    print('End')

#teste 1 login
def test_login(setup):
    '''Esta função faz o login com user e password e testa se a página abriu'''
    site = open_site()
    login(site, 'standard_user', 'secret_sauce')

    # Testar se o login foi feito com sucesso, pela verificação do icone do carrinho
    cart = site.find_element(By.CLASS_NAME, 'shopping_cart_link')

#teste 2 login e adicionar 6 produtos
def test_add_to_cart(setup):
    '''Esta função faz login e adiciona seis elementos'''
    site = open_site()
    login(site, 'standard_user', 'secret_sauce')

    add_to_cart(site, 6)

    cart_badge = site.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    badge_verification = int(cart_badge.text)

    assert badge_verification == 6

#teste 3 clicar no carro e verificar que entrou no carro
def test_click_on_cart(setup):
    site = open_site()
    login(site, 'standard_user', 'secret_sauce')

    add_to_cart(site, 6)
    click_cart(site)

    cart_page_title = site.find_element(By.CLASS_NAME, 'title')

#teste 4 login, adicionar 6 elementos, remover elemento e verificar que ficaram 5 elementos no carro

def test_remove_element(setup):
    '''Esta função abre o site,adicionar 6 elementos, remove 1 e verifica'''
    site = open_site()
    login(site, 'standard_user', 'secret_sauce')

    add_to_cart(site, 6)
    click_cart(site)
    remove_item(site)
    cart_badge = site.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    badge_verification = int(cart_badge.text)


    assert badge_verification == 5
    
#Teste Final 5, todos os passos anteriores+checkout+finish

def test_all_cicle(setup):
    '''Faz todo o circuito, login+adição de 6 elementos+remoção de 1+ checkout+finish e testa'''
    site = open_site()
    login(site, 'standard_user', 'secret_sauce')

    add_to_cart(site, 6)
    sleep(1)
    click_cart(site)
    sleep(1)
    remove_item(site)

    sleep(1)
    checkout(site, 'teste', 'apelidoteste', '4000')

    # Clicar no botão finish
    finish_button = site.find_element(By.ID, 'finish')
    finish_button.click()
    sleep(1)

    thank_you = site.find_element(By.CLASS_NAME, 'complete-header')
    assert 'Thank you for your order!' == thank_you.text


# Fluxo 2 - Fazer login
    
#Teste para verificar o login e logout    
def test_login_logout(setup):
    '''Esta função faz login e logout e verifica o funcionamento dos mesmos ao ver o botão de login'''
    site = open_site()
    login(site, 'problem_user', 'secret_sauce')

    sleep(1)

    logout(site)

    #Foi necessário colocar sleep no logout pois sem o mesmo o teste falhava, pela rapidez
    #e pelo facto da página não responder rápido o suficiente

    sleep(1)

    login_el = site.find_element(By.ID, 'login-button')

#Fluxo 3 - Fazer login com um utilizador que dá erro
    
def test_error(setup):
    '''Esta função abre e faz login com um utilizador que dá erro e verifica a mensagem de erro'''
    site = open_site()
    login(site, 'locked_out_user', 'secret_sauce')

    sleep(1)

    message_error_el = site.find_element(By.XPATH, '//h3')
    assert 'Epic sadface: Sorry, this user has been locked out.' == message_error_el.text


#Fluxo 4 - Fazer login, adicionar um item ao carro e fazer reset
def test_fluxo4(setup):
    
    site = open_site()
    login(site, 'standard_user', 'secret_sauce')

    add_to_cart(site, 2)
    sleep(1)
    remove_item(site)

    sleep(1)
    cart_badge = site.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    badge_verification = int(cart_badge.text)
    assert badge_verification == 1
    




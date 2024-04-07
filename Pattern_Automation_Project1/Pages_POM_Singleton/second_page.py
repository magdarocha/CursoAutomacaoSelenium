from selenium.webdriver.common.by import By
from Pages_POM_Singleton.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, 'btn_inventory')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    SPECIFIC_BUTTON = (By.CSS_SELECTOR, 'button:nth-child(2)')
    TREE_LINE_MENU = (By.CSS_SELECTOR, 'body div div div div div div div div div button')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')


    def add_to_cart(self, num_click=6):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        number_of_clicks = 0
    
        for button in buttons:
            button.click()
            number_of_clicks += 1
            if number_of_clicks == num_click:
                break

    def remove_item(self):
        remove = self.wait_for_element(self.SPECIFIC_BUTTON)
        remove.click()

    def click_cart(self):
        cart_badge = self.wait_for_element(self.CART_BADGE)
        cart_badge.click()

    def logout(self):
        tree_line_el = self.wait_for_element(self.TREE_LINE_MENU)
        tree_line_el.click()

        logout_el = self.driver.find_element(*self.LOGOUT_BUTTON)
        logout_el.click()
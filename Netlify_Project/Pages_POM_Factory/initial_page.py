from Pages_POM_Factory.base_page import BasePage
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class InitialPage(BasePage, PageFactory):
    locators = {'username':('XPATH','//body /div /main /section /div /form /div /input'), 
                'search':('XPATH','//body /div /main /section /div /form /div /button'),
                'link':('XPATH','//body/div/main/section[3]/div/article/div/a'),
                'followers':('XPATH', "//p[text()='followers']/preceding-sibling::h3"),
                'followers_list':('XPATH', "//div[@class='followers']/article")}
    
    FOLLOWERS = (By.XPATH, "//div[@class='followers']/article")
   
    def find_github_username(self, username):
        self.username.set_text(username)
        self.search.click_button()

    def get_link(self):
        link = self.link.getAttribute('href')
        return link
    
    def get_followers(self):
        followers_num = self.followers.get_text()
        return followers_num
    
    def get_followers_num_list(self):
        followers_nums = self.driver.find_elements(*self.FOLLOWERS)
        n = len(followers_nums)
        return n
    
        
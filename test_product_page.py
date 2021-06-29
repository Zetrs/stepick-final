import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
  @pytest.fixture(scope="function", autouse=True)
  def setup(self, browser):
    self.link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, self.link)
    page.open()
    page.go_to_login_page()
    email = str(time.time()) + "@fakemail.org"
    login_page = LoginPage(browser, browser.current_url)
    login_page.register_new_user(email, "SecPAss123")
    login_page.should_be_authorized_user()

  def test_guest_cant_see_success_message(self, browser):
    page = ProductPage(browser,self.link)
    page.open()
    page.should_not_be_success_message()
  def test_guest_can_add_product_to_basket(self, browser):
    page = ProductPage(browser,self.link)
    page.open()
    page.should_add2basket_chk()
    
''' 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
  page = ProductPage(browser,link)
  page.open()
  page.should_not_be_success_message_after_adding_product_to_basket()
  
 
def test_message_disappeared_after_adding_product_to_basket(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
  page = ProductPage(browser,link)
  page.open()
  page.success_message_disappeared_after_adding_product_to_basket()
'''

def test_guest_should_see_login_link_on_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(browser, link)
  page.open()
  page.should_be_login_link()
   
def test_guest_can_go_to_login_page_from_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(browser, link)
  page.open()
  page.go_to_login_page()
  login_page = LoginPage(browser, browser.current_url)
  login_page.should_be_login_page()
  
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(browser, link)
  page.open()
  page.go_to_basket_page()
  basket_page = BasketPage(browser, browser.current_url)
  basket_page.should_be_no_items_text()
  

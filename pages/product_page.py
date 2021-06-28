from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
  def should_add2basket(self):
    add2basket_link=self.browser.find_element(*ProductPageLocators.ADD_2_CARD_BTN)
    add2basket_link.click()

  def should_add2basket_chk(self):
    self.should_add2basket()
    self.solve_quiz_and_get_code()
    name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    basket_sum=self.browser.find_element(*ProductPageLocators.BASKET_SUM).text
    added_product_name=self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
    assert price == basket_sum, "Basket sum not eaqual to Product price"
    assert name == added_product_name, "Wrong product added to cart"
  
  def should_not_be_success_message_after_adding_product_to_basket(self):
    self.should_add2basket()
    self.solve_quiz_and_get_code()
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented after added to cart, but should not be"
  def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
  def success_message_disappeared_after_adding_product_to_basket(self):
    self.should_add2basket()
    self.solve_quiz_and_get_code()
    assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

  
    
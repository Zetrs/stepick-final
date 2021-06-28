from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
  def should_add2basket(self):
    add2basket_link=self.browser.find_element(*ProductPageLocators.ADD_2_CARD_BTN)
    add2basket_link.click()
    self.solve_quiz_and_get_code()
    name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    basket_sum=self.browser.find_element(*ProductPageLocators.BASKET_SUM).text
    added_product_name=self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
    assert price == basket_sum, "Basket sum not eaqual to Product price"
    assert name == added_product_name, "Wrong product added to cart"
    
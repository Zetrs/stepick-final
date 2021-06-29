from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
 def should_be_no_items_in_basket(self):
   assert self.is_not_element_present(*BasketPageLocators.ITEM_FORM), "Items form present, but should not be"
  
 def should_be_no_items_text(self):
   assert self.is_element_present(*BasketPageLocators.NO_ITEMS_TEXT), "No Items text is not presented"
  
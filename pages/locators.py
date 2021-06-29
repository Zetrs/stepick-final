from selenium.webdriver.common.by import By

class BasePageLocators():
  LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
  LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
  BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a.btn")
class MainPageLocators():
  LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators ():
  LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
  REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators ():
  ADD_2_CARD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
  PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
  PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
  BASKET_SUM = (By.CSS_SELECTOR, ".alert.alert-info .alertinner p strong")
  ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
  SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
class BasketPageLocators ():
  NO_ITEMS_TEXT = (By.CSS_SELECTOR, "#content_inner p")
  ITEM_FORM = (By.CSS_SELECTOR, "#basket_formset")

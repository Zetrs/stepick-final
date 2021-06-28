from selenium.webdriver.common.by import By

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

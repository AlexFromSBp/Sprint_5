from selenium.webdriver.common.by import By


class Registration:
    re_name = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    re_email = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    re_password = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    re_button_registration = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    re_error = (By.XPATH, ".//p[contains(@class, 'input__error')]")


class HomePage:
    hp_button_constructor = (By.XPATH, ".//p[text()='Конструктор']")
    hp_order_feed = (By.XPATH, ".//p[text()='Лента Заказов']")
    hp_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    hp_button_personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']")
    hp_sauces = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    hp_bride = (By.XPATH, ".//span[text()='Булки']/parent::*")
    hp_filling = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    hp_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    hp_button_order = (By.XPATH, ".//button[text()='Оформить заказ']")

    hp_text_s = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    hp_text_b = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"
    hp_text_f = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"
    hp_activ_page = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"

class ButtonEnter:
    be_login_text = (By.XPATH, ".//h2[text()='Вход']")
    be_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")
    be_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")
    be_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    be_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    be_element_with_login_text = (By.XPATH, ".//*[text() = 'Вход']")
    be_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")


class LKProfile:
    lk_out_button = (By.XPATH, "//nav//button[contains(text(), 'Выход')]")
    lk_info = (By.XPATH, ".//p[contains(text(),'Профиль')]")
    lk_history_shop = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

class LKEnter:
    lke_button_constructor = (By.XPATH, ".//p[text()='Конструктор']")
    lke_button_enter = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2]")
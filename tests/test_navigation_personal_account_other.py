import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locator import *
from data.urls import Urls
from data.data import PersonData
from selenium.webdriver.support import expected_conditions



class TestStellarBurgersCrossingPage:
    """def test_on_homepage_click_personal_account(self, driver): # Проверка успешного перехода Главная страница -> Личный кабинет
        driver.get(Urls.url_home_page)                                    # Загружаем Главную страницу
        driver.find_element(*HomePage.hp_button_personal_account).click() # Найти Личный кабинет ->Тап
                                                                          # Ждем загрузку
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_element_with_login_text))
                                                                          # Проверить, что url = url_personal_account
        assert driver.current_url == Urls.url_personal_account

    def test_from_personal_account_click_in_constructor(self, driver): # Проверка успешного перехода Личный кабинет -> Конструктор
        driver.get(Urls.url_personal_account)                             # Загружаем Личный кабинет
        driver.find_element(*LKEnter.lke_button_constructor).click()      # Найти Конструктор ->Тап
                                                                         # Проверить, что текущий url = url_home_page
        assert driver.current_url == Urls.url_home_page

    def test_from_personal_account_click_on_logo_stellar_burgers(self, driver): # Проверка успешного перехода Личный кабинет -> Главная страница
        driver.get(Urls.url_personal_account)                             # Загружаем Личный кабинет
        driver.find_element(*HomePage.hp_logo).click()                    # Найти логотип Stellar Burger ->Тап

                                                                         # Проверить, что текущий url = url_home_page
        assert driver.current_url == Urls.url_home_page"""

    def test_click_exit_from_personal_account(self, driver):  # Проверка успешного выхода из Личного кабинета
        driver.get(Urls.url_personal_account)  # Загружаем Личный кабинет
        # Заполняем данные
        driver.find_element(*ButtonEnter.be_email_field).send_keys(PersonData.login)
        driver.find_element(*ButtonEnter.be_password_field).send_keys(PersonData.password)

        driver.find_element(*ButtonEnter.be_login_button_any_forms).click()  # Найти кнопку Войти -> Тап. Ждем загрузку страницы
        WebDriverWait(driver, 8).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))

        assert driver.current_url == Urls.url_home_page

        """ driver.find_element(*HomePage.hp_button_personal_account).click()  # Загружаем Личный кабинет
        WebDriverWait(driver, 8).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == Urls.url_personal_account
        driver.find_element(*LKProfile.lk_out_button).click()  # Найти кнопку Выход -> Тап
        # Проверить, что на текущей странице есть кнопка Войти
        assert driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa").text == 'Войти'"""


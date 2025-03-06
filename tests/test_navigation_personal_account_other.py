import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locator import *
from data.urls import Urls
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersCrossingPage:

    def test_on_homepage_click_personal_account(self, driver): # Проверка успешного перехода Главная страница -> Личный кабинет
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
        assert driver.current_url == Urls.url_home_page

    def test_click_exit_from_personal_account(self, login, driver):  # Проверка успешного выхода из Личного кабинета

        driver = login

        driver.find_element(*HomePage.hp_button_personal_account).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LKProfile.lk_out_button))

        driver.find_element(*LKProfile.lk_out_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_login_button_any_forms))

        login_button = driver.find_element(*ButtonEnter.be_element_with_login_text)
        assert driver.current_url == Urls.url_personal_account and login_button.text == 'Вход'

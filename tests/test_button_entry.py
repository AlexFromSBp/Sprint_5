from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locator import *
from data.urls import Urls
from data.data import PersonData


class TestStellarBurgersButtonEntry:
    def test_auth_through_button_enter_on_homepage(self, driver): # Проверка успешной авторизации через кнопку Войти на главном экране
        driver.get(Urls.url_home_page)  # Загружаем Главную страницу
        driver.find_element(*HomePage.hp_auth).click()            # Найти кнопку Войти в аккаунт
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_login_text)) # Ждём загрузку страницы
                                                                 # Заполняем данные
        driver.find_element(*ButtonEnter.be_email_field).send_keys(PersonData.login)
        driver.find_element(*ButtonEnter.be_password_field).send_keys(PersonData.password)
                                                                 # Найти кнопку Войти -> Тап
        driver.find_element(*ButtonEnter.be_login_button_any_forms).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(HomePage.hp_button_order))  # Ждём загрузку страницы
                                                                 # Проверить, что текущий url = url_home_page
        assert driver.current_url == Urls.url_home_page

    def test_auth_through_personal_account(self, driver):        # Проверка успешной авторизации через Личный Кабинет
        driver.get(Urls.url_personal_account)                    # Загружаем Личный кабинет
        driver.find_element(*HomePage.hp_button_personal_account).click() # Переход на страницу Личный Кабинет
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_login_text)) # Ждём загрузку страницы
                                                                 # Заполняем данные
        driver.find_element(*ButtonEnter.be_email_field).send_keys(PersonData.login)
        driver.find_element(*ButtonEnter.be_password_field).send_keys(PersonData.password)

        driver.find_element(*ButtonEnter.be_login_button_any_forms).click() # Найти кнопку Войти -> Тап
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(HomePage.hp_button_order)) # Ждём загрузку страницы
                                                                 # Проверить, что текущий url = url_home_page
        assert driver.current_url == Urls.url_home_page

    def test_auth_through_button_enter_on_page_registration(self, driver): # Проверка успешной авторизации по кнопке Войти из окна регистрации
        driver.get(Urls.url_register)                            # Переход на страницу Регистрация

        driver.find_element(*ButtonEnter.be_login_text_with_href).click() # Найти кнопку Войти -> Тап
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_login_text)) # Ждём загрузку страницы
                                                                  # Заполняем данные
        driver.find_element(*ButtonEnter.be_email_field).send_keys(PersonData.login)
        driver.find_element(*ButtonEnter.be_password_field).send_keys(PersonData.password)
                                                                  # Найти кнопку Войти -> Тап
        driver.find_element(*ButtonEnter.be_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(HomePage.hp_button_order)) # Ждём загрузку страницы
                                                                  # Проверить, что текущий url = url_home_page
        assert driver.current_url == Urls.url_home_page

    def test_auth_through_button_enter_from_password_resert_form(self, driver): # Проверка успешной авторизации по кнопке Войти из окна Восстановление пароля
        driver.get(Urls.url_resert_password)                     # Переход на форму восстановления пароля
                                                                 # Найти кнопку Войти -> Тап
        driver.find_element(*AuthPassword.ap_login_text_with_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_login_text))
                                                                 # Заполняем данные
        driver.find_element(*ButtonEnter.be_email_field).send_keys(PersonData.login)
        driver.find_element(*ButtonEnter.be_password_field).send_keys(PersonData.password)
                                                                 # Найти кнопку Войти -> Тап
        driver.find_element(*ButtonEnter.be_login_button_any_forms).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(HomePage.hp_button_order))
                                                                 # Проверить, что текущий url = url_home_page
        assert driver.current_url == Urls.url_home_page

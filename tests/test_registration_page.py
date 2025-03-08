import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locator import *
from data.urls import Urls
from data.data import PersonData, VariosData


class TestStellarBurgersRegistration:

    def test_registration_page_successful_registration(self, driver): # Поля формы регистрации заполнены валидными данными
        driver.get(Urls.url_register) # Загружаем форму регистрации
        driver.find_element(*Registration.re_name).send_keys(VariosData.name) # Найти поле Имя и заполнить
        driver.find_element(*Registration.re_email).send_keys(VariosData.login) # Найти поле Email и заполнить
        driver.find_element(*Registration.re_password).send_keys(VariosData.password) # Найти поле Пароль и заполнить

        driver.find_element(*Registration.re_button_registration).click() # Тап по кнопке Зарегистрироваться. Ждем загрузку страницы
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(ButtonEnter.be_element_with_login_text))
                                                            # Проверить, что url соответствует Личному кабинету
        assert driver.current_url == Urls.url_personal_account

    @pytest.mark.parametrize('incorrect_password', ['q', 'qwert'])
    def test_registration_password_error(self, driver, incorrect_password): # В поле Пароль формы регистрации менее 5 символов
        driver.get(Urls.url_register) # Загружаем форму регистрации

        driver.find_element(*Registration.re_name).send_keys(VariosData.name) # Найти поле Имя и заполнить
        driver.find_element(*Registration.re_email).send_keys(VariosData.login) # Найти поле Email и заполнить
        driver.find_element(*Registration.re_password).send_keys(incorrect_password) # Найти поле Пароль и заполнить

        driver.find_element(*Registration.re_button_registration).click() # Тап по кнопке Зарегистрироваться. Ждем текст ошибки
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(Registration.re_error))

        error = driver.find_element(*Registration.re_error) # Текст ошибки сохранить в переменную

        assert error.text == 'Некорректный пароль' # И сравнить с ключом.

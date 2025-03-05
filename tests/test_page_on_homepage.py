from web_locators.locator import *
import pytest

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestStellarBurgersPageConstructor:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, driver, login): #Проверка перехода на вкладку Соусы

        driver = login

        driver.find_element(*HomePage.hp_button_constructor).click()
        driver.find_element(*HomePage.hp_sauces).click()

        h_sauce = driver.find_element(*HomePage.hp_text_s)

        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_filling_scroll_to_filling(self, driver, login): #Проверка перехода на вкладку Начинки

        driver = login

        driver.find_element(*HomePage.hp_button_constructor).click()
        driver.find_element(*HomePage.hp_filling).click()
        h_filling = driver.find_element(*HomePage.hp_text_f)

        assert h_filling.text == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(self, driver, login): #Проверка перехода на вкладку Булки

        driver = login

        driver.find_element(*HomePage.hp_button_constructor).click()
        driver.find_element(*HomePage.hp_filling).click()
        driver.find_element(*HomePage.hp_bride).click()

        h_ban = driver.find_element(*HomePage.hp_text_b)

        assert h_ban.text == 'Булки'

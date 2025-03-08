from web_locators.locator import *
import pytest


class TestStellarBurgersPageConstructor:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, driver, login): #Проверка перехода на вкладку Соусы

        driver = login

        driver.find_element(*HomePage.hp_button_constructor).click()
        driver.find_element(*HomePage.hp_sauces).click()

        h_sauce = driver.find_element(*HomePage.hp_activ_page).text
                                             # Проверить что секция Соусы активна
        assert h_sauce == 'Соусы'

    def test_constructor_go_to_filling_scroll_to_filling(self, driver, login): #Проверка перехода на вкладку Начинки

        driver = login

        driver.find_element(*HomePage.hp_button_constructor).click()
        driver.find_element(*HomePage.hp_filling).click()

        h_filling = driver.find_element(*HomePage.hp_activ_page).text
                                              # Проверить что секция Начинки активна
        assert h_filling == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(self, driver, login): #Проверка перехода на вкладку Булки

        driver = login

        driver.find_element(*HomePage.hp_button_constructor).click()
        driver.find_element(*HomePage.hp_filling).click()
        driver.find_element(*HomePage.hp_bride).click()

        h_ban = driver.find_element(*HomePage.hp_activ_page).text
                                             # Проверить что секция Булки активна
        assert h_ban == 'Булки'
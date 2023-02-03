# pytest -v -s --driver Chrome tests/test_rtk.py

import pytest
from pages.rostelecom import AuthPage, RegPage
from settings import letters_ru, valid_guest_data, random_password


class TestAuthPage:

    def test_auth_page_is_correct(self, web_browser):
        """ Проверка страницы авторизации: название страницы, таб по умолчанию,
        кликабельность полей и кнопок, "Личный кабинет". """
        page = AuthPage(web_browser)
        assert 'active' in page.phone_tab.get_attribute('class')
        assert page.phone.is_clickable()
        assert page.password.is_clickable()
        assert page.btn_login.is_clickable()
        assert page.registration_link.is_clickable()
        assert page.auth_title.get_text() == "Авторизация"
        assert page.logo_lk.get_text() == "Личный кабинет"

    @pytest.mark.xfail(reason="Таб выбора 'Номер' не соответсвует ожидаемым требованиям")
    def test_phone_tab(self, web_browser):
        """ Проверка названия таб выбора "Номер". """
        page = AuthPage(web_browser)
        assert page.phone_tab.get_text() == "Номер"

    @pytest.mark.xfail(reason='БАГ!!! Не переключается таб "Лицевой счёт" ')
    @pytest.mark.parametrize('tab', ['phone', 'email', 'login', 'ls'])
    def test_check_tab_active(self, web_browser, tab):
        """ Проверка автоматического переключения табов при вводе корректного
        значения в поле логина. """
        page = AuthPage(web_browser)
        page.phone.send_keys(valid_guest_data[tab])
        page.password.click()
        assert page.check_tabs.get_attribute('value').lower() == tab


class TestRegPage:

    @pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить'")
    def test_registration_page_and_continue_button(self, web_browser):
        """ Проверка названия полей и кнопки. """
        auth_page = AuthPage(web_browser)
        auth_page.registration_link.click()
        reg_page = RegPage(web_browser, auth_page.get_current_url())
        elements = reg_page.name_fields_text
        fields_name = ['Имя', 'Фамилия', 'Регион', 'E-mail или мобильный телефон',
                       'Пароль', 'Подтверждение пароля']
        for elem, name in zip(elements.get_text(), fields_name):
            assert elem == name
        assert reg_page.continue_button.get_text() == "Продолжить"

    @pytest.mark.parametrize('count', [2, 3, 30], ids='{} symbols'.format)
    def test_registration_page_correct_first_name(self, web_browser, count):
        """ Проверка регистрации с корректным значением в поле "Имя". """
        auth_page = AuthPage(web_browser)
        auth_page.registration_link.click()
        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name_field.send_keys(letters_ru(count))
        reg_page.last_name_field.send_keys(valid_guest_data['last_name'])
        reg_page.email_or_mobile_phone_field.send_keys(valid_guest_data['email'])
        [eye.click() for eye in reg_page.eyes_password]
        reg_page.password_field.send_keys(random_password)
        reg_page.password_confirmation_field.send_keys(random_password)
        reg_page.continue_button.click()
        assert reg_page.name_page.get_text() == "Подтверждение email"

    @pytest.mark.parametrize('count', [0, 1, 31], ids='{} symbols'.format)
    def test_registration_page_incorrect_first_name(self, web_browser, count):
        """ Проверка регистрации с некорректным значением в поле "Имя". """
        auth_page = AuthPage(web_browser)
        auth_page.registration_link.click()
        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name_field.send_keys(letters_ru(count))
        reg_page.last_name_field.send_keys(valid_guest_data['last_name'])
        reg_page.email_or_mobile_phone_field.send_keys(valid_guest_data['email'])
        [eye.click() for eye in reg_page.eyes_password]
        reg_page.password_field.send_keys(random_password)
        reg_page.password_confirmation_field.send_keys(random_password)
        reg_page.continue_button.click()
        reg_page.error_message_first_name.is_visible()
        assert reg_page.error_message_first_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    @pytest.mark.parametrize('count', [2, 3, 30], ids='{} symbols'.format)
    def test_registration_page_correct_last_name(self, web_browser, count):
        """ Проверка регистрации с корректным значением в поле "Фамилия". """
        auth_page = AuthPage(web_browser)
        auth_page.registration_link.click()
        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name_field.send_keys(valid_guest_data['first_name'])
        reg_page.last_name_field.send_keys(letters_ru(count))
        reg_page.email_or_mobile_phone_field.send_keys(valid_guest_data['email'])
        [eye.click() for eye in reg_page.eyes_password]
        reg_page.password_field.send_keys(random_password)
        reg_page.password_confirmation_field.send_keys(random_password)
        reg_page.continue_button.click()
        assert reg_page.name_page.get_text() == "Подтверждение email"

    @pytest.mark.parametrize('count', [0, 1, 31], ids='{} symbols'.format)
    def test_registration_page_incorrect_last_name(self, web_browser, count):
        """ Проверка регистрации с некорректным значением в поле "Фамилия". """
        auth_page = AuthPage(web_browser)
        auth_page.registration_link.click()
        reg_page = RegPage(web_browser, auth_page.get_current_url())
        reg_page.name_field.send_keys(valid_guest_data['first_name'])
        reg_page.last_name_field.send_keys(letters_ru(count))
        reg_page.email_or_mobile_phone_field.send_keys(valid_guest_data['email'])
        [eye.click() for eye in reg_page.eyes_password]
        reg_page.password_field.send_keys(random_password)
        reg_page.password_confirmation_field.send_keys(random_password)
        reg_page.continue_button.click()
        reg_page.error_message_last_name.is_visible()
        assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
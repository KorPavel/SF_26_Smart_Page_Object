import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    password = WebElement(id='password')
    btn_login = WebElement(id='kc-login')
    auth_title = WebElement(tag_name='h1')
    registration_link = WebElement(id='kc-register')
    phone_tab = WebElement(id='t-btn-tab-phone')
    logo_lk = WebElement(class_name='what-is__title')
    auth_form = WebElement(id='page-left')
    lk_form = WebElement(id='page-right')
    message_invalid_username_or_password = WebElement(id="form-error-message")
    the_element_forgot_the_password = WebElement(id="forgot_password")
    check_tabs = WebElement(name='tab_type')


class RegPage(WebPage):

    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    name_fields_text = ManyWebElements(class_name='rt-input__placeholder')
    continue_button = WebElement(name="register")

    name_page = WebElement(class_name='card-container__title')
    name_field = WebElement(name='firstName')
    last_name_field = WebElement(name='lastName')
    region_field = WebElement(css_selector='.rt-select [autocomplete="new-password"]')
    email_or_mobile_phone_field = WebElement(id='address')
    eyes_password = ManyWebElements(class_name='rt-eye-icon')
    password_field = WebElement(id='password')
    password_confirmation_field = WebElement(id='password-confirm')
    error_message_first_name = WebElement(css_selector='.rt-input-container--error .rt-input-container__meta--error')
    error_message_last_name = WebElement(css_selector='.rt-input-container .rt-input-container__meta--error')
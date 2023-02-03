#     python -m pytest -v --driver Chrome tests/test_auth_page.py

import pytest
from pages.auth_page import AuthPage

def test_authorisation(web_browser):

    page = AuthPage(web_browser)
    page.email.send_keys('sf_qap-96@mail.ru')
    page.password.send_keys('qwerty54321')
    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

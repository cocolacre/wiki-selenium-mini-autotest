import time, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from URLs import *
from locators import *
from wiki_creds import *


#https://en.wikipedia.org/wiki/Main_Page
def test_main_page(browser):
    browser.get(MAIN_PAGE_URL)
    try:
        main_page_logo = None
        main_page_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_LOGO_CSS_SELECTOR)))
    except TimeoutException as _e:
        print("Главный логотип Википедии не отобразился в браузере за корректное время!")
        raise

    try:
        main_page_link = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_PAGE_LINK_CSS_SELECTOR)))        
    except TimeoutException as _e:
        print("На главной страницу не найдена ссылка на саму себя!")
        raise

    try:
        main_page_talk_link = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_TALK_LINK_CSS_SELECTOR)))
    except TimeoutException as _e:
        print("Не найдена ссылка на обсуждение главной страницы Википедии!")
        raise

    try:
        main_page_dropdown_menu = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_MENU_DROPDOWN_CSS_SELECTOR)))
    except TimeoutException as _e:
        print("Не найдена кнопка с выпадающим меню слева!")
        raise

    try:
        powered_by_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_POWERED_BY_CSS_SELECTOR)))
    except TimeoutException as _e:
        print("Не найден powered-by логотип внизу страницы!")
        raise

    try:
        copyright_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_COPYRIGHT_ICO_CSS_SELECTOR)))
    except TimeoutException as _e:
        print("Wikimedia copyright logo not found! Hence, page was not loaded propely.")
        raise

    try:
        login_link_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)))
        login_link_element.click()
    except TimeoutException as _e:
        print("Не найдена кнопка перехода на страницу входа в учётную запись!")
        raise

    try:
        username_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_USERNAME_INPUT_CSS_SELECTOR)))
        username_input.clear()
        time.sleep(3)
        username_input.send_keys(wrong_username)
        time.sleep(5)
    except TimeoutException as _e:
        print("Не найдено поле для ввода имени пользователя!")
        raise

    try:
        password_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_PASSWORD_INPUT_CSS_SELECTOR)))
        #password_input.clear()
        #time.sleep(3)
        password_input.send_keys(wrong_password)
        time.sleep(5)
    except TimeoutException as _e:
        print("Не найдено поле для ввода пароля!")
        raise

    try:
        sign_in_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_SIGN_IN_BUTTON_CSS_SELECTOR)))
        sign_in_button.click()
    except TimeoutException as _e:
        print("Не найдена кнопка для подтверждения входа в учётную запись!")
        raise

    wrong_credentials_message_element = None
    try:
        wrong_credentials_message_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_INCORRECT_CREDS_MESSAGE_ELEMENT_CSS_SELECTOR)))
        assert "Incorrect username or password entered" in wrong_credentials_message_element.text.strip(), "Не найдено сообщение об ошибке, указывающее на то, что введены неправильные данные для входа!"
    except Exception as _e:
        print("Не найдено сообщение о неверных данных учётной записи!")
        raise


    try:
        username_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_USERNAME_INPUT_CSS_SELECTOR)))
        username_input.clear()
        time.sleep(3)
        username_input.send_keys(correct_username)
    except TimeoutException as _e:
        print("Не найдено поле для ввода имени пользователя!")
        raise

    try:
        password_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_PASSWORD_INPUT_CSS_SELECTOR)))
        #password_input.clear()
        time.sleep(3)
        password_input.send_keys(correct_password)
        time.sleep(3)
    except TimeoutException as _e:
        print("Не найдено поле для ввода пароля!")
        raise

    try:
        sign_in_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_SIGN_IN_BUTTON_CSS_SELECTOR)))
        sign_in_button.click()
    except TimeoutException as _e:
        print("Не найдена кнопка для подтверждения входа в учётную запись!")
        raise

    time.sleep(5)

    try:
        article_count = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_ARTICLE_COUNT_ELEMENT_CSS_SELECTOR)))
    except TimeoutException as _e:
        print("Браузер не отобразил счётчик статей на википедии, значит главная страница не загрузилась!")
        raise

    time.sleep(5)
    assert browser.current_url == 'https://en.wikipedia.org/wiki/Main_Page', "Браузер не перешёл на главную страницу!"

    try:
        dropdown_account_menu = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_DROPDOWN_ACCOUNT_MENU_CSS_SELECTOR)))
        dropdown_account_menu.click()
    except TimeoutException as _e:
        print("Кнопка выпадающего меню с кнопкой 'Log out' не найдена!")
        raise

    try:
        logout_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_DROPDOWN_LOGOUT_BUTTON_CSS_SELECTOR)))
        logout_button.click()
    except TimeoutException as _e:
        print("Не найдена кнопка 'Log out' !")
        raise

    try:
        login_link_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)))
        time.sleep(3)
    except TimeoutException as _e:
        print("Не найдена кнопка 'Log in', а значит не произошёл корректный выход из системы и перенаправление.")
        raise


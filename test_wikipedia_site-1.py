import time, sys
#import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from URLs import *
from locators import *
from wiki_creds import *


# ЭТОТ КОММЕНТИРОВАННЫЙ БЛОК - АРТЕФАКТ от предыдущего тест-дизайна.
#class TestMainPage(unittest.TestCase):
#    def setUp(self):
#        self.browser = ...
#    
#    def test_main_page(self):
#        # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №1)
#        self.assertIsNotNone(WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_PAGE_LINK_CSS_SELECTOR))))
#
#        # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №2)
#        self.assertIsNotNone(WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_TALK_LINK_CSS_SELECTOR))))


def test_main_page(browser):
    """
    ---------------------------------------------------------------------------
    Задание:
    - [1.1] Перейдите на главную страницу сайта https://en.wikipedia.org/wiki/Main_Page.
    - [1.2] Проверьте, что главная страница отображается корректно.
    - [1.3] Найдите и кликните на ссылку "Вход", чтобы перейти на страницу входа.
    - [1.4] На странице входа введите некорректные данные (например, "testtest" для имени пользователя и "testtest" для пароля) и нажмите кнопку входа.
    - [1.5] Проверьте, что отображается сообщение об ошибке, указывающее на то, что введены неправильные данные для входа ("Incorrect username or password entered").
    - [1.6] Введите корректные данные для входа и нажмите кнопку входа (correct_username = 'Cyberbioclown'; correct_password = 'e2718281828#').
    - [1.7] Проверьте, что вы успешно вошли в систему и были перенаправлены на главную страницу.
    - [1.8] Найдите и кликните на ссылку "Выход", чтобы выйти из системы.
    - [1.9] Проверьте, что вы успешно вышли из системы и присутствует кнопка "Log in".
    - [2.0] Опишите документацию для тестов, включая все предположения и ограничения, которые были сделаны в процессе создания тестов.

    ---------------------------------------------------------------------------
    ОГРАНИЧЕНИЯ И ПРЕДПОЛОЖЕНИЯ ДЛЯ ДАННОГО ТЕСТА.

    Предположения:
    - установлены Python 3.10, pytest==8.0.0 и иные python зависимости тех версий, с которыми велась разработка и запуск теста. Зависимости перечислены в requitements.txt
    - для формирования отчётов allure - корректно установлен allure в системе, а значит установлена Java (и прописана в PATH).
    - сайт Википедии (анлийская версия) доступен по сети с тестового стенда.
    - сервер Википедии не подвержен DDoS атаке и готов отдавать ответы на GET\POST запросы за обычные <2 секунды.
    - предполагается запуск в десктопной среде на ОС Windows 10 с разрешением экрана 1920х1080.
    - наличие зарегистрированной учётной записи с логином-паролем, указанным в качестве correct_username и correct_password.
    - в системе установлен Google Chrome свежей версии, как и подходящий chromedriver.
    - при запуске Chrome и chromedriver не используются куки и иные данные существующего пользователя - т.е. сессия "чистая".
    - поведение тестируемого сайта не меняется после разработки теста - не меняется вёрстка, аттрибуты и CSS-селекторы для проверяемых элементов страницы (указанных в locators.py)
    - т.к. в формулировке задаче не указаны критерии "корректности отображения страницы", то за таковые взята проверка presence_of_element произвольно выбранного ряда элементов. Предполагается, что совокупность этих проверок составляют признак корректности отображения сайта.

    Ограничения:
    - Не используется venv, не используется docker, что является существенным недостатком дизайна теста, например это может усложнить решение потенциальных проблем при развёртывании и запуске на, например, Linux системе без установленной виртуальной машины с Windows 10 (обратите внимание на путь до chromedriver.exe, корректный лишь в Windows системах).
    - тест проверяет лишь некоторые произвольно выбранные признаки (элементы DOM-дерева) корректности отображения главной страницы.
      Не осуществляется полной проверки всех признаков корректности отображения главной страницы англоязычной Википедии, поскольку (а) её структура может меняться и (б) она имеет разную структуру для разных языков.
    - тест проверяет наличие специфичного сообщения об ошибке при некорректных введённых учетных данных в форме авторизации, и не осуществляет более полную проверку корректной реакции сервера(сайта).
    - тест осуществляется лишь с Chrome, другие браузеры не используются, из-за чего невозможно отловить специфичные для других браузеров дефекты.
    - конкретно сайт Википедии с едва ли параметризуется по списку различных локалей\языков, потому как для каждого языкового портала принят свой дизайн главной страницы и других страниц (формы авторизации), включая свои соответствующие селекторы и элементы HTML страницы.
    - не приведена инструкция по установке Java. :)
    """ 

    # [1.1] Перейдите на главную страницу сайта https://en.wikipedia.org/wiki/Main_Page.
    browser.get(MAIN_PAGE_URL)
    try:
        main_page_logo = None
        main_page_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_LOGO_CSS_SELECTOR)))
    except TimeoutException as _e:
        extended_msg = "Главный логотип Википедии не отобразился в браузере за корректное время!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Главный логотип Википедии не отобразился в браузере за корректное время!")
        raise TimeoutException(full_msg) from _e

    # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №1)
    try:
        main_page_link = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_PAGE_LINK_CSS_SELECTOR)))        
    except TimeoutException as _e:
        extended_msg = "На главной страницу не найдена ссылка на саму себя!"
        # print("На главной страницу не найдена ссылка на саму себя!")
        full_msg = f"{extended_msg}, {str(_e)}"
        raise TimeoutException(full_msg) from _e

    # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №2)
    try:
        main_page_talk_link = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_TALK_LINK_CSS_SELECTOR)))
    except TimeoutException as _e:
        extended_msg = "Не найдена ссылка на обсуждение главной страницы Википедии!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена ссылка на обсуждение главной страницы Википедии!")
        raise TimeoutException(full_msg) from _e

    # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №3)
    try:
        main_page_dropdown_menu = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_MENU_DROPDOWN_CSS_SELECTOR)))
    except TimeoutException as _e:
        extended_msg = "Не найдена кнопка с выпадающим меню слева!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена кнопка с выпадающим меню слева!")
        raise TimeoutException(full_msg) from _e

    # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №4)
    try:
        powered_by_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_POWERED_BY_CSS_SELECTOR)))
    except TimeoutException as _e:
        extended_msg = "Не найден powered-by логотип внизу страницы!"
        full_msg = f"{extended_msg}, {str(_e)}"
        raise TimeoutException(full_msg) from _e

    # [1.2] Проверьте, что главная страница отображается корректно.(признак главной страницы №5)
    try:
        copyright_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_COPYRIGHT_ICO_CSS_SELECTOR)))
    except TimeoutException as _e:
        extended_msg = "Wikimedia copyright logo not found! Hence, page was not loaded propely."
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Wikimedia copyright logo not found! Hence, page was not loaded propely.")
        raise TimeoutException(full_msg) from _e

    # [1.2] Проверьте, что главная страница отображается корректно.
    # and [1.3] Найдите и кликните на ссылку "Вход", чтобы перейти на страницу входа.
    try:
        login_link_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)))
        # [1.3]
        login_link_element.click()
    except TimeoutException as _e:
        extended_msg = "Не найдена кнопка перехода на страницу входа в учётную запись!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена кнопка перехода на страницу входа в учётную запись!")
        raise TimeoutException(full_msg) from _e

    # [1.4] На странице входа введите некорректные данные (№1)
    # [1.4] ("testtest" для имени пользователя и "testtest" для пароля) и нажмите кнопку входа.
    try:
        username_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_USERNAME_INPUT_CSS_SELECTOR)))
        username_input.clear()
        time.sleep(3)
        username_input.send_keys(wrong_username)
        time.sleep(5)
    except TimeoutException as _e:
        extended_msg = "Не найдено поле для ввода имени пользователя!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдено поле для ввода имени пользователя!")
        raise TimeoutException(full_msg) from _e

    # [1.4] На странице входа введите некорректные данные (№2)
    try:
        password_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_PASSWORD_INPUT_CSS_SELECTOR)))
        #password_input.clear()
        #time.sleep(3)
        password_input.send_keys(wrong_password)
        time.sleep(5)
    except TimeoutException as _e:
        extended_msg = "Не найдено поле для ввода пароля!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдено поле для ввода пароля!")
        raise TimeoutException(full_msg) from _e

    # [1.4] На странице входа введите некорректные данные ... и нажмите кнопку входа (№3)
    try:
        sign_in_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_SIGN_IN_BUTTON_CSS_SELECTOR)))
        sign_in_button.click()
    except TimeoutException as _e:
        extended_msg = "Не найдена кнопка для подтверждения входа в учётную запись!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена кнопка для подтверждения входа в учётную запись!")
        raise TimeoutException(full_msg) from _e

    # [1.5] Проверьте, что отображается сообщение об ошибке,
    #  указывающее на то, что введены неправильные данные для входа
    # ("Incorrect username or password entered")
    wrong_credentials_message_element = None
    try:
        wrong_credentials_message_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_INCORRECT_CREDS_MESSAGE_ELEMENT_CSS_SELECTOR)))
        assert "Incorrect username or password entered" in wrong_credentials_message_element.text.strip(), "Не найдено сообщение об ошибке, указывающее на то, что введены неправильные данные для входа!"
    except Exception as _e:
        extended_msg = "Не найдено сообщение о неверных данных учётной записи!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдено сообщение о неверных данных учётной записи!")
        raise Exception(full_msg) from _e

    # [1.6] Введите корректные данные для входа и нажмите кнопку входа (№1)
    try: 
        username_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_USERNAME_INPUT_CSS_SELECTOR)))
        username_input.clear()
        time.sleep(3)
        username_input.send_keys(correct_username)
    except TimeoutException as _e:
        extended_msg = "Не найдено поле для ввода имени пользователя!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдено поле для ввода имени пользователя!")
        raise TimeoutException(full_msg) from _e


    # [1.6] Введите корректные данные для входа и нажмите кнопку входа (№2)
    try:
        password_input = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_PASSWORD_INPUT_CSS_SELECTOR)))
        #password_input.clear()
        time.sleep(3)
        password_input.send_keys(correct_password)
        time.sleep(3)
    except TimeoutException as _e:
        extended_msg = "Не найдено поле для ввода пароля!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдено поле для ввода пароля!")
        raise TimeoutException(full_msg) from _e


    # [1.6] Введите корректные данные для входа и нажмите кнопку входа (№3)
    try:
        sign_in_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_SIGN_IN_BUTTON_CSS_SELECTOR)))
        sign_in_button.click()
    except TimeoutException as _e:
        extended_msg = "Не найдена кнопка для подтверждения входа в учётную запись!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена кнопка для подтверждения входа в учётную запись!")
        raise TimeoutException(full_msg) from _e

    time.sleep(5)


    # [1.7] Проверьте, что вы успешно вошли в систему и были перенаправлены на главную страницу.
    try:
        # article_count is only visible on the [en]Wikipedia main page.
        article_count = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_ARTICLE_COUNT_ELEMENT_CSS_SELECTOR)))
    except TimeoutException as _e:
        extended_msg = "Браузер не отобразил счётчик статей на википедии, значит главная страница не загрузилась!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Браузер не отобразил счётчик статей на википедии, значит главная страница не загрузилась!")
        raise TimeoutException(full_msg) from _e


    time.sleep(5)
    # [1.7] Проверьте, что вы успешно вошли в систему и были перенаправлены на главную страницу.
    # [1.7] Double check that we are on the main page by directly reading browswe.current_url
    assert browser.current_url == 'https://en.wikipedia.org/wiki/Main_Page', "Браузер не перешёл на главную страницу!"


    # [1.8] Найдите и кликните на ссылку "Выход", чтобы выйти из системы (№1)
    # Accessing "Log out" button.
    try:
        dropdown_account_menu = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_DROPDOWN_ACCOUNT_MENU_CSS_SELECTOR)))
        dropdown_account_menu.click()
    except TimeoutException as _e:
        extended_msg = "Кнопка выпадающего меню с кнопкой 'Log out' не найдена!"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Кнопка выпадающего меню с кнопкой 'Log out' не найдена!")
        raise TimeoutException(full_msg) from _e

    # [1.8] Найдите и кликните на ссылку "Выход", чтобы выйти из системы (№2)
    try:
        logout_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_DROPDOWN_LOGOUT_BUTTON_CSS_SELECTOR)))
        logout_button.click()
    except TimeoutException as _e:
        extended_msg = "Не найдена кнопка 'Log out' !"
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена кнопка 'Log out' !")
        raise TimeoutException(full_msg) from _e

    # [1.9] Проверьте, что вы успешно вышли из системы и присутствует кнопка "Log in".
    try:
        login_link_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)))
        time.sleep(3)
    except TimeoutException as _e:
        extended_msg = "Не найдена кнопка 'Log in', а значит не произошёл корректный выход из системы и перенаправление."
        full_msg = f"{extended_msg}, {str(_e)}"
        # print("Не найдена кнопка 'Log in', а значит не произошёл корректный выход из системы и перенаправление.")
        raise TimeoutException(full_msg) from _e

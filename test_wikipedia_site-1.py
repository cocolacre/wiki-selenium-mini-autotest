import time, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service

from URLs import *
from locators import *
from wiki_creds import *


def test_main_page(browser):
    browser.get(MAIN_PAGE_URL)
    try:
        main_page_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_LOGO_CSS_SELECTOR)))
        assert main_page_logo, "Главный логотип Википедии не отобразился в браузере за корректное время!"
    except AssertionError as _ae:
        print(str(_ae))
        raise
    # except Exception as _e:
    #     print(str(_e))
    #     #make screenshot of a page.

    try:
        main_page_link = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_PAGE_LINK_CSS_SELECTOR)))
        assert main_page_link, "На главной страницу не найдена ссылка на саму себя!"
    except AssertionError as _ae:
        print(str(_ae))
        raise
    # except Exception as _e:
    #     print(str(_e))
    #     #make screenshot of a page.

    try:
        main_page_talk_link = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_TALK_LINK_CSS_SELECTOR)))
        assert main_page_talk_link, "Не найдена ссылка на обсуждение главной страницы Википедии!"
    except AssertionError as _ae:
        print(str(_ae))
        raise
    # except Exception as _e:
    #     print(str(_e))
    #     #make screenshot of a page.

    try:
        main_page_dropdown_menu = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_MAIN_MENU_DROPDOWN_CSS_SELECTOR)))
        assert main_page_dropdown_menu, "Не найдена кнопка с выпадающим меню слева!"
    except AssertionError as _ae:
        print(str(_ae))
        raise
    # except Exception as _e:
    #     print(str(_e))
    #     #make screenshot of a page.

    try:
        powered_by_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_POWERED_BY_CSS_SELECTOR)))
        assert powered_by_logo, "Не найден powered-by логотип внизу страницы!"
    except AssertionError as _ae:
        print(str(_ae))
        raise
    # except Exception as _e:
    #     print(str(_e))
    #     #make screenshot of a page.

    try:
        copyright_logo = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_COPYRIGHT_ICO_CSS_SELECTOR)))
        assert copyright_logo, "Wikimedia copyright logo not found! Hence, page was not loaded propely."
    except AssertionError as _ae:
        print(str(_ae))
        raise
    # except Exception as _e:
    #     print(str(_e))
    #     #make screenshot of a page.

    try: # здесь тест должен падать. (вынести в отдельный xfail-тест?)
        nonexistent_element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.badselector')))
        assert copyright_logo, "This test fail is NAMERENNIY."
    finally:
        print("THIS IS A FAILED TEST!")
        sys.exit()
    # except AssertionError as _ae:
    #     print(str(_ae))
    # raise

    

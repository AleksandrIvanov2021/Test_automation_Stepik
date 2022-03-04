import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # В командную строку передается параметр вида '--language=es'
    # По умолчанию передается параметр, включающий английский интерфейс в браузере
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')
    print("\nstart chrome browser for test..")
    options = Options()  # Инициализируются опции браузера
    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()



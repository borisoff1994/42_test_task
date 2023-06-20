import time
from locators import Locators
from selenium.webdriver.common.keys import Keys


def test_typing_speed(browser):
    # Данные для сравнения
    human_speed = 400
    good_result = 0

    # Переходим на сайт
    browser.get("https://klavogonki.ru")

    # Находим и нажимаем кнопку "Быстрый старт"
    time.sleep(2)
    browser.find_element(Locators.FAST_START).click()

    # Закрываем pop-up c правилами проведения
    time.sleep(2)
    browser.find_element(Locators.CLOSE_RULES_BTN).click()

    # Получаем текст, который нужно ввести
    time.sleep(2)
    text = browser.find_element(Locators.TEXT).text

    # Сплитим полученную строку в массив
    text_to_array = text.split()

    # Вводим слова из полученного текста
    for i in text_to_array:
        browser.find_element(Locators.INPUT_FIELD).send_keys(i)
        browser.send_keys(Keys.SPACE)
        time.sleep(0.1)

    # Ожидаем завершения игры и получаем результаты
    time.sleep(10)

    # Получаем скорость ввода и количество ошибок
    speed = int(browser.find_element(Locators.SPEED_VALUE).text)
    errors = int(browser.find_element(Locators.ERRORS_VALUE).text)

    # Проверяем, что скорость набора выше 400 зн/мин и нет ошибок
    assert speed > human_speed and errors == good_result, \
        f'Ваша скорость набора = {speed} зн/м, она меньше человеческой на {human_speed - speed}.' \
        f' Количество ошибок {errors}'

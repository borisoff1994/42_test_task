import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("browser")
def test_typing_speed(browser):
    # Данные для сравнения
    human_speed = 400
    good_result = 0

    # Переходим на сайт
    browser.get("https://klavogonki.ru")

    # Находим и нажимаем кнопку "Быстрый старт"
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[@id=\"index\"]/div[1]/div[2]/div/a[2]").click()

    # Закрываем pop-up c правилами проведения
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[@id=\"howtoplay\"]/div[2]/div/table/tbody/tr[2]/td[2]/p[5]/input").click()

    # Получаем текст, который нужно ввести
    time.sleep(2)
    text = browser.find_element(By.XPATH, "//*[@id=\"typetext\"]").text

    # Сплитим полученную строку в массив
    text_to_array = text.split()

    # Вводим слова из полученного текста
    for i in text_to_array:
        browser.find_element(By.XPATH, "//*[@id=\"inputtext\"]").send_keys(i)
        browser.send_keys(Keys.SPACE)
        time.sleep(0.1)

    # Ожидаем завершения игры и получаем результаты
    time.sleep(10)

    # Получаем скорость ввода и количество ошибок
    speed = int(browser.find_element(By.XPATH, "//*[@id=\"stats0\"]/div[2]/span[1]/span").text)
    errors = int(browser.find_element(By.XPATH, "//*[@id=\"stats0\"]/div[3]/span[1]/span").text)

    # Проверяем, что скорость набора выше 400 зн/мин и нет ошибок
    assert speed > human_speed and errors == good_result, \
        f'Ваша скорость набора = {speed} зн/м, она меньше человеческой на {human_speed - speed}.' \
        f' Количество ошибок {errors}'

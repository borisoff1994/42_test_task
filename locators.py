from selenium.webdriver.common.by import By


class Locators:
    FAST_START = (By.XPATH, "//*[@id=\"index\"]/div[1]/div[2]/div/a[2]")
    CLOSE_RULES_BTN = (By.XPATH, "//*[@id=\"howtoplay\"]/div[2]/div/table/tbody/tr[2]/td[2]/p[5]/input")
    TEXT = (By.XPATH, "//*[@id=\"typetext\"]")
    INPUT_FIELD = (By.XPATH, "//*[@id=\"inputtext\"]")
    SPEED_VALUE = (By.XPATH, "//*[@id=\"stats0\"]/div[2]/span[1]/span")
    ERRORS_VALUE = (By.XPATH, "//*[@id=\"stats0\"]/div[3]/span[1]/span")

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка пустой формы")
def test_empty_form_buy(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        buy_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить')]"
        )
        submit_button = driver.find_element(*buy_button_locator)
        submit_button.click()

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем селектор для сообщения об ошибке"):
        error_selector = ".input__box + .input__sub"
        error_element = driver.find_element(By.CSS_SELECTOR, error_selector)

    with allure.step("Сравниваем текст в сообщении об ошибке с реальным"):
        expected_text = "Неверный формат"
        actual_text = error_element.text
        assert expected_text == actual_text, (
            f"Ожидался текст ошибки '{expected_text}', но был получен '{actual_text}'")


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура (ищем иконку одобрения)")
def test_form_buy_input_valid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        buy_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить')]"
        )
        submit_button = driver.find_element(*buy_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем элемент-иконку одобрения"):
        check_element = driver.find_element(By.CSS_SELECTOR,
                                        ".icon.icon_size_m.icon_name_ok.icon_theme_alfa-on-color")
        assert check_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура (ищем текст одобрения)")
def test_form_buy_input_valid_card_number_by_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        buy_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить')]"
        )
        submit_button = driver.find_element(*buy_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Проверяем всплывающее уведомление об одобрении"):
        notification_locator = (
            By.XPATH,
            "//div[contains(@class, 'notification_status_ok')]"
            "[.//div[contains(@class, 'notification__content') "
            "and contains(., 'Операция одобрена банком.')]]"
        )
        error_notification = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(notification_locator)
        )
        title_element = error_notification.find_element(By.CLASS_NAME, "notification__title")
        assert title_element.text == "Успешно", f"Ожидался заголовок 'Успешно', но был '{title_element.text}'"


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура (ищем иконку отказа)")
def test_form_buy_input_invalid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        buy_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить')]"
        )
        submit_button = driver.find_element(*buy_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для отказа"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4442")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем элемент-иконку отказа"):
        check_element = driver.find_element(By.CSS_SELECTOR,
                                        ".icon.icon_size_m.icon_name_error.icon_theme_alfa-on-color")
        assert check_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура (ищем текст отказа)")
def test_form_buy_input_invalid_card_number_by_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        buy_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить')]"
        )
        submit_button = driver.find_element(*buy_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для отказа"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4442")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Проверяем всплывающее уведомление об отказе банка"):
        notification_locator = (
            By.XPATH,
            "//div[contains(@class, 'notification_status_error')]"
            "[.//div[contains(@class, 'notification__content') "
            "and contains(., 'Ошибка! Банк отказал в проведении операции.')]]"
        )
        error_notification = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(notification_locator)
        )
        title_element = error_notification.find_element(By.CLASS_NAME, "notification__title")
        assert title_element.text == "Ошибка", f"Ожидался заголовок 'Ошибка', но был '{title_element.text}'"


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем иконку одобрения)")
def test_form_credit_input_valid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем элемент-иконку одобрения"):
        check_element = driver.find_element(By.CSS_SELECTOR,
                                            ".icon.icon_size_m.icon_name_ok.icon_theme_alfa-on-color")
        assert check_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем текст одобрения)")
def test_form_credit_valid_card_number_by_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Проверяем всплывающее уведомление об одобрении"):
        notification_locator = (
            By.XPATH,
            "//div[contains(@class, 'notification_status_ok')]"
            "[.//div[contains(@class, 'notification__content') "
            "and contains(., 'Операция одобрена банком.')]]"
        )
        error_notification = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(notification_locator)
        )
        title_element = error_notification.find_element(By.CLASS_NAME, "notification__title")
        assert title_element.text == "Успешно", f"Ожидался заголовок 'Успешно', но был '{title_element.text}'"


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем иконку отказа)")
def test_form_credit_input_invalid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для отказа"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем элемент-иконку отказа"):
        check_element = driver.find_element(By.CSS_SELECTOR,
                                        ".icon.icon_size_m.icon_name_error.icon_theme_alfa-on-color")
        assert check_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем текст отказа)")
def test_form_credit_invalid_card_number_by_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для отказа"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4442")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Проверяем всплывающее уведомление об отказе банка"):
        notification_locator = (
            By.XPATH,
            "//div[contains(@class, 'notification_status_error')]"
            "[.//div[contains(@class, 'notification__content') "
            "and contains(., 'Ошибка! Банк отказал в проведении операции.')]]"
        )
        error_notification = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(notification_locator)
        )
        title_element = error_notification.find_element(By.CLASS_NAME, "notification__title")
        assert title_element.text == "Ошибка", f"Ожидался заголовок 'Ошибка', но был '{title_element.text}'"


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы со слишком большим сроком действия карты")
def test_form_invalid_duration_card (driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("99")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем сообщение об ошибке"):
        error_element = driver.find_element(By.XPATH, "//*[text()='Неверно указан срок действия карты']")
        assert error_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы с истёкшим сроком действия карты")
def test_form_expired_card (driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим валидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("08")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("22")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем сообщение об ошибке"):
        error_element = driver.find_element(By.XPATH, "//*[text()='Истёк срок действия карты']")
        assert error_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы с невалидным значением в поле 'Месяц'")
def test_form_invalid_month_value (driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        credit_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_theme_alfa-on-white') and contains(., 'Купить в кредит')]"
        )
        submit_button = driver.find_element(*credit_button_locator)
        submit_button.click()

    with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
        input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        input_card.clear()
        input_card.send_keys("4444 4444 4444 4441")

    with allure.step("Вводим невалидное значение в поле 'Месяц'"):
        input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
        input_month.clear()
        input_month.send_keys("99")

    with allure.step("Вводим валидное значение в поле 'Год'"):
        input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
        input_year.clear()
        input_year.send_keys("26")

    with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
        input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
        input_cvc.clear()
        input_cvc.send_keys("999")

    with allure.step("Вводим валидное значение в поле 'Владелец'"):
        name_locator = (By.XPATH, "//span[contains(@class, 'input')][.//text()='Владелец']//input")
        input_name = driver.find_element(*name_locator)
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        continue_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'button_view_extra') and contains(., 'Продолжить')]"
        )
        submit_button = driver.find_element(*continue_button_locator)
        submit_button.click()

    with allure.step("Ищем селектор для сообщения об ошибке"):
        error_selector = ".input__box + .input__sub"
        error_element = driver.find_element(By.CSS_SELECTOR, error_selector)

    with allure.step("Сравниваем текст в сообщении об ошибке с реальным"):
        expected_text = "Неверно указан срок действия карты"
        actual_text = error_element.text
        assert expected_text == actual_text, (
            f"Ожидался текст ошибки '{expected_text}', но был получен '{actual_text}'")
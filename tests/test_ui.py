import allure
from selenium.webdriver.common.by import By

# @allure.epic("QA_Diplom")
# @allure.feature("Симуляция действий пользователя с помощью Selenium")
# @allure.story("Отправка пустой формы")
# def test_empty_form_buy(driver, app_url):
#     with allure.step("Загрузка стартовой страницы"):
#         driver.get(app_url)
#
#     with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR, ".button.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Нажимаем на кнопку 'Продолжить'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                         ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Ищем селектор для сообщения об ошибке"):
#         error_selector = ".input__top + .input__sub"
#         error_element = driver.find_element(By.CSS_SELECTOR, error_selector)
#
#     with allure.step("Сравниваем текст в сообщении об ошибке с реальным"):
#         expected_text = "Неверный формат"
#         actual_text = error_element.text
#         assert expected_text in actual_text, (
#             f"Ожидался текст ошибки '{expected_text}', но был получен '{actual_text}'")

@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура (ищем иконку одобрения)")
def test_form_buy_input_valid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR, ".button.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
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
        submit_button = driver.find_element(By.CSS_SELECTOR, ".button.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
        submit_button.click()

    with allure.step("Ищем текст сообщения об одобрении"):
        check_title = driver.find_element(By.CSS_SELECTOR, ".notification__content")
        assert "Операция одобрена банком." in check_title.text

@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура (ищем иконку отказа)")
def test_form_buy_input_invalid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR, ".button.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
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
        submit_button = driver.find_element(By.CSS_SELECTOR, ".button.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
        submit_button.click()

    with allure.step("Ищем текст сообщения об отказе"):
        check_title = driver.find_element(By.CSS_SELECTOR, ".notification__content")
        assert "Операция одобрена банком." in check_title.text

@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем иконку одобрения)")
def test_form_credit_input_valid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                        ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
        submit_button.click()

    with allure.step("Ищем элемент-иконку одобрения"):
        check_element = driver.find_element(By.CSS_SELECTOR,
                                            ".icon.icon_size_m.icon_name_ok.icon_theme_alfa-on-color")
        assert check_element

@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем текст одобрения)")
def test_form_buy_credit_valid_card_number_by_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
        submit_button.click()

    with allure.step("Ищем текст сообщения об одобрении"):
        check_title = driver.find_element(By.CSS_SELECTOR, ".notification__content")
        assert "Ошибка! Банк отказал в проведении операции." in check_title.text

@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем иконку отказа)")
def test_form_credit_input_invalid_card_number_by_element(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
        submit_button.click()

    with allure.step("Ищем элемент-иконку отказа"):
        check_element = driver.find_element(By.CSS_SELECTOR,
                                        ".icon.icon_size_m.icon_name_error.icon_theme_alfa-on-color")
        assert check_element


@allure.epic("QA_Diplom")
@allure.feature("Симуляция действий пользователя с помощью Selenium")
@allure.story("Отправка заполненной формы для покупки тура в кредит (ищем текст отказа)")
def test_form_buy_credit_invalid_card_number_by_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)

    with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
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
        input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
        input_name.clear()
        input_name.send_keys("Ivan Ivanov")

    with allure.step("Нажимаем на кнопку 'Продолжить'"):
        submit_button = driver.find_element(By.CSS_SELECTOR,
                                            ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
        submit_button.click()

    with allure.step("Ищем текст сообщения об отказе"):
        check_title = driver.find_element(By.CSS_SELECTOR, ".notification__content")
        assert "Ошибка! Банк отказал в проведении операции." in check_title.text


# @allure.epic("QA_Diplom")
# @allure.feature("Симуляция действий пользователя с помощью Selenium")
# @allure.story("Отправка заполненной формы со слишком большим сроком действия карты")
# def test_form_buy_credit_invalid_duration_card (driver, app_url):
#     with allure.step("Загрузка стартовой страницы"):
#         driver.get(app_url)
#
#     with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                             ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
#         input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
#         input_card.clear()
#         input_card.send_keys("4444 4444 4444 4441")
#
#     with allure.step("Вводим валидное значение в поле 'Месяц'"):
#         input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
#         input_month.clear()
#         input_month.send_keys("08")
#
#     with allure.step("Вводим валидное значение в поле 'Год'"):
#         input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
#         input_year.clear()
#         input_year.send_keys("99")
#
#     with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
#         input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
#         input_cvc.clear()
#         input_cvc.send_keys("999")
#
#     with allure.step("Вводим валидное значение в поле 'Владелец'"):
#         input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
#         input_name.clear()
#         input_name.send_keys("Ivan Ivanov")
#
#     with allure.step("Нажимаем на кнопку 'Продолжить'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                             ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Ищем сообщение об ошибке"):
#         error_element = driver.find_element(By.XPATH, "//*[text()='Неверно указан срок действия карты']")
#         assert error_element


# @allure.epic("QA_Diplom")
# @allure.feature("Симуляция действий пользователя с помощью Selenium")
# @allure.story("Отправка заполненной формы с истёкшим сроком действия карты")
# def test_form_buy_credit_expired_card (driver, app_url):
#     with allure.step("Загрузка стартовой страницы"):
#         driver.get(app_url)
#
#     with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                             ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
#         input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
#         input_card.clear()
#         input_card.send_keys("4444 4444 4444 4441")
#
#     with allure.step("Вводим валидное значение в поле 'Месяц'"):
#         input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
#         input_month.clear()
#         input_month.send_keys("08")
#
#     with allure.step("Вводим валидное значение в поле 'Год'"):
#         input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
#         input_year.clear()
#         input_year.send_keys("22")
#
#     with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
#         input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
#         input_cvc.clear()
#         input_cvc.send_keys("999")
#
#     with allure.step("Вводим валидное значение в поле 'Владелец'"):
#         input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
#         input_name.clear()
#         input_name.send_keys("Ivan Ivanov")
#
#     with allure.step("Нажимаем на кнопку 'Продолжить'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                             ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Ищем сообщение об ошибке"):
#         error_element = driver.find_element(By.XPATH, "//*[text()='Истёк срок действия карты']")
#         assert error_element


# @allure.epic("QA_Diplom")
# @allure.feature("Симуляция действий пользователя с помощью Selenium")
# @allure.story("Отправка заполненной формы с невалидным значением в поле 'Месяц'")
# def test_form_buy_credit_invalid_duration_card (driver, app_url):
#     with allure.step("Загрузка стартовой страницы"):
#         driver.get(app_url)
#
#     with allure.step("Вызываем форму заполнения данных с помощью кнопки 'Купить в кредит'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                             ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Вводим валидный номер карты в поле 'Номер карты' для одобрения"):
#         input_card = driver.find_element(By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
#         input_card.clear()
#         input_card.send_keys("4444 4444 4444 4441")
#
#     with allure.step("Вводим валидное значение в поле 'Месяц'"):
#         input_month = driver.find_element(By.CSS_SELECTOR, "input[placeholder='08']")
#         input_month.clear()
#         input_month.send_keys("99")
#
#     with allure.step("Вводим валидное значение в поле 'Год'"):
#         input_year = driver.find_element(By.CSS_SELECTOR, "input[placeholder='22']")
#         input_year.clear()
#         input_year.send_keys("26")
#
#     with allure.step("Вводим валидное значение в поле 'CVC/CVV'"):
#         input_cvc = driver.find_element(By.CSS_SELECTOR, "input[placeholder='999']")
#         input_cvc.clear()
#         input_cvc.send_keys("999")
#
#     with allure.step("Вводим валидное значение в поле 'Владелец'"):
#         input_name = driver.find_element(By.CSS_SELECTOR, ".input__box input")
#         input_name.clear()
#         input_name.send_keys("Ivan Ivanov")
#
#     with allure.step("Нажимаем на кнопку 'Продолжить'"):
#         submit_button = driver.find_element(By.CSS_SELECTOR,
#                                             ".button.button_view_extra.button_size_m.button_theme_alfa-on-white")
#         submit_button.click()
#
#     with allure.step("Ищем сообщение об ошибке"):
#         error_element = driver.find_element(By.XPATH, "//span[@class='input__sub']")
#         assert "Неверно указан срок действия карты" in error_element.text
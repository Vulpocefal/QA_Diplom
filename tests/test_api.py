import allure


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Покупка тура по тестовой карте с номером для одобрения")
def test_valid_pay (api_session, app_url):
    with allure.step("JSON-файл с валидными данными"):
        payload = {
            "number": "4444 4444 4444 4441",
            "year": "26",
            "month": "08",
            "holder": "Ivan Ivanov",
            "cvc": "999"
        }

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/pay", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 200


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Покупка тура в кредит по тестовой карте с номером для одобрения")
def test_valid_credit (api_session, app_url):
    with allure.step("JSON-файл с валидными данными"):
        payload = {
            "number": "4444 4444 4444 4441",
            "year": "26",
            "month": "08",
            "holder": "Ivan Ivanov",
            "cvc": "999"
        }

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/credit", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 200


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Покупка тура по тестовой карте с номером для отказа")
def test_invalid_pay (api_session, app_url):
    with allure.step("JSON-файл с валидными данными"):
        payload = {
            "number": "4444 4444 4444 4442",
            "year": "26",
            "month": "08",
            "holder": "Ivan Ivanov",
            "cvc": "999"
        }

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/pay", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 400

    with allure.step("Получение ответа на post-запрос"):
        error_message = response.json().get("message")
    with allure.step("Сравнение ожидаемого ответа с реальным"):
        assert error_message == "Ошибка! Банк отказал в проведении операции.", \
            f"Ожидали сообщение 'Ошибка! Банк отказал в проведении операции.', получили '{error_message}'"


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Покупка тура в кредит по тестовой карте с номером для отказа")
def test_invalid_credit (api_session, app_url):
    with allure.step("JSON-файл с валидными данными"):
        payload = {
            "number": "4444 4444 4444 4442",
            "year": "26",
            "month": "08",
            "holder": "Ivan Ivanov",
            "cvc": "999"
        }

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/credit", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 400

    with allure.step("Получение ответа на post-запрос"):
        error_message = response.json().get("message")
    with allure.step("Сравнение ожидаемого ответа с реальным"):
        assert error_message == "Ошибка! Банк отказал в проведении операции.", \
            f"Ожидали сообщение 'Ошибка! Банк отказал в проведении операции.', получили '{error_message}'"


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Отправка пустого JSON-файла при покупке тура в кредит")
def test_empty_form_credit (api_session, app_url):
    with allure.step("Пустой JSON-файл"):
        payload = {}

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/credit", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 400

    with allure.step("Получение ответа на post-запрос"):
        error_message = response.json().get("message")
    with allure.step("Сравнение ожидаемого ответа с реальным"):
        assert error_message == "Заполните форму", \
            f"Ожидали сообщение 'Заполните форму', получили '{error_message}'"


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Отправка пустого JSON-файла при покупке тура")
def test_empty_form_pay (api_session, app_url):
    with allure.step("Пустой JSON-файл"):
        payload = {}

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/pay", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 400

    with allure.step("Получение ответа на post-запрос"):
        error_message = response.json().get("message")
    with allure.step("Сравнение ожидаемого ответа с реальным"):
        assert error_message == "Заполните форму", \
            f"Ожидали сообщение 'Заполните форму', получили '{error_message}'"


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Отправка невалидного JSON-файла при покупке тура в кредит")
def test_empty_form_credit (api_session, app_url):
    with allure.step("Невалидный JSON-файл"):
        payload = {
            "number": "qwerty",
            "year": "qwerty",
            "month": "qwerty",
            "holder": "123456790",
            "cvc": "qwerty"
        }

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/credit", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 400

    with allure.step("Получение ответа на post-запрос"):
        error_message = response.json().get("message")
    with allure.step("Сравнение ожидаемого ответа с реальным"):
        assert error_message == "Invalid JSON", \
            f"Ожидали сообщение 'Invalid JSON', получили '{error_message}'"


@allure.epic("QA_Diplom")
@allure.feature("API-запросы")
@allure.story("Отправка невалидного JSON-файла при покупке тура")
def test_empty_form_pay (api_session, app_url):
    with allure.step("Невалидный JSON-файл"):
        payload = {
            "number": "qwerty",
            "year": "qwerty",
            "month": "qwerty",
            "holder": "123456790",
            "cvc": "qwerty"
        }

    with allure.step("Создание post-запроса"):
        response = api_session.post(f"{app_url}/api/v1/pay", params=payload)
    with allure.step("Сравнение ожидаемого статус-кода ответа с реальным"):
        assert response.status_code == 400

    with allure.step("Получение ответа на post-запрос"):
        error_message = response.json().get("message")
    with allure.step("Сравнение ожидаемого ответа с реальным"):
        assert error_message == "Invalid JSON", \
            f"Ожидали сообщение 'Invalid JSON', получили '{error_message}'"
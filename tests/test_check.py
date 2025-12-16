import allure


@allure.epic("QA_Diplom")
@allure.feature("Загрузка тестовой сборки с помощью Docker")
@allure.story("Проверочный тест")
def test_page_title(driver, app_url):
    with allure.step("Загрузка стартовой страницы"):
        driver.get(app_url)
    with allure.step("Название страницы"):
        assert "AQA: Заявка на карту" in driver.title
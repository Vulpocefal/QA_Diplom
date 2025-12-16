# Фреймворк автоматизации тестирования [Название вашего проекта]

Этот репозиторий содержит UI-тесты для веб-сервиса "Путешествие дня", реализованные с использованием Python, Selenium и Docker.

---

## Используемый стек технологий

|Технология|Описание|
|:-|:-|
|Python|Основной язык разработки|
|Selenium|Для автоматизации взаимодействия с веб-браузером|
|Docker/Docker Compose|Для создания изолированного, воспроизводимого тестового окружения (браузеры, хабы)|
|Allure Report|Для генерации красивых и информативных отчетов о прохождении тестов|
|Pytest|Тестовый фреймворк для запуска тестов|

## Требования к окружению

Для запуска тестов локально вам потребуется установленный Docker и Docker Compose.

## Установка и запуск тестов

1. Для установки необходимых модулей используйте команду "pip install -r requirements.txt"
2. Для запуска тестов без использования модуля Allure Report используйте команду "pytest tests"

## Просмотр отчетов Allure Report

//здесь будет описание действий для генерации и просмотра отчетов с помощью Allure Report//

## Структура проекта

//здесь будет описание структуры проекта (иерархия папок, что в них и т.д.)//



//Это всё, что удалось выудить из БД (скопировал из docker exec. 
//DBeaver при запуске скрипта пишет, что нет соединения, хотя базу видит и к ней подключается).
//Порт поменял на 5433:5432

su postgres
postgres@2ebe98739f2e:/$ psql
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  role "postgres" does not exist
postgres@2ebe98739f2e:/$ psql -U aqa_user
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "aqa_user" does not exist
postgres@2ebe98739f2e:/$ psql -U aqa_user -d aqa_db
psql (13.23 (Debian 13.23-1.pgdg13+1))
Type "help" for help.

aqa_db=# \ll
invalid command \ll
Try \? for help.
aqa_db=# \?
aqa_db=# \dt
                 List of relations
 Schema |         Name          | Type  |  Owner   
--------+-----------------------+-------+----------
 public | credit_request_entity | table | aqa_user
 public | order_entity          | table | aqa_user
 public | payment_entity        | table | aqa_user
(3 rows)

aqa_db=# select * from order_entity;
 id | created | credit_id | payment_id 
----+---------+-----------+------------
(0 rows)

aqa_db=# select * from payment_entity;
 id | amount | created | status | transaction_id 
----+--------+---------+--------+----------------
(0 rows)

aqa_db=# select * from credit_request_entity;
 id | bank_id | created | status 
----+---------+---------+--------
(0 rows)

aqa_db=# \dd
         Object descriptions
 Schema | Name | Object | Description 
--------+------+--------+-------------
(0 rows)

aqa_db=# \?
aqa_db=#
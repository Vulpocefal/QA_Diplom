-- "Показывает таблицу order_entity"
SELECT * FROM order_entity LIMIT 10;

-- "Показывает таблицу credit_request_entity"
SELECT * FROM credit_request_entity LIMIT 10;

-- "Показывает таблицу payment_entity"
SELECT * FROM payment_entity LIMIT 10;

-- "Показывает одобренные запросы из таблицы payment_entity"
SELECT * FROM payment_entity
WHERE status = 'APPROVED'
LIMIT 10;

-- "Показывает отклонённые запросы из таблицы payment_entity"
SELECT * FROM payment_entity
WHERE status = 'DECLINED'
LIMIT 10;

-- "Показывает одобренные запросы из таблицы credit_request_entity"
SELECT * FROM credit_request_entity
WHERE status = 'APPROVED'
LIMIT 10;

-- "Показывает отклонённые запросы из таблицы credit_request_entity"
SELECT * FROM credit_request_entity
WHERE status = 'DECLINED'
LIMIT 10;
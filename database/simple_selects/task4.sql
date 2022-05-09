-- 1. среднюю сумму всех завершенных сделок

SELECT avg(total) FROM orders WHERE order_status_order_status_id=4;

-- 2. вывести максимальную сумму сделки за 3 квартал 2020


SELECT max(total) FROM orders WHERE updated_at BETWEEN '2020-07-01' and '2020-09-30' and order_status_order_status_id=4;

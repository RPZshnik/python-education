-- 1. Продукты, цена которых больше 80.00 и меньше или равно 150.00

SELECT * FROM products
WHERE price BETWEEN 80 and 150;

SELECT * FROM products
WHERE price > 80 and price <= 150;

-- 2. заказы совершенные после 01.10.2020 (поле created_at)

SELECT * FROM orders
WHERE created_at >'2020-10-01'::date;

-- 3. заказы полученные за первое полугодие 2020 года

SELECT * FROM order
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

SELECT * FROM order
WHERE created_at >= '2020-01-01'AND created_at < '2020-07-01';


-- 4. подукты следующих категорий Category 7, Category 11, Category 18

SELECT * FROM products
         WHERE category_id in (7, 11, 18);

-- 5. незавершенные заказы по состоянию на 31.12.2020

SELECT * FROM orders
WHERE order_status_order_status_id != 4 and updated_at <= '2020-12-31';

-- 6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.

SELECT * FROM carts
WHERE cart_id in (SELECT carts_cart_id FROM orders WHERE order_status_order_status_id=5);

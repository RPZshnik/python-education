-- Использовать транзакции для insert, update, delete на 3х таблицах.
-- Предоставить разнообразные примеры включая возврат к savepoints.
-- Доп: разные уровни доступа

-- ISOLATION LEVEL READ COMMITTED

BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT * FROM products;
INSERT INTO products(product_id, product_title, product_description, in_stock, price, slug, category_id)
VALUES (4002, 'Product 1234567', 'Product description 1234567', 2, 123, 'Product-1234567', 4);
SELECT * FROM products;
ROLLBACK;
COMMIT;


BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT * FROM products;
UPDATE products SET price=1000 WHERE product_id=4001;
ROLLBACK;
COMMIT;

-- ISOLATION LEVEL REPEATABLE READ

BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
INSERT INTO potential_customers (id, email, name, surname, second_name, city)
VALUES(3001, 'gmail1@gmail.com', 'name_1', 'surname_1', 'second_name_1', 'city_2200');
SELECT * FROM potential_customers;
SAVEPOINT update_point;
UPDATE potential_customers SET name='********' WHERE city='city_2200';
SELECT * FROM potential_customers WHERE name='********';
ROLLBACK TO SAVEPOINT update_point;
ROLLBACK;
COMMIT;


BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT * FROM potential_customers;
DELETE FROM potential_customers WHERE email='gmail1@gmail.com';
ROLLBACK;
COMMIT;

-- ISOLATION LEVEL SERIALIZABLE

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE ;
SELECT user_id, is_staff FROM users;
UPDATE users SET is_staff=1 WHERE is_staff=0;
SELECT user_id, is_staff FROM users;
ROLLBACK;
COMMIT;


BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT user_id, is_staff FROM users;
UPDATE users SET is_staff=0 WHERE is_staff=1;
SELECT user_id, is_staff FROM users;
ROLLBACK;
COMMIT;

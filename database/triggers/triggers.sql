-- 1. Сравнить цену каждого продукта n с средней ценой продуктов в категории
-- продукта n. Использовать window function. Таблица результата должна
-- содержать такие колонки: category_title, product_title, price, avg.

SELECT category_title,
       product_title,
       price,
       avg as category_avg,
       avg - price as difference
FROM(
    SELECT category_title,
       product_title,
       price,
       (AVG(price) OVER ( PARTITION BY category_title)) as avg
    FROM products
    JOIN categories c on c.category_id = products.category_id
) as pc;

-- 2. Добавить 2 любых триггера и обработчика к ним, обязательно использовать транзакции. Снабдить комментариями - что делают триггеры и обработчики.


-- update field updated_at after order updating

CREATE OR REPLACE FUNCTION update_at_updated()
RETURNS TRIGGER
language plpgsql
AS
$$
BEGIN
    UPDATE orders SET updated_at=now() WHERE order_id=NEW.order_id;
    return NEW;
end;
$$;


DROP FUNCTION IF EXISTS update_at_updated();

-- after order updating trigger call update_at_updated func
CREATE TRIGGER update_orders_update
    AFTER UPDATE
    ON orders
    FOR EACH ROW
    WHEN (pg_trigger_depth() = 0)
    EXECUTE PROCEDURE update_at_updated();

DROP TRIGGER IF EXISTS update_orders_update ON orders;


SELECT * FROM orders WHERE order_id=1;

UPDATE orders SET total=total*1.2 where order_id=1;



CREATE OR REPLACE FUNCTION password_difficult_check()
RETURNS TRIGGER
language plpgsql
AS
$$
BEGIN
    IF (NEW.password not like '%[0-9]%') then
        RAISE EXCEPTION 'Bad password';
    end if;
    return NEW;
end;
$$;


DROP FUNCTION IF EXISTS password_difficult_check();

-- before user updating password field or
-- inserting new user trigger call password_difficult_check func
CREATE TRIGGER password_check
    BEFORE UPDATE OR INSERT
    ON users
    FOR EACH ROW
    EXECUTE PROCEDURE password_difficult_check();

DROP TRIGGER IF EXISTS password_check on users;


SELECT password FROM users WHERE user_id=1;

INSERT INTO users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number)
VALUES (max(user_id) + 1, 'email1@gmail.com', '123456', 'fname', 'lname', 'mname', 1, 'UA', 'Kh', 'address', '+380677081311');

UPDATE users SET password='1234' WHERE user_id=1;
UPDATE users SET password='12345678_T' WHERE user_id=1;

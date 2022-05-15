CREATE VIEW Products_view AS
SELECT product_title, product_description, price
FROM products
ORDER BY price;

SELECT * FROM Products_view
WHERE price > 200;

DROP VIEW Products_view;



CREATE VIEW Products_category_view AS
SELECT product_title, product_description, category_title, price
FROM products
JOIN categories c on c.category_id = products.category_id;

SELECT category_title as category, sum(price)
FROM Products_category_view
WHERE price < 300
GROUP BY category_title
ORDER BY sum(price) DESC;

DROP View Products_category_view;



CREATE VIEW Orders_statuses_view AS
SELECT order_id, status_name
FROM orders o
JOIN order_status os on o.order_status_order_status_id=os.order_status_id
ORDER BY o.total;


SELECT status_name as status, count(order_id)
FROM Orders_statuses_view
GROUP BY status_name;

DROP View Orders_statuses_view;


CREATE MATERIALIZED VIEW M_view AS
SELECT product_id, product_title, product_description, in_stock, price, slug,
       users_user_id, subtotal, c.total as c_total, time_stamp,
       user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number,
       o.carts_cart_id, order_status_order_status_id, shipping_total, o.total as o_total, created_at, updated_at,
       category_title, category_description
FROM cart_product
JOIN products p on p.product_id = cart_product.products_product_id
JOIN carts c on c.cart_id = cart_product.carts_cart_id
JOIN users u on c.users_user_id = u.user_id
JOIN orders o on c.cart_id = o.carts_cart_id
JOIN categories using (category_id);

SELECT first_name, middle_name, sum(o_total)
FROM M_view
GROUP BY user_id, first_name, middle_name
ORDER BY sum(o_total) DESC;

DROP MATERIALIZED VIEW M_view;



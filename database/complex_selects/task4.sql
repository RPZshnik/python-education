-- 1. Вывести продукты, которые ни разу не попадали в корзину.

SELECT product_title as product
FROM products LEFT JOIN cart_product cp
on products.product_id = cp.products_product_id
WHERE carts_cart_id is NULL;

-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).


SELECT DISTINCT(product_title), product_description, in_stock, price, slug, category_id
FROM products
LEFT JOIN cart_product cp on products.product_id = cp.products_product_id
LEFT JOIN orders o on cp.carts_cart_id = o.carts_cart_id
WHERE o.carts_cart_id is null
ORDER BY product_title;

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.

SELECT product_title, product_description, in_stock, price, slug, category_id
FROM products
JOIN cart_product cp on products.product_id = cp.products_product_id
GROUP BY product_id
ORDER BY COUNT(product_id) DESC
LIMIT 10;


-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT product_title, product_description, in_stock, price, slug, category_id
FROM products
LEFT JOIN cart_product cp on products.product_id = cp.products_product_id
LEFT JOIN orders o on cp.carts_cart_id = o.carts_cart_id
WHERE o.carts_cart_id is not null
GROUP BY product_id
ORDER BY COUNT(product_id) DESC
LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT user_id, first_name, last_name, MAX(o.total)
FROM users
JOIN carts c on users.user_id = c.users_user_id
JOIN orders o on c.cart_id = o.carts_cart_id
GROUP BY user_id
ORDER BY SUM(o.total) DESC
LIMIT 5;

-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).

SELECT user_id, first_name, last_name, COUNT(order_id)
FROM users
JOIN carts c on users.user_id = c.users_user_id
JOIN orders o on c.cart_id = o.carts_cart_id
GROUP BY user_id
ORDER BY COUNT(order_id) DESC
LIMIT 5;

-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.

SELECT carts.users_user_id, COUNT(carts.cart_id)
FROM carts
LEFT JOIN orders
ON carts.cart_id = orders.carts_cart_id
WHERE orders.carts_cart_id is NULL
GROUP BY carts.users_user_id
ORDER BY COUNT(carts.cart_id) DESC
LIMIT 5;

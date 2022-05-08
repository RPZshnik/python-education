COPY users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
FROM '/usr/src/csv_files/users.csv'
DELIMITER ',' CSV;

COPY carts(cart_id, users_user_id, subtotal, total, time_stamp)
FROM '/usr/src/csv_files/carts.csv'
DELIMITER ',' CSV;

COPY categories(category_id, category_title, category_description)
FROM '/usr/src/csv_files/categories.csv'
DELIMITER ',' CSV;

COPY products(product_id, product_title, product_description, in_stock, price, slug, category_id)
FROM '/usr/src/csv_files/products.csv'
DELIMITER ',' CSV;

COPY cart_product(carts_cart_id, products_product_id)
FROM '/usr/src/csv_files/cart_products.csv'
DELIMITER ',' CSV;

COPY order_status(order_status_id, status_name)
FROM '/usr/src/csv_files/order_statuses.csv'
DELIMITER ',' CSV;

COPY orders(order_id, carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at)
FROM '/usr/src/csv_files/orders.csv'
DELIMITER ',' CSV;


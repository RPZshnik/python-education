CREATE INDEX order_carts_cart_id_idx ON orders(carts_cart_id);
CREATE INDEX cart_users_user_id_idx ON carts(users_user_id);
CREATE INDEX user_password_idx ON users(password);

DROP INDEX IF EXISTS user_password_idx;
DROP INDEX IF EXISTS cart_users_user_id_idx;
DROP INDEX IF EXISTS order_carts_cart_id_idx;


SELECT * FROM users LIMIT 10;

EXPLAIN ANALYSE
SELECT user_id, order_id, cart_id
FROM users
    JOIN carts c on users.user_id = c.users_user_id
    JOIN orders o on c.cart_id = o.carts_cart_id
WHERE password='1234565';

-- Without indexes

-- Hash Join  (cost=137.79..171.42 rows=1 width=12) (actual time=0.697..0.701 rows=0 loops=1)
--   Hash Cond: (o.carts_cart_id = c.cart_id)
--   ->  Seq Scan on orders o  (cost=0.00..28.00 rows=1500 width=8) (actual time=0.009..0.009 rows=1 loops=1)
--   ->  Hash  (cost=137.77..137.77 rows=1 width=8) (actual time=0.682..0.685 rows=0 loops=1)
--         Buckets: 1024  Batches: 1  Memory Usage: 8kB
--         ->  Hash Join  (cost=97.51..137.77 rows=1 width=8) (actual time=0.682..0.684 rows=0 loops=1)
--               Hash Cond: (c.users_user_id = users.user_id)
--               ->  Seq Scan on carts c  (cost=0.00..35.00 rows=2000 width=8) (actual time=0.003..0.004 rows=1 loops=1)
--               ->  Hash  (cost=97.50..97.50 rows=1 width=4) (actual time=0.675..0.676 rows=0 loops=1)
--                     Buckets: 1024  Batches: 1  Memory Usage: 8kB
--                     ->  Seq Scan on users  (cost=0.00..97.50 rows=1 width=4) (actual time=0.674..0.674 rows=0 loops=1)
--                           Filter: ((password)::text = '1234565'::text)
--                           Rows Removed by Filter: 3000
-- Planning Time: 0.635 ms
-- Execution Time: 0.747 ms


-- Indexing

-- Nested Loop  (cost=0.84..16.95 rows=1 width=12) (actual time=0.007..0.007 rows=0 loops=1)
--   ->  Nested Loop  (cost=0.56..16.60 rows=1 width=8) (actual time=0.006..0.007 rows=0 loops=1)
--         ->  Index Scan using user_password_idx on users  (cost=0.28..8.30 rows=1 width=4) (actual time=0.006..0.006 rows=0 loops=1)
--               Index Cond: ((password)::text = '1234565'::text)
--         ->  Index Scan using cart_users_user_id_idx on carts c  (cost=0.28..8.29 rows=1 width=8) (never executed)
--               Index Cond: (users_user_id = users.user_id)
--   ->  Index Scan using order_carts_cart_id_idx on orders o  (cost=0.28..0.33 rows=1 width=8) (never executed)
--         Index Cond: (carts_cart_id = c.cart_id)
-- Planning Time: 0.413 ms
-- Execution Time: 0.023 ms


CREATE INDEX ON cart_product(carts_cart_id);
CREATE INDEX ON orders(carts_cart_id);
CREATE INDEX ON carts(users_user_id);
CREATE INDEX ON orders(total);


DROP INDEX cart_product_carts_cart_id_idx;
DROP INDEX orders_carts_cart_id_idx;
DROP INDEX carts_users_user_id_idx;
DROP INDEX orders_total_idx;



EXPLAIN ANALYSE
SELECT total, count(order_id)
FROM products
    JOIN cart_product
        JOIN orders
        ON cart_product.carts_cart_id = orders.carts_cart_id
    ON products.product_id = cart_product.products_product_id
GROUP BY total;

-- Without indexes

-- GroupAggregate  (cost=20000002633.84..20000002817.37 rows=1493 width=14) (actual time=136.727..140.476 rows=1493 loops=1)
--   Group Key: orders.total
--   ->  Sort  (cost=20000002633.84..20000002690.04 rows=22480 width=10) (actual time=136.716..137.594 rows=22456 loops=1)
--         Sort Key: orders.total
--         Sort Method: quicksort  Memory: 1821kB
--         ->  Hash Join  (cost=20000000452.84..20000001008.95 rows=22480 width=10) (actual time=126.497..131.404 rows=22456 loops=1)
--               Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--               ->  Hash Join  (cost=10000000360.34..10000000616.67 rows=14995 width=4) (actual time=1.227..3.890 rows=14995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     ->  Seq Scan on cart_product  (cost=10000000000.00..10000000216.95 rows=14995 width=8) (actual time=0.004..0.700 rows=14995 loops=1)
--                     ->  Hash  (cost=260.31..260.31 rows=8002 width=4) (actual time=1.215..1.217 rows=8002 loops=1)
--                           Buckets: 8192  Batches: 1  Memory Usage: 346kB
--                           ->  Index Only Scan using products_pkey on products  (cost=0.28..260.31 rows=8002 width=4) (actual time=0.009..0.577 rows=8002 loops=1)
--                                 Heap Fetches: 0
--               ->  Hash  (cost=10000000055.00..10000000055.00 rows=3000 width=14) (actual time=125.258..125.259 rows=3000 loops=1)
--                     Buckets: 4096  Batches: 1  Memory Usage: 173kB
--                     ->  Seq Scan on orders  (cost=10000000000.00..10000000055.00 rows=3000 width=14) (actual time=124.762..124.957 rows=3000 loops=1)
-- Planning Time: 0.439 ms
-- JIT:
--   Functions: 21
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 4.274 ms, Inlining 12.036 ms, Optimization 70.608 ms, Emission 41.943 ms, Total 128.861 ms"
-- Execution Time: 145.024 ms


-- Indexing

-- HashAggregate  (cost=1406.92..1421.85 rows=1493 width=14) (actual time=18.122..18.293 rows=1493 loops=1)
--   Group Key: orders.total
--   Batches: 1  Memory Usage: 193kB
--   ->  Hash Join  (cost=360.90..1294.52 rows=22480 width=10) (actual time=1.255..12.874 rows=22456 loops=1)
--         Hash Cond: (cart_product.products_product_id = products.product_id)
--         ->  Merge Join  (cost=0.57..875.14 rows=22480 width=14) (actual time=0.014..7.557 rows=22456 loops=1)
--               Merge Cond: (orders.carts_cart_id = cart_product.carts_cart_id)
--               ->  Index Scan using orders_carts_cart_id_idx on orders  (cost=0.28..167.24 rows=3000 width=14) (actual time=0.005..0.908 rows=3000 loops=1)
--               ->  Materialize  (cost=0.29..547.90 rows=14995 width=8) (actual time=0.005..3.609 rows=22457 loops=1)
--                     ->  Index Scan using cart_product_carts_cart_id_idx on cart_product  (cost=0.29..510.42 rows=14995 width=8) (actual time=0.004..2.185 rows=11229 loops=1)
--         ->  Hash  (cost=260.31..260.31 rows=8002 width=4) (actual time=1.235..1.236 rows=8002 loops=1)
--               Buckets: 8192  Batches: 1  Memory Usage: 346kB
--               ->  Index Only Scan using products_pkey on products  (cost=0.28..260.31 rows=8002 width=4) (actual time=0.005..0.604 rows=8002 loops=1)
--                     Heap Fetches: 0
-- Planning Time: 0.390 ms
-- Execution Time: 18.359 ms


CREATE INDEX ON carts(total);
CREATE INDEX ON cart_product(carts_cart_id, products_product_id);


DROP INDEX IF EXISTS cart_total_idx;
DROP INDEX cart_product_carts_cart_id_products_product_id_idx;



EXPLAIN ANALYSE
SELECT total, cart_id
FROM cart_product
JOIN carts c on c.cart_id = cart_product.carts_cart_id
JOIN products p on p.product_id = cart_product.products_product_id
ORDER BY total;


-- Without indexes

-- Nested Loop  (cost=10000000360.62..10000900586.41 rows=14995 width=10) (actual time=75.218..3623.605 rows=14995 loops=1)
--   Join Filter: (cart_product.carts_cart_id = c.cart_id)
--   Rows Removed by Join Filter: 59965005
--   ->  Index Scan using carts_total_idx on carts c  (cost=0.28..232.26 rows=4000 width=10) (actual time=0.061..3.685 rows=4000 loops=1)
--   ->  Materialize  (cost=10000000360.34..10000000691.65 rows=14995 width=4) (actual time=0.019..0.473 rows=14995 loops=4000)
--         ->  Hash Join  (cost=10000000360.34..10000000616.67 rows=14995 width=4) (actual time=74.419..76.909 rows=14995 loops=1)
--               Hash Cond: (cart_product.products_product_id = p.product_id)
--               ->  Seq Scan on cart_product  (cost=10000000000.00..10000000216.95 rows=14995 width=8) (actual time=0.005..0.696 rows=14995 loops=1)
--               ->  Hash  (cost=260.31..260.31 rows=8002 width=4) (actual time=74.398..74.399 rows=8002 loops=1)
--                     Buckets: 8192  Batches: 1  Memory Usage: 346kB
--                     ->  Index Only Scan using products_pkey on products p  (cost=0.28..260.31 rows=8002 width=4) (actual time=0.016..0.598 rows=8002 loops=1)
--                           Heap Fetches: 0
-- Planning Time: 0.376 ms
-- JIT:
--   Functions: 13
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 1.973 ms, Inlining 4.673 ms, Optimization 45.089 ms, Emission 23.266 ms, Total 75.001 ms"
-- Execution Time: 3626.203 ms


-- Indexing

-- Sort  (cost=2071.69..2109.17 rows=14995 width=10) (actual time=12.147..12.633 rows=14995 loops=1)
--   Sort Key: c.total
--   Sort Method: quicksort  Memory: 1087kB
--   ->  Hash Join  (cost=555.90..1031.62 rows=14995 width=10) (actual time=2.459..8.714 rows=14995 loops=1)
--         Hash Cond: (cart_product.products_product_id = p.product_id)
--         ->  Hash Join  (cost=195.56..631.90 rows=14995 width=14) (actual time=1.227..4.978 rows=14995 loops=1)
--               Hash Cond: (cart_product.carts_cart_id = c.cart_id)
--               ->  Index Only Scan using cart_product_carts_cart_id_products_product_id_idx on cart_product  (cost=0.29..397.21 rows=14995 width=8) (actual time=0.022..1.395 rows=14995 loops=1)
--                     Heap Fetches: 0
--               ->  Hash  (cost=145.28..145.28 rows=4000 width=10) (actual time=1.198..1.198 rows=4000 loops=1)
--                     Buckets: 4096  Batches: 1  Memory Usage: 204kB
--                     ->  Index Scan using carts_pkey on carts c  (cost=0.28..145.28 rows=4000 width=10) (actual time=0.012..0.716 rows=4000 loops=1)
--         ->  Hash  (cost=260.31..260.31 rows=8002 width=4) (actual time=1.226..1.226 rows=8002 loops=1)
--               Buckets: 8192  Batches: 1  Memory Usage: 346kB
--               ->  Index Only Scan using products_pkey on products p  (cost=0.28..260.31 rows=8002 width=4) (actual time=0.006..0.585 rows=8002 loops=1)
--                     Heap Fetches: 0
-- Planning Time: 0.660 ms
-- Execution Time: 12.975 ms

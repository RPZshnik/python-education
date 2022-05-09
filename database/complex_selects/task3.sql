-- Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества

SELECT category_id, count(category_id)
FROM products
GROUP BY category_id
ORDER BY count(category_id) DESC;

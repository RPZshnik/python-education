
-- Top 10 rented car's model


EXPLAIN ANALYSE SELECT model, company_title as company, count(models_model_id)
FROM rents
JOIN cars c on c.car_id = rents.cars_car_id
JOIN car_models cm on c.models_model_id = cm.model_id
JOIN car_companies cc on cc.company_id = cm.companies_company_id
GROUP BY model_id, model, company_title
ORDER BY count(models_model_id) DESC
limit 10;


-- Top profitable branches

SELECT branch_id, sum(total_price)
FROM
(
SELECT branch_id, price * period_of_renting as total_price FROM rents
JOIN cars c on c.car_id = rents.cars_car_id
JOIN branches b on b.branch_id = c.branches_branch_id
) as rcbbi
GROUP BY branch_id
ORDER BY sum(total_price);


-- AVG price by each car model


EXPLAIN ANALYSE SELECT DISTINCT model,
AVG(price) OVER (PARTITION BY model_id) AS model_avg
FROM car_models
JOIN cars c on car_models.model_id = c.models_model_id
ORDER BY model_avg;


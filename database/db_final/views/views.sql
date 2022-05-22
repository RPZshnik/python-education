CREATE MATERIALIZED VIEW user_addresses AS
SELECT customer_id, city, street, building
FROM customers
JOIN addresses a on a.address_id = customers.customer_address_id
JOIN buildings b on b.building_id = a.buildings_building_id
JOIN streets s on s.street_id = b.streets_street_id
JOIN cities c on c.city_id = s.cities_city_id
ORDER BY customer_id;



SELECT * FROM user_addresses;


CREATE OR REPLACE VIEW rents_info AS
SELECT first_name, second_name, model, car_number, date_of_renting, period_of_renting
FROM rents
JOIN cars c on c.car_id = rents.cars_car_id
JOIN customers c2 on c2.customer_id = rents.customers_customer_id
JOIN car_models cm on cm.model_id = c.models_model_id;

SELECT * FROM rents_info
ORDER BY date_of_renting;


CREATE OR REPLACE VIEW cars_info AS
SELECT car_number, model, company_title, price
FROM cars
JOIN car_models cm on cm.model_id = cars.models_model_id
JOIN car_companies cc on cc.company_id = cm.companies_company_id;

SELECT model, company_title,  MAX(price) from cars_info
GROUP BY model, company_title
ORDER BY MAX(price);

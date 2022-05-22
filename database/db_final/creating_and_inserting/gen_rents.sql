CREATE OR REPLACE PROCEDURE generate_rents(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_car_id INT;
    rand_customer_id INT;
    rand_date date;
BEGIN
    for i in 1..amount loop
        SELECT timestamp '2022-01-10 20:00:00' + random() * (timestamp '2022-01-20 20:00:00' - timestamp '2021-01-10 10:00:00')
        INTO rand_date;
        SELECT car_id FROM cars ORDER BY random() limit 1 into rand_car_id;
        SELECT customer_id FROM customers ORDER BY random() limit 1 into rand_customer_id;
        INSERT INTO rents(customers_customer_id, cars_car_id, date_of_renting, period_of_renting)
        VALUES (rand_customer_id, rand_car_id, rand_date, random()*(30-1)+1);
    end loop;
END
$$;

DROP PROCEDURE generate_rents(amount INT);

call generate_rents(1000);

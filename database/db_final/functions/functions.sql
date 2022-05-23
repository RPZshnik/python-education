CREATE OR REPLACE FUNCTION available_cars(cash float)
RETURNS TABLE(
    car_id INT,
    car_number char(50),
    price float
)
language plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT
            cars.car_id, cars.car_number, cars.price
    FROM cars
    WHERE cash >= cars.price
    ORDER BY cars.price;
END
$$;

DROP FUNCTION available_cars(cash float);

SELECT * FROM available_cars(6000);



CREATE OR REPLACE FUNCTION get_cash_profit(start date, finish date)
RETURNS float
language plpgsql
AS $$
DECLARE
    rec record;
    sum float default 0;
BEGIN
    for rec in (
        SELECT * FROM cars
        JOIN rents r on cars.car_id = r.cars_car_id
    ) loop
        if rec.date_of_renting > start and rec.date_of_renting < finish then
            sum := sum + rec.price * rec.period_of_renting;
        end if;
        end loop;
    RETURN sum;
END
$$;

DROP FUNCTION get_cash_profit(start date, finish date);


SELECT * FROM get_cash_profit('2022-06-01', '2023-04-30');



create or replace function get_models(c_price integer)
   returns text as $$
declare
	 models text default '';
	 rec record;
	 cur_model cursor(p_year integer)
		 for select DISTINCT model
		 from cars
		 JOIN car_models cm on cm.model_id = cars.models_model_id
		 where price >= c_price;
begin
   open cur_model(c_price);
   models := 'Models: ';
   loop
      fetch cur_model into rec;
      exit when not found;
        models := models || ' ' || rec.model;
   end loop;
   close cur_model;
   return models;
end; $$
language plpgsql;

DROP FUNCTION get_models(c_price integer);

SELECT * FROM get_models(6000);

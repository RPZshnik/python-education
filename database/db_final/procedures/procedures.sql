CREATE OR REPLACE PROCEDURE create_rent(
    id_customer INT, id_car INT, period INT
)
language plpgsql
AS
$$
BEGIN
    if period > 30 then
        raise EXCEPTION 'Max renting period is 30';
    end if;
    INSERT INTO rents(customers_customer_id, cars_car_id, date_of_renting, period_of_renting)
    VALUES (id_customer, id_car, now(), period);
END
$$;

call create_rent(10, 1000, 12);
call create_rent(101, 1052, 60);


CREATE OR REPLACE PROCEDURE update_price(car_model varchar, coefficient float)
language plpgsql
AS
$$
DECLARE
    rec record;
BEGIN
    for rec in (
        SELECT car_id as id FROM cars
        JOIN car_models cm on cm.model_id = cars.models_model_id
        WHERE model=car_model
    ) loop
        UPDATE cars SET price=price * coefficient WHERE car_id=rec.id;
    end loop;

END
$$;



call update_price('Model 1', '0.9');



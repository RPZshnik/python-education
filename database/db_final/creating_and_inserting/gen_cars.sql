CREATE OR REPLACE PROCEDURE generate_cars(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_model_id INT;
    rand_branch_id INT;
    rand_number varchar;
BEGIN
    for i in 1..amount loop
        SELECT left(md5(random()::text), 6) into rand_number;
        SELECT model_id FROM car_models ORDER BY random() limit 1 into rand_model_id;
        SELECT branch_id FROM branches ORDER BY random() limit 1 into rand_branch_id;
        INSERT INTO cars(models_model_id, branches_branch_id, car_number, price)
        VALUES (rand_model_id, rand_branch_id, rand_number, random()*(10000-5000)+5000);
    end loop;
END
$$;

DROP PROCEDURE generate_cars(amount INT);

call generate_cars(1000);

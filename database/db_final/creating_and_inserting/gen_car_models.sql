CREATE OR REPLACE PROCEDURE generate_models(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_company_id INT;
BEGIN
    for i in 1..amount loop
        SELECT company_id FROM car_companies ORDER BY random() limit 1 into rand_company_id;
        INSERT INTO car_models(model, companies_company_id) VALUES ('Model ' || i, rand_company_id);
    end loop;
END
$$;

DROP PROCEDURE generate_models(amount INT);

call generate_models(1000);

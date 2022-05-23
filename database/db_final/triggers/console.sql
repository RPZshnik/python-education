CREATE OR REPLACE FUNCTION check_price()
returns TRIGGER
language plpgsql
AS
$$
DECLARE
    avg_model_price float;
BEGIN
    SELECT AVG(price) FROM cars
    WHERE models_model_id=NEW.models_model_id into avg_model_price;
    if abs(avg_model_price - NEW.price) > 1000 then
        raise exception 'Ne nado tak';
    end if;
    return new;
END
$$;


CREATE TRIGGER check_price
    BEFORE INSERT or UPDATE
    ON cars
    FOR EACH ROW
    EXECUTE PROCEDURE check_price();



CREATE OR REPLACE FUNCTION check_renting_period()
returns TRIGGER
language plpgsql
AS
$$
BEGIN
    if NEW.period_of_renting > 30 then
        return OLD;
    end if;
    return NEW;
END
$$;


CREATE TRIGGER check_renting_period
    AFTER INSERT or UPDATE
    ON rents
    FOR EACH ROW
    EXECUTE PROCEDURE check_renting_period();



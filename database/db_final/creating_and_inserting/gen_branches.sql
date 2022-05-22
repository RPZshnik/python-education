CREATE OR REPLACE PROCEDURE generate_car_companies(amount INT)
language plpgsql
AS
$$
BEGIN
    while counter < amount loop
        flag := 0;
        SELECT address_id FROM addresses
        ORDER BY random() limit 1 into rand_address_id;
        SELECT count(*) FROM branches
        WHERE branch_address_id=rand_address_id into flag;
        IF flag = 0 then
            SELECT count(*) FROM customers
            WHERE customer_address_id=rand_address_id into flag;
        end if;
        IF flag = 0 then
            SELECT * FROM gen_phone() into phone;
            INSERT INTO branches(branch_id, branch_address_id, phone_number) VALUES (counter, rand_address_id, phone);
            counter := counter + 1;
        end if;
    end loop;
END
$$;

DROP PROCEDURE generate_branches(amount INT);


call generate_branches(2000);

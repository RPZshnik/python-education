CREATE OR REPLACE FUNCTION gen_phone()
RETURNS varchar
language plpgsql
AS
$$
DECLARE
    phone_num varchar default '';
BEGIN
    for i in 1..10 loop
        phone_num := phone_num || (floor(random() * 9));
    end loop;
    return phone_num;
END
$$;


CREATE OR REPLACE PROCEDURE generate_customers(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_address_id INT;
    counter INT default 0;
    flag INT;
    phone varchar;
BEGIN
    while counter < amount loop
        flag := 0;
        SELECT address_id FROM addresses
        ORDER BY random() limit 1 into rand_address_id;
        SELECT count(*) FROM customers
        WHERE customer_address_id=rand_address_id into flag;
        IF flag = 0 then
            SELECT * FROM gen_phone() into phone;
            INSERT INTO customers(customer_id, first_name, second_name, customer_address_id, phone_number)
            VALUES (counter, 'first_name ' || counter, 'second_name ' || counter, rand_address_id, phone);
            counter := counter + 1;
        end if;
    end loop;
END
$$;


call generate_customers(2000);

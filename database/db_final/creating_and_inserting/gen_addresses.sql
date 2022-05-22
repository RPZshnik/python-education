CREATE OR REPLACE PROCEDURE generate_cities(amount INT)
language plpgsql
AS
$$
BEGIN
    for i in 1..amount loop
        INSERT INTO cities(city) VALUES ('City ' || i);
    end loop;
END
$$;


CREATE OR REPLACE PROCEDURE generate_streets(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_city_id INT;
BEGIN
    for i in 1..amount loop
        SELECT city_id FROM cities
        ORDER BY random() limit 1 into rand_city_id;
        INSERT INTO streets(cities_city_id, street) VALUES (rand_city_id, 'Street ' || i);
    end loop;
END
$$;

CREATE OR REPLACE PROCEDURE generate_buildings(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_street_id INT;
BEGIN
    for i in 1..amount loop
        SELECT street_id FROM streets
        ORDER BY random() limit 1 into rand_street_id;
        INSERT INTO buildings(streets_street_id, building) VALUES (rand_street_id, 'Bldg ' || i);
    end loop;
END
$$;

CREATE OR REPLACE PROCEDURE generate_addresses(amount INT)
language plpgsql
AS
$$
DECLARE
    rand_building_id INT;
    counter INT default 0;
    flag INT;
BEGIN
    while counter < amount loop
        flag := 0;
        SELECT building_id FROM buildings
        ORDER BY random() limit 1 into rand_building_id;
        SELECT count(*) FROM addresses
        WHERE buildings_building_id=rand_building_id into flag;
        IF flag = 0 then
            INSERT INTO addresses(buildings_building_id) VALUES (rand_building_id);
            counter := counter + 1;
        end if;
    end loop;
END
$$;

DROP procedure generate_addresses(amount INT);

call generate_cities(10000);
call generate_streets(10000);
call generate_buildings(10000);
call generate_addresses(5000);


SELECT * FROM addresses
JOIN buildings b on b.building_id = addresses.buildings_building_id
JOIN streets s on s.street_id = b.streets_street_id
JOIN cities c on c.city_id = s.cities_city_id;

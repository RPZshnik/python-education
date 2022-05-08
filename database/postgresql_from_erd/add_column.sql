ALTER TABLE users
ADD phone_number int;

ALTER TABLE users
ALTER COLUMN phone_number TYPE varchar(255);

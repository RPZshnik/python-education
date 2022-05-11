-- Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city

CREATE TABLE IF NOT EXISTS potential_customers(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);

-- Заполните данными таблицу.

INSERT INTO potential_customers(email, name, surname, second_name, city)
VALUES('gmail1@gmail.com', 'name_1', 'surname_1', 'second_name_1', 'city_1'),
      ('gmail2@gmail.com', 'name_2', 'surname_2', 'second_name 2', 'city 17'),
      ('gmail3@gmail.com', 'name_3', 'surname_3', 'second_name_3', 'city 3'),
      ('gmail4@gmail.com', 'name_4', 'surname_4', 'second_name_4', 'city 17'),
      ('gmail5@gmail.com', 'name_5', 'surname_5', 'second_name_5', 'city 5'),
      ('gmail6@gmail.com', 'name_6', 'surname_6', 'second_name_6', 'city 6'),
      ('gmail7@gmail.com', 'name_7', 'surname_7', 'second_name_7', 'city 17');

-- Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17

SELECT first_name, email
FROM users
WHERE city = 'city 17'
UNION
SELECT name, email
FROM potential_customers
WHERE city = 'city 17';

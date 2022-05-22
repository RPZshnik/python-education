CREATE DATABASE CarRental;

CREATE TABLE IF NOT EXISTS cities(
  city_id serial PRIMARY KEY,
  city char(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS streets(
  street_id serial PRIMARY KEY,
  cities_city_id int REFERENCES cities(city_id),
  street char(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS buildings(
  building_id serial PRIMARY KEY,
  streets_street_id int REFERENCES streets(street_id),
  building char(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS addresses(
  address_id serial PRIMARY KEY,
  buildings_building_id int REFERENCES buildings(building_id)
);

CREATE TABLE IF NOT EXISTS Customers(
  customer_id serial PRIMARY KEY,
  first_name char(50),
  second_name char(50),
  customer_address_id int REFERENCES addresses(address_id),
  phone_number char(50)
);

CREATE TABLE IF NOT EXISTS Branches(
  branch_id serial PRIMARY KEY,
  branch_address_id int REFERENCES addresses(address_id),
  phone_number char(50)
);

CREATE TABLE IF NOT EXISTS car_companies(
    company_id serial PRIMARY KEY,
    company_title char(50)
);

CREATE TABLE IF NOT EXISTS car_models(
    model_id serial PRIMARY KEY,
    model char(50),
    companies_company_id int REFERENCES car_companies(company_id)
);

CREATE TABLE IF NOT EXISTS Cars(
    car_id serial PRIMARY KEY,
    models_model_id int REFERENCES car_models(model_id),
    branches_branch_id int REFERENCES Branches(branch_id),
    car_number char(50),
    price float
);

CREATE TABLE IF NOT EXISTS Rents(
    rent_id serial PRIMARY KEY,
    customers_customer_id int REFERENCES Customers(customer_id),
    cars_car_id int REFERENCES Cars(car_id),
    date_of_renting date,
    period_of_renting int
);

-- DROP TABLE IF EXISTS Rents;
-- DROP TABLE IF EXISTS Cars;
-- DROP TABLE IF EXISTS Branches;
-- DROP TABLE IF EXISTS Customers;
-- DROP TABLE IF EXISTS addresses;



create table if not exists Users(
    user_id serial primary key,
    email varchar(255),
    password varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    middle_name varchar(255),
    is_staff smallint,
    country varchar(255),
    city varchar(255),
    address text
);

create table if not exists Order_status(
    order_status_id serial primary key,
    status_name varchar(255)
);

create table if not exists Carts(
    cart_id serial primary key,
    Users_user_id int references Users(user_id),
    subtotal decimal,
    total decimal,
    time_stamp timestamp(2)
);

create table if not exists Orders(
    order_id serial primary key,
    Carts_cart_id int references Carts(cart_id),
    Order_status_order_status_id int references Orders(order_id),
    shipping_total decimal,
    total decimal,
    created_at timestamp(2),
    updated_at timestamp(2)
);

create table if not exists Categories(
    category_id serial primary key,
    category_title varchar(255),
    category_description text
);

create table if not exists Products(
    product_id serial primary key,
    product_title varchar(255),
    product_description text,
    in_stock int,
    price real,
    slug varchar(45),
    category_id int references Categories(category_id)
);

create table if not exists Cart_product(
    Carts_cart_id int references Carts(cart_id),
    products_product_id int references Products(product_id)
);

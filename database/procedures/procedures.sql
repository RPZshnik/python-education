-- 1. Создать функцию, которая сетит shipping_total = 0 в таблице order,
-- если город юзера равен x (аргумент функции), и возвращает сумму всех
-- заказов для поля shipping_total. Использовать IF clause.

create or replace view task1_view as
        select order_id, city, shipping_total
        from users
        join carts c on users.user_id = c.users_user_id
        join orders o on c.cart_id = o.carts_cart_id;

create or replace function task1(user_city varchar(255))
returns float
language plpgsql
as
    $$
    declare
        orders_sum int;
        t1_view record;
    begin
        select sum(shipping_total) from task1_view where city=user_city into orders_sum;
        for t1_view in (select * from task1_view)
        loop
        if t1_view.city = user_city
            then
                update orders
                set shipping_total = 0
                where order_id = t1_view.order_id;
            end if;
        end loop;
        return orders_sum;
    end;
    $$;

drop function task1(user_city varchar(255));

select * from task1('city 4');


-- 2. Написать 3 любые (НО осмысленные) хранимые процедуры с использованием условий, циклов и транзакций. Дать комментарии что делает каждая процедура.


-- procedure that add product to cart if product's amount is enough and update all followings fields

create or replace procedure proc1(id_product int, id_cart float, amount int)
language plpgsql
as $$
    declare
        product_price float;
        product_amount int;
        updated_sum float;
    begin
        if id_product not in (select product_id from products) then
            raise notice 'Product id not exist';
        end if;
        if id_cart not in (select cart_id from carts) then
            raise notice 'Cart id not exist';
        end if;
        select in_stock from products where product_id=id_product into product_amount;
        if amount > product_amount then
            raise notice 'Not enough of product';
        else
            update products
            set in_stock = in_stock - amount
            where product_id = id_product;
            select price from products into product_price;
            update carts
            set total = total + product_price * amount, time_stamp = now()
            where cart_id = id_cart;
            insert into cart_product (carts_cart_id, products_product_id)
            values (id_cart, id_product);
            update orders
            SET total = updated_sum, updated_at = now()
            WHERE carts_cart_id = id_cart;
            COMMIT;
        end if;
end;

$$;

call proc1(3, 5, 5); -- success
call proc1(3, 5, 200); -- product not enough
call proc1(110001101, 5, 20); -- product not exist
call proc1(3, 101011011010, 20); -- cart not exist
drop procedure proc1(id_product int, id_cart float, amount int);


-- updating user full name by user_id (first_name, middle_name and last_name must be not empty)
create or replace procedure proc2(id_user int, f_name varchar, m_name varchar, l_name varchar)
language plpgsql
as $$
    declare
        u record;
    begin
        update users set
        first_name=initcap(f_name),
        middle_name=initcap(m_name),
        last_name=initcap(l_name)
        where user_id=id_user;
        select * from users
        where user_id=id_user
        into u;
        if u.first_name='' or u.middle_name='' or u.last_name='' then
            rollback;
        end if;
        commit;
end;
$$;

select first_name, middle_name, last_name
from users
where user_id=5;
call proc2(5, 'Dimon', 'dimonch', 'dimoncha'); -- success
call proc2(5, '', 't', 's');
drop procedure proc2(id_user int, f_name varchar, m_name varchar, l_name varchar);


-- discount to products of some category (change total in order)

create or replace view proc3_view as
        select order_id, category_id, o.total, price
        from cart_product
        join carts c on c.cart_id = cart_product.carts_cart_id
        join products p on p.product_id = cart_product.products_product_id
        join orders o on c.cart_id = o.carts_cart_id;

create or replace procedure proc3(id_category int, discount int)
language plpgsql
as $$
    declare
        rec record;
    begin
        if discount > 100 or discount < 0 then
            return;
        end if;
        for rec in (select * from proc3_view where category_id=id_category)
        loop
            update orders
            set total=total - rec.price * (1 - discount / 100),
                updated_at=now()
            where order_id=rec.order_id;
        end loop;
end;
$$;


select *
from cart_product
join carts c on c.cart_id = cart_product.carts_cart_id
join products p on p.product_id = cart_product.products_product_id
join orders o on c.cart_id = o.carts_cart_id
where category_id=5
limit 5;

call proc3(5, 20);
drop procedure proc3();

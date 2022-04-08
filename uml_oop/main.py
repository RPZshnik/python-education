from datetime import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class AuthorizationData:
    email: str
    username: str
    password: str


class Person(ABC):
    __id: int = 0

    def __init__(self, *args, **kwargs):
        Person.__id += 1


class Customer(Person):
    def __init__(self, email, address, password, name, surname):
        super().__init__()
        self.__restaurant = None
        self.__name: str = name
        self.__surname: str = surname
        self.__email = email
        self.__address = address
        self.__password = password
        self.__orders = list()

    @property
    def restaurant(self):
        return self.__restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        self.__restaurant = restaurant

    def get_customer_info(self):
        return {"name": self.__name,
                "surname": self.__surname,
                "user": self.__address}

    def __waiter_call(self):
        waiters_list = self.__restaurant.waiters
        waiter = waiters_list[-1]
        if waiter.is_free:
            waiter.is_free = False
            waiters_list.insert(0, waiters_list.pop())
            return waiter
        else:
            return None

    def make_order(self, dish_list):
        waiter = self.__waiter_call()
        if waiter is not None:
            order = Order(dish_list, waiter)
            self.__orders.append(order)
            return order
        else:
            print("No free waiters")

    def finish_order(self, order):
        for index, customer_order in enumerate(self.__orders):
            if customer_order.id == order.id:
                self.__orders[index].is_finished = True
                order.waiter.is_free = True
                return True
        return False


class Employee(Person):
    def __init__(self, name: str, position: str, salary: float):
        super().__init__()
        self.__position = position
        self.__salary = salary
        self.__name = name

    def get_position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary


class Waiter(Employee):
    position = "waiter"

    def __init__(self, name, salary, *args, **kwargs):
        super().__init__(name, Waiter.position, salary)
        self.__is_free = True

    @property
    def is_free(self):
        return self.__is_free

    @is_free.setter
    def is_free(self, is_free):
        self.__is_free = is_free


class Product:
    def __init__(self, product_name: str, price: float):
        self.__product_name = product_name
        self.__price = price

    @property
    def product_name(self):
        return self.__product_name

    @property
    def price(self):
        return self.__price


class DishProduct:
    def __init__(self, product: Product, quantity: float, unit: str = "kg"):
        self.__product = product
        self.__quantity = quantity
        self.__unit = unit

    def get_cost(self):
        return self.__quantity * self.__product.price

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity


class Dish:
    def __init__(self, dish_name: str, composition_list: list):
        self._dish_name = dish_name
        self._composition_list = composition_list

    def get_composition(self):
        products_names: list = list()
        for dish_product in self._composition_list:
            products_names.append(dish_product.product.product_name)
        return products_names

    def get_dish_price(self):
        price = 0
        for dish_product in self._composition_list:
            price += dish_product.get_cost()
        return price


class Order:
    __id: int = 0

    def __new__(cls, dish_list, waiter, *args, **kwargs):
        Order.__id += 1
        return super(Order, cls).__new__(cls, *args, **kwargs)

    def __init__(self, dish_list: list, waiter: Waiter):
        self.id: int = Order.__id
        self.__dish_list: list = dish_list
        self.__order_datetime = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.is_finished = False
        self.__waiter = waiter

    def add_dish(self, dish: Dish):
        self.__dish_list.append(dish)

    @property
    def waiter(self):
        return self.__waiter

    @waiter.setter
    def waiter(self, waiter):
        self.__waiter = waiter


class Restaurant:
    __id: int = 0

    def __new__(cls, address: str, *args, **kwargs):
        Restaurant.__id += 1
        return super(Restaurant, cls).__new__(cls, *args, **kwargs)

    def __init__(self, address: str):
        self.__address = address
        self.__dishes = list()
        self.__waiters = list()
        self.__customers = list()

    def hire_waiter(self, name, salary: float):
        waiter = Waiter(name, salary)
        self.__waiters.append(waiter)

    def add_customer(self, customer: Customer):
        self.__customers.append(customer)
        customer.restaurant = self

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    @property
    def waiters(self):
        return self.__waiters

    @waiters.setter
    def waiters(self, waiters):
        self.__waiters = waiters

    def __str__(self):
        return f"Restaurant({self.__address})"

    def __repr__(self):
        return str(self)


def main():
    restaurant = Restaurant("вулиця Сумська, 84/2")
    restaurant.hire_waiter("Pavel", 100)
    restaurant.hire_waiter("Maria", 150)
    borsch = Dish("Borsch", [DishProduct(Product("potatoes", 20), 0.25),
                             DishProduct(Product("chicken broth", 100), 0.2),
                             DishProduct(Product("carrot", 15), 0.1),
                             DishProduct(Product("beets", 20), 0.2)])
    restaurant.add_dish(borsch)
    den = Customer("test@gmail.com", "testik", "******", "Den", "Bandera")
    restaurant.add_customer(den)
    order = den.make_order(dish_list=[borsch])
    den.finish_order(order)


if __name__ == "__main__":
    main()

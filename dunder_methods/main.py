from __future__ import annotations
from abc import ABC, abstractmethod


class Speed:

    def __set_name__(self, owner, name):
        """Magical method that implements comparison for objects with engine"""
        self.name = name

    def __set__(self, instance, value):
        """Magical method that implements comparison for objects with engine"""
        if value < 0:
            raise ValueError("Are you seriously? Speed less than 0. You are cool!")
        if value > 1079252848.8:
            raise ValueError("You successfully destroyed the universe by accelerating faster than the speed of light.")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        """Magical method that implements comparison for objects with engine"""
        return instance.__dict__[self.name]


class Transport(ABC):
    """Abstract class, that defines some methods for subclasses"""
    transport_amount = 0
    speed = Speed()

    def __init__(self, transport_type, speed, cost):
        Transport.transport_amount += 1
        self.transport_type = transport_type
        self.speed = speed
        self.__cost = cost
        self.mileage = 0

    @staticmethod
    def m_to_km(speed):
        return speed * 1.609

    @classmethod
    def from_m_to_km(cls, transport_type, speed, cost):
        return Transport(transport_type, cls.m_to_km(speed), cost)

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value: float):
        self.__cost = value

    @abstractmethod
    def move(self, travel_time):
        self.mileage += travel_time * self.speed


class Fuel:
    """Class, that defines some methods for subclasses"""
    def __init__(self, amount: float, fuel_type):
        self.__amount = amount
        self.__fuel_type = fuel_type

    def __lt__(self, other):
        """Magical method that implements comparison of fuel amount"""
        return self.__fuel_type < other.__fuel_type

    def __gt__(self, other):
        """Magical method that implements comparison fuel amount"""
        return self.__fuel_type > other.__fuel_type

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def fuel_type(self):
        return self.__fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self.__fuel_type = value

    def __add__(self, other):
        self.__amount += other
        return self

    def __sub__(self, other):
        self.__amount -= other
        return self

    def __isub__(self, other):
        self.__amount -= other
        return self

    def __truediv__(self, other):
        return self.__amount / other

    def __bool__(self):
        return bool(self.__amount)


class Engine(ABC):
    """Abstract class, that defines some methods for subclasses"""
    def __init__(self, power, fuel: Fuel, consumption):
        self.__fuel = fuel
        self.__power = power
        self.consumption = consumption

    def __lt__(self, other):
        """Magical method that implements comparison for objects with engine"""
        return self.__power < other.__fuel_type

    def __gt__(self, other):
        """Magical method that implements comparison for objects with engine"""
        return self.__power > other.__power

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value: str):
        self.__fuel = value


class Car(Transport, Engine):
    """Class, that represents car as subclass"""
    transport_type = "Car"

    def __init__(self, speed, cost, engine_power, fuel, consumption, color="Grey"):
        Transport.__init__(self, Car.transport_type, speed, cost)
        Engine.__init__(self, engine_power, fuel, consumption)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def move(self, travel_time):
        if self.fuel == 0:
            print("Fuel on zero")
            return
        if self.fuel / self.consumption < travel_time:
            print("Not enough fuel")
            return
        super(Car, self).move(travel_time)
        fuel_spend = travel_time * self.consumption
        self.fuel -= fuel_spend
        print(f"During the trip was spent {fuel_spend} unit of {self.fuel.fuel_type}")


class Ship(Transport, Engine):
    """Class, that represents ship as subclass"""
    transport_type = "Ship"

    def __init__(self, speed, cost, engine_power, fuel, consumption, country="Ukraine"):
        Transport.__init__(self, Ship.transport_type, speed, cost)
        Engine.__init__(self, engine_power, fuel, consumption)
        self.__country = country

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    def move(self, travel_time):
        if self.country == "Russia":
            print("Russian warship, fuck you")
            return
        if self.fuel == 0:
            print("Fuel on zero")
            return
        if self.fuel / self.consumption < travel_time:
            print("Not enough fuel")
            return
        super(Ship, self).move(travel_time)
        fuel_spend = travel_time * self.consumption
        self.fuel -= fuel_spend
        print(f"During the boating was spent {fuel_spend} unit of {self.fuel.fuel_type}")


class Airplane(Transport, Engine):
    """Class, that represents airplane as subclass"""
    transport_type = "Airplane"

    def __init__(self, speed, cost, engine_power, fuel, consumption, company):
        Transport.__init__(self, Airplane.transport_type, speed, cost)
        Engine.__init__(self, engine_power, fuel, consumption)
        self.__company = company

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        self.__company = value

    def move(self, travel_time):
        if self.fuel == 0:
            print("Fuel on zero")
            return
        if self.fuel / self.consumption < travel_time:
            print("Not enough fuel")
            return
        super(Airplane, self).move(travel_time)
        fuel_spend = travel_time * self.consumption
        self.fuel -= fuel_spend
        print(f"During the flight was spent {fuel_spend} unit of {self.fuel.fuel_type}")


class Bike(Transport):
    """Class, that represents bike as subclass"""
    transport_type = "Bike"

    def __init__(self, speed, cost):
        super().__init__(Bike.transport_type, speed, cost)

    def move(self, travel_time):
        distance = travel_time * self.speed
        super(Bike, self).move(travel_time)
        if distance > 1:
            print(f"{distance} kilometers covered")
        else:
            print(f"{distance} kilometer covered")


if __name__ == "__main__":
    car1 = Car(100, 100000, 120 * 10 ** 3, Fuel(123, "petrol"), 10)
    ship = Ship(100, 100000, 1200 * 10 ** 3, Fuel(2000, "diesel"), 10, "Russia")
    print("Car fuel amount: ", car1.fuel.amount)
    print("Ship fuel amount: ", ship.fuel.amount)
    car1.move(1)
    ship.move(2)
    print("Car fuel amount: ", car1.fuel.amount)
    print("Ship fuel amount: ", ship.fuel.amount)

    if car1 > ship:
        print("Car engine more powerful")
    else:
        print("Ship engine more powerful")

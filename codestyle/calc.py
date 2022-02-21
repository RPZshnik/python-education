"""
This module implements the Calculator class.

"""


class Calculator:
    """
    This is a class for mathematical operations on real numbers

    :param value: The arg is used as start value of counter.

    :ivar __counter: This is where we store our current value of Calculator object,
    """
    def __init__(self, value: float = 0):
        self.__counter: float = value

    def addition(self, value: float) -> float:
        """

        :param value: The value to be added to the counter
        :return: Current value of counter
        """
        self.__counter += value
        return self.counter

    def subtraction(self, value: float) -> float:
        """

        :param value: The value to be subtracted from the counter
        :return: Current value of counter
        """
        self.__counter -= value
        return self.counter

    def multiplication(self, value: float) -> float:
        """

        :param value: The value by which the counter will be multiplied
        :return: Current value of counter
        """
        self.__counter *= value
        return self.counter

    def division(self, value: float) -> float:
        """

        :param value: The value by which the counter will be divided
        :return: Current value of counter
        """
        try:
            self.__counter /= value
        except ZeroDivisionError:
            print("division by zero")
        return self.counter

    @property
    def counter(self) -> float:
        """

        :return: Current value of counter
        """
        return self.__counter

    def __str__(self):
        """

        :return: String representation of object
        """
        return f"Calculator: {self.__counter}"

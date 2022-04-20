"""Module that implement Player class"""


class Player:
    """Class implement players"""
    def __init__(self, sign: str, name="Bot"):
        self.__name = name
        self.sign = sign
        self.win_count = 0

    def __str__(self):
        return f"Player({self.__name})"

    @property
    def name(self):
        """Property that return name of player"""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

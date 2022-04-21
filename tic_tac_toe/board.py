"""Module implement Board class"""
from typing import List, Optional


class Board:
    """Board class"""
    def __init__(self, size=3):
        self.__size = size
        self.__fields: List[List[Optional]] = [[None] * size for _ in range(size)]

    def clear_board(self):
        """Method that clear the board fields"""
        self.__fields = [[None] * self.__size for _ in range(self.__size)]

    def get_field(self, row: int, column: int):
        """Method that return the fields"""
        return self.__fields[row][column]

    def set_field(self, row: int, column: int, value: str):
        """Method that set the fields"""
        self.__fields[row][column] = value

    def is_full(self):
        """Method that return if all fields are occupied"""
        return None not in sum(self.__fields, [])

    def get_columns(self):
        """Method that return columns of board"""
        columns = [[None] * self.__size for _ in range(self.__size)]
        for i, row in enumerate(self.__fields):
            for j, field in enumerate(row):
                columns[j][i] = field
        return columns

    def get_diagonal(self):
        """Method that return diagonals of board"""
        diagonals = [[] for _ in range(2)]
        for index in range(3):
            diagonals[0].append(self.__fields[index][index])
            diagonals[1].append(self.__fields[index][self.__size - index - 1])
        return diagonals

    @staticmethod
    def check_line(array):
        """Method that check line for win"""
        return len(set(array)) == 1 and None not in array

    def check_for_win(self):
        """Method that check board for win"""
        lines = [*self.fields, *self.get_columns(), *self.get_diagonal()]
        for line in lines:
            if self.check_line(line):
                return True
        return False

    @property
    def fields(self):
        """Property that return the fields of board"""
        return self.__fields

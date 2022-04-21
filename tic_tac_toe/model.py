"""This module implement class Model (model in MVC)"""
from board import Board
from player import Player
from logger import logger


class Model:
    """Class provides data and methods for working with them"""
    def __init__(self):
        self.__players = [Player("x"), Player("o")]
        self.__board = Board()

    @staticmethod
    def print_log_file():
        """Static method that print a wins log file"""
        logger.debug("Print wins log file: ")
        with open("wins_file.log", "r", encoding="utf-8") as file:
            for line in file.readlines():
                print(line)

    @staticmethod
    def clear_log_file():
        """Static method that clear a wins log file"""
        logger.debug("Clear wins log file")
        with open('wins_file.log', 'w', encoding="utf-8") as file:
            file.close()

    @property
    def players(self):
        """players getter"""
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    @property
    def board(self):
        """board getter"""
        return self.__board

    @board.setter
    def board(self, value):
        self.__board = value

"""This module implements abstract class View"""
from abc import ABC, abstractmethod
from board import Board


class View(ABC):
    """Class responsible for getting the required data from the model and sending it to the user"""
    @abstractmethod
    def display_menu(self):
        """Method to display a menu"""
        raise NotImplementedError

    @abstractmethod
    def display_board(self, board: Board):
        """Method to display a board"""
        raise NotImplementedError

    @abstractmethod
    def make_input(self, message: str = ""):
        """Method for user input"""
        raise NotImplementedError

    @abstractmethod
    def print_message(self, message: str):
        """Method to print message for user"""
        raise NotImplementedError

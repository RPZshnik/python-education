"""Module that implement abstract class View"""
from view import View
from board import Board


class TerminalView(View):
    """Class that implement abstract class View"""
    def print_message(self, message: str):
        print(message)

    def display_board(self, board: Board):
        fields = board.fields
        for i, _ in enumerate(fields):
            for j, _ in enumerate(fields[i]):
                if fields[i][j] is None:
                    print(" _ ", end="")
                else:
                    print(f" {fields[i][j]} ", end="")
            print("\n")

    def display_menu(self):
        print("1. Start game")
        print("2. Start game with bot")
        print("3. Print wins log")
        print("4. Clear wins log")
        print("5. Exit")

    def make_input(self, message: str = ""):
        value = input(message)
        return value

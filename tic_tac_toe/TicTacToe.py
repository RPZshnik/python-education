from model import Model
from controller import Controller
from terminal_view import TerminalView


class TicTacToe:
    def __init__(self):
        self.view = TerminalView()
        self.model = Model()
        self.controller = Controller(self.model, self.view)

    def start_game(self):
        self.controller.start()

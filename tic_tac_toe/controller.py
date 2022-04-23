"""This module implement class Controller (controller in MVC)"""
from logger import logger
from player import Player
from model import Model
from view import View
from bot import Bot


class Controller:
    """Class provides communication between the user and the system"""

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start(self):
        """Method that start the game"""
        logger.debug("Start game")
        self.menu()

    def __names_request(self, with_bot=False):
        """Method that requests the players names"""
        logger.debug("Name's request")
        player1_name = self.view.make_input("Enter first player name: ")
        player2_name = self.view.make_input("Enter second player name: ")
        first_player = Player("x", player1_name)
        if with_bot:
            second_player = Bot(player2_name, "o", first_player)
        else:
            second_player = Player("o", player2_name)
        self.model.players[0] = first_player
        self.model.players[1] = second_player

    def __event_choice(self):
        """Method for choose menu item"""
        self.view.display_menu()
        event = int(self.view.make_input("Enter your choice: "))
        if 1 <= event <= 5:
            return event
        logger.debug("Choice event error")
        raise ValueError("Choice must be between 1 and 4")

    def menu(self):
        """Method that implemented a menu"""
        event = -1
        while event != 5:
            event = self.__event_choice()
            if event in (1, 2):
                game_with_bot = event == 2
                self.__names_request(game_with_bot)
                logger.info(f"New game. {self.model.players[0]}"
                            f" vs {self.model.players[1]}")
                self.__game_loop()
            elif event == 3:
                self.model.print_log_file()
            elif event == 4:
                self.model.clear_log_file()

    def field_input(self):
        """Method that implemented input of field cords"""
        possible_moves = self.model.board.get_possible_moves()
        while True:
            message = "Enter row and column through a space: "
            row, column = map(int,
                              self.view.make_input(message).split())
            if (row - 1, column - 1) not in possible_moves:
                logger.info("This field already occupied")
            else:
                return row, column

    def proceed_game(self):
        """Method that returns True if the round should continue, False otherwise"""
        is_full = self.model.board.is_full()
        is_a_winner = self.model.board.check_for_win()
        return not is_a_winner and not is_full

    def game_match(self):
        """Method that implements game match"""
        player_index = 0
        board = self.model.board
        players = self.model.players
        self.view.display_board(board)
        while self.proceed_game():
            if isinstance(players[player_index], Bot):
                row, column = players[player_index].next_move(board)
            else:
                row, column = self.field_input()
            board.set_field(row - 1, column - 1,
                            players[player_index].sign)
            player_index = (player_index + 1) % len(players)
            self.view.display_board(board)
        if board.check_for_win():
            winner_index = (player_index + 1) % len(players)
            return winner_index
        return None

    def __game_loop(self):
        """Method that implements game loop"""
        while True:
            winner_index = self.game_match()
            self.print_winner(winner_index)
            self.model.board.clear_board()
            if self.view.make_input("Rematch? (yes/no): ") != "yes":
                return None

    def print_winner(self, winner_index):
        """Method print the winner and score"""
        players = self.model.players
        if winner_index is not None:
            winner = players[winner_index]
            loser = players[(winner_index + 1) % len(players)]
            players[winner_index].win_count += 1
            message = f"{winner.name} won! Game score:" \
                      f" {winner.name} - {winner.win_count}," \
                      f" {loser.name} - {loser.win_count}"
            logger.info(message)
            self.view.print_message(message)
        else:
            first_player = players[0]
            second_player = players[1]
            message = f"Draw! Game score:" \
                      f" {first_player.name} - {first_player.win_count}," \
                      f" {second_player.name} - {second_player.win_count}"
            logger.info(message)
            self.view.print_message(message)

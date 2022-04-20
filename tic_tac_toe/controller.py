"""This module implement class Controller (controller in MVC)"""
from logger import logger
from model import Model
from view import View


class Controller:
    """Class provides communication between the user and the system"""

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start(self):
        """Method that start the game"""
        logger.debug("Start game")
        self.menu()

    def __names_request(self):
        """Method that requests the players names"""
        logger.debug("Name's request")
        player1_name = self.view.make_input("Enter first player name: ")
        player2_name = self.view.make_input("Enter second player name: ")
        self.model.players[0].name = player1_name
        self.model.players[1].name = player2_name

    def __event_choice(self):
        """Method for choose menu item"""
        self.view.display_menu()
        event = int(self.view.make_input("Enter your choice: "))
        if 1 <= event <= 4:
            return event
        logger.debug("Choice event error")
        raise ValueError("Choice must be between 1 and 4")

    def menu(self):
        """Method that implemented a menu"""
        event = -1
        while event != 4:
            event = self.__event_choice()
            if event == 1:
                self.__names_request()
                logger.info(f"New game. {self.model.players[0]}"
                            f" vs {self.model.players[1]}")
                self.__game_loop()
            elif event == 2:
                self.model.print_log_file()
            elif event == 3:
                self.model.clear_log_file()

    def field_input(self):
        """Method that implemented input of field cords"""
        fields = self.model.board.fields
        while True:
            message = "Enter row and column through a space: "
            row, column = map(int,
                              self.view.make_input(message).split())
            if fields[row - 1][column - 1] is not None:
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
            players = self.model.players
            if winner_index is not None:
                winner = players[winner_index]
                loser = players[(winner_index + 1) % len(players)]
                players[winner_index].win_count += 1
                message = f"{winner.name} won! Game score:"\
                          f" {winner.name} - {winner.win_count},"\
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
            self.model.board.clear_board()
            if self.view.make_input("Rematch? (yes/no): ") != "yes":
                return None

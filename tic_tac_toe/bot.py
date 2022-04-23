from player import Player
from board import Board
from copy import deepcopy


class Bot(Player):
    def __init__(self, bot_name: str, sign: str, opponent: Player):
        self.opponent: Player = opponent
        super().__init__(sign, name=bot_name)

    @staticmethod
    def __score(board: Board, player: Player):
        """Return move score"""
        if board.check_for_win():
            if isinstance(player, Bot):
                return -10
            else:
                return 10
        else:
            return 0

    def __minmax(self, board: Board, player: Player):
        """Realization of minmax algorithm"""
        if board.check_for_win() or board.is_full():
            return self.__score(board, player)
        scores: list = []
        moves: list = []
        for move in board.get_possible_moves():
            possible_board = deepcopy(board)
            possible_board.set_field(*move, value=player.sign)
            if isinstance(player, Bot):
                scores.append(self.__minmax(possible_board, self.opponent))
            else:
                scores.append(self.__minmax(possible_board, self))
            moves.append(move)
        if isinstance(player, Bot):
            index_of_max = scores.index(max(scores))
            self.move = moves[index_of_max]
            return scores[index_of_max]
        else:
            index_of_min = scores.index(min(scores))
            self.move = moves[index_of_min]
            return scores[index_of_min]

    def next_move(self, board: Board) -> tuple:
        """Method that return best cord to the next move"""
        self.__minmax(board, self)
        return tuple([index + 1 for index in self.move])

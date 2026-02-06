from src.Board import Board
from src.Player import Player


class Game:

    def __init__(self, player1, player2):
        self._board = Board()
        self._players = [player1, player2]
        self._current_index = 0
    

    @property
    def board(self):
        return self._board  

    @property
    def current_player(self):
        return self._players[self._current_index]
    
    def next_turn(self):
        self._current_index = self._current_index + 1
        if self._current_index == 2:
            self._current_index = 0
    
    def get_status(self):
        jugador_actual = self.current_player
        return "Turno de " + jugador_actual.name + " (" + jugador_actual.symbol + ")"

    def make_mark(self, coords):
        fil = coords[0]
        col = coords[1]
        jugador_actual = self.current_player
        possible = self._board.mark(fil, col, jugador_actual.symbol)
        if possible:
            self.next_turn()
            return True
        return False

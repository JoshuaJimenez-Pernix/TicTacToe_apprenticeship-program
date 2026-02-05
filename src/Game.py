from src.board import Board
from src.player import Player


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

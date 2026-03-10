from src.Board import Board
from src.Player import Player


class Game:

    def __init__(self, player1, player2):
        self._board = Board()
        self._players = [player1, player2]
        self._current_index = 0
        self.running = False
        self._score = {player1.symbol: 0, player2.symbol: 0, "draw": 0}
    

    @property
    def board(self):
        return self._board  

    @property
    def current_player(self):
        return self._players[self._current_index]
    
    @property
    def score(self):
        """Returns the current score."""
        return self._copy_score()
    
    def _copy_score(self):
        """Returns a copy of the score dictionary."""
        return self._score.copy()
    
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

    def isOver(self):
        """
        Indica si la partida ha terminado (victoria o empate).
        """
        estado = self.boardCheck()
        return estado["status"] in ["win", "draw"]
    
    def startGame(self):
        self.running = True
    
    def stopGame(self):
        self.running = False

    def reset(self):
        """
        Reinicia el juego a su estado inicial:
        - Limpia el tablero
        - Reinicia al primer jugador
        - Establece el estado del juego como no terminado
        """
        self._board.reset()
        self._current_index = 0
        self.running = False

    def reset_score(self):
        """Reinicia el marcador a cero."""
        for key in self._score:
            self._score[key] = 0

    def update_score(self, result: str):
        """
        Actualiza el marcador según el resultado del juego.
        
        Args:
            result: "X", "O" para victoria, o "draw" para empate
        """
        if result in self._score:
            self._score[result] += 1

    def boardCheck(self):
        """
        Devuelve el estado actual de la partida desde la perspectiva del juego.

        Returns:
            dict: {
                "status": "win" | "draw" | "ongoing",
                "winner": Player | None,
            }
        """
        board_state = self._board.search()
        status = board_state["status"]
        winner_symbol = board_state["winner_symbol"]

        if status == "win" and winner_symbol is not None:
            winner_player = next(
                player for player in self._players if player.symbol == winner_symbol
            )
            return {
                "status": "win",
                "winner": winner_player,
            }

        if status == "draw":
            return {
                "status": "draw",
                "winner": None,
            }

        return {
            "status": "ongoing",
            "winner": None,
        }

    
    

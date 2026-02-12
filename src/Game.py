from src.Board import Board
from src.Player import Player


class Game:

    def __init__(self, player1, player2):
        self._board = Board()
        self._players = [player1, player2]
        self._current_index = 0
        self.running = False
    

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

    
    

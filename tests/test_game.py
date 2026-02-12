"""Unit tests for Game: flow, make_move, winner, tie."""
from src.Board import Board
from src.Player import Player
from src.Game import Game
import pytest

@pytest.fixture
def players() -> tuple[Player, Player]:
    return Player("X", "Jugador 1"), Player("O", "Jugador 2")

@pytest.fixture
def game(players: tuple[Player, Player]) -> Game:
    return Game(players[0], players[1])

class TestGameFlow:
    """Tests for game flow and turns."""

    def test_current_player_starts_with_x(self, game: Game, players: tuple[Player, Player]) -> None:
        assert game.current_player.symbol == "X"
        assert game.current_player is players[0]



class TestGameStatusMessage:
    """Tests for status messages."""

    def test_status_during_play(self, game: Game) -> None:
        msg = game.get_status()
        assert "Turno" in msg
        assert "X" in msg
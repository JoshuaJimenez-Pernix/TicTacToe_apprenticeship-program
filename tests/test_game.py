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
    
    def test_make_mark_switches_turn(self, game: Game, players: tuple[Player, Player]) -> None:
        game.make_mark((0, 0))
        assert game.current_player.symbol == "O"
        assert game.current_player is players[1]
        game.make_mark((1, 0))
        assert game.current_player.symbol == "X"

    def test_make_move_invalid_does_not_switch(self, game: Game) -> None:
        game.make_mark((0, 0))
        game.make_mark((0, 0))  # same cell
        assert game.current_player.symbol == "O"
        game.make_mark((5, 5))  # out of bounds (place returns False)
        assert game.current_player.symbol == "O"

    def test_make_move_returns_true_when_valid(self, game: Game) -> None:
        assert game.make_mark((0, 0)) is True
        assert game.make_mark((1, 1)) is True

    def test_make_move_returns_false_when_invalid(self, game: Game) -> None:
        game.make_mark((0, 0))
        assert game.make_mark((0, 0)) is False

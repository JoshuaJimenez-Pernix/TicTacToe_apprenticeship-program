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


class TestGameWinnerDetection:
    """Tests for automatic win detection after each move."""

    def test_detect_winner_row_0(self, game: Game, players: tuple[Player, Player]) -> None:
        """Test winning by having three marks in the first row."""
        # Player X moves
        game.make_mark((0, 0))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((0, 1))  # X
        game.make_mark((1, 1))  # O
        game.make_mark((0, 2))  # X - wins!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"
        assert estado["winner"] is players[0]

    def test_detect_winner_row_1(self, game: Game, players: tuple[Player, Player]) -> None:
        """Test winning by having three marks in the second row."""
        game.make_mark((2, 0))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((2, 1))  # X
        game.make_mark((1, 1))  # O
        game.make_mark((2, 2))  # X
        game.make_mark((1, 2))  # O - wins!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"
        assert estado["winner"] is players[1]

    def test_detect_winner_column_0(self, game: Game, players: tuple[Player, Player]) -> None:
        """Test winning by having three marks in the first column."""
        game.make_mark((0, 0))  # X
        game.make_mark((0, 1))  # O
        game.make_mark((1, 0))  # X
        game.make_mark((1, 1))  # O
        game.make_mark((2, 0))  # X - wins!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"
        assert estado["winner"] is players[0]

    def test_detect_winner_column_2(self, game: Game, players: tuple[Player, Player]) -> None:
        """Test winning by having three marks in the third column."""
        game.make_mark((0, 2))  # X
        game.make_mark((0, 0))  # O
        game.make_mark((1, 2))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((2, 2))  # X
        game.make_mark((2, 0))  # O - wins!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"
        assert estado["winner"] is players[1]

    def test_detect_winner_main_diagonal(self, game: Game, players: tuple[Player, Player]) -> None:
        """Test winning by having three marks in the main diagonal (top-left to bottom-right)."""
        game.make_mark((0, 0))  # X
        game.make_mark((0, 1))  # O
        game.make_mark((1, 1))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((2, 2))  # X - wins!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"
        assert estado["winner"] is players[0]

    def test_detect_winner_secondary_diagonal(self, game: Game, players: tuple[Player, Player]) -> None:
        """Test winning by having three marks in the secondary diagonal (top-right to bottom-left)."""
        game.make_mark((0, 2))  # X
        game.make_mark((0, 0))  # O
        game.make_mark((1, 1))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((2, 0))  # X - wins!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"
        assert estado["winner"] is players[0]

    def test_detect_ongoing_game(self, game: Game) -> None:
        """Test that game is not over when there's no winner yet."""
        game.make_mark((0, 0))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((0, 1))  # X
        
        assert game.isOver() is False
        estado = game.boardCheck()
        assert estado["status"] == "ongoing"
        assert estado["winner"] is None


class TestGameDrawDetection:
    """Tests for draw detection when all cells are filled with no winner."""

    def test_detect_draw_full_board_no_winner(self, game: Game) -> None:
        """Test draw detection when board is full with no winner."""
        # Create a draw scenario:
        # X | O | X
        # X | O | O
        # O | X | X
        game.make_mark((0, 0))  # X
        game.make_mark((0, 1))  # O
        game.make_mark((0, 2))  # X
        game.make_mark((1, 1))  # O
        game.make_mark((1, 0))  # X
        game.make_mark((1, 2))  # O
        game.make_mark((2, 1))  # X
        game.make_mark((2, 0))  # O
        game.make_mark((2, 2))  # X - board full, draw!
        
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "draw"
        assert estado["winner"] is None

    def test_detect_draw_after_win_not_possible(self, game: Game) -> None:
        """Test that once there's a winner, game is over (not draw)."""
        # X wins in first row
        game.make_mark((0, 0))  # X
        game.make_mark((1, 0))  # O
        game.make_mark((0, 1))  # X
        game.make_mark((1, 1))  # O
        game.make_mark((0, 2))  # X - wins!
        
        # Even if more moves are made, status should be win
        assert game.isOver() is True
        estado = game.boardCheck()
        assert estado["status"] == "win"

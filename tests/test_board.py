
"""Unit tests for Board: validation, win, tie."""
from src.Board import Board
import pytest


class TestBoardDisplay:
    """Tests for board string representation."""

    def test_str_empty_board(self) -> None:
        board = Board()
        s = str(board)
        assert " | " in s
        assert "---" in s
        assert " " in s
    
    def test_str_after_placements(self) -> None:
        board = Board()
        board.mark(0, 0, "X")
        board.mark(1, 1, "O")
        s = str(board)
        assert "X" in s
        assert "O" in s

class TestBoardValidation:
    """Tests for move validation."""

    def test_valid_move_empty_cell(self) -> None:
        board = Board()
        assert board.valid_move(0, 0) is True
        assert board.valid_move(1, 2) is True
        assert board.valid_move(2, 2) is True

    def test_invalid_move_out_of_bounds_negative(self) -> None:
        board = Board()
        assert board.valid_move(-1, 0) is False
        assert board.valid_move(0, -1) is False
        assert board.valid_move(-1, -1) is False

    def test_invalid_move_out_of_bounds_too_large(self) -> None:
        board = Board()
        assert board.valid_move(3, 0) is False
        assert board.valid_move(0, 3) is False
        assert board.valid_move(3, 3) is False

    def test_invalid_move_occupied_cell(self) -> None:
        board = Board()
        board.mark(0, 0, "X")
        assert board.valid_move(0, 0) is False
        assert board.valid_move(0, 1) is True

    def test_mark_returns_true_when_valid(self) -> None:
        board = Board()
        assert board.mark(0, 0, "X") is True
        assert board.mark(1, 1, "O") is True

    def test_mark_returns_false_when_invalid(self) -> None:
        board = Board()
        board.mark(0, 0, "X")
        assert board.mark(0, 0, "O") is False
        assert board.mark(-1, 0, "O") is False
        assert board.mark(0, 3, "O") is False


class TestBoardWinnerDetection:
    """Tests for automatic winner detection in rows, columns, and diagonals."""

    def test_get_winner_row_0(self) -> None:
        """Test get_winner() detects winner in first row."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(0, 1, "X")
        board.mark(0, 2, "X")
        
        assert board.get_winner() == "X"

    def test_get_winner_row_1(self) -> None:
        """Test get_winner() detects winner in second row."""
        board = Board()
        board.mark(1, 0, "O")
        board.mark(1, 1, "O")
        board.mark(1, 2, "O")
        
        assert board.get_winner() == "O"

    def test_get_winner_row_2(self) -> None:
        """Test get_winner() detects winner in third row."""
        board = Board()
        board.mark(2, 0, "X")
        board.mark(2, 1, "X")
        board.mark(2, 2, "X")
        
        assert board.get_winner() == "X"

    def test_get_winner_column_0(self) -> None:
        """Test get_winner() detects winner in first column."""
        board = Board()
        board.mark(0, 0, "O")
        board.mark(1, 0, "O")
        board.mark(2, 0, "O")
        
        assert board.get_winner() == "O"

    def test_get_winner_column_1(self) -> None:
        """Test get_winner() detects winner in second column."""
        board = Board()
        board.mark(0, 1, "X")
        board.mark(1, 1, "X")
        board.mark(2, 1, "X")
        
        assert board.get_winner() == "X"

    def test_get_winner_column_2(self) -> None:
        """Test get_winner() detects winner in third column."""
        board = Board()
        board.mark(0, 2, "O")
        board.mark(1, 2, "O")
        board.mark(2, 2, "O")
        
        assert board.get_winner() == "O"

    def test_get_winner_main_diagonal(self) -> None:
        """Test get_winner() detects winner in main diagonal (top-left to bottom-right)."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(1, 1, "X")
        board.mark(2, 2, "X")
        
        assert board.get_winner() == "X"

    def test_get_winner_secondary_diagonal(self) -> None:
        """Test get_winner() detects winner in secondary diagonal (top-right to bottom-left)."""
        board = Board()
        board.mark(0, 2, "O")
        board.mark(1, 1, "O")
        board.mark(2, 0, "O")
        
        assert board.get_winner() == "O"

    def test_get_winner_no_winner(self) -> None:
        """Test get_winner() returns None when there's no winner."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(0, 1, "O")
        board.mark(0, 2, "X")
        
        assert board.get_winner() is None

    def test_is_full_true(self) -> None:
        """Test is_full() returns True when board is full."""
        board = Board()
        marks = [
            (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
            (1, 0, "O"), (1, 1, "X"), (1, 2, "O"),
            (2, 0, "X"), (2, 1, "O"), (2, 2, "X")
        ]
        for fil, col, symbol in marks:
            board.mark(fil, col, symbol)
        
        assert board.is_full() is True

    def test_is_full_false(self) -> None:
        """Test is_full() returns False when board is not full."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(0, 1, "O")
        
        assert board.is_full() is False

    def test_search_returns_win_status(self) -> None:
        """Test search() returns 'win' status when there's a winner."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(0, 1, "X")
        board.mark(0, 2, "X")
        
        result = board.search()
        assert result["status"] == "win"
        assert result["winner_symbol"] == "X"

    def test_search_returns_draw_status(self) -> None:
        """Test search() returns 'draw' status when board is full with no winner."""
        board = Board()
        marks = [
            (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
            (1, 0, "X"), (1, 1, "O"), (1, 2, "O"),
            (2, 0, "O"), (2, 1, "X"), (2, 2, "X")
        ]
        for fil, col, symbol in marks:
            board.mark(fil, col, symbol)
        
        result = board.search()
        assert result["status"] == "draw"
        assert result["winner_symbol"] is None

    def test_search_returns_ongoing_status(self) -> None:
        """Test search() returns 'ongoing' status when game is not over."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(0, 1, "O")
        
        result = board.search()
        assert result["status"] == "ongoing"
        assert result["winner_symbol"] is None



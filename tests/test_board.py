
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



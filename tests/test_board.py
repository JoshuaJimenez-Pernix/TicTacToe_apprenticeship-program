
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
"""Unit tests for Player."""
from src.Player import Player
import pytest


class TestPlayer:
    """Tests for Player class."""

    def test_player_x(self) -> None:
        p = Player("X","")
        assert p.symbol == "X"
        assert "X" in p.name

    def test_player_o(self) -> None:
        p = Player("O","")
        assert p.symbol == "O"
        assert "O" in p.name

    def test_player_custom_name(self) -> None:
        p = Player("X", "Alice")
        assert p.symbol == "X"
        assert p.name == "Alice"

    def test_invalid_symbol_raises(self) -> None:
        with pytest.raises(ValueError, match="El símbolo debe ser 'X' o 'O'"):
            Player("Z","")
        with pytest.raises(ValueError, match="El símbolo debe ser 'X' o 'O'"):
            Player("","")

    def test_str_representation(self) -> None:
        p = Player("X", "Bob")
        s = str(p)
        assert "Bob" in s
        assert "X" in s
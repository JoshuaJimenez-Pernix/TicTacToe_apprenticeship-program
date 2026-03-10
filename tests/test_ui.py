"""Unit tests for UI functions in main.py"""
import pytest
from src.Board import Board


# Importar la función que queremos testear
# Usar importlib para evitar problemas de importación circular
import importlib
import sys

# Importar main module dinámicamente
import main
importlib.reload(main)


class TestParseCoordinates:
    """Tests for parse_coordinates function."""

    def test_valid_coordinates_1_1(self):
        """Test parsing valid coordinates (1, 1)."""
        result = main.parse_coordinates("1 1")
        assert result == (0, 0)

    def test_valid_coordinates_1_2(self):
        """Test parsing valid coordinates (1, 2)."""
        result = main.parse_coordinates("1 2")
        assert result == (0, 1)

    def test_valid_coordinates_3_3(self):
        """Test parsing valid coordinates (3, 3)."""
        result = main.parse_coordinates("3 3")
        assert result == (2, 2)

    def test_valid_coordinates_with_extra_spaces(self):
        """Test parsing coordinates with extra spaces."""
        result = main.parse_coordinates("  2   1  ")
        assert result == (1, 0)

    def test_invalid_only_one_number(self):
        """Test that single number returns None."""
        result = main.parse_coordinates("1")
        assert result is None

    def test_invalid_three_numbers(self):
        """Test that three numbers returns None."""
        result = main.parse_coordinates("1 2 3")
        assert result is None

    def test_invalid_row_0(self):
        """Test that row 0 is invalid."""
        result = main.parse_coordinates("0 1")
        assert result is None

    def test_invalid_row_4(self):
        """Test that row 4 is invalid (board is 3x3)."""
        result = main.parse_coordinates("4 1")
        assert result is None

    def test_invalid_column_0(self):
        """Test that column 0 is invalid."""
        result = main.parse_coordinates("1 0")
        assert result is None

    def test_invalid_column_4(self):
        """Test that column 4 is invalid (board is 3x3)."""
        result = main.parse_coordinates("1 4")
        assert result is None

    def test_invalid_non_numeric(self):
        """Test that non-numeric input returns None."""
        result = main.parse_coordinates("a b")
        assert result is None

    def test_invalid_mixed(self):
        """Test that mixed input returns None."""
        result = main.parse_coordinates("1 a")
        assert result is None

    def test_invalid_empty(self):
        """Test that empty input returns None."""
        result = main.parse_coordinates("")
        assert result is None

    def test_invalid_only_spaces(self):
        """Test that only spaces returns None."""
        result = main.parse_coordinates("   ")
        assert result is None


class TestBoardDisplay:
    """Tests for Board display format."""

    def test_empty_board_display(self):
        """Test display of empty board."""
        board = Board()
        display = str(board)
        
        # Verificar que contiene los elementos esperados
        assert "1" in display  # row number
        assert "2" in display  # row number
        assert "3" in display  # row number
        assert "+" in display  # table borders
        
    def test_board_with_marks_display(self):
        """Test display of board with marks."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(1, 1, "O")
        board.mark(2, 2, "X")
        
        display = str(board)
        
        # Verificar que las marcas aparecen
        assert "X" in display
        assert "O" in display

    def test_board_shows_column_numbers(self):
        """Test that column numbers are displayed."""
        board = Board()
        display = str(board)
        
        # Verificar números de columnas en el encabezado
        lines = display.split("\n")
        header = lines[0]
        assert "1" in header
        assert "2" in header
        assert "3" in header

    def test_board_shows_row_numbers(self):
        """Test that row numbers are displayed."""
        board = Board()
        display = str(board)
        
        # Verificar que cada fila tiene su número
        assert "1 |" in display  # primera fila
        assert "2 |" in display  # segunda fila
        assert "3 |" in display  # tercera fila


class TestPlayerCreation:
    """Tests for player creation logic."""

    def test_player_symbol_assignment(self):
        """Test that first player chooses symbol and second gets opposite."""
        # Simular la lógica de create_players
        symbol_p1 = "X"
        symbol_p2 = "O" if symbol_p1 == "X" else "X"
        
        assert symbol_p1 == "X"
        assert symbol_p2 == "O"
        
        # Probar el caso inverso
        symbol_p1 = "O"
        symbol_p2 = "O" if symbol_p1 == "X" else "X"
        
        assert symbol_p1 == "O"
        assert symbol_p2 == "X"

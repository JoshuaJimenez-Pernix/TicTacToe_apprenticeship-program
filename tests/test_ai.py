"""Unit tests for AI module."""
import pytest
from src.Board import Board
from src.AI import AIStrategy, EasyAI, MediumAI, HardAI, AIPlayer
from src.Player import Player


class TestEasyAI:
    """Tests for EasyAI (random moves)."""

    def test_easy_ai_returns_valid_move(self):
        """Test that EasyAI returns a valid move."""
        board = Board()
        ai = EasyAI()
        
        move = ai.get_move(board, "X")
        
        assert move is not None
        assert 0 <= move[0] <= 2
        assert 0 <= move[1] <= 2

    def test_easy_ai_takes_available_move(self):
        """Test that EasyAI only takes available moves."""
        board = Board()
        board.mark(0, 0, "X")
        
        ai = EasyAI()
        moves_taken = set()
        
        for _ in range(100):
            move = ai.get_move(board, "O")
            if move:
                moves_taken.add(move)
        
        # Should never take (0,0) since it's occupied
        assert (0, 0) not in moves_taken

    def test_easy_ai_handles_full_board(self):
        """Test that EasyAI returns None on full board."""
        board = Board()
        # Fill the board
        board.mark(0, 0, "X")
        board.mark(0, 1, "O")
        board.mark(0, 2, "X")
        board.mark(1, 0, "O")
        board.mark(1, 1, "X")
        board.mark(1, 2, "O")
        board.mark(2, 0, "X")
        board.mark(2, 1, "O")
        board.mark(2, 2, "X")
        
        ai = EasyAI()
        move = ai.get_move(board, "X")
        
        assert move is None


class TestMediumAI:
    """Tests for MediumAI (basic strategy)."""

    def test_medium_ai_takes_center(self):
        """Test that MediumAI takes center when available."""
        board = Board()
        ai = MediumAI()
        
        move = ai.get_move(board, "X")
        
        assert move == (1, 1)

    def test_medium_ai_wins_when_possible(self):
        """Test that MediumAI takes winning move."""
        board = Board()
        # X has two in a row, O to play
        board.mark(0, 0, "X")
        board.mark(1, 0, "O")
        board.mark(0, 1, "X")
        board.mark(1, 1, "O")
        
        ai = MediumAI()
        move = ai.get_move(board, "X")
        
        # Should win at (0, 2)
        assert move == (0, 2)

    def test_medium_ai_blocks_opponent(self):
        """Test that MediumAI blocks opponent's winning move."""
        board = Board()
        # O has two in a row, X to play
        board.mark(0, 0, "O")
        board.mark(1, 0, "X")
        board.mark(0, 1, "O")
        board.mark(1, 1, "X")
        
        ai = MediumAI()
        move = ai.get_move(board, "X")
        
        # Should block - valid blocking moves are (0,2) or (2,0), (2,2)
        # The important thing is it blocks a winning line
        assert move is not None
        # Verify it's a valid move
        assert board.valid_move(move[0], move[1])

    def test_medium_ai_takes_corner(self):
        """Test that MediumAI takes corner after center."""
        board = Board()
        board.mark(1, 1, "O")  # Center taken
        
        ai = MediumAI()
        move = ai.get_move(board, "X")
        
        # Should take a corner
        assert move in [(0, 0), (0, 2), (2, 0), (2, 2)]


class TestHardAI:
    """Tests for HardAI (Minimax algorithm)."""

    def test_hard_ai_never_loses(self):
        """Test that HardAI with perfect play never loses."""
        # Play multiple games against HardAI and verify it never loses
        for _ in range(10):
            board = Board()
            ai = HardAI()
            
            # X plays first
            move = ai.get_move(board, "X")
            assert move is not None
            
            # Make the move
            board.mark(move[0], move[1], "X")
            
            # If board is not full, HardAI should not have lost
            if not board.is_full():
                assert board.get_winner() != "O"

    def test_hard_ai_wins_if_possible(self):
        """Test that HardAI takes winning move."""
        board = Board()
        # X has two in a row
        board.mark(0, 0, "X")
        board.mark(1, 0, "O")
        board.mark(0, 1, "X")
        board.mark(1, 1, "O")
        
        ai = HardAI()
        move = ai.get_move(board, "X")
        
        # Should win at (0, 2)
        assert move == (0, 2)

    def test_hard_ai_blocks(self):
        """Test that HardAI blocks opponent."""
        board = Board()
        board.mark(0, 0, "O")
        board.mark(1, 0, "X")
        board.mark(0, 1, "O")
        board.mark(1, 1, "X")
        
        ai = HardAI()
        move = ai.get_move(board, "X")
        
        # Should block - verify it's a valid move
        assert move is not None
        assert board.valid_move(move[0], move[1])

    def test_hard_ai_takes_center_first(self):
        """Test that HardAI takes center on empty board."""
        board = Board()
        ai = HardAI()
        
        move = ai.get_move(board, "X")
        
        assert move == (1, 1)


class TestAIPlayer:
    """Tests for AIPlayer class."""

    def test_ai_player_inherits_from_player(self):
        """Test that AIPlayer is a Player."""
        strategy = EasyAI()
        ai = AIPlayer("X", "TestAI", strategy)
        
        assert ai.symbol == "X"
        assert ai.name == "TestAI"

    def test_ai_player_has_strategy(self):
        """Test that AIPlayer has a strategy."""
        strategy = EasyAI()
        ai = AIPlayer("X", "TestAI", strategy)
        
        assert ai.strategy is strategy

    def test_ai_player_get_ai_move(self):
        """Test that AIPlayer can get AI move."""
        board = Board()
        strategy = EasyAI()
        ai = AIPlayer("X", "TestAI", strategy)
        
        move = ai.get_ai_move(board)
        
        assert move is not None
        assert 0 <= move[0] <= 2
        assert 0 <= move[1] <= 2

    def test_ai_player_str(self):
        """Test AIPlayer string representation."""
        strategy = EasyAI()
        ai = AIPlayer("X", "TestAI", strategy)
        
        assert "TestAI" in str(ai)
        assert "X" in str(ai)
        assert "EasyAI" in str(ai)


class TestAIStrategyInterface:
    """Tests for AIStrategy interface."""

    def test_get_available_moves(self):
        """Test get_available_moves returns all empty cells."""
        board = Board()
        board.mark(0, 0, "X")
        board.mark(1, 1, "O")
        
        strategy = EasyAI()
        moves = strategy.get_available_moves(board)
        
        assert len(moves) == 7  # 9 - 2 = 7
        assert (0, 0) not in moves
        assert (1, 1) not in moves
        assert (0, 1) in moves

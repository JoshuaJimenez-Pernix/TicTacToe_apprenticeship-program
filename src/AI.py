"""
Módulo de Inteligencia Artificial para Tic-Tac-Toe.

Implementa el patrón Strategy para permitir diferentes niveles de dificultad:
- EasyAI: Movimientos aleatorios
- MediumAI: Estrategia básica (bloquea, toma centro)
- HardAI: Algoritmo Minimax (invencible)
"""
from abc import ABC, abstractmethod
from typing import Optional
import random
from src.Board import Board
from src.Player import Player


class AIStrategy(ABC):
    """
    Clase abstracta base para estrategias de IA.
    
    Sigue el principio Open/Closed: podemos agregar nuevas estrategias
    sin modificar las existentes.
    """
    
    @abstractmethod
    def get_move(self, board: Board, player_symbol: str) -> Optional[tuple[int, int]]:
        """
        Calcula el siguiente movimiento para la IA.
        
        Args:
            board: El tablero actual del juego
            player_symbol: El símbolo de la IA ('X' u 'O')
            
        Returns:
            Tupla (fila, columna) con las coordenadas del movimiento, o None si no hay movimientos disponibles
        """
        pass
    
    def get_available_moves(self, board: Board) -> list[tuple[int, int]]:
        """Retorna lista de movimientos disponibles."""
        moves = []
        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                if board.valid_move(row, col):
                    moves.append((row, col))
        return moves


class EasyAI(AIStrategy):
    """
    IA de dificultad fácil - movimientos completamente aleatorios.
    
    Principio Single Responsibility: solo se encarga de movimientos aleatorios.
    """
    
    def get_move(self, board: Board, player_symbol: str) -> Optional[tuple[int, int]]:
        """Retorna un movimiento aleatorio válido."""
        available_moves = self.get_available_moves(board)
        if not available_moves:
            return None
        return random.choice(available_moves)


class MediumAI(AIStrategy):
    """
    IA de dificultad media - estrategia básica.
    
    Estrategia:
    1. Ganar si tiene oportunidad
    2. Bloquear al oponente si va a ganar
    3. Tomar el centro si está disponible
    4. Tomar una esquina si está disponible
    5. Movimiento aleatorio
    
    Principio Single Responsibility: solo se encarga de la lógica de dificultad media.
    """
    
    def get_move(self, board: Board, player_symbol: str) -> Optional[tuple[int, int]]:
        opponent_symbol = "O" if player_symbol == "X" else "X"
        
        # 0. Si el centro está disponible, tomarlo (solo en el primer o segundo movimiento)
        if board.valid_move(1, 1):
            available = self.get_available_moves(board)
            if len(available) >= 8:  # Primer o segundo movimiento
                return (1, 1)
        
        # 1. Ganar si tiene oportunidad
        winning_move = self._find_winning_move(board, player_symbol)
        if winning_move:
            return winning_move
        
        # 2. Bloquear al oponente - verificar cada posición vacía
        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                if board.valid_move(row, col):
                    # Simular que el oponente juega aquí
                    board.mark(row, col, opponent_symbol)
                    if board.get_winner() == opponent_symbol:
                        board._grid[row][col] = Board.EMPTY
                        return (row, col)
                    board._grid[row][col] = Board.EMPTY
        
        # 3. Tomar el centro si está disponible
        if board.valid_move(1, 1):
            return (1, 1)
        
        # 4. Tomar una esquina
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [c for c in corners if board.valid_move(c[0], c[1])]
        if available_corners:
            return random.choice(available_corners)
        
        # 5. Movimiento aleatorio
        return self.get_available_moves(board)[0] if self.get_available_moves(board) else None
    
    def _find_winning_move(self, board: Board, symbol: str) -> Optional[tuple[int, int]]:
        """Encuentra un movimiento que resulte en victoria o bloqueo."""
        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                if board.valid_move(row, col):
                    # Simular el movimiento
                    board.mark(row, col, symbol)
                    if board.get_winner() == symbol:
                        board._grid[row][col] = Board.EMPTY  # Deshacer
                        return (row, col)
                    board._grid[row][col] = Board.EMPTY  # Deshacer
        return None
    
    def _find_blocking_move(self, board: Board, opponent_symbol: str) -> Optional[tuple[int, int]]:
        """Encuentra un movimiento que bloquee al oponente."""
        return self._find_winning_move(board, opponent_symbol)


class HardAI(AIStrategy):
    """
    IA de dificultad difícil - algoritmo Minimax (invencible).
    
    Utiliza el algoritmo Minimax con poda alfa-beta para encontrar
    la mejor decisión posible.
    
    Principio Single Responsibility: solo se encarga de la lógica Minimax.
    """
    
    def get_move(self, board: Board, player_symbol: str) -> Optional[tuple[int, int]]:
        """Encuentra el mejor movimiento usando Minimax."""
        available_moves = self.get_available_moves(board)
        if not available_moves:
            return None
        
        # Si es el primer movimiento, tomar el centro
        center = (1, 1)
        if center in available_moves and len(available_moves) == 9:
            return center
        
        best_score = float('-inf')
        best_move = None
        
        for move in available_moves:
            # Hacer el movimiento
            board.mark(move[0], move[1], player_symbol)
            
            # Calcular score
            score = self._minimax(
                board, 
                0, 
                False, 
                player_symbol,
                float('-inf'), 
                float('inf')
            )
            
            # Deshacer el movimiento
            board._grid[move[0]][move[1]] = Board.EMPTY
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(
        self, 
        board: Board, 
        depth: int, 
        is_maximizing: bool, 
        player_symbol: str,
        alpha: float,
        beta: float
    ) -> float:
        """
        Algoritmo Minimax con poda alfa-beta.
        
        Args:
            board: Estado actual del tablero
            depth: Profundidad actual en el árbol
            is_maximizing: True si es turno de maximización
            player_symbol: Símbolo del jugador IA
            alpha: Mejor valor para el maximizador
            beta: Mejor valor para el minimizador
            
        Returns:
            Valor de utilidad del estado actual
        """
        opponent_symbol = "O" if player_symbol == "X" else "X"
        
        # Verificar estado terminal
        winner = board.get_winner()
        if winner == player_symbol:
            return 10 - depth  # Victoria - preferimos ganar más rápido
        if winner == opponent_symbol:
            return depth - 10  # Derrota - preferimos perder más lento
        if board.is_full():
            return 0  # Empate
        
        available_moves = self.get_available_moves(board)
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in available_moves:
                board.mark(move[0], move[1], player_symbol)
                eval = self._minimax(board, depth + 1, False, player_symbol, alpha, beta)
                board._grid[move[0]][move[1]] = Board.EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Poda beta
            return max_eval
        else:
            min_eval = float('inf')
            for move in available_moves:
                board.mark(move[0], move[1], opponent_symbol)
                eval = self._minimax(board, depth + 1, True, player_symbol, alpha, beta)
                board._grid[move[0]][move[1]] = Board.EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Poda alfa
            return min_eval


class AIPlayer(Player):
    """
    Jugador controlado por Inteligencia Artificial.
    
    Extiende Player para integrarse con el sistema existente.
    Usa composición (has-a) con AIStrategy en lugar de herencia,
    siguiendo el principio de Dependency Inversion.
    """
    
    def __init__(self, symbol: str, name: str, strategy: AIStrategy):
        """
        Inicializa un jugador IA.
        
        Args:
            symbol: Símbolo del jugador ('X' o 'O')
            name: Nombre del jugador
            strategy: Estrategia de IA a usar
        """
        super().__init__(symbol, name)
        self._strategy = strategy
    
    @property
    def strategy(self) -> AIStrategy:
        """Retorna la estrategia de IA."""
        return self._strategy
    
    def get_ai_move(self, board: Board) -> Optional[tuple[int, int]]:
        """
        Obtiene el siguiente movimiento de la IA.
        
        Args:
            board: Estado actual del tablero
            
        Returns:
            Tupla (fila, columna) con el movimiento decidido
        """
        return self._strategy.get_move(board, self.symbol)
    
    def __str__(self):
        return f"{self._name} (AI-{self._strategy.__class__.__name__})({self.symbol})"

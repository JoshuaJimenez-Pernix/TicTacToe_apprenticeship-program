from src.Board import Board
#from src.Game import Game
from src.Player import Player

def run_game():
    print("\n=== TicTacToe ===\n")
    print("Bienvenido to TicTacToe Game")
    #Board
    board = Board()
    print(board)

    #Type
    type = 2
    """ Future request 
    type = input("Select the type of game (1: Human vs Human, 2: Human vs Computer): ")
    while symbolP1 not in ["X", "O"]:
        symbolP1 = input("Invalid symbol. Please select X or O:").strip().upper()
    """
    #Players
    nameP1 = input("Write your name: ")
    symbolP1 = input("Select your simbol(X|O):").strip().upper()
    while symbolP1 not in ["X", "O"]:
        symbolP1 = input("Invalid symbol. Please select X or O:").strip().upper()
    symbolP2 = "O" if symbolP1 == "X" else "X"
    if type == 1:
        nameP2 = input("Write second player name: ")
    else:
        nameP2 = "Computer (AI)"
    player1 = Player(symbolP1, nameP1)
    player2 = Player(symbolP2, nameP2)
    print(f"{player1.name} will use {player1.symbol}")
    print(f"{player2.name} will use {player2.symbol}")

    #Game
    #game = Game(board)
    #game.start()

if __name__ == "__main__":
    run_game()

from src.Board import Board
from src.Game import Game
from src.Player import Player

def run_game():
    print("\n=== TicTacToe ===\n")
    print("Bienvenido to TicTacToe Game")
    #Board
    board = Board()

    #Type
    type = 0
    """ Future request 
    type = input("Select the type of game (1: Human vs Human, 2: Human vs Computer): ")
    while symbolP1 not in ["X", "O"]:
        symbolP1 = input("Invalid symbol. Please select X or O:").strip().upper()
    """
    #Players
    #1st Player
    nameP1 = input("Write your name: ")
    symbolP1 = input("Select your simbol(X|O):").strip().upper()
    while symbolP1 not in ["X", "O"]:
        symbolP1 = input("Invalid symbol. Please select X or O:").strip().upper()
    
    #2nd player
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
    game = Game(player1, player2)

    while True:
        print(game.get_status())
        print(game.board)
        coordinates = input("Ingrese las coordinadas que quiere marcar : ").strip()
        coordinates = parse_coordnates(coordinates)
        if coordinates == None:
            print(
                "Coordenadas inválidas. Usa dos números del 1 al 3, "
                "por ejemplo: 1 1 o 2 3.\n"
            )
            continue
        valid = game.make_mark(coordinates)
        if not valid:
            print(" xxx Movimiento invalido xxx ")



    #game.next_turn()
    #print(game.get_status())

def parse_coordnates(input):
    texto = input.strip()
    text = texto.replace(""," ")
    partes = texto.split()

    if len(partes) != 2:
        return None
    
    try:
        fila = int(partes[0])
        col = int(partes[1])
        if fila >= 1 and fila <= Board.SIZE and col >= 1 and col <= Board.SIZE:
            return (fila - 1, col - 1)
    except ValueError:
        pass

    return None

if __name__ == "__main__":
    run_game()

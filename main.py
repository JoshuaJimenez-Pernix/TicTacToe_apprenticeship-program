from src.Board import Board
from src.Game import Game
from src.Player import Player


def create_players():
    """
    Solicita al usuario crear los jugadores y retorna los objetos Player.
    Permite seleccionar quién será 'X' y quién será 'O'.
    """
    print("\n=== Configuración de Jugadores ===")
    name_p1 = input("> Ingresa tu nombre: ")
    symbol_p1 = input("> Selecciona tu símbolo (X|O): ").strip().upper()
    
    while symbol_p1 not in ["X", "O"]:
        symbol_p1 = input("Símbolo inválido. Por favor selecciona X o O: ").strip().upper()
    
    # El segundo jugador usa el símbolo opuesto
    symbol_p2 = "O" if symbol_p1 == "X" else "X"
    name_p2 = input("> Ingresa el nombre del segundo jugador: ")
    
    player1 = Player(symbol_p1, name_p1)
    player2 = Player(symbol_p2, name_p2)
    
    print(f"{player1.name} usará '{player1.symbol}'")
    print(f"{player2.name} usará '{player2.symbol}'")
    
    return player1, player2


def play_game(player1, player2):
    """
    Ejecuta una partida de TicTacToe.
    Retorna True si el juego terminó, False si se reinició.
    """
    game = Game(player1, player2)
    
    while True:
        print("\n" + "=" * 40)
        print(game.get_status())
        print(game.board)
        print("=" * 40)
        print("\nOpciones:")
        print("  - Ingresa coordenadas (fila columna) para marcar")
        print("  - Escribe 'R' o 'reiniciar' para reiniciar el juego")
        print("  - Escribe 'S' o 'salir' para terminar el programa")
        
        choice = input("> Tu movimiento: ").strip().lower()
        
        # Opción de salir
        if choice in ["s", "salir"]:
            print("\n¡Gracias por jugar! Hasta luego.")
            return "exit"
        
        # Opción de reiniciar
        if choice in ["r", "reiniciar"]:
            print("\n--- Reiniciando juego ---")
            return "restart"
        
        # Intentar parsear coordenadas
        coordinates = parse_coordinates(choice)
        if coordinates is None:
            print("Coordenadas inválidas. Usa dos números del 1 al 3 (ej: 1 1 o 2 3).")
            continue
        
        # Realizar el movimiento
        if game.make_mark(coordinates):
            estado = game.boardCheck()
            if estado["status"] == "win":
                print("\n" + str(game.board))
                ganador = estado["winner"]
                print(f"\n¡{ganador.name} ha ganado la partida con '{ganador.symbol}'!")
                print("\nOpciones:")
                print("  - Presiona Enter para jugar de nuevo")
                print("  - Escribe 'S' o 'salir' para terminar")
                end_choice = input("> ").strip().lower()
                
                if end_choice in ["s", "salir"]:
                    return "exit"
                return "play_again"
            
            elif estado["status"] == "draw":
                print("\n" + str(game.board))
                print("\n¡La partida ha terminado en empate!")
                print("\nOpciones:")
                print("  - Presiona Enter para jugar de nuevo")
                print("  - Escribe 'S' o 'salir' para terminar")
                end_choice = input("> ").strip().lower()
                
                if end_choice in ["s", "salir"]:
                    return "exit"
                return "play_again"
        else:
            print("xxx Movimiento inválido xxx")


def parse_coordinates(input_text):
    """
    Parsea la entrada del usuario en coordenadas (fila, columna).
    Retorna None si la entrada es inválida.
    """
    partes = input_text.split()
    
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


def run_game():
    """
    Función principal que controla el flujo del juego.
    Maneja la creación de jugadores y el ciclo de juegos.
    """
    print("\n" + "=" * 50)
    print("       ¡Bienvenido a TicTacToe!")
    print("=" * 50)
    
    while True:
        # Crear nuevos jugadores
        player1, player2 = create_players()
        
        # Jugar una partida
        result = play_game(player1, player2)
        
        # Manejar el resultado
        if result == "exit":
            break
        # Si es "restart" o "play_again", el ciclo continúa y crea nuevos jugadores o reinicia
        
    print("\nJuego finalizado.")


if __name__ == "__main__":
    run_game()

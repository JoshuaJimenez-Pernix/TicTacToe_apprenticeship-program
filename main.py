from src.Board import Board
from src.Game import Game
from src.Player import Player


# Códigos de color ANSI
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def create_players():
    """
    Solicita al usuario crear los jugadores y retorna los objetos Player.
    Permite seleccionar quién será 'X' y quién será 'O'.
    """
    print("\n" + "=" * 40)
    print("      ⚙️  CONFIGURACIÓN DE JUGADORES  ⚙️")
    print("=" * 40)
    
    name_p1 = input("👉  Ingresa tu nombre: ").strip()
    while name_p1 == "":
        name_p1 = input("⚠️  Nombre no válido. Ingresa tu nombre: ").strip()
    
    symbol_p1 = input("👉  Selecciona tu símbolo (X|O): ").strip().upper()
    
    while symbol_p1 not in ["X", "O"]:
        symbol_p1 = input("⚠️  Símbolo inválido. Por favor selecciona X o O: ").strip().upper()
    
    # El segundo jugador usa el símbolo opuesto
    symbol_p2 = "O" if symbol_p1 == "X" else "X"
    
    name_p2 = input("👉  Ingresa el nombre del segundo jugador: ").strip()
    while name_p2 == "":
        name_p2 = input("⚠️  Nombre no válido. Ingresa el nombre: ").strip()
    
    player1 = Player(symbol_p1, name_p1)
    player2 = Player(symbol_p2, name_p2)
    
    print("\n✅  ¡Listo!")
    print(f"   🎮  {player1.name} será '{player1.symbol}'")
    print(f"   🎮  {player2.name} será '{player2.symbol}'")
    
    return player1, player2


def show_score(player1, player2, score):
    """Muestra el marcador actual."""
    print("\n" + "=" * 40)
    print("           📊  MARCADOR  📊")
    print("=" * 40)
    print(f"   {player1.name} ({player1.symbol}):  {score[player1.symbol]} victorias")
    print(f"   {player2.name} ({player2.symbol}):  {score[player2.symbol]} victorias")
    print(f"   Empates:  {score['draw']}")
    print("=" * 40)


def play_game(player1, player2, score):
    """
    Ejecuta una partida de TicTacToe.
    """
    game = Game(player1, player2)
    
    while True:
        print("\n" + "=" * 40)
        print(f"🎯  TURNO DE: {game.current_player.name} ({game.current_player.symbol})")
        print("=" * 40)
        print(game.board)
        print("=" * 40)
        print("📝  Instrucciones:")
        print("   - Ingresa las coordenadas (fila columna), ej: 1 2")
        print("   - Escribe 'R' para reiniciar el juego")
        print("   - Escribe 'S' para salir del programa")
        
        choice = input("\n👉  Tu movimiento: ").strip().lower()
        
        # Opción de salir
        if choice in ["s", "salir"]:
            print("\n🙏  ¡Gracias por jugar! Hasta luego.")
            return "exit"
        
        # Opción de reiniciar
        if choice in ["r", "reiniciar"]:
            print("\n🔄  Reiniciando juego...")
            return "restart"
        
        # Intentar parsear coordenadas
        coordinates = parse_coordinates(choice)
        if coordinates is None:
            print(f"\n{Colors.RED}⚠️  Coordenadas inválidas.{Colors.RESET}")
            print(f"{Colors.YELLOW}   Usa dos números del 1 al 3 (ej: 1 1 o 2 3){Colors.RESET}")
            continue
        
        # Realizar el movimiento
        if game.make_mark(coordinates):
            estado = game.boardCheck()
            if estado["status"] == "win":
                print("\n" + "=" * 40)
                print(game.board)
                print("=" * 40)
                ganador = estado["winner"]
                score[ganador.symbol] += 1
                print(f"\n{Colors.GREEN}{Colors.BOLD}🎉  ¡FELICIDADES! {ganador.name} ha ganado la partida!{Colors.RESET}")
                print(f"{Colors.GREEN}   Símbolo: '{ganador.symbol}'{Colors.RESET}")
                print("\n📊  ¿Qué deseas hacer ahora?")
                print("   - Presiona ENTER para jugar de nuevo")
                print("   - Escribe 'S' para salir")
                end_choice = input("\n👉  ").strip().lower()
                
                if end_choice in ["s", "salir"]:
                    return "exit"
                return "play_again"
            
            elif estado["status"] == "draw":
                print("\n" + "=" * 40)
                print(game.board)
                print("=" * 40)
                score['draw'] += 1
                print(f"\n{Colors.MAGENTA}{Colors.BOLD}🤝  ¡EMPATE! La partida ha terminado en tablas.{Colors.RESET}")
                print("\n📊  ¿Qué deseas hacer ahora?")
                print("   - Presiona ENTER para jugar de nuevo")
                print("   - Escribe 'S' para salir")
                end_choice = input("\n👉  ").strip().lower()
                
                if end_choice in ["s", "salir"]:
                    return "exit"
                return "play_again"
        else:
            print(f"\n{Colors.RED}❌  Movimiento inválido. Intenta de nuevo.{Colors.RESET}")


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
    print("\n" + "🌟  " + "=" * 40)
    print("      ¡BIENVENIDOS A TIC TAC TOE!")
    print("=" * 40 + "  🌟")
    print("🎮  Un juego para dos jugadores")
    print("📱  Juegan en el mismo dispositivo")
    
    # Marcador
    score = {"X": 0, "O": 0, "draw": 0}
    
    while True:
        # Crear nuevos jugadores
        player1, player2 = create_players()
        
        # Jugar una partida
        result = play_game(player1, player2, score)
        
        # Manejar el resultado
        if result == "exit":
            show_score(player1, player2, score)
            print("\n🙏  ¡Gracias por jugar! Hasta la próxima.")
            break
        # Si es "restart" o "play_again", el ciclo continúa


if __name__ == "__main__":
    run_game()

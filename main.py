from src.Board import Board
from src.Game import Game
from src.Player import Player
from src.AI import AIPlayer, EasyAI, MediumAI, HardAI


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


def select_game_mode():
    """
    Permite seleccionar el modo de juego:
    - 1: Jugador vs Jugador
    - 2: Jugador vs Computadora
    """
    print("\n" + "=" * 40)
    print("      🎮  SELECCIONAR MODO  🎮")
    print("=" * 40)
    print("   1️⃣  Jugador vs Jugador")
    print("   2️⃣  Jugador vs Computadora")
    print("=" * 40)
    
    while True:
        mode = input("\n👉  Selecciona una opción (1-2): ").strip()
        if mode in ["1", "2"]:
            return mode
        print(f"{Colors.RED}⚠️  Opción inválida. Intenta de nuevo.{Colors.RESET}")


def select_difficulty():
    """
    Permite seleccionar la dificultad de la IA.
    """
    print("\n" + "=" * 40)
    print("      🤖  SELECCIONAR DIFICULTAD  🤖")
    print("=" * 40)
    print("   1️⃣  Fácil    - La IA juega aleatoriamente")
    print("   2️⃣  Medio    - La IA usa estrategia básica")
    print("   3️⃣  Difícil  - La IA usa Minimax (casi imposible)")
    print("=" * 40)
    
    while True:
        diff = input("\n👉  Selecciona una opción (1-3): ").strip()
        if diff in ["1", "2", "3"]:
            return diff
        print(f"{Colors.RED}⚠️  Opción inválida. Intenta de nuevo.{Colors.RESET}")


def create_players_human():
    """
    Crea dos jugadores humanos.
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


def create_player_vs_ai():
    """
    Crea un jugador humano y una IA.
    """
    print("\n" + "=" * 40)
    print("      ⚙️  CONFIGURACIÓN DE JUGADOR  ⚙️")
    print("=" * 40)
    
    name_p1 = input("👉  Ingresa tu nombre: ").strip()
    while name_p1 == "":
        name_p1 = input("⚠️  Nombre no válido. Ingresa tu nombre: ").strip()
    
    symbol_p1 = input("👉  Selecciona tu símbolo (X|O): ").strip().upper()
    
    while symbol_p1 not in ["X", "O"]:
        symbol_p1 = input("⚠️  Símbolo inválido. Por favor selecciona X o O: ").strip().upper()
    
    # Seleccionar dificultad
    difficulty = select_difficulty()
    
    # Seleccionar estrategia de IA
    symbol_p2 = "O" if symbol_p1 == "X" else "X"
    
    if difficulty == "1":
        strategy = EasyAI()
        ai_name = "Computadora (Fácil)"
    elif difficulty == "2":
        strategy = MediumAI()
        ai_name = "Computadora (Medio)"
    else:
        strategy = HardAI()
        ai_name = "Computadora (Difícil)"
    
    player1 = Player(symbol_p1, name_p1)
    player2 = AIPlayer(symbol_p2, ai_name, strategy)
    
    print("\n✅  ¡Listo!")
    print(f"   🎮  {player1.name} será '{player1.symbol}'")
    print(f"   🤖  {player2.name} usará '{player2.symbol}'")
    
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


def is_ai_player(player) -> bool:
    """Verifica si un jugador es una IA."""
    return isinstance(player, AIPlayer)


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
        
        # Verificar si es turno de la IA
        if is_ai_player(game.current_player):
            print(f"{Colors.CYAN}🤖  La computadora está pensando...{Colors.RESET}")
            ai_move = game.current_player.get_ai_move(game.board)
            if ai_move:
                print(f"{Colors.CYAN}   La IA juega: {ai_move[0]+1} {ai_move[1]+1}{Colors.RESET}")
        else:
            print("📝  Instrucciones:")
            print("   - Ingresa las coordenadas (fila columna), ej: 1 2")
            print("   - Escribe 'R' para reiniciar el juego")
            print("   - Escribe 'S' para salir del programa")
        
        # Si es IA, hacer movimiento automáticamente
        if is_ai_player(game.current_player):
            input(f"\n{Colors.YELLOW}👉  Presiona Enter para continuar...{Colors.RESET}")
            if ai_move:
                game.make_mark(ai_move)
        else:
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
            if not game.make_mark(coordinates):
                print(f"\n{Colors.RED}❌  Movimiento inválido. Intenta de nuevo.{Colors.RESET}")
                continue
        
        # Verificar resultado del juego (solo si no fue movimiento de IA automática)
        if not is_ai_player(game.current_player) or (hasattr(game, '_last_ai_move') and game._last_ai_move):
            pass  # El resultado se verifica después de hacer el movimiento
        
        # Verificar estado del juego después del movimiento
        estado = game.boardCheck()
        if estado["status"] == "win":
            print("\n" + "=" * 40)
            print(game.board)
            print("=" * 40)
            ganador = estado["winner"]
            score[ganador.symbol] += 1
            
            if is_ai_player(ganador):
                print(f"\n{Colors.RED}{Colors.BOLD}💻  La computadora ha ganado!{Colors.RESET}")
            else:
                print(f"\n{Colors.GREEN}{Colors.BOLD}🎉  ¡FELICIDADES! {ganador.name} ha ganado la partida!{Colors.RESET}")
            
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
    print("🎮  Un juego clásico para dos jugadores")
    
    # Marcador
    score = {"X": 0, "O": 0, "draw": 0}
    
    while True:
        # Seleccionar modo de juego
        mode = select_game_mode()
        
        # Crear jugadores según el modo
        if mode == "1":
            player1, player2 = create_players_human()
        else:
            player1, player2 = create_player_vs_ai()
        
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

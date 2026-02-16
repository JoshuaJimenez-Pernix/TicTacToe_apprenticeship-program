class Board:
    SIZE = 3
    EMPTY = " "

    def __init__(self):
        self._grid = []
        for fila in range (self.SIZE):
            nueva_fila = []
            for columna in range (self.SIZE):
                nueva_fila.append(self.EMPTY)
            self._grid.append(nueva_fila)
    
    #Solo lectura
    @property
    def grid(self):
        copia = []
        for fila in self._grid:
            copia.append(fila[:])
        return copia

    def mark(self, fil, col, symbol):
        if self.valid_move(fil, col):
            self._grid[fil][col] = symbol
            return True
        return False

    def valid_move(self, fil, col):
        if fil < 0 or fil >= self.SIZE:
            return False
        if col < 0 or col >= self.SIZE:
            return False
        if self._grid[fil][col] != self.EMPTY:
            return False
        return True
    
    def __str__(self):
        lineas = []
        for i in range(self.SIZE):
            fila = self._grid[i]
            linea = " " + " | ".join(fila) + " "
            lineas.append(linea)
            if i < self.SIZE - 1:
                lineas.append("---+---+---")
        return "\n".join(lineas)

    def search(self):
        """
        Evalúa el estado actual del tablero.

        Returns:
            dict: {
                "status": "win" | "draw" | "ongoing",
                "winner_symbol": str | None,
            }
        """
        winner_symbol = self.get_winner()
        if winner_symbol is not None:
            return {
                "status": "win",
                "winner_symbol": winner_symbol,
            }

        if self.is_full():
            return {
                "status": "draw",
                "winner_symbol": None,
            }

        return {
            "status": "ongoing",
            "winner_symbol": None,
        }

    def get_winner(self):
        """
        Determina si hay un ganador en el tablero.

        Returns:
            str | None: símbolo del ganador ("X" u "O") o None si no hay ganador.
        """
        lineas = []

        # Filas
        for fila in self._grid:
            lineas.append(fila)

        # Columnas
        for col in range(self.SIZE):
            columna = [self._grid[fila][col] for fila in range(self.SIZE)]
            lineas.append(columna)

        # Diagonal principal
        diagonal_principal = [self._grid[i][i] for i in range(self.SIZE)]
        lineas.append(diagonal_principal)

        # Diagonal secundaria
        diagonal_secundaria = [
            self._grid[i][self.SIZE - 1 - i] for i in range(self.SIZE)
        ]
        lineas.append(diagonal_secundaria)

        for linea in lineas:
            simbolo = linea[0]
            if simbolo == self.EMPTY:
                continue
            if all(celda == simbolo for celda in linea):
                return simbolo

        return None

    def is_full(self):
        """
        Indica si el tablero está completamente lleno.

        Returns:
            bool: True si no hay casillas vacías, False en caso contrario.
        """
        for fila in self._grid:
            for celda in fila:
                if celda == self.EMPTY:
                    return False
        return True

    def reset(self):
        """
        Reinicia el tablero a su estado inicial (vacío).
        """
        for fila in range(self.SIZE):
            for columna in range(self.SIZE):
                self._grid[fila][columna] = self.EMPTY
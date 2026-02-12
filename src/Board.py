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
            if i < self.SIZE -1:
                lineas.append("---+---+---")
        return "\n".join(lineas)

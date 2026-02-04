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
    
    @property
    def grid(self):
        copia = []
        for fila in self._grid:
            copia.append(fila[:])
        return copia

    
    def __str__(self):
        lineas = []
        for i in range(self.SIZE):
            fila = self._grid[i]
            linea = " " + " | ".join(fila) + " "
            lineas.append(linea)
            if i < self.SIZE -1:
                lineas.append("---+---+---")
        return "\n".join(lineas)

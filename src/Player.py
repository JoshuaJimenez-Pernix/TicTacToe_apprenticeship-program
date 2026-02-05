class Player:

    def __init__(self, symbol, name):
        self._symbol = symbol
        if name == "":
            self._name = "Jugador " + symbol
        else:
            self._name = name
        
    
    @property
    def symbol(self):
        return self._symbol

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return self._name + "(" + self._symbol + ")"

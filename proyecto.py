class Ship: # clase base para todos los tipos de barcos
    def __init__(self, name, size): # constructo de la clase con parametro como nombre y tamaño
        self.name = name # self.name almacena el nombre del barco
        self.size = size # self.size almacena el tamaño del barco
        self.positions = [] # self.positións es una lista vacia que se almacenara con las coordenadas de los barcos que se coloquen en el tablero
        self.hits = 0 # self.hits cuenta la cantidad de veces que el barco ha sido impactado    

    def place_ship(self, start_row, start_col, direction, board): # es un metodo que intenta colocar colocar el barco en el tablero tiene como parametros, las coordenadas iniciales, la dirección y el tablero
        positions = [] # es una lista temporal donde se almacenara  la posiciones que ira ocupando el barco
        if direction == 'H': # si la dirección es horizontal
            if start_col + self.size > len(board[0]): # se verifica que el barco no se salga del tablero hacia la derecha
                return False # si lo hace devuelve False indicando que la colocación no es válida
            for i in range(self.size): # recorre cada posición donde se intentara colocar el barco
                if board[start_row][start_col + i] != ' ': # Si algunas de estas posiciones ya esta ocupada, devulve False
                    return False
                positions.append((start_row, start_col + i)) # si la posición esta libre devuelve positions
        elif direction == 'V': # si la direccion es vertical
            if start_row + self.size > len(board): # se verifica que el barco no se salga del tablero hacia abajo. si lo hace devuelve False
                return False
            for i in range(self.size): # recorre cada posicion donde se intentara colocar el barco
                if board[start_row + i][start_col] != ' ': # si alguna poiscion ya esta ocupada, devuelve false
                    return False
                positions.append((start_row + i, start_col)) # en caso este libre, lo añade a positions
        else: # en caso no se cumpla ninguna de estas dos condiciones 
            return False #  Si la direccion no es H ni V entonces devuelve False que no es válida
        
        for pos in positions: # recorre pos en cada una de las posiciones
            board[pos[0]][pos[1]] = self.name[0] # si la colocación es valida, actualiza el tablero board colocando la inicial del nombre del barco en cada una de las posiciones
        self.positions = positions # guarda las posiciones del barco en self.positions y devuelve verdadero indicando que la colocación fue exitosa
        return True

    def hit(self): # el metodo hit incrementa el contador de impactos cada vez que el barco es atacado
        self.hits += 1
        return self.hits == self.size # si el numero de impactos es igual al tamaño del barco, el barco es hundido y devuelve True, en caso contrario devuelve False

class Destroyer(Ship): # se define la subclase Destroyer
    def __init__(self):
        super().__init__('Destructor', 2) # es un barco tamaño 2 

class Submarine(Ship): # se define la subclase Submarino
    def __init__(self):
        super().__init__('Submarino', 3) # es un submarino tamaño 3

class Battleship(Ship): # se define la subclase acorazado
    def __init__(self):
        super().__init__('Acorazado', 4) # es un acorazado tamaño 4

class Player: # clase Jugador
    def __init__(self, name):
        self.name = name # almacena el nombre del jugador
        self.board = [[' ' for _ in range(10)] for _ in range(10)] # crea un tablero vacio de 10 x 10
        self.ships = [] # lista para almacenar los barcos del jugador
        self.hits = [[' ' for _ in range(10)] for _ in range(10)] # crea un tablero vacio para registrar los impactos

    def place_ships(self): # metodo del lugar de los barcos
        ships = [Destroyer(), Submarine(), Battleship()] # Lista de barcos a colocar
        for ship in ships: # iteracion sobre cada barco
            while True: # Bucle para intentar colocar cada barco
                print(f"{self.name}, coloca tu {ship.name} de tamaño {ship.size}.")
                start_row = int(input("Fila inicial: ")) # pide la fila inicial
                start_col = int(input("Columna inicial: ")) # pide la columna inicial
                direction = input("Dirección (H para horizontal, V para vertical): ").upper() # pide la direccion, convierte toda la cadena en mayusculas
                if ship.place_ship(start_row, start_col, direction, self.board): # Intenta colocar el barco
                    self.ships.append(ship) # si se tiene exito, se anade el barco a la lista de barcos
                    self.print_board(self.board) # Imprime el tablero
                    break # sale del bucle si el barco ha sido colocado en el tablero
                else: # si no se cumple if
                    print("Posición no válida. Inténtalo de nuevo.") # Entonce imprime que la posicion no es valida

    def print_board(self, board): # metodo de imprimir el tablero
        for row in board: # itera o recorre cada fila del tablero
            print(" ".join(row)) # imprime la fila como una cadena separada por espacios
        print() # añade una linea en blanco al final

    def attack(self, opponent): # metodo ataque
        while True: # bucle si es verdad 
            print(f"{self.name}, elige una posición para atacar.") # imprime el nombre con el mensaje de la posición para atacar
            row = int(input("Fila: ")) # pide que se ingrese la posicion de la fila para atacar
            col = int(input("Columna: ")) # pide que se ingrese la posicion de la columna para atacar
            if 0 <= row < 10 and 0 <= col < 10: # verifica si la posicion esta dentro del tablero, osea las coordenadas fila,columna
                if opponent.board[row][col] == ' ': # verifica si el disparo se realizo al agua (espacio vacio)
                    print("Agua!") # si fuera el caso entonces, imprime agua
                    self.hits[row][col] = 'A' # Marcara agua en el tablero de impactos del jugador
                    opponent.board[row][col] = 'A' # marcara agua en el tablero de impactos del oponente 
                    break # sale del bucle
                elif opponent.board[row][col] != 'A': # verifica si no es agua y no ha sido atacada antes
                    print("Impacto!") # En caso fuera asi, entonces imprime Impacto
                    self.hits[row][col] = 'T' # Marcara el impacto en el tablero de impactos
                    for ship in opponent.ships: # buscarara el barco impactado 
                        if (row, col) in ship.positions: # verifica la fila y la columna en la posicion de impactos
                            if ship.hit(): #   registra el impacto y verifica si ha sido hundido
                                print(f"¡Hundido! Has hundido el {ship.name}.") # Imprimira si se ha hundido el barco
                            break  # sale del bucle
                    opponent.board[row][col] = 'T' # marca el impacto en el tablero del oponente    
                    break # sale del bucle
                else: # si no se cumple if entoces imprimira el siguiente mensaje
                    print("Ya has atacado esta posición. Intenta de nuevo.") # que ya se ataco la misma posicion y que reintente nuevamente
            else: # si no se cumple if
                print("Posición no válida. Intenta de nuevo.") # imprimira que la posicion esta fuera del tablero que reintente nuevamente

    def all_ships_sunk(self): # método para verificar si todos los los barcos han sido hundidos
        return all(ship.hits == ship.size for ship in self.ships)

class BattleshipGame:
    def __init__(self):
        self.player1 = Player("Jugador 1")
        self.player2 = Player("Jugador 2")

    def play(self):
        print("Bienvenido al juego de Batalla Naval!")
        print("Jugador 1 coloca sus barcos.")
        self.player1.place_ships()
        print("Jugador 2 coloca sus barcos.")
        self.player2.place_ships()

        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"¡{current_player.name} ha ganado el juego!")
                break
            current_player, opponent = opponent, current_player

# Crear una instancia del juego y jugar
game = BattleshipGame()
game.play()
import numpy as np 

class Labirinto:
    def __init__(self):
        #Definindo matriz do labirinto 12x12 sendo 1 o espaço livre e 0 espaço ocupado
        self.grid = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

    #Verifica se o espaço está livre
    def espaco_livre(self, x, y):
        return self.grid[x][y] == 1;
    
    #Sequencia de movimentos predefinida 
    def vizinhos_validos(self, x, y):
        vizinhos = []

        #Agente para cima
        if x > 0 and self.espaco_livre(x - 1, y):
            vizinhos.append((x - 1, y))

        #Agente para esquerda
        if y > 0 and self.espaco_livre(x, y - 1):
            vizinhos.append((x, y - 1))

        #Agente para direita
        if y < len(self.grid[0]) - 1 and self.espaco_livre(x, y + 1):
            vizinhos.append((x, y + 1))
            
        #Agente para baixo
        if x < len(self.grid) - 1 and self.espaco_livre(x + 1, y):
            vizinhos.append((x + 1, y))
        return vizinhos
        
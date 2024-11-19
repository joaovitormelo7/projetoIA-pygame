import numpy as np 

class Labirinto:
    def __init__(self):
        # Definindo matriz do labirinto 12x12 (1: espaço livre, 0: parede)
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

    # Verifica se o espaço está livre
    def espaco_livre(self, x, y):
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return self.grid[x][y] == 1
        return False
    
    # Retorna os vizinhos válidos de uma posição (x, y)
    def vizinhos_validos(self, x, y):
        vizinhos = []

        if x > 0 and self.espaco_livre(x - 1, y):
            vizinhos.append((x - 1, y))
        
        if y > 0 and self.espaco_livre(x, y - 1):
            vizinhos.append((x, y - 1))
        
        # Agente para a direita
        if y < len(self.grid[0]) - 1 and self.espaco_livre(x, y + 1):
            vizinhos.append((x, y + 1))

        # Agente para baixo
        if x < len(self.grid) - 1 and self.espaco_livre(x + 1, y):
            vizinhos.append((x + 1, y))

        # Direções: (delta_x, delta_y)
        direcoes = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Cima, Esquerda, Direita, Baixo

        for dx, dy in direcoes:
            novo_x, novo_y = x + dx, y + dy
            if self.espaco_livre(novo_x, novo_y):
                vizinhos.append((novo_x, novo_y))

        return vizinhos

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
        # Ordem das direções: Direita, Cima, Esquerda, Baixo
        direcoes = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        vizinhos = []
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.espaco_livre(nx, ny):
                vizinhos.append((nx, ny))
        return vizinhos

import numpy as np 

class Labirinto:
    def __init__(self, goal=None):
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
        self.goal = goal        

    
    def espaco_livre(self, x, y):
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return self.grid[x][y] == 1
        return False
    
    def vizinhos_validos(self, x, y, ordem=None):
        direcoes = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        vizinhos = []

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.espaco_livre(nx, ny):
                vizinhos.append((nx, ny))
        
        if ordem == "reversa":
            return list(reversed(vizinhos))
        elif ordem == "heuristica":
            return sorted(vizinhos, key=lambda v: abs(v[0] - self.goal[0]) + abs(v[1] - self.goal[1]))
        return vizinhos


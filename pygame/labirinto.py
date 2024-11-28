import numpy as np

class Labirinto:
    def __init__(self, goal=None):
        if goal is None or not isinstance(goal, tuple) or len(goal) != 2:
            raise ValueError("O objetivo deve ser uma tupla com duas coordenadas") #debug manual
        self.goal = goal
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
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] == 1

    def vizinhos_validos(self, x, y):
        direcoes = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        return [
            (x + dx, y + dy)
            for dx, dy in direcoes
            if self.espaco_livre(x + dx, y + dy)
        ]

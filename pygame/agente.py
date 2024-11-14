class Agente: 
    def __init__(self, labirinto, start, goal):
        self.labirinto = labirinto
        self.start = start
        self.goal = goal
        self.caminho = []
        self.posicao_atual = start
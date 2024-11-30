class Agente:
    def __init__(self, labirinto, start, goal):
        self.labirinto = labirinto
        self.start = start
        self.goal = goal
        self.caminho = []

    def buscar_caminho(self, metodo="largura"):
        from busca import busca_largura, busca_profundidade

        if metodo == "largura":
            return busca_largura(self.labirinto, self.start, self.goal)
        elif metodo == "profundidade":
            return busca_profundidade(self.labirinto, self.start, self.goal)
        else:
            raise ValueError("Método inválido.")

class Agente:
    def __init__(self, labirinto, start, goal):
        if not goal:
            raise ValueError("O objetivo deve ser definido.")
        self.labirinto = labirinto
        self.start = start
        self.goal = goal
        self.caminho = []
        self.posicao_atual = start

    def buscar_caminho(self, metodo="largura"):
        if metodo == "largura":
            from busca import busca_largura
            resultado = busca_largura(self.labirinto, self.start, self.goal)
            if resultado:
                caminho, visitados, ordem_visita = resultado
                self.caminho = caminho
                return caminho, visitados, ordem_visita
            else:
                raise ValueError("A busca em largura falhou em retornar um resultado válido.")

        elif metodo == "profundidade":
            from busca import busca_profundidade
            resultado = busca_profundidade(self.labirinto, self.start, self.goal)
            if resultado:
                caminho, visitados, ordem_visita, ordem_map = resultado
                self.caminho = caminho
                return caminho, visitados, ordem_visita, ordem_map
            else:
                raise ValueError("A busca em profundidade falhou em retornar um resultado válido.")

        else:
            raise ValueError("Método de busca inválido. Escolha 'largura' ou 'profundidade'.")

    def mover(self):
        if not self.caminho:
            print("Nenhum caminho disponível para mover.")
            return

        if self.posicao_atual != self.goal:
            proxima_posicao = self.caminho.pop(0)
            print(f"Movendo de {self.posicao_atual} para {proxima_posicao}")
            self.posicao_atual = proxima_posicao
        else:
            print("O agente já chegou ao objetivo.")

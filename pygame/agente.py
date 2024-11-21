class Agente: 
    def __init__(self, labirinto, start, goal):
        self.labirinto = labirinto
        self.start = start
        self.goal = goal
        self.caminho = []
        self.posicao_atual = start
    
    def buscar_caminho(self, metodo="largura"):
        if metodo == "largura":
            from busca import busca_largura
            self.caminho = busca_largura(self.labirinto, self.start, self.goal)

        elif metodo == "profundidade":
            from busca import busca_profundidade
            self.caminho = busca_profundidade(self.labirinto, self.start, self.goal)

        elif metodo == "gulosa":
            from busca import busca_gulosa
            self.caminho = busca_gulosa(self.labirinto, self.start, self.goal)
            
        else:
            raise ValueError("Método de busca inválido. Use 'largura' ou 'profundidade' ou 'gulosa'.")
        
        if self.caminho:
            print(f"Caminho encontrado: {self.caminho}")
        else:
            print("Nenhum caminho encontrado. Verifique se as posições são válidas e se o labirinto é acessível.")
    
    def mover(self):
        if not self.caminho:
            print("Nenhum caminho disponível para mover.")
            return
        
        if self.posicao_atual != self.goal:
            proxima_posicao = self.caminho.pop(0)
            self.posicao_atual = proxima_posicao
            print(f"Movendo para {proxima_posicao}")
        else:
            print("O agente já chegou ao objetivo.")

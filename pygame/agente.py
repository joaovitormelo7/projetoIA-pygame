class Agente: 
    def __init__(self, labirinto, start, goal):
        self.labirinto = labirinto  # O labirinto onde o agente opera
        self.start = start  # Posição inicial do agente
        self.goal = goal  # Posição do objetivo
        self.caminho = []  # Caminho encontrado
        self.posicao_atual = start  # Posição atual do agente
    
    def buscar_caminho(self, metodo="largura"):
        if metodo == "largura":
            from busca import busca_largura
            self.caminho = busca_largura(self.labirinto, self.start, self.goal)
        elif metodo == "profundidade":
            from busca import busca_profundidade
            self.caminho = busca_profundidade(self.labirinto, self.start, self.goal)
        else:
            raise ValueError("Método de busca inválido. Use 'largura' ou 'profundidade'.")
        
        if self.caminho:
            print(f"Caminho encontrado: {self.caminho}")
        else:
            print("Nenhum caminho encontrado.")
    
    def mover(self):
        if not self.caminho:
            print("Nenhum caminho disponível para mover.")
            return
        
        # Se houver mais posições no caminho, atualiza a posição atual
        if self.posicao_atual != self.goal:
            proxima_posicao = self.caminho.pop(0)
            self.posicao_atual = proxima_posicao
            print(f"Movendo para {proxima_posicao}")
        else:
            print("O agente já chegou ao objetivo.")

import pygame
from labirinto import Labirinto
from agente import Agente

# Menu para escolher o metodo de busca, a busca so irá começar após a escolha
def escolher_metodo():
    print("Selecione o método de busca:")
    print("1 - Busca em Largura (BFS)")
    print("2 - Busca em Profundidade (DFS)")
    print("3 - Busca A* (A-estrela)")
    escolha = input("Digite o número correspondente ao método desejado: ")

    if escolha == "1":
        return "largura"
    
    elif escolha == "2":
        return "profundidade"
    
    elif escolha == "3":
        return "a_estrela"
    else:
        print("Escolha inválida. Tente novamente.")
        return escolher_metodo()

pygame.init()

# Configurações da tela
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto com Busca")
tamanho_celula = largura // 12

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Inicializar labirinto
labirinto = Labirinto(goal=(10, 0))

# Inicializar agente
agente = Agente(labirinto, (4, 10), (10, 0))

# Escolher método de busca 'largura', 'profundidade' ou 'a_estrela'
metodo_busca = escolher_metodo()  

# Executar busca
if metodo_busca == "largura":
    caminho, visitados, ordem_visita = agente.buscar_caminho(metodo="largura")
elif metodo_busca == "profundidade":
    caminho, visitados, ordem_visita = agente.buscar_caminho(metodo="profundidade")
elif metodo_busca == "a_estrela":
    caminho, visitados, ordem_visita = agente.buscar_caminho(metodo="a_estrela")
else:
    raise ValueError("Método de busca inválido. Escolha 'largura' ou 'profundidade' ou 'a_estrela'.")

# Funções de desenho
def desenhar_labirinto():
    for x in range(12):
        for y in range(12):
            cor = PRETO if labirinto.grid[x][y] == 0 else BRANCO
            pygame.draw.rect(tela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))

def desenhar_rastro(ordem_visita, indice, cor):
    for i in range(min(len(ordem_visita), indice)):
        x, y = ordem_visita[i]
        pygame.draw.rect(tela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))

# Controle do loop principal
running = True
indice = 0  # Controle do progresso da busca
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher a tela
    tela.fill(BRANCO)

    # Desenhar o labirinto
    desenhar_labirinto()

    # Mostrar o rastro progressivamente
    desenhar_rastro(ordem_visita, indice, VERDE if metodo_busca == "largura" else VERMELHO)

    # Avançar o índice para mostrar o próximo passo da busca
    if indice < len(ordem_visita):
        indice += 1
    else:
        print(f"Busca concluída utilizando {metodo_busca}.")
        running = False

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(5)  # Controlar a velocidade da animação

pygame.quit()

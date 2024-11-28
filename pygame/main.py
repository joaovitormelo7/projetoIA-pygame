import pygame
import sys
from labirinto import Labirinto
from agente import Agente

# Iniciar pygame
pygame.init()

# Configuração da janela
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Visualização do Labirinto")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE_CLARO = (200, 255, 200)
VERMELHO_CLARO = (255, 200, 200)
AZUL = (0, 0, 255)

# Configuração do labirinto
tamanho_celula = largura // 12

# Iniciar labirinto e posições do agente e objetivo
labirinto = Labirinto(goal=(10, 0))
posicao_inicial = (4, 10)
goal = (10, 0)

# Método de busca (largura ou profundidade)
metodo_busca = "largura"

# Inicializar agente
agente = Agente(labirinto, posicao_inicial, goal)

try:
    if metodo_busca == "largura":
        # Busca em largura
        caminho, visitados, ordem_visita = agente.buscar_caminho(metodo="largura")
    elif metodo_busca == "profundidade":
        # Busca em profundidade
        caminho, visitados, ordem_visita, ordem_map = agente.buscar_caminho(metodo="profundidade")
    else:
        raise ValueError("Método de busca inválido. Escolha 'largura' ou 'profundidade'.")
except ValueError as e:
    print(f"Erro: {e}")
    pygame.quit()
    sys.exit()

# Caminho encontrado
print("Caminho encontrado:", caminho)

# Função para desenhar o labirinto
def labirinto_desenho():
    for x in range(12):
        for y in range(12):
            cor = PRETO if labirinto.grid[x][y] == 0 else BRANCO
            pygame.draw.rect(tela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))

# Função para desenhar o rastro
def rastro_desenho(visitados):
    for (x, y) in visitados:
        pygame.draw.rect(
            tela,
            VERDE_CLARO if metodo_busca == "largura" else VERMELHO_CLARO,
            (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula),
        )
    pygame.draw.rect(tela, AZUL, (goal[1] * tamanho_celula, goal[0] * tamanho_celula, tamanho_celula, tamanho_celula))

# Loop principal para animação
running = True
controle_velocidade = pygame.time.Clock()
indice = 0  # Índice para o caminho do agente

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.fill(BRANCO)
    labirinto_desenho()
    rastro_desenho(visitados)

    if indice < len(caminho):
        # Desenhar o agente na célula atual
        pos_atual = caminho[indice]
        pygame.draw.rect(
            tela,
            AZUL,
            (
                pos_atual[1] * tamanho_celula + tamanho_celula // 4,
                pos_atual[0] * tamanho_celula + tamanho_celula // 4,
                tamanho_celula // 2,
                tamanho_celula // 2,
            ),
        )
        indice += 1
    else:
        # Mostrar o agente na posição final
        pygame.draw.rect(
            tela,
            AZUL,
            (
                goal[1] * tamanho_celula + tamanho_celula // 4,
                goal[0] * tamanho_celula + tamanho_celula // 4,
                tamanho_celula // 2,
                tamanho_celula // 2,
            ),
        )

    pygame.display.flip()
    controle_velocidade.tick(5)  # Velocidade da animação (5 FPS)

pygame.quit()

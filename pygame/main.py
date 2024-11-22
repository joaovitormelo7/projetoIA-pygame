import pygame
import sys
from labirinto import Labirinto
from busca import busca_gulosa
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
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configuração do labirinto
tamanho_celula = largura // 12

# Iniciar labirinto e posições do agente e objetivo
labirinto = Labirinto()
posicao_agente = (4, 10)
goal = (10, 0)

#configuração inicial
agente = Agente(labirinto, posicao_agente, goal)

#buscar caminho
agente.buscar_caminho(metodo="gulosa")

if not agente.caminho:
    print("Nenhum caminho encontrado. Saindo...")
    pygame.quit()
    sys.exit()

# Caminho encontrado
print("Caminho encontrado:", agente.caminho)

# Inicializar posição e estado de animação
passo_atual = 0
posicao_animada = [posicao_agente[1] * tamanho_celula + tamanho_celula // 2,
                   posicao_agente[0] * tamanho_celula + tamanho_celula // 2]
velocidade = 5

# Função para desenhar o labirinto
def labirinto_desenho():
    for x in range(12):
        for y in range(12):
            cor = PRETO if labirinto.grid[x][y] == 0 else BRANCO
            pygame.draw.rect(tela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))

# Função para desenhar o agente e o objetivo
def agente_desenho():
    # Desenhar o agente na posição animada
    pygame.draw.circle(tela, VERDE, (int(posicao_animada[0]), int(posicao_animada[1])), tamanho_celula // 3)
    
    # Desenhar o objetivo
    pygame.draw.circle(tela, AZUL, 
                       (goal[1] * tamanho_celula + tamanho_celula // 2, 
                        goal[0] * tamanho_celula + tamanho_celula // 2), 
                       tamanho_celula // 3)

# Loop do jogo
running = True
controle_velocidade = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar se há caminho e se ainda há passos a seguir
    if agente.caminho and passo_atual < len(agente.caminho):
        proxima_posicao = agente.caminho[passo_atual]
        objetivo_x = proxima_posicao[1] * tamanho_celula + tamanho_celula // 2
        objetivo_y = proxima_posicao[0] * tamanho_celula + tamanho_celula // 2

        # Mover na direção do próximo objetivo
        if posicao_animada[0] < objetivo_x:
            posicao_animada[0] += velocidade
        elif posicao_animada[0] > objetivo_x:
            posicao_animada[0] -= velocidade

        if posicao_animada[1] < objetivo_y:
            posicao_animada[1] += velocidade
        elif posicao_animada[1] > objetivo_y:
            posicao_animada[1] -= velocidade

        # Verificar se alcançou a posição do próximo passo
        if abs(posicao_animada[0] - objetivo_x) < velocidade and abs(posicao_animada[1] - objetivo_y) < velocidade:
            posicao_animada = [objetivo_x, objetivo_y]
            posicao_agente = proxima_posicao
            passo_atual += 1

    # Atualizar tela
    tela.fill(BRANCO)
    labirinto_desenho()
    agente_desenho()
    pygame.display.flip()
    controle_velocidade.tick(30)

pygame.quit()
sys.exit()

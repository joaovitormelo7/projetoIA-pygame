import pygame
import sys
import numpy as np
from labirinto import Labirinto
from busca import buscaLargura

#Iniciar pygame
pygame.init()

#Configuração da janela
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Visualização do labirinto")

#Cor 
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Configuração do labirinto
tamanho_celula = largura // 12

#Iniciar labirinto e posição do agente e obejtivo do agente
labirinto = Labirinto()
posicao_agente = (4,11)
goal = (10, 0)

#Labirinto
def labirinto_desenho():
    for x in range(12):
        for y in range(12):
            cor = BRANCO if labirinto.grid[x][y] == 1 else PRETO
            pygame.draw.rect(tela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))

def agente_desenho(posicao_agente, goal):
    # Desenhar o agente
    pygame.draw.circle(tela, VERDE, 
                       (posicao_agente[1] * tamanho_celula + tamanho_celula // 2, 
                        posicao_agente[0] * tamanho_celula + tamanho_celula // 2), 
                       tamanho_celula // 3)
    
    # Desenhar o objetivo
    pygame.draw.circle(tela, AZUL, 
                       (goal[1] * tamanho_celula + tamanho_celula // 2, 
                        goal[0] * tamanho_celula + tamanho_celula // 2), 
                       tamanho_celula // 3)

#Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.fill(BRANCO)
    labirinto_desenho()
    agente_desenho(posicao_agente, goal)

    pygame.display.flip()


pygame.quit()
sys.exit()
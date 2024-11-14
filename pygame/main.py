import pygame
import sys
import numpy as np
from labirinto import Labirinto
from busca import buscaProfundidade

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
posicao_agente = (4,10)
goal = (10, 0)

caminho = buscaProfundidade(labirinto, posicao_agente, goal)
if not caminho:
    print("Erro ao encontrar um caminho")
else:
    print("caminho encontrado: ", caminho)
    
passo_atual = 0

#Animação
posicao_animada = [posicao_agente[1] * tamanho_celula + tamanho_celula // 2,
                  posicao_agente[0] * tamanho_celula + tamanho_celula // 2]
velocidade = 5    

#Labirinto
def labirinto_desenho():
    for x in range(12):
        for y in range(12):
            cor = BRANCO if labirinto.grid[x][y] == 1 else PRETO
            pygame.draw.rect(tela, cor, (y * tamanho_celula, x * tamanho_celula, tamanho_celula, tamanho_celula))

def agente_desenho(goal):
    # Desenhar o agente na posição animada
    pygame.draw.circle(tela, VERDE, (int(posicao_animada[0]), int(posicao_animada[1])), tamanho_celula // 3)
    
    # Desenhar o objetivo
    pygame.draw.circle(tela, AZUL, 
                       (goal[1] * tamanho_celula + tamanho_celula // 2, 
                        goal[0] * tamanho_celula + tamanho_celula // 2), 
                       tamanho_celula // 3)
    

#Loop do jogo
running = True

#Teste para controlar a velocidade do agente
ControleVelocidade = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if caminho and passo_atual < len(caminho):
        proxima_posicao = caminho[passo_atual]
    
    if labirinto.grid[proxima_posicao[0]][proxima_posicao[1]] == 1:
        objetivo_x = proxima_posicao[1] * tamanho_celula + tamanho_celula // 2
        objetivo_y = proxima_posicao[1] * tamanho_celula + tamanho_celula // 2
        

        if posicao_animada[0] < objetivo_x:
            posicao_animada[0] += velocidade
        elif posicao_animada[0] > objetivo_x:
            posicao_animada[0] -= velocidade

        if posicao_animada[1] < objetivo_y:
            posicao_animada[1] += velocidade
        elif posicao_animada[1] > objetivo_y:
            posicao_animada[1] -= velocidade
        
        if abs(posicao_animada[0] - objetivo_x) < velocidade and abs(posicao_animada[1] - objetivo_y) < velocidade:
            posicao_animada = [objetivo_x, objetivo_y]
            posicao_agente = proxima_posicao
            passo_atual += 1

    tela.fill(BRANCO)
    labirinto_desenho()
    agente_desenho(goal)

    pygame.display.flip()
    ControleVelocidade.tick(30)


pygame.quit()
sys.exit()
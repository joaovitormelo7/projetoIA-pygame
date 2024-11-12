import pygame
import sys

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

#Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
    
    tela.fill(BRANCO)

    pygame.display.flip()

pygame.quit()
sys.exit()
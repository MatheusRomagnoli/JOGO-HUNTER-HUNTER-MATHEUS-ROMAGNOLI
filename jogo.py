#Feito por matheus othavio romagnoli

import pygame

#cria a janela do jogo
pygame.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo muito difícil mesmo da MATHEUS ROMAGNOLI")

#fazendo a tela funcionar
rodando = True
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
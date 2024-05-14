#Feito por matheus othavio romagnoli

import pygame
from objeto import *

#cria a janela do jogo
pygame.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo Hunter x Hunter MATHEUS ROMAGNOLI")

#carregando as imagens
gon = pygame.image.load("imagens/gon1.png")
killua = pygame.image.load("imagens/killua1.png")
gon_e_killua = pygame.image.load("imagens/gonkillua.png")
gon = pygame.transform.scale(gon,(80,110))
killua = pygame.transform.scale(killua,(80,110))


#posical inicial do GON
gon_posx = 350
gon_posy = 390
mascara = pygame.mask.from_surface(gon)

#posição inicial do KILLUA
killua_posx = 350
killua_posy = 1

#imagem de fundo
FUNDO = pygame.image.load("imagens/fundo.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#lista de objetos
lista_objetos = [Objeto("imagens/baralho.png", 100,50,950,50),
                 Objeto("imagens/aranha.png", 100,50,950,50),
                 Objeto("imagens/vara.png", 100,50,950,50),
                 Objeto("imagens/anel.png", 100,50,950,50),
                 Objeto("imagens/cartao.png", 100,50,950,50),]

#fazendo a tela funcionar
rodando = True
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    #adiciona o fundo a janela do jogo
    tela.blit(FUNDO,(0,0))
    
    #define posição do gon na tela
    tela.blit(gon,(gon_posx,gon_posy))
    #define posição do killua na tela
    tela.blit(killua,(killua_posx,killua_posy))

    #atualiza a tela
    pygame.display.update()
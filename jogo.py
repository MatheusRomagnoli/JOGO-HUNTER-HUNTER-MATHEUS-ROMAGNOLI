#Feito por matheus othavio romagnoli

import pygame

#cria a janela do jogo
pygame.init()
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo Hunter x Hunter MATHEUS ROMAGNOLI")

#carregando as imagens
gon = pygame.image.load("imagens/gon1.png")
killua = pygame.image.load("imagens/killua1.png")
gon_e_killua = gon = pygame.image.load("imagens/gonkillua.png")
gon = pygame.transform.scale(gon,(80,80))
killua = pygame.transform.scale(killua,(80,80))

#posição inicial do GON
#posical inicial do GON
gon_posx = 375
gon_posy = 430

#imagem de fundo
FUNDO = pygame.image.load("imagens/fundo.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

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
    
    #atualiza a tela
    pygame.display.update()
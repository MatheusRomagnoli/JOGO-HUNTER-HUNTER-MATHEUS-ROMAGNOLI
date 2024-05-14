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
lista_objetos = [Objeto("imagens/baralho.png", 100,50,420,1),
                 Objeto("imagens/aranha.png", 100,50,270,1),
                 Objeto("imagens/vara.png", 100,50,380,1),
                 Objeto("imagens/anel.png", 100,50,110,1),
                 Objeto("imagens/cartao.png", 100,50,590,1),]

#configura o fps
clock = pygame.time.Clock()

#pontuação
pontuacao = 10

#fazendo a tela funcionar
rodando = True
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    #adiciona o fundo a janela do jogo
    tela.blit(FUNDO,(0,0))
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        gon_posx = gon_posx + 5
    if teclas[pygame.K_LEFT]:
        gon_posx = gon_posx - 5

    #define posição do gon na tela
    tela.blit(gon,(gon_posx,gon_posy))
    #define posição do killua na tela
    tela.blit(killua,(killua_posx,killua_posy))

    #configurando os objetos
    for objeto in lista_objetos:
        objeto.apareca(tela)
        objeto.movimenta()
        if mascara.overlap(objeto.mascara,(objeto.pos_x - gon_posx, objeto.pos_y - gon_posy)):
            pontuacao = pontuacao -1
    #atualiza a tela
    pygame.display.update()
    
    #fps
    clock.tick(60)
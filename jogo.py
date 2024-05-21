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

#lista de objetos bons
lista_objetos1 = [Objeto("imagens/vara.png", 100,50,380,1),
                 Objeto("imagens/anel.png", 100,50,110,1)]
#lista objetos ruins
lista_objetos2 = [Objeto("imagens/baralho.png", 100,50,420,1),
                 Objeto("imagens/aranha.png", 100,50,270,1),
                 Objeto("imagens/cartao.png", 100,50,590,1)]

#configura o fps
clock = pygame.time.Clock()

#criando a fonte
fonte = pygame.font.SysFont("Arial Black", 18)
#pontuação
pontuacao = 10
texto_pontos = fonte.render(f"Pontuação do GON: {pontuacao}",True,(255,255,255))
perdi = True
textoover = fonte.render("Game Over",True,(255,255,255))
textovence = fonte.render("Você Venceu!!",True,(255,255,255))
textoespecial = fonte.render(f"Você ativou a habilidade especial de VELOCIDADE",True,(255,255,255))

velkillua = 10
velgon = 5
poder = False
#fazendo a tela funcionar
rodando = True
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velgon = velgon + 10
                poder = True
                if poder == True:
                    textoespecial = fonte.render(f"Você ativou a habilidade especial de VELOCIDADE",True,(255,255,255))
                    tela.blit(textoespecial,(5,30))

    #adiciona o fundo a janela do jogo
    tela.blit(FUNDO,(0,0))
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        gon_posx = gon_posx + velgon
    if teclas[pygame.K_LEFT]:
        gon_posx = gon_posx - velgon
    
    #define posição do gon na tela
    tela.blit(gon,(gon_posx,gon_posy))
    #define posição do killua na tela
    killua_posx += velkillua
    if killua_posx < 0 or killua_posx > 800:
        velkillua = velkillua * -1
    tela.blit(killua,(killua_posx,killua_posy))

    #configurando os objetos bons
    for objeto in lista_objetos1:
        objeto.apareca(tela)
        objeto.movimenta()
        if mascara.overlap(objeto.mascara,(objeto.pos_x - gon_posx, objeto.pos_y - gon_posy)):
            pontuacao = pontuacao + 1
            texto_pontos = fonte.render(f"Pontuação do GON: {pontuacao}",True,(255,255,255))
            objeto.pos_y = 1
            objeto.pos_x = random.randint(1,700)
    #configurando os objetos ruins
    for objeto in lista_objetos2:
        objeto.apareca(tela)
        objeto.movimenta()
        if mascara.overlap(objeto.mascara,(objeto.pos_x - gon_posx, objeto.pos_y - gon_posy)):
            pontuacao = pontuacao - 1
            texto_pontos = fonte.render(f"Pontuação do GON: {pontuacao}",True,(255,255,255))
            objeto.pos_y = 1
            objeto.pos_x = random.randint(1,700)
    
    #atualiza o texto de pontos
    tela.blit(texto_pontos,(5,10))
    
    #tela de GAME OVER
    if pontuacao <= 0:
        tela.fill((0, 255, 0))
        textoover = fonte.render("Game Over",True,(255,255,255))
        tela.blit(textoover,(320,270))
    #tela de VOCÊ VENCEU
    if pontuacao > 20:
        tela.fill((0, 255, 0))
        textovence = fonte.render("Você Venceu!!",True,(255,255,255))
        tela.blit(textovence,(320,270))

    #atualiza a tela
    pygame.display.update()
    
    #fps
    clock.tick(60)
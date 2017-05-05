import pygame
import ConfigParser

ANCHO = 1302
ALTO = 651
BLANCO=(255,255,255)
NEGRO=(0,0,0)
VERDE=(0,255,0)

class Barra_info():
    def __init__(self,enemigos,vidas,nivel):
        self.enemigos=enemigos
        self.vidas=vidas
        self.nivel=nivel

    def Perder_vidas(self):
        v=str(self.vidas)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render("Vidas:",True,BLANCO)
        vida=fuente.render(v,True,BLANCO)
        pantalla.blit(texto,[1250,70])
        pantalla.blit(vida,[1200,50])
        pygame.display.flip()

    def Matar_enemigos(self):
        M=str(self.enemigos)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render("Enemigos:",True,BLANCO)
        enemigos=fuente.render(M,True,BLANCO)
        pantalla.blit(texto,[1250,70])
        pantalla.blit(enemigos,[1200,70])
        pygame.display.flip()

    def Nivel_actual(self):
        N=str(self.nivel)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render("Nivel Actual:",True,BLANCO)
        nivel=fuente.render(N,True,BLANCO)
        pantalla.blit(texto,[1300,90])
        pantalla.blit(nivel,[1200,90])
        pygame.display.flip()




if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)

    vida=Barra_info(3,10-1,3)



    fin=False

    while not fin:
        for event in pygame.event.get():
            vida.Perder_vidas()
            vida.Matar_enemigos()
            vida.Nivel_actual()
            if event.type==pygame.QUIT:
                fin=True

import pygame
from libc import *

ANCHO = 600
ALTO = 600
CENTRO = (ANCHO/2,ALTO/2)

if __name__ == '__main__':
    # Inicializacion Pantalla Pygame
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    # Dibujar plano cartesiano
    planoCartesiano(ANCHO,ALTO,pantalla)

    # Dibujar una linea
    PuntoI = cart(CENTRO,[0,0])
    PuntoF = cart(CENTRO,[100,-100])
    linea(pantalla, AMARILLO, PuntoI, PuntoF)

    # Dibujar un triangulo
    PuntoT = [[20,10], [60,10], [60,30]]
    PuntoA = cart(CENTRO, PuntoT[0])
    PuntoB = cart(CENTRO, PuntoT[1])
    PuntoC = cart(CENTRO, PuntoT[2])
    poligono(pantalla, LILA, [PuntoA, PuntoB, PuntoC])

    # Escalar triangulo (lineas) (valor de sx, sy)
    PuntoAl = cart(CENTRO,escalar(PuntoT[0], [3,2]))
    PuntoBl = cart(CENTRO,escalar(PuntoT[1], [3,2]))
    PuntoCl = cart(CENTRO,escalar(PuntoT[2], [3,2]))
    poligono(pantalla, LILA, [PuntoAl, PuntoBl, PuntoCl])

    # Rotar figura respecto a un punto
    d = PuntoT[0] # Respecto a este punto se hara rotar la figura
    PuntoAR = rotacionPunto(PuntoT[0], d, 180)
    PuntoBR = rotacionPunto(PuntoT[1], d, 180)
    PuntoCR = rotacionPunto(PuntoT[2], d, 180)
    PuntoAR = cart(CENTRO, PuntoAR)
    PuntoBR = cart(CENTRO, PuntoBR)
    PuntoCR = cart(CENTRO, PuntoCR)
    poligono(pantalla, ROJO, [PuntoAR, PuntoBR, PuntoCR])

    # ----- Rotar figura con respecto al plano -----
    # Figura Original
    PuntoTP = [[0,0], [100,0], [100,80]]
    PuntoA = cart(CENTRO, PuntoTP[0])
    PuntoB = cart(CENTRO, PuntoTP[1])
    PuntoC = cart(CENTRO, PuntoTP[2])
    poligono(pantalla, AZULC, [PuntoA, PuntoB, PuntoC])

    # Figura Rotada
    PuntoAR = rotacionPlano(PuntoTP[0], 180)
    PuntoBR = rotacionPlano(PuntoTP[1], 180)
    PuntoCR = rotacionPlano(PuntoTP[2], 180)
    PuntoAR = cart(CENTRO, PuntoAR)
    PuntoBR = cart(CENTRO, PuntoBR)
    PuntoCR = cart(CENTRO, PuntoCR)
    poligono(pantalla, AZULC, [PuntoAR, PuntoBR, PuntoCR])



    # Mantener Pantalla Activa
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        pygame.display.flip()

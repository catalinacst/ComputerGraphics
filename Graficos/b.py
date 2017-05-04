import pygame
from libc import *

ANCHO = 600
ALTO = 600
CENTRO = (ANCHO/2,ALTO/2)

'''
1. Trazar linea de horizonte
2. Fijar un punto cerca al limite izquierdo de la pantalla sobre el horizonte
3. Posicionar una recta que rote sobre ese punto
'''

if __name__ == '__main__':
    # Inicializacion Pantalla Pygame
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    # Dibujar linea horizontal en el plano
    linea(pantalla, AZUL, [0,ALTO/2], [600,ALTO/2])

    # Puntos de la recta que se dibujara
    PuntoR = [[0,0], [50, 0]]

    # Estableciendo sobre que eje rotara la linea
    d = PuntoR[0]
    ang = 0
    pygame.display.flip()
    
    # Mantener Pantalla Activa
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PuntoRF = rotacionPunto(PuntoR[1], d, ang)
                    linea(pantalla, AZUL, cart(CENTRO,PuntoR[0]), cart(CENTRO,PuntoRF))
                    ang = ang + 1
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    PuntoRF = rotacionPunto(PuntoR[1], d, ang)
                    linea(pantalla, AZUL, cart(CENTRO,PuntoR[0]), cart(CENTRO,PuntoRF))
                    ang = ang - 1
                    pygame.display.flip()
                pantalla.fill(NEGRO)
                linea(pantalla, AZUL, [0,ALTO/2], [600,ALTO/2])
    pygame.display.flip()

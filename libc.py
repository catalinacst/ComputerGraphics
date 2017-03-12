import pygame
import math

# Colores
ROJO = [255, 0, 0]
AZUL = [034, 113, 179]
LILA = [108, 070, 117]
AZULC = [22, 209, 222]
AMARILLO = [250, 227, 19]

# Recibe el punto y lo devuelve trasladado con respecto al punto de origen
def cart(centro, punto):
    '''
    p[x,y]: p[0] = x , p[1] = y
    '''
    xp = centro[0] + punto[0]
    yp = centro[1] - punto[1]
    return [xp, yp]

# Dibuja el plano cartesiano
def planoCartesiano(ANCHO, ALTO, pantalla):
    pygame.draw.line(pantalla, AZUL, [0,ALTO/2], [ANCHO,ALTO/2])
    pygame.draw.line(pantalla, AZUL, [ANCHO/2,0], [ANCHO/2,ALTO])

def linea(pantalla, color, i, f):
    pygame.draw.line(pantalla, color, i, f, 1)

def poligono(pantalla, color, puntos):
    pygame.draw.polygon(pantalla, color, puntos, 1)

def escalar(punto, s_escalar):
    x = punto[0] * s_escalar[0]
    y = punto[1] * s_escalar[1]
    return (x, y)

def rotacionPunto(punto, d, theta): #d es el diferencial (dx,dy) con el origen.
    #punto es el punto que se va a rotar
    ang = math.radians(theta)
    x= d[0] + math.cos(ang) * (punto[0] - d[0]) - math.sin(ang) * (punto[1] - d[1])
    y= d[1] + math.sin(ang) * (punto[0] - d[0]) + math.cos(ang) * (punto[1] - d[1])
    return (x, y)

def rotacionPlano(punto, theta):
    x = punto[0]
    y = punto[1]
    xr = (x * math.cos(math.radians(theta))) - (y * math.sin(math.radians(theta)))
    yr = (x * math.sin(math.radians(theta))) + (y * math.cos(math.radians(theta)))
    return (xr, yr)

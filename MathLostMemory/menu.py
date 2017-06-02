import pygame
import sys
import random
from pygame.locals import *
from pygame import gfxdraw
import time

NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
AMARILLO = (255,255,0)
dimensiones=(700,400)
ANCHO=800
ALTO=350

#--------------------------Audio e historias de Math------------------------------------  

    #pygame.mixer.music.play(-10)
   

def h1():
    his1=pygame.image.load('h10.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()
    
def h2():
    his1=pygame.image.load('h2.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h3():
    his1=pygame.image.load('h30.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h4():
    his1=pygame.image.load('h1.png')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h5():
    his1=pygame.image.load('h3.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h6():
    his1=pygame.image.load('h.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h7():
    his1=pygame.image.load('h.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h8():
    his1=pygame.image.load('h70.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h9():
    his1=pygame.image.load('h12.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h10():
    his1=pygame.image.load('h12.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h11():
    his1=pygame.image.load('h80.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()
    
def h12():
    his1=pygame.image.load('h11.jpg')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()

def h13():
    his1=pygame.image.load('h7.png')
    his1=pygame.transform.scale(his1,(450,300))
    pantalla.blit(his1, (100,100))
    pygame.display.flip()
    
def Historia():
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.mouse.set_visible(False)
    pygame.init()
    fuente=pygame.font.Font(None,25)
   
    pag=1
    seguir=True
    
    reloj = pygame.time.Clock()
    while seguir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Sale de ciclo y termina programa
                fin=True
                seguir=False
            if event.type == pygame.KEYDOWN:
                #pygame.mixer.music.stop()
                print 'tecla'
                pag+=1
                if pag>2:
                    
                    seguir=False

            if pag==1:
                texto=fuente.render("Historia de Math Lost Memory", True, BLANCO)
                
                pantalla.blit(texto, (200,50))
                #voz.play()
                pygame.mixer.music.load('historia1.mp3')
                pygame.mixer.music.play(0)
                pag+=1           
                for i in range(15):
                    if i==0:                   
                        h1()
                        archivo='h10.jpg'
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    elif i==1:
                        h2()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    if i==2:
                        h3()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    elif i==3:
                        h4()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    if i==4:
                        h5()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    elif i==5:
                        h7()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    if i==6:
                        h8()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    elif i==7:
                        h9()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    if i==8:
                        h10()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    elif i==9:
                        h11()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    if i==10:
                        h11()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    elif i==11:
                        h12()
                        reloj.tick(0.5)
                        pygame.display.flip()
                        i+=1
                    if i==12:
                        h13()
                        reloj.tick(0.3)
                        pygame.display.flip()
                        i+=1
                    elif i==13:
                        h13()
                        reloj.tick(0.3)
                        pygame.display.flip()
                        i+=1
                        pygame.mixer.music.stop()
                        
                    elif i==14:
                        #pag+=1
                        seguir=False
                        pygame.mixer.music.stop()
                    
class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (255, 255, 255))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada() 

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('walk3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.y_inicial = 205
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)
class Menu:
    
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 20)
        x = 105
        y = 205
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                
                self.opciones[self.seleccionado].activar()

        
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, pantalla):
        

        self.cursor.imprimir(pantalla)

        for opcion in self.opciones:
            opcion.imprimir(pantalla)    


def Salir():
    print " Gracias por utilizar este programa."
    sys.exit(0)



def Jugar():
    pass
   


    
if __name__ == '__main__':

    
    salir = False
    opciones = [
        ("Jugar", Jugar),
        ("Historia", Historia),
        ("Salir", Salir)
        ]
    

    pygame.font.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fuente=pygame.font.Font('Wedgie Regular.ttf',80)
    texto=fuente.render('MATH LOST MEMORY ', True, BLANCO)
    pantalla.blit(texto, [400,200])
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("fondo1p.jpg").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
        for i in opciones:
            if opciones == Salir:
               Salir()
            elif opciones==Jugar:
                Jugar()
                
                
               
        pantalla.blit(fondo, (0, 0))

        fuente=pygame.font.Font('BADABB__.ttf',100)
        texto=fuente.render('MATH LOST MEMORY', True, BLANCO)
        pantalla.blit(texto, [30,50])
        menu.actualizar()
        menu.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)

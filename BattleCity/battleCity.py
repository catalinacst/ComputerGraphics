import pygame
import random

ANCHO = 1302
ALTO = 651

NEGRO = (0, 0, 0)
BLANCO = (255,255,255)

'''
'1', -> muro ladrillo
'2', -> muro acero
'3', -> cesped
'4', -> agua
'5', -> jefe
'6', -> enemigo estatico (1 right, 2 left, 3 up, 4 down)
'7', -> enemigo dinamico
'.', -> nada
'''
#            1    2      3     4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
#            20   21   22   23   24   25   26   27   28   29   30   31   32   33
mapa_one = [ '.', '.', '6_4', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '1', '2',  # 1

             '.', '.', '.', '2', '6_1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '2', '.', '.', '2', '2', '2', '2', '1', '1', '1', '1', '.', '2',  # 2

             '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '6_2', '2', '.', '2', '.', '.', '.', '.', '.', '.', '2', '1', '1', '2',  # 3

             '.', '.', '.', '1', '1', '1', '1', '1', '1', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.',
             '.', '2', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 4

             '.', '1', '.', '1', '6_4', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '2', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 5

             '.', '3', '.', '1', '.', '.', '.', '.', '.', '1', '1', '1', '1', '.', '2', '.', '.', '1', '.',
             '.', '2', '1', '1', '1', '1', '1', '1', '.', '.', '.', '.', '.', '2',  # 6

             '.', '1', '.', '1', '.', '2', '.', '2', '.', '2', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '2', '1', '.', '.', '.', '2', '1', '.', '.', '.', '.', '.', '2',  # 7

             '.', '1', '.', '1', '.', '2', '.', '2', '.', '1', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '2', '1', '.', '.', '.', '2', '1', '.', '.', '.', '.', '.', '2',  # 8

             '.', '1', '.', '1', '.', '2', '.', '2', '.', '2', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '.', '1', '1', '1', '1', '1', '1', '.', '.', '.', '.', '.', '2', # 9

             '.', '1', '.', '1', '.', '2', '.', '2', '.', '2', '.', '1', '.', '.', '.', '.', '.', '1', '.',
             '.', '.', '1', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 10

             '.', '2', '.', '1', '.', '2', '.', '2', '.', '2', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '.', '1', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 11

             '.', '1', '.', '1', '.', '2', '.', '2', '.', '2', '.', '1', '.', '6_3', '2', '.', '.', '.', '.',
             '.', '6_2', '1', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 12

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '2', '1', '2', '2', '2', '2', '.', '.', '1', '1',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 13

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '.', '1', '1',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 14

             '.', '1', '.', '1', '.', '.', '2', '2', '.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 15

             '.', '1', '1', '2', '.', '.', '2', '2', '.', '3', '4', '4', '4', '4', '3', '2', '.', '.', '.',
             '.', '.', '1', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 16

             '.', '1', '.', '.', '.', '.', '2', '2', '.', '3', '3', '3', '3', '3', '3', '2', '.', '.', '.',
             '.', '.', '1', '1', '1', '2', '.', '.', '.', '1', '.', '.', '.', '2', # 17

             '.', '2', '.', '.', '2', '.', '2', '2', '.', '3', '3', '3', '3', '3', '3', '2', '.', '.', '.',
             '.', '.', '3', '3', '3', '3', '2', '1', '1', '1', '.', '.', '.', '2', # 18

             '.', '2', '.', '.', '2', '6_3', '.', '.', '.', '.', '3', '3', '3', '3', '2', '.', '6_3', '.', '.',
             '.', '3', '3', '3', '3', '3', '3', '2', '.', '.', '.', '.', '.', '2', # 19

             '.', '1', '1', '2', '3', '3', '3', '2', '2', '4', '4', '4', '4', '4', '4', '4', '4', '4', '.',
             '.', '2', '4', '4', '4', '4', '2', '.', '.', '.', '.', '.', '.', '2',  # 20

             '.', '2', '2', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '6_3',
             '.', '2', '4', '4', '4', '2', '.', '.', '.', '.', '.', '.', '.', '2',  # 21
             ]

#            1    2      3     4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
#            20   21   22   23   24   25   26   27   28   29   30   31   32   33
mapa_two = [ '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2',
             '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2',  # 1

             '2', '.', '6_4', '.', '.', '.', '.', '6_4', '.', '.', '.', '.', '.', '.', '.', '6_1', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 2

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 3

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '4', '.', '.', '.', '.', '.', '.', '.', '2',  # 4

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '4', '.', '.', '.', '.', '.', '.', '6_2', '2',  # 5

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '4', '.', '.', '.', '.', '.', '.', '.', '2',  # 6

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '4', '.', '.', '.', '.', '.', '.', '.', '2',  # 7

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '4', '4', '4', '4', '4', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 8

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '3', '3', '3', '3', '4', '.', '.',
             '.', '.', '3', '3', '3', '3', '3', '3', '.', '.', '.', '.', '.', '2', # 9

             '2', '6_1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '3', '3', '3', '4', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 10

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '4', '4', '4', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 11

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 12

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '6_3', '2', '2',
             '2', '3', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 13

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '3',
             '3', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 14

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '3', '2',
             '2', '2', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 15

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '3', '2',
             '6_4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 16

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '6_2', '2', # 17

             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 18

             '3', '3', '3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 19

             '3', '3', '3', '.', '.', '6_3', '.', '.', '.', '.', '6_3', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 20

             '.', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2',
             '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', # 21
             ]

#            1    2      3     4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
#            20   21   22   23   24   25   26   27   28   29   30   31   32   33
#            1    2      3     4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
#            20   21   22   23   24   25   26   27   28   29   30   31   32   33
mapa_three = [ '.', '.', '.', '.', '.', '.', '.', '6_4', '.', '.', '.', '.', '.', '.', '6_4', '.', '.', '.',
              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '1', '.', '1',  # 1

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '1', '.', '1',  # 2

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '1', '.', '1',  # 3

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '6_2', '2', '1', '.', '1',  # 4

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '6_2', '2', '1', '.', '1',  # 5

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '1', '.', '1',  # 6

             '.', '.', '.', '.', '.', '6_1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '2',  # 7

             '.', '.', '.', '.', '2', '2', '3', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '.', '6_4', '2',  # 8

             '.', '.', '.', '.', '2', '3', '3', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '2', # 9

             '.', '.', '.', '.', '2', '3', '2', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '.', '.', '2', # 10

             '.', '.', '.', '.', '2', '1', '2', '2', '.', '.', '.', '.', '3', '3', '3', '3', '1', '.', '.',
             '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', '6_1', '.', '2', # 11

             '.', '.', '.', '.', '2', '1', '1', '2', '.', '.', '.', '.', '3', '.', '.', '.', '1', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 12

             '.', '.', '.', '.', '2', '1', '6_2', '2', '.', '.', '.', '.', '3', '.', '.', '.', '1', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 13

             '.', '.', '.', '.', '2', '1', '2', '2', '.', '.', '.', '.', '3', '.', '.', '.', '1', '.', '.', '.',
              '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 14

             '.', '.', '.', '.', '2', '1', '1', '2', '.', '.', '.', '.', '1', '1', '1', '1', '1', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 15

             '.', '.', '.', '.', '2', '2', '1', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2', # 16

             '.', '.', '.', '.', '2', '6_4', '1', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '.', '.', '2', # 17

             '.', '.', '.', '.', '2', '1', '1', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '3', '3', '3', '3', '3', '3', '3', '3', '3', '.', '.', '2', # 18

             '2', '2', '2', '2', '2', '1', '2', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '3', '3', '3', '3', '3', '3', '3', '.', '.', '.', '2', # 19

             '.', '.', '.', '.', '1', '1', '2', '2', '.', '.', '6_3', '.', '.', '.', '.', '.', '.', '6_3',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 20

             '.', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '2', '4', '4',
             '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '1', '6_3', '2', # 21
             ]

map_columnas = 33
map_filas = 21

muro_x = 31
muro_y = 31

# Creando grupos - Globales -
muros_ladrillo = pygame.sprite.Group()
muros_acero = pygame.sprite.Group()
muros_obstaculo = pygame.sprite.Group()
muros_cesped = pygame.sprite.Group()
bala_jp = pygame.sprite.Group()
bala_enemy = pygame.sprite.Group()
jefes = pygame.sprite.Group()
enemies_static = pygame.sprite.Group()
enemies_dinamic = pygame.sprite.Group()
todos = pygame.sprite.Group()

class Jugador(pygame.sprite.Sprite):
    def __init__(self, archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 625
        self.dir = 0
        self.orientacion = 0
        self.var_x = 31
        self.var_y = 31
        self.muros = []
        self.vidas = 3
        self.enemies = 12
        self.victoria = 0

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        desplx = self.rect.x
        desply = self.rect.y
        '''
        dir = 1 derecha
        dir = 2 izquierda
        dir = 3 arriba
        dir = 4 abajo
        '''
        if self.dir == 1:
            self.orientacion = 1
            self.rect.x = self.rect.x + self.var_x
            if desplx > ANCHO - 25:
                self.dir = 2
            self.nueva_img('tanqueright.png')
        if self.dir == 2:
            self.orientacion = 2
            self.rect.x = self.rect.x - self.var_x
            if desplx < 0:
                self.dir = 1
            self.nueva_img('tanqueleft.png')
        if self.dir == 3:
            self.orientacion = 3
            self.rect.y = self.rect.y - self.var_y
            if desply < 0:
                self.dir = 4
            self.nueva_img('tanqueup.png')
        if self.dir == 4:
            self.orientacion = 4
            self.rect.y = self.rect.y + self.var_y
            if desply > ALTO - 25:
                self.dir = 3
            self.nueva_img('tanquedown.png')

        # analisis de colision
        l_col = pygame.sprite.spritecollide(self, self.muros, False)
        for m in l_col:
            if self.dir == 1:
                if self.rect.right > m.rect.left:
                    self.rect.right = m.rect.left
            if self.dir == 2:
                if self.rect.left < m.rect.right:
                    self.rect.left = m.rect.right
            if self.dir == 3:
                if self.rect.top < m.rect.bottom:
                    self.rect.top = m.rect.bottom
            if self.dir == 4:
                if self.rect.bottom > m.rect.top:
                    self.rect.bottom = m.rect.top
        self.dir = 0

class Bala_Enemigos(pygame.sprite.Sprite):
    def __init__(self,archivo_img, pos, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dire
        self.var_x = 1
        self.var_y = 1

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        desplx = self.rect.x
        desply = self.rect.y
        if self.dir == 1:
            self.rect.x = self.rect.x + self.var_x
            self.nueva_img('bala_right.png')
        elif self.dir == 2:
            self.rect.x = self.rect.x - self.var_x
            self.nueva_img('bala_left.png')
        elif self.dir == 3:
            self.rect.y = self.rect.y - self.var_y
            self.nueva_img('bala_up.png')
        elif self.dir == 4:
            self.rect.y = self.rect.y + self.var_y
            self.nueva_img('bala_down.png')

class EnemyStatic(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dire
        self.temp = random.randint(200,500)

    def update(self):
        self.temp = self.temp - 1
        if self.temp == 0:
            if self.dir == 1:
                bala = Bala_Enemigos('bala_right.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)
            elif self.dir == 2:
                bala = Bala_Enemigos('bala_left.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)
            elif self.dir == 3:
                bala = Bala_Enemigos('bala_up.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)
            elif self.dir == 4:
                bala = Bala_Enemigos('bala_down.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)

class EnemyDinamic(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos, dire, top, bottom, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dire
        self.var_y = 1
        self.var_x = 1
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom
        self.temp = random.randint(150,200)

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        if self.bottom != 0 and self.rect.y > self.bottom and self.dir == 4:
            self.dir = 3
        if self.top != 0 and self.rect.y < self.top and self.dir == 3:
           self.dir = 4
        if self.left != 0 and self.rect.x < self.left and self.dir == 2:
           self.dir = 1
        if self.right != 0 and self.rect.x > self.right and self.dir == 1:
           self.dir = 2
        if self.dir == 1:
            self.rect.x += self.var_x
            self.nueva_img('enemydinamic_right.png')
        elif self.dir == 2:
            self.rect.x -= self.var_x
            self.nueva_img('enemydinamic_left.png')
        elif self.dir == 3:
            self.rect.y -= self.var_y
            self.nueva_img('enemydinamic_up.png')
        elif self.dir == 4:
            self.rect.y += self.var_y
            self.nueva_img('enemydinamic_down.png')

        self.temp = self.temp - 1
        if self.temp == 0:
            if self.dir == 1:
                bala = Bala_Enemigos('bala_right.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)
            elif self.dir == 2:
                bala = Bala_Enemigos('bala_left.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)
            elif self.dir == 3:
                bala = Bala_Enemigos('bala_up.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)
            elif self.dir == 4:
                bala = Bala_Enemigos('bala_down.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(200,500)

class Muro(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Bala_Jugador(pygame.sprite.Sprite):
    def __init__(self,archivo_img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 0
        self.var_y = 2
        self.var_x = 2

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        desplx = self.rect.x
        desply = self.rect.y
        if self.dir == 1:
            self.rect.x = self.rect.x + self.var_x
            self.nueva_img('bala_right.png')
        if self.dir == 2:
            self.rect.x = self.rect.x - self.var_x
            self.nueva_img('bala_left.png')
        if self.dir == 3:
            self.rect.y = self.rect.y - self.var_y
            self.nueva_img('bala_up.png')
        if self.dir == 4:
            self.rect.y = self.rect.y + self.var_y
            self.nueva_img('bala_down.png')

def create_EnemyDinamic():
    # creacion enemigo dinamico (archivo,           posxy,  dir, top, bottom, left, right)
    dinamic = EnemyDinamic('enemydinamic_up.png', [192, 346], 3, 192, 366, 0, 0)
    enemies_dinamic.add(dinamic)
    muros_obstaculo.add(dinamic)
    todos.add(dinamic)

    dinamic = EnemyDinamic('enemydinamic_down.png', [899, 471], 4, 471, 600, 0, 0)
    enemies_dinamic.add(dinamic)
    muros_obstaculo.add(dinamic)
    todos.add(dinamic)

def create_EnemyDinamicThree():
    '''
    dinamicos
    left 6 - right 155
    bottom 428 - top 279
    left 620 - right 893
    left 620 - right 924
    '''
    # creacion enemigo dinamico (archivo,           posxy,  dir, top, bottom, left, right)
    dinamic = EnemyDinamic('enemydinamic_left.png', [6, 186], 2, 0, 0, 6, 155)
    enemies_dinamic.add(dinamic)
    muros_obstaculo.add(dinamic)
    todos.add(dinamic)

    dinamic = EnemyDinamic('enemydinamic_up.png', [465, 403], 3, 279, 428, 0, 0)
    enemies_dinamic.add(dinamic)
    muros_obstaculo.add(dinamic)
    todos.add(dinamic)

    dinamic = EnemyDinamic('enemydinamic_left.png', [620, 248], 2, 0, 0, 620, 893)
    enemies_dinamic.add(dinamic)
    muros_obstaculo.add(dinamic)
    todos.add(dinamic)

    dinamic = EnemyDinamic('enemydinamic_left.png', [589, 465], 2, 0, 0, 589, 924)
    enemies_dinamic.add(dinamic)
    muros_obstaculo.add(dinamic)
    todos.add(dinamic)

def analizar_Colisiones():
    # Se analiza colision de las balas del jugador
    # con los diferentes muros (destruye ladrillos) (no destruye acero)
    for bala in bala_jp:
        col_ladrillos = pygame.sprite.spritecollide(bala, muros_ladrillo, True)
        col_aceros = pygame.sprite.spritecollide(bala, muros_acero, False)
        for e in col_ladrillos:
            bala_jp.remove(bala)
            todos.remove(bala)
        for i in col_aceros:
            bala_jp.remove(bala)
            todos.remove(bala)

    # Se analiza colision de las balas del enemigo
    # con los diferentes muros (destruye ladrillos) (no destruye acero)
    for bala in bala_enemy:
        col_ladrillos = pygame.sprite.spritecollide(bala, muros_ladrillo, True)
        col_aceros = pygame.sprite.spritecollide(bala, muros_acero, False)
        for e in col_ladrillos:
            bala_enemy.remove(bala)
            todos.remove(bala)
        for i in col_aceros:
            bala_enemy.remove(bala)
            todos.remove(bala)

    # Se analiza colision de bala de enemigo y bala del jugador, para que se autodestruyan entre si
    for bala in bala_enemy:
        col_balas = pygame.sprite.spritecollide(bala, bala_jp, True)
        for e in col_balas:
            bala_enemy.remove(bala)
            todos.remove(bala)
            # for bala in bala_jp:
            #     bala_jp.remove(bala)
            #     todos.remove(bala)
    jp.muros = muros_obstaculo

    # Se analiza colision bala enemigo con el tanque jugador
    balaEnemy_jp = pygame.sprite.spritecollide(jp, bala_enemy, True)
    for e in balaEnemy_jp:
        print "disparo jugador"
        perder_vida.play()
        jp.vidas = jp.vidas - 1
        # info.vidas = info.vidas - 1

    # Se analiza colision bala jugador con el tanque enemigo estatico
    for bala in bala_jp:
        balaJp_enemy = pygame.sprite.spritecollide(bala, enemies_static, True)
        for e in balaJp_enemy:
            disparo_tanqueEnemigo.play()
            bala_jp.remove(bala)
            jp.enemies = jp.enemies - 1
            todos.remove(bala)
            # info.enemigos = info.enemigos - 1

    # Se analiza colision bala jugador con el tanque enemigo dinamico
    for bala in bala_jp:
        balaJp_enemy = pygame.sprite.spritecollide(bala, enemies_dinamic, True)
        for e in balaJp_enemy:
            disparo_tanqueEnemigo.play()
            bala_jp.remove(bala)
            jp.enemies = jp.enemies - 1
            todos.remove(bala)

def Leer_Mapa(nombre_mapa):
    inicio = y = x_i = y_j = 0
    fin = map_columnas
    for k in range(map_filas):
        x_i = 0
        fila = nombre_mapa[inicio:fin]
        # print fila
        for element in fila:
            x = 0 + (x_i * muro_x)
            if element == '1':
                ladrillo = Muro('muro_ladrillo.png', [x,y])
                muros_ladrillo.add(ladrillo)
                muros_obstaculo.add(ladrillo)
                todos.add(ladrillo)
            elif element == '2':
                acero = Muro('muro_acero.png', [x,y])
                muros_acero.add(acero)
                muros_obstaculo.add(acero)
                todos.add(acero)
            elif element == '3':
                cesped = Muro('cesped.png', [x,y])
                todos.add(cesped)
                muros_cesped.add(cesped)
            elif element == '4':
                agua = Muro('agua.png', [x,y])
                muros_obstaculo.add(agua)
                todos.add(agua)
            elif element == '6_1':
                static = EnemyStatic('enemystatic_right.png', [x,y], 1)
                enemies_static.add(static)
                muros_obstaculo.add(static)
                todos.add(static)
            elif element == '6_2':
                static = EnemyStatic('enemystatic_left.png', [x,y], 2)
                enemies_static.add(static)
                muros_obstaculo.add(static)
                todos.add(static)
            elif element == '6_3':
                static = EnemyStatic('enemystatic_up.png', [x,y], 3)
                enemies_static.add(static)
                muros_obstaculo.add(static)
                todos.add(static)
            elif element == '6_4':
                static = EnemyStatic('enemystatic_down.png', [x,y], 4)
                enemies_static.add(static)
                muros_obstaculo.add(static)
                todos.add(static)
            elif element == '.':
                pass
                # print "numeral"
            x_i = x_i + 1
        y_j = y_j + 1
        y = 0 + (y_j * muro_y)
        inicio = fin
        fin = fin + map_columnas

class Barra_info(pygame.sprite.Sprite):
    def __init__(self):
        self.enemigos = 0
        self.vidas = 0
        self.nivel = 0

    def Perder_vidas(self):
        v=str(self.vidas)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render("Vidas:",True,BLANCO)
        vida=fuente.render(v,True,BLANCO)
        pantalla.blit(texto,[1100,50])
        pantalla.blit(vida,[1250,50])
        pygame.display.flip()

    def Matar_enemigos(self):
        M=str(self.enemigos)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render("Enemigos:",True,BLANCO)
        enemigos=fuente.render(M,True,BLANCO)
        pantalla.blit(texto,[1100,70])
        pantalla.blit(enemigos,[1250,70])
        pygame.display.flip()

    def Nivel_actual(self):
        N=str(self.nivel)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render("Nivel Actual:",True,BLANCO)
        nivel=fuente.render(N,True,BLANCO)
        pantalla.blit(texto,[1100,90])
        pantalla.blit(nivel,[1250,90])
        pygame.display.flip()

# info = Barra_info()

if __name__ == '__main__':
    # Inicializar pygame
    pygame.init()
    # Inicializar pantalla
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fuente = pygame.font.Font(None, 40)

    # info.enemigos = 12
    # info.vidas = 3
    # info.nivel = 1

    disparo_tanqueEnemigo = pygame.mixer.Sound("mato-enemigo.ogg")
    avance_nivel = pygame.mixer.Sound("ganar-primer-nivel.ogg")
    perder_vida = pygame.mixer.Sound("perder-vida.ogg")
    gameover = pygame.mixer.Sound("gameover.ogg")

    level_one = pygame.mixer.Sound("music_b.ogg")
    level_two = pygame.mixer.Sound("music_a.ogg")
    level_three = pygame.mixer.Sound("music_c.ogg")

    # PRIMER NIVEl
    fin = False
    pag = 1
    seguir = True
    victoria = False

    # Bienvenidad, titulo
    while not fin and seguir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Sale de ciclo y termina programa
                fin = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                pag += 1
                if pag > 2:
                    seguir = False
        if pag == 1:
            pantalla.fill(NEGRO)
            imagen = pygame.image.load('battle-city.png')
            imagen = pygame.transform.scale(imagen,(900,300))
            pantalla.blit(imagen, (150,150))
            pygame.display.flip()
        if pag == 2:
            pantalla.fill(NEGRO)
            letra30 = pygame.font.SysFont("Arial", 30)
            imagenTextoPresent = letra30.render("Pulsa Espacio para jugar", True, (200,200,200), (0,0,0) )
            rectanguloTextoPresent = imagenTextoPresent.get_rect()
            rectanguloTextoPresent.centerx = pantalla.get_rect().centerx
            rectanguloTextoPresent.centery = 520
            pantalla.blit(imagenTextoPresent, rectanguloTextoPresent)
            pygame.display.flip()

    seguir = True
    victoria = False

    # PRIMER NIVEL

    # Leer mapa PRIMER NIVEL (x y -> posiciones de la imagen)
    Leer_Mapa(mapa_one)

    # JUGADOR PRIMER NIVEL
    jp = Jugador('tanquedown.png')
    jp.muros = muros_obstaculo
    todos.add(jp)

    jefe = Muro('jefe.png', [961, 31])
    todos.add(jefe)

    # creacion enemigo dinamico (archivo, posxy, dir, top, bottom, left, right)
    create_EnemyDinamic()

    # DINAMICA NIVEL 1
    level_one.play()
    while seguir and not fin:
        # info.Perder_vidas()
        # info.Matar_enemigos()
        # info.Nivel_actual()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                # print "right",jp.rect.right
                # print "left",jp.rect.left
                # print "top",jp.rect.top
                # print "bottom",jp.rect.bottom,'\n'
                if event.key == pygame.K_RIGHT:
                    jp.dir = 1
                    jp.orientacion = 1
                if event.key == pygame.K_LEFT:
                    jp.dir = 2
                    jp.orientacion = 2
                if event.key == pygame.K_UP:
                    jp.dir = 3
                    jp.orientacion = 3
                if event.key == pygame.K_DOWN:
                    jp.dir = 4
                    jp.orientacion = 4
                if event.key == pygame.K_SPACE:

                    if jp.orientacion == 1:
                        bala = Bala_Jugador('bala_right.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 1
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 2:
                        bala = Bala_Jugador('bala_left.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 2
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 3:
                        bala = Bala_Jugador('bala_up.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 3
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 4:
                        bala = Bala_Jugador('bala_down.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 4
                        bala_jp.add(bala)
                        todos.add(bala)
        # Analiza todas las colisiones del juego GENERAL
        analizar_Colisiones()

        if jp.vidas <= 0:
            level_one.stop()
            gameover.play()
            victoria = False
            seguir = False
        if jp.rect.left == jefe.rect.left and jp.rect.top == jefe.rect.top:
            level_one.stop()
            avance_nivel.play()
            victoria = True
            seguir = False

        pantalla.fill(NEGRO)
        todos.add(jp)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

    # Si gano nivel uno o no
    if victoria:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Sale de ciclo y termina programa
                    fin= True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            texto1 = fuente.render("BONUS", True, BLANCO)
            texto2 = fuente.render("Objetivo: DESTRUYE A TODOS TUS ENEMIGOS", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto1, (400,60))
            pantalla.blit(texto2, (400,200))
            pygame.display.flip()
        fin = False
        seguir = True
    else:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Sale de ciclo y termina programa
                    fin = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            texto = fuente.render("JUEGA DE NUEVO", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto, (250,150))
            pygame.display.flip()

    # Limpia los grupos para el segundo nivel
    muros_ladrillo.empty()
    muros_acero.empty()
    muros_obstaculo.empty()
    muros_cesped.empty()
    bala_jp.empty()
    bala_enemy.empty()
    jefes.empty()
    enemies_static.empty()
    enemies_dinamic.empty()
    todos.empty()


    # SEGUNDO NIVEL BONUS
    # Leer mapa dos (x y -> posiciones de la imagen)
    Leer_Mapa(mapa_two)

    jp = Jugador('tanquedown.png')
    jp.muros = muros_obstaculo
    todos.add(jp)

    # creacion enemigo dinamico (archivo, posxy, dir, top, bottom, left, right)
    create_EnemyDinamic()

    level_two.play()
    # DINAMICA NIVEL 2
    while not fin and seguir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                # print "right",jp.rect.right
                # print "left",jp.rect.left
                # print "top",jp.rect.top
                # print "bottom",jp.rect.bottom,'\n'
                if event.key == pygame.K_RIGHT:
                    jp.dir = 1
                    jp.orientacion = 1
                if event.key == pygame.K_LEFT:
                    jp.dir = 2
                    jp.orientacion = 2
                if event.key == pygame.K_UP:
                    jp.dir = 3
                    jp.orientacion = 3
                if event.key == pygame.K_DOWN:
                    jp.dir = 4
                    jp.orientacion = 4
                if event.key == pygame.K_SPACE:

                    if jp.orientacion == 1:
                        bala = Bala_Jugador('bala_right.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 1
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 2:
                        bala = Bala_Jugador('bala_left.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 2
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 3:
                        bala = Bala_Jugador('bala_up.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 3
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 4:
                        bala = Bala_Jugador('bala_down.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 4
                        bala_jp.add(bala)
                        todos.add(bala)

        # Analiza todas las colisiones del juego GENERAL
        analizar_Colisiones()

        if jp.vidas <= 0:
            level_two.stop()
            gameover.play()
            victoria = False
            seguir = False
        if jp.enemies == 0:
            level_two.stop()
            avance_nivel.play()
            victoria = True
            seguir = False
            print "victoria"

        todos.add(jp)
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

    # Si gano nivel uno o no
    if victoria:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Sale de ciclo y termina programa
                    fin= True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            texto1 = fuente.render("NIVEL TRES", True, BLANCO)
            texto2 = fuente.render("DERROTA TODOS LOS ENEMIGOS Y LLEGA AL ESCUDO", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto1, (400,60))
            pantalla.blit(texto2, (400,200))
            pygame.display.flip()
        fin = False
        seguir = True
    else:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Sale de ciclo y termina programa
                    fin = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            texto = fuente.render("PERDISTE - JUEGA DE NUEVO", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto, (250,150))
            pygame.display.flip()

    # Limpia los grupos para el segundo nivel
    muros_ladrillo.empty()
    muros_acero.empty()
    muros_obstaculo.empty()
    muros_cesped.empty()
    bala_jp.empty()
    bala_enemy.empty()
    jefes.empty()
    enemies_static.empty()
    enemies_dinamic.empty()
    todos.empty()

    # TERCER NIVEL
    # Leer mapa TRES (x y -> posiciones de la imagen)
    Leer_Mapa(mapa_three)

    jp = Jugador('tanquedown.png')
    jp.muros = muros_obstaculo
    todos.add(jp)

    jefe = Muro('jefe.png', [961, 0])
    todos.add(jefe)
    jp.enemies = 16

    # creacion enemigo dinamico (archivo, posxy, dir, top, bottom, left, right)
    create_EnemyDinamicThree()

    level_three.play()
    # DINAMICA NIVEL 3
    '''
    dinamicos
    left 6 - right 155
    bottom 428 - top 279
    left 620 - right 893
    left 620 - right 924
    '''
    while not fin and seguir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                # print "right",jp.rect.right
                # print "left",jp.rect.left
                # print "top",jp.rect.top
                # print "bottom",jp.rect.bottom,'\n'
                if event.key == pygame.K_RIGHT:
                    jp.dir = 1
                    jp.orientacion = 1
                if event.key == pygame.K_LEFT:
                    jp.dir = 2
                    jp.orientacion = 2
                if event.key == pygame.K_UP:
                    jp.dir = 3
                    jp.orientacion = 3
                if event.key == pygame.K_DOWN:
                    jp.dir = 4
                    jp.orientacion = 4
                if event.key == pygame.K_SPACE:

                    if jp.orientacion == 1:
                        bala = Bala_Jugador('bala_right.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 1
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 2:
                        bala = Bala_Jugador('bala_left.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 2
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 3:
                        bala = Bala_Jugador('bala_up.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 3
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 4:
                        bala = Bala_Jugador('bala_down.png', [jp.rect.x, jp.rect.y])
                        bala.dir = 4
                        bala_jp.add(bala)
                        todos.add(bala)

        # Analiza todas las colisiones del juego GENERAL
        analizar_Colisiones()

        if jp.vidas <= 0:
            level_three.stop()
            gameover.play()
            victoria = False
            seguir = False
        if jp.enemies == 0 and (jp.rect.left == jefe.rect.left and jp.rect.top == jefe.rect.top) or (jp.rect.left == 961 and jp.rect.top == 6):
            level_three.stop()
            avance_nivel.play()
            victoria = True
            seguir = False
            print "victoria"

        todos.add(jp)
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

    # Si gano nivel uno o no
    if victoria:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Sale de ciclo y termina programa
                    fin= True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            texto1 = fuente.render("FELICITACIONES", True, BLANCO)
            texto2 = fuente.render("HAS GANADO", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto1, (400,60))
            pantalla.blit(texto2, (400,200))
            pygame.display.flip()
        fin = False
        seguir = True
    else:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Sale de ciclo y termina programa
                    fin = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            texto = fuente.render("PERDISTE - JUEGA DE NUEVO", True, BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto, (250,150))
            pygame.display.flip()

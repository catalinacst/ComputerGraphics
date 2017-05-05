import pygame
import random

ANCHO = 1302
ALTO = 651

NEGRO = (0, 0, 0)

'''
'1', -> muro ladrillo
'2', -> muro acero
'3', -> cesped
'4', -> agua
'5', -> jefe
'.', -> nada
'''
#             1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
#            20   21   22   23   24   25   26   27   28   29   30   31   32   33
mapa_one = [ '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '1', '2',  # 1

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '1', '5', '2',  # 2

             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '1', '2',  # 3

             '.', '.', '1', '1', '1', '1', '1', '1', '1', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.',
             '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 4

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 5

             '.', '3', '.', '1', '.', '.', '.', '.', '1', '1', '1', '1', '1', '1', '.', '.', '.', '1', '.',
             '.', '2', '1', '1', '1', '1', '1', '1', '1', '.', '.', '.', '.', '2',  # 6

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '2', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2',  # 7

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '2', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2',  # 8

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 9

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '1', '.',
             '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 10

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '2', '.', '.', '1', '.',
             '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 11

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '2', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '.', '2', # 12

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '2', '2', '2', '2', '2', '2', '.', '.', '1', '1',
             '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '.', '.', '2', # 13

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '1',
             '.', '.', '.', '.', '1', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 14

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '1', '.', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 15

             '.', '2', '2', '2', '.', '.', '.', '.', '.', '3', '4', '4', '4', '4', '3', '.', '.', '.', '.',
             '.', '.', '1', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 16

             '.', '1', '.', '.', '.', '.', '.', '.', '.', '3', '3', '3', '3', '3', '3', '.', '.', '.', '.',
             '.', '.', '1', '1', '1', '.', '.', '.', '.', '1', '.', '.', '.', '2', # 17

             '.', '1', '.', '.', '.', '.', '.', '.', '.', '3', '3', '3', '3', '3', '3', '.', '.', '.', '.',
             '.', '.', '1', '3', '1', '1', '1', '1', '1', '1', '.', '.', '.', '2', # 18

             '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '3', '3', '3', '3', '.', '.', '.', '.', '.',
             '.', '.', '2', '3', '3', '3', '3', '.', '.', '.', '.', '.', '.', '2', # 19

             '.', '1', '2', '1', '1', '1', '1', '2', '2', '3', '3', '4', '4', '4', '4', '4', '4', '4', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 21

             '.', '1', '2', '1', '1', '1', '1', '2', '2', '3', '3', '4', '4', '4', '4', '4', '4', '4', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 22
             ]

map_columnas = 33
map_filas = 22

muro_x = 31
muro_y = 31

# Creando grupos - Globales -
muros_ladrillo = pygame.sprite.Group()
muros_acero = pygame.sprite.Group()
muros_duros = pygame.sprite.Group()
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
            if desplx > ANCHO - 48:
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
            if desply > ALTO - 50:
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
    def __init__(self,archivo_img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 0
        self.var_y = 1

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        desply = self.rect.y
        self.rect.y = self.rect.y + self.var_y
        self.nueva_img('bala_down.png')

class EnemyStatic(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.temp = random.randint(200,500)

    def update(self):
        self.temp = self.temp - 1
        if self.temp == 0:
            bala = Bala_Enemigos('bala_down.png', [self.rect.x, self.rect.y])
            bala.dir = 4
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
        self.var_y = 1
        self.var_x = 1

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


if __name__ == '__main__':
    # Inicializar pygame
    pygame.init()
    # Inicializar pantalla
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    # Leer mapa (x y -> posiciones de la imagen)
    inicio = y = x_i = y_j = 0
    fin = map_columnas
    for k in range(map_filas):
        x_i = 0
        fila = mapa_one[inicio:fin]
        # print fila
        for element in fila:
            x = 0 + (x_i * muro_x)
            if element == '1':
                ladrillo = Muro('muro_ladrillo.png', [x,y])
                muros_ladrillo.add(ladrillo)
                muros_duros.add(ladrillo)
                todos.add(ladrillo)
            elif element == '2':
                acero = Muro('muro_acero.png', [x,y])
                muros_acero.add(acero)
                muros_duros.add(acero)
                todos.add(acero)
            elif element == '3':
                cesped = Muro('cesped.png', [x,y])
                todos.add(cesped)
                muros_ladrillo.add(cesped)
            elif element == '4':
                agua = Muro('agua.png', [x,y])
                todos.add(agua)
                muros_ladrillo.add(agua)
            elif element == '5':
                jefe = Muro('jefe.png', [x,y])
                todos.add(jefe)
                jefes.add(jefe)
            elif element == '.':
                pass
                # print "numeral"
            x_i = x_i + 1
        y_j = y_j + 1
        y = 0 + (y_j * muro_y)
        inicio = fin
        fin = fin + map_columnas

    jp = Jugador('tanquedown.png')
    jp.muros = muros_duros
    todos.add(jp)

    static = EnemyStatic('enemystatic_down.png', [64, 5])
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_down.png', [64, 5])
    enemies_static.add(static)
    todos.add(static)

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
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
            col_balas = pygame.sprite.spritecollide(bala, bala_jp, False)
            for e in col_balas:
                bala_enemy.remove(bala)
                todos.remove(bala)
                for bala in bala_jp:
                    bala_jp.remove(bala)
                    todos.remove(bala)
        jp.muros = muros_duros

        # Se analiza colision bala enemigo con el tanque jugador
        balaEnemy_jp = pygame.sprite.spritecollide(jp, bala_enemy, True)
        for e in balaEnemy_jp:
            print "disparo jugador"

        # Se analiza colision bala jugador con el tanque enemigo
        for bala in bala_jp:
            balaJp_enemy = pygame.sprite.spritecollide(bala, enemies_static, True)
            for e in balaJp_enemy:
                bala_jp.remove(bala)
                todos.remove(bala)

        todos.add(jp)
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

        # print "left",e.rect.left
        # print "right",e.rect.right
        # print "down",e.rect.bottom # down
        # print "up",e.rect.top # up
        # print "x",e.rect.x
        # print "y",e.rect.y
        # print "bala_left",bala.rect.left
        # print "bala_right",bala.rect.right
        # print "bala_down",bala.rect.bottom
        # print "bala_up",bala.rect.top,'\n'

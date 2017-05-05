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
'.', -> nada
'''
#             1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
#            20   21   22   23   24   25   26   27   28   29   30   31   32   33
mapa_one = [ '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '1', '1', '2',  # 1

             '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '2', '.', '.', '2', '2', '2', '2', '1', '1', '1', '1', '.', '2',  # 2

             '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '2', '.', '2', '.', '.', '.', '.', '.', '.', '2', '1', '1', '2',  # 3

             '.', '.', '.', '1', '1', '1', '1', '1', '1', '.', '.', '.', '.', '.', '.', '.', '.', '1', '.',
             '.', '2', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '2',  # 4

             '.', '1', '.', '1', '.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.', '.', '.', '.', '.',
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

             '.', '1', '.', '1', '.', '2', '.', '2', '.', '2', '.', '1', '.', '.', '2', '.', '.', '.', '.',
             '.', '.', '1', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '2', # 12

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

             '.', '2', '.', '.', '2', '.', '.', '.', '.', '.', '3', '3', '3', '3', '2', '.', '.', '.', '.',
             '.', '3', '3', '3', '3', '3', '3', '2', '.', '.', '.', '.', '.', '2', # 19

             '.', '1', '1', '2', '3', '3', '3', '2', '2', '4', '4', '4', '4', '4', '4', '4', '4', '4', '.',
             '.', '2', '4', '4', '4', '4', '2', '.', '.', '.', '.', '.', '.', '2',  # 21

             '.', '2', '2', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '.',
             '.', '2', '4', '4', '4', '2', '.', '.', '.', '.', '.', '.', '.', '2',  # 22
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
        self.vidas = 3
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

def create_EnemyStatic():
    static = EnemyStatic('enemystatic_down.png', [62, 5], 4)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_up.png', [248, 563], 3)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_up.png', [409, 347], 3)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_down.png', [124, 124], 4)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_up.png', [409, 347], 3)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_up.png', [589, 589], 3)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_left.png', [527, 67], 2)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_left.png', [843, 372], 2)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_left.png', [651, 285], 2)
    enemies_static.add(static)
    todos.add(static)

    static = EnemyStatic('enemystatic_left.png', [905, 6], 2)
    enemies_static.add(static)
    todos.add(static)

def create_EnemyDinamic():
    dinamic = EnemyDinamic('enemydinamic_up.png', [192, 346], 3, 192, 346, 0, 0)
    enemies_dinamic.add(dinamic)
    todos.add(dinamic)

    dinamic = EnemyDinamic('enemydinamic_down.png', [899, 471], 4, 471, 626, 0, 0)
    enemies_dinamic.add(dinamic)
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
        jp.vidas = jp.vidas - 1
        info.vidas = info.vidas - 1

    # Se analiza colision bala jugador con el tanque enemigo estatico
    for bala in bala_jp:
        balaJp_enemy = pygame.sprite.spritecollide(bala, enemies_static, True)
        for e in balaJp_enemy:
            bala_jp.remove(bala)
            todos.remove(bala)
            info.enemigos = info.enemigos - 1


    # Se analiza colision bala jugador con el tanque enemigo dinamico
    for bala in bala_jp:
        balaJp_enemy = pygame.sprite.spritecollide(bala, enemies_dinamic, True)
        for e in balaJp_enemy:
            bala_jp.remove(bala)
            todos.remove(bala)

def Leer_Mapa_NivelUno():
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

info = Barra_info()

if __name__ == '__main__':
    # Inicializar pygame
    pygame.init()
    # Inicializar pantalla
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    # Leer mapa PRIMER NIVEL (x y -> posiciones de la imagen)
    Leer_Mapa_NivelUno()

    jp = Jugador('tanquedown.png')
    jp.muros = muros_duros
    todos.add(jp)

    jefe = Muro('jefe.png', [961, 31])
    todos.add(jefe)

    # creacion enemigo dinamicos
    create_EnemyStatic()

    # creacion enemigo dinamico (archivo, posxy, dir, top, bottom, left, right)
    create_EnemyDinamic()

    info.enemigos = 12
    info.vidas = 3
    info.nivel = 1

    # PRIMER NIVEl
    fin = False
    victoria = False
    seguir = True
    while seguir and not fin:
        info.Perder_vidas()
        info.Matar_enemigos()
        info.Nivel_actual()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                seguir = False
            if jp.vidas == 0:
                victoria = False
            if (jp.rect.left == jefe.rect.left) or (jp.rect.left == 961 and jp.rect.top == 62):
                victoria = True

                print "victoria"
            if event.type == pygame.KEYDOWN:
                print "left",jp.rect.left
                print "top",jp.rect.top
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

        todos.add(jp)
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

        # SEGUNDO NIVEL

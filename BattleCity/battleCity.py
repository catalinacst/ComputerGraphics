import pygame
import random

ANCHO = 1302
ALTO = 651

NEGRO = (0, 0, 0)

'''
'$', -> nada
'#', -> muro ladrillo
'&', -> muro acero
'.', -> pasto
'''
#             1    2    3    4    5    6    7    8    9   10   11   12   13   14
mapa_one = [ '$', '$', '$', '$', '$', '$', '$', '$', '$', '&', '$', '$', '$', '$', # 1
             '$', '#', '#', '#', '$', '#', '#', '$', '#', '&', '$', '#', '#', '#', # 2
             '$', '#', '$', '#', '$', '$', '.', '$', '#', '&', '$', '#', '$', '#', # 3
             '$', '#', '$', '#', '$', '$', '.', '$', '#', '&', '$', '#', '#', '#', # 4
             '$', '#', '$', '#', '$', '$', '.', '$', '#', '&', '$', '#', '$', '#', # 5
             '$', '#', '$', '#', '$', '$', '.', '$', '#', '#', '$', '#', '$', '#', # 6
             '$', '#', '$', '#', '$', '#', '#', '$', '#', '#', '$', '#', '$', '#'  # 7
             ]

map_columnas = 14
map_filas = 7
muro_x = 31
muro_y = 31

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
        # self.rect = self.image.get_rec()

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

class Muro(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Bala(pygame.sprite.Sprite):
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
        '''
        dir = 1 derecha
        dir = 2 izquierda
        dir = 3 arriba
        dir = 4 abajo
        '''
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

    # Creando grupos
    muros = pygame.sprite.Group()
    enemies_estatic = pygame.sprite.Group()
    enemies_dinamic = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    todos = pygame.sprite.Group()

    # Leer mapa
    # x y -> posiciones de la imagen
    inicio = y = x_i = y_j = 0
    fin = map_columnas
    for k in range(map_filas):
        x_i = 0
        fila = mapa_one[inicio:fin]
        # print fila
        for element in fila:
            x = 0 + (x_i * muro_x)
            if element == '#':
                muro_ladrillo = Muro('muro_ladrillo.png', [x,y])
                todos.add(muro_ladrillo)
                muros.add(muro_ladrillo)
                #print [x,y]
            elif element == '&':
                muro_acero = Muro('muro_acero.png', [x,y])
                todos.add(muro_acero)
                muros.add(muro_acero)
            elif element == '.':
                cesped = Muro('cesped.png', [x,y])
                todos.add(cesped)
                muros.add(cesped)
            elif element == '$':
                pass
                # print "numeral"
            x_i = x_i + 1
        y_j = y_j + 1
        y = 0 + (y_j * muro_y)
        inicio = fin
        fin = fin + map_columnas

    jp = Jugador('tanquedown.png')
    jp.muros = muros
    todos.add(jp)

    # # Nivel 1
    # static = 2
    # dinamic = 4

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
                        bala = Bala('bala_right.png', [jp.rect.x, jp.rect.y])
                        print jp.rect.x,"right",jp.rect.y,'\n'
                        bala.dir = 1
                        balas.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 2:
                        bala = Bala('bala_left.png', [jp.rect.x, jp.rect.y])
                        print jp.rect.x,"left",jp.rect.y,'\n'
                        bala.dir = 2
                        balas.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 3:
                        bala = Bala('bala_up.png', [jp.rect.x, jp.rect.y])
                        print jp.rect.x,"up",jp.rect.y,'\n'
                        bala.dir = 3
                        balas.add(bala)
                        todos.add(bala)
                    elif jp.orientacion == 4:
                        bala = Bala('bala_down.png', [jp.rect.x, jp.rect.y])
                        print jp.rect.x,"down",jp.rect.y,'\n'
                        bala.dir = 4
                        balas.add(bala)
                        todos.add(bala)

        for bala in balas:
            l_imp = pygame.sprite.spritecollide(bala, muros, True)
            for e in l_imp:
                balas.remove(bala)
                todos.remove(bala)

        jp.muros = muros
        todos.add(jp)
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

        # dir = 1 derecha
        # dir = 2 izquierda
        # dir = 3 arriba
        # dir = 4 abajo

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

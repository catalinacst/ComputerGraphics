import pygame
import random
#Mostrar texto en pantalla
ALTO = 500
ANCHO = 1200

BLANCO = (255,255,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)

todos = pygame.sprite.Group()
bloques = pygame.sprite.Group()
enemies_static = pygame.sprite.Group()
bala_jp = pygame.sprite.Group()

class Bala_Jugador(pygame.sprite.Sprite):
    def __init__(self,archivo_img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 0
        self.var_x = 10

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        desplx = self.rect.x
        if self.dir == 1:
            self.rect.x = self.rect.x + self.var_x
            self.nueva_img('bala_right.png')
        if self.dir == 2:
            self.rect.x = self.rect.x - self.var_x
            self.nueva_img('bala_left.png')

class Bala_Enemigos(pygame.sprite.Sprite):
    def __init__(self,archivo_img, pos, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dire
        self.var_x = 7
        self.var_y = 7

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def update(self):
        desplx = self.rect.x
        desply = self.rect.y
        if self.dir == 2:
            self.rect.x = self.rect.x - self.var_x
            self.nueva_img('bala_enemy01.png')
        elif self.dir == 3:
            self.rect.y = self.rect.y - self.var_y
            self.nueva_img('bala_enemy01.png')
        elif self.dir == 4:
            self.rect.y = self.rect.y + self.var_y
            self.nueva_img('bala_enemy01.png')

class EnemyStatic(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dire
        self.temp = random.randint(100,200)

    def update(self):
        self.temp = self.temp - 1
        if self.temp == 0:
            if self.dir == 2:
                bala = Bala_Enemigos('bala_enemy01.png', [self.rect.x, self.rect.y], self.dir)
                todos.add(bala)
                self.temp = random.randint(100,200)

class Muro(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.velocidad = 1
        self.vary = 0
        self.varx = 4
        self.saltar = 0
        self.bloques = []
        self.dir = 0
        self.orientacion = 0
        self.balaright = 0
        self.balaleft = 0

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()

    def salto(self):
        if self.vary == 0:
            self.vary = -9

    def gravedad(self):
        if self.vary == 0:
            self.vary = 1
        else:
            self.vary += 0.35
        piso = ALTO - self.rect.height
        if self.rect.y >= piso and self.vary >= 0:
            self.vary = 0
            self.rect.y = piso

    def update(self):
        self.gravedad()
        desplx = self.rect.x
        '''
        dir = 1 derecha
        dir = 2 izquierda
        dir = 3 arriba
        dir = 4 abajo
        '''
        if self.dir == 1:
            self.rect.x = self.rect.x + self.varx
            self.nueva_img('right.png')
        if self.dir == 2:
            self.rect.x = self.rect.x - self.varx
            if self.rect.left <= 0:
                self.rect.left = 0
            self.nueva_img('left.png')


        lc = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in lc:
            if self.dir == 1:
                self.rect.right = b.rect.left
            elif self.dir == 2:
                self.rect.left = b.rect.right

        self.rect.y += self.vary

        # cambio de posicion en y
        lc = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in lc:
            if self.vary > 0:
                self.rect.bottom = b.rect.top
            if self.vary < 0:
                self.rect.top = b.rect.bottom

            self.vary = 0
            self.varx = 4

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))

    # cargar imagen
    fondo = pygame.image.load("fondo01.png")

    # static = EnemyStatic('enemystatic_right.png', [x,y], 1)

    jp = Jugador("right.png")
    jp.bloques  =  bloques
    todos.add(jp)

    muro = Muro("ladrillo.png", [200,400])
    bloques.add(muro)
    todos.add(muro)

    muro2 = Muro("ladrillo.png", [300,400])
    bloques.add(muro2)
    todos.add(muro2)

    muro3 = Muro("ladrillo.png", [1000,400])
    bloques.add(muro3)
    todos.add(muro3)

    muro4 = Muro("ladrillo.png", [1500,400])
    bloques.add(muro4)
    todos.add(muro4)

    muro5 = Muro("ladrillo.png", [1545,400])
    bloques.add(muro5)
    todos.add(muro5)

    static = EnemyStatic('seniortopo.png', [1545,359], 2)
    enemies_static.add(static)
    todos.add(static)

    # seniortopo.png

    jp.bloques = bloques

    posx = 0
    posy = -300
    mov_x = 1
    pantalla.blit(fondo,(posx,posy))
    pantalla_tam = 0
    fin  = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.dir = 1
                if event.key == pygame.K_LEFT:
                    jp.dir = 2
                if event.key == pygame.K_UP:
                    print 'salto'
                    jp.salto()
                if event.key == pygame.K_SPACE:
                    if jp.dir == 1:
                        bala = Bala_Jugador('bala_right.png', [jp.rect.x, jp.rect.y + 15])
                        jp.balaright = 1
                        bala.dir = 1
                        bala_jp.add(bala)
                        todos.add(bala)
                    elif jp.dir == 2:
                        bala = Bala_Jugador('bala_left.png', [jp.rect.x, jp.rect.y + 15])
                        jp.balaright = 2
                        bala.dir = 2
                        bala_jp.add(bala)
                        todos.add(bala)

        muro.rect.x = muro.rect.x - 2
        muro2.rect.x = muro2.rect.x - 2
        muro3.rect.x = muro3.rect.x - 2
        muro4.rect.x = muro4.rect.x - 2
        muro5.rect.x = muro5.rect.x - 2
        static.rect.x = static.rect.x - 2

        if posx == -500:
            # cargar imagen
            fondo = pygame.image.load("fondo01.png")
            posx = 0
            posy = -300
            mov_x = 2
            pantalla_tam = pantalla_tam + 1

        posx = posx - mov_x
        pantalla.fill(NEGRO)
        pantalla.blit(fondo,(posx,posy))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()

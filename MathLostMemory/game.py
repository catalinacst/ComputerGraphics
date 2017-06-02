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
bala_enemy = pygame.sprite.Group()
jefe = pygame.sprite.Group()

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
        self.temp = random.randint(150,200)

    def update(self):
        self.temp = self.temp - 1
        if self.temp == 0:
            if self.dir == 2:
                bala = Bala_Enemigos('bala_enemy01.png', [self.rect.x, self.rect.y + 10], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(150,200)
            if self.dir == 3:
                bala = Bala_Enemigos('bala_enemy01.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(50,100)

class Bruja(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dire
        self.vida = 20
        self.temp = random.randint(90,150)

    def update(self):
        self.temp = self.temp - 1
        if self.temp == 0:
            if self.dir == 2:
                bala = Bala_Enemigos('bala_enemy01.png', [self.rect.x, self.rect.y + 10], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(150,200)
            if self.dir == 3:
                bala = Bala_Enemigos('bala_enemy01.png', [self.rect.x, self.rect.y], self.dir)
                bala_enemy.add(bala)
                todos.add(bala)
                self.temp = random.randint(50,100)


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
        self.vidas = 3

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

def analizar_Colisiones():
    # Se analiza colision de bala de enemigo y bala del jugador, para que se autodestruyan entre si
    for bala in bala_enemy:
        col_balas = pygame.sprite.spritecollide(bala, bala_jp, True)
        for e in col_balas:
            bala_enemy.remove(bala)
            todos.remove(bala)

    # Se analiza colision bala enemigo con el tanque jugador
    balaEnemy_jp = pygame.sprite.spritecollide(jp, bala_enemy, True)
    for e in balaEnemy_jp:
        print "disparo jugador"
        jp.vidas = jp.vidas - 1

    # Se analiza colision bala jugador con el tanque enemigo estatico
    for bala in bala_jp:
        balaJp_enemy = pygame.sprite.spritecollide(bala, enemies_static, True)
        for e in balaJp_enemy:
            bala_jp.remove(bala)
            todos.remove(bala)

    # Se analiza colision de las balas del jugador
    # con los diferentes muros (destruye muritosjpgno destruye acero)
    for bala in bala_jp:
        col_ladrillos = pygame.sprite.spritecollide(bala, bloques, False)
        for e in col_ladrillos:
            bala_jp.remove(bala)
            todos.remove(bala)

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

    topo1 = EnemyStatic('seniortopo.png', [1545,359], 2)
    bloques.add(topo1)
    enemies_static.add(topo1)
    todos.add(topo1)

    muro6 = Muro("ladrillo.png", [1700,400])
    bloques.add(muro6)
    todos.add(muro6)

    muro7 = Muro("ladrillo.png", [1745,400])
    bloques.add(muro7)
    todos.add(muro7)

    muro8 = Muro("ladrillo.png", [1790,400])
    bloques.add(muro8)
    todos.add(muro8)

    muro9 = Muro("ladrillo.png", [1790,445])
    bloques.add(muro9)
    todos.add(muro9)

    topo2 = EnemyStatic('seniortopo.png', [1700,459], 2)
    enemies_static.add(topo2)
    bloques.add(topo2)
    todos.add(topo2)

    volcano1 = EnemyStatic('volcano.png', [1900,459], 3)
    enemies_static.add(volcano1)
    bloques.add(volcano1)
    todos.add(volcano1)

    volcano2 = EnemyStatic('volcano.png', [1975,459], 3)
    enemies_static.add(volcano2)
    bloques.add(volcano2)
    todos.add(volcano2)

    muro10 = Muro("ladrillo.png", [2100,445])
    bloques.add(muro10)
    todos.add(muro10)

    muro11 = Muro("ladrillo.png", [2175,445])
    bloques.add(muro11)
    todos.add(muro11)

    muro12 = Muro("ladrillo.png", [2245,445])
    bloques.add(muro12)
    todos.add(muro12)

    muro13 = Muro("ladrillo.png", [2400,400])
    bloques.add(muro13)
    todos.add(muro13)

    muro14 = Muro("ladrillo.png", [2475,400])
    bloques.add(muro14)
    todos.add(muro14)

    topo3 = EnemyStatic('seniortopo.png', [2475,359], 2)
    bloques.add(topo3)
    enemies_static.add(topo3)
    todos.add(topo3)

    muro15 = Muro("ladrillo.png", [2600,400])
    bloques.add(muro15)
    todos.add(muro15)

    volcano3 = EnemyStatic('volcano.png', [2600,357], 3)
    enemies_static.add(volcano3)
    bloques.add(volcano3)
    todos.add(volcano3)

    topo4 = EnemyStatic('seniortopo.png', [2600,459], 2)
    bloques.add(topo4)
    enemies_static.add(topo4)
    todos.add(topo4)

    topo5 = EnemyStatic('seniortopo.png', [2800,459], 2)
    bloques.add(topo5)
    enemies_static.add(topo5)
    todos.add(topo5)

    volcano4 = EnemyStatic('volcano.png', [2900,457], 3)
    enemies_static.add(volcano4)
    bloques.add(volcano4)
    todos.add(volcano4)

    muro16 = Muro("ladrillo.png", [3000,400])
    bloques.add(muro16)
    todos.add(muro16)

    muro17 = Muro("ladrillo.png", [3045,400])
    bloques.add(muro17)
    todos.add(muro17)

    muro18 = Muro("ladrillo.png", [3090,400])
    bloques.add(muro18)
    todos.add(muro18)

    muro19 = Muro("ladrillo.png", [3135,400])
    bloques.add(muro19)
    todos.add(muro19)

    muro20 = Muro("ladrillo.png", [3180,400])
    bloques.add(muro20)
    todos.add(muro20)

    muro21 = Muro("ladrillo.png", [3225,400])
    bloques.add(muro21)
    todos.add(muro21)

    muro22 = Muro("ladrillo.png", [3225,445])
    bloques.add(muro22)
    todos.add(muro22)

    topo6 = EnemyStatic('seniortopo.png', [3225,359], 2)
    bloques.add(topo6)
    enemies_static.add(topo6)
    todos.add(topo6)

    volcano5 = EnemyStatic('volcano.png', [3270,457], 3)
    enemies_static.add(volcano5)
    bloques.add(volcano5)
    todos.add(volcano5)

    meta = Muro('meta.png', [3500,457])
    bloques.add(meta)
    todos.add(meta)

    # seniortopo.png
    # volcano.png

    jp.bloques = bloques
    level_one = pygame.mixer.Sound("music01.ogg")
    flecha = pygame.mixer.Sound("flecha.ogg")
    fireball = pygame.mixer.Sound("fireball.ogg")

    posx = 0
    posy = -300
    mov_x = 1
    pantalla.blit(fondo,(posx,posy))
    pantalla_tam = 0
    fin  = False
    level_one.play()
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
                    flecha.play()
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
        muro2.rect.x -= 2
        muro3.rect.x -= 2
        muro4.rect.x -= 2
        muro5.rect.x -= 2
        muro6.rect.x -= 2
        muro7.rect.x -= 2
        muro8.rect.x -= 2
        muro9.rect.x -= 2
        muro10.rect.x -= 2
        muro11.rect.x -= 2
        muro12.rect.x -= 2
        muro13.rect.x -= 2
        muro14.rect.x -= 2
        muro15.rect.x -= 2
        muro16.rect.x -= 2
        muro17.rect.x -= 2
        muro18.rect.x -= 2
        muro19.rect.x -= 2
        muro20.rect.x -= 2
        muro21.rect.x -= 2
        muro22.rect.x -= 2

        topo1.rect.x -= 2
        topo2.rect.x -= 2
        topo3.rect.x -= 2
        topo4.rect.x -= 2
        topo5.rect.x -= 2
        topo6.rect.x -= 2

        volcano1.rect.x -= 2
        volcano2.rect.x -= 2
        volcano3.rect.x -= 2
        volcano4.rect.x -= 2
        volcano5.rect.x -= 2

        meta.rect.x -= 2

        jp.bloques = bloques

        if not jp.rect.right >= meta.rect.left - 10:
            if posx == -500:
                # cargar imagen
                fondo = pygame.image.load("fondo01.png")
                posx = 0
                posy = -300
                mov_x = 2
                pantalla_tam = pantalla_tam + 1

            # Analiza todas las colisiones del juego GENERAL
            analizar_Colisiones()

            posx = posx - mov_x
            pantalla.fill(NEGRO)
            pantalla.blit(fondo,(posx,posy))
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
        else:
            level_one.stop()
            pantalla.fill(NEGRO)
            pygame.display.flip()

            todos.empty()
            bloques.empty()
            enemies_static.empty()
            bala_jp.empty()
            bala_enemy.empty()

            # cargar imagen
            fondo = pygame.image.load("fondo02.png")

            jp = Jugador("right.png")
            jp.bloques  =  bloques
            todos.add(jp)

            muro = Muro("murito.jpg", [200,400])
            bloques.add(muro)
            todos.add(muro)

            muro2 = Muro("murito.jpg", [300,400])
            bloques.add(muro2)
            todos.add(muro2)

            muro3 = Muro("murito.jpg", [1000,400])
            bloques.add(muro3)
            todos.add(muro3)

            muro4 = Muro("murito.jpg", [1500,400])
            bloques.add(muro4)
            todos.add(muro4)

            muro5 = Muro("murito.jpg", [1545,400])
            bloques.add(muro5)
            todos.add(muro5)

            topo1 = EnemyStatic('gordito.png', [1545,359], 2)
            bloques.add(topo1)
            enemies_static.add(topo1)
            todos.add(topo1)

            muro6 = Muro("murito.jpg", [1700,400])
            bloques.add(muro6)
            todos.add(muro6)

            muro7 = Muro("murito.jpg", [1745,400])
            bloques.add(muro7)
            todos.add(muro7)

            muro8 = Muro("murito.jpg", [1790,400])
            bloques.add(muro8)
            todos.add(muro8)

            muro9 = Muro("murito.jpg", [1790,445])
            bloques.add(muro9)
            todos.add(muro9)

            topo2 = EnemyStatic('gordito.png', [1700,459], 2)
            enemies_static.add(topo2)
            bloques.add(topo2)
            todos.add(topo2)

            volcano1 = EnemyStatic('nano.png', [1900,459], 3)
            enemies_static.add(volcano1)
            bloques.add(volcano1)
            todos.add(volcano1)

            volcano2 = EnemyStatic('nano.png', [1975,459], 3)
            enemies_static.add(volcano2)
            bloques.add(volcano2)
            todos.add(volcano2)

            muro10 = Muro("murito.jpg", [2100,445])
            bloques.add(muro10)
            todos.add(muro10)

            muro11 = Muro("murito.jpg", [2175,445])
            bloques.add(muro11)
            todos.add(muro11)

            muro12 = Muro("murito.jpg", [2245,445])
            bloques.add(muro12)
            todos.add(muro12)

            muro13 = Muro("murito.jpg", [2400,400])
            bloques.add(muro13)
            todos.add(muro13)

            muro14 = Muro("murito.jpg", [2475,400])
            bloques.add(muro14)
            todos.add(muro14)

            topo3 = EnemyStatic('gordito.png', [2475,359], 2)
            bloques.add(topo3)
            enemies_static.add(topo3)
            todos.add(topo3)

            muro15 = Muro("murito.jpg", [2600,400])
            bloques.add(muro15)
            todos.add(muro15)

            volcano3 = EnemyStatic('nano.png', [2600,357], 3)
            enemies_static.add(volcano3)
            bloques.add(volcano3)
            todos.add(volcano3)

            topo4 = EnemyStatic('gordito.png', [2600,459], 2)
            bloques.add(topo4)
            enemies_static.add(topo4)
            todos.add(topo4)

            topo5 = EnemyStatic('gordito.png', [2800,459], 2)
            bloques.add(topo5)
            enemies_static.add(topo5)
            todos.add(topo5)

            volcano4 = EnemyStatic('nano.png', [2900,457], 3)
            enemies_static.add(volcano4)
            bloques.add(volcano4)
            todos.add(volcano4)

            muro16 = Muro("murito.jpg", [3000,400])
            bloques.add(muro16)
            todos.add(muro16)

            muro17 = Muro("murito.jpg", [3045,400])
            bloques.add(muro17)
            todos.add(muro17)

            muro18 = Muro("murito.jpg", [3090,400])
            bloques.add(muro18)
            todos.add(muro18)

            muro19 = Muro("murito.jpg", [3135,400])
            bloques.add(muro19)
            todos.add(muro19)

            muro20 = Muro("murito.jpg", [3180,400])
            bloques.add(muro20)
            todos.add(muro20)

            muro21 = Muro("murito.jpg", [3225,400])
            bloques.add(muro21)
            todos.add(muro21)

            muro22 = Muro("murito.jpg", [3225,445])
            bloques.add(muro22)
            todos.add(muro22)

            topo6 = EnemyStatic('gordito.png', [3225,359], 2)
            bloques.add(topo6)
            enemies_static.add(topo6)
            todos.add(topo6)

            volcano5 = EnemyStatic('nano.png', [3270,457], 3)
            enemies_static.add(volcano5)
            bloques.add(volcano5)
            todos.add(volcano5)

            bruja = Bruja('bruja.png', [3500,359], 2)
            bloques.add(bruja)
            todos.add(bruja)

            bruja2 = Bruja('bruja.png', [3500,439], 2)
            bloques.add(bruja2)
            todos.add(bruja2)

            jp.bloques = bloques
            level2 = pygame.mixer.Sound("level2.ogg")
            flecha = pygame.mixer.Sound("flecha.ogg")
            fireball = pygame.mixer.Sound("fireball.ogg")

            posx = 0
            posy = -300
            mov_x = 1
            pantalla.blit(fondo,(posx,posy))
            pantalla_tam = 0
            fin  = False
            level2.play()
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
                            flecha.play()
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
                muro2.rect.x -= 2
                muro3.rect.x -= 2
                muro4.rect.x -= 2
                muro5.rect.x -= 2
                muro6.rect.x -= 2
                muro7.rect.x -= 2
                muro8.rect.x -= 2
                muro9.rect.x -= 2
                muro10.rect.x -= 2
                muro11.rect.x -= 2
                muro12.rect.x -= 2
                muro13.rect.x -= 2
                muro14.rect.x -= 2
                muro15.rect.x -= 2
                muro16.rect.x -= 2
                muro17.rect.x -= 2
                muro18.rect.x -= 2
                muro19.rect.x -= 2
                muro20.rect.x -= 2
                muro21.rect.x -= 2
                muro22.rect.x -= 2

                topo1.rect.x -= 2
                topo2.rect.x -= 2
                topo3.rect.x -= 2
                topo4.rect.x -= 2
                topo5.rect.x -= 2
                topo6.rect.x -= 2

                volcano1.rect.x -= 2
                volcano2.rect.x -= 2
                volcano3.rect.x -= 2
                volcano4.rect.x -= 2
                volcano5.rect.x -= 2

                if bruja.rect.x > 1200 - 100:
                    bruja.rect.x -= 2
                    bruja2.rect.x -= 2

                jp.bloques = bloques

                if 0 or (bruja2.vida > 0 and bruja.vida > 0):
                    if posx == -500:
                        # cargar imagen
                        fondo = pygame.image.load("fondo02.png")
                        posx = 0
                        posy = -300
                        mov_x = 2
                        pantalla_tam = pantalla_tam + 1

                    # Se analiza colision bala jugador con el tanque enemigo dinamico
                    balaJp_enemy = pygame.sprite.spritecollide(bruja2, bala_jp, False)
                    for e in balaJp_enemy:
                        bala_jp.remove(bala)
                        print "vida menos bruja2"
                        print bruja2.vida
                        bruja2.vida = bruja2.vida - 1
                        todos.remove(bala)

                    balaJp_enemy = pygame.sprite.spritecollide(bruja, bala_jp, False)
                    for e in balaJp_enemy:
                        bala_jp.remove(bala)
                        print "vida menos bruja"
                        print bruja.vida
                        bruja.vida = bruja.vida - 1
                        todos.remove(bala)

                    # Analiza todas las colisiones del juego GENERAL
                    analizar_Colisiones()

                    posx = posx - mov_x
                    pantalla.fill(NEGRO)
                    pantalla.blit(fondo,(posx,posy))
                    todos.update()
                    todos.draw(pantalla)
                    pygame.display.flip()
                else:
                    pantalla.fill(NEGRO)
                    pygame.display.flip()

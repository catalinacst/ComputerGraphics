import pygame
import random
import ConfigParser

ANCHO = 1000
ALTO = 600

NEGRO = (0, 0, 0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.dir = 0
        self.var_x = 4
        self.var_y = 4
        self.muros = []

    def nueva_img(self, archivo):
        self.image = pygame.image.load(archivo).convert_alpha()
        # self.rect = self.image.get_rec()

    def update(self):
        desplx = self.rect.x
        desply = self.rect.y
        if self.dir == 1:
            self.rect.x += self.var_x
            if desplx > ANCHO - 48:
                self.dir = 2
            self.nueva_img('tanqueright.png')
        if self.dir == 2:
            self.rect.x -= self.var_x
            if desplx < 0:
                self.dir = 1
            self.nueva_img('tanqueleft.png')
        if self.dir == 3:
            self.rect.y -= self.var_y
            if desply < 0:
                self.dir = 4
            self.nueva_img('tanqueup.png')
        if self.dir == 4:
            self.rect.y += self.var_y
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

class Muro(pygame.sprite.Sprite):
    def __init__(self, archivo_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def load_image(self, archivo='mapa.txt'):
        infomapa = ConfigParser.ConfigParser()
        infomapa.read(archivo)
        archivo = infomapa.get('nivel', 'origen')
        c_x = int (infomapa.get('nivel', 'c_x'))
        c_y = int (infomapa.get('nivel', 'c_y'))
        mapa = infomapa.get('nivel', 'mapa').split("\n")
        j = 0
        x = 0
        y = 0
        for seccion in mapa:
            i = 0
            for objeto in seccion:
                x = 0 + (i * c_x)
                b = Muro('muro.jpg', [x,y])
                todos.add(b)
                muros.add(b)
                i += 1
            j += 0
            y = 0 + (j * c_y)

if __name__ == '__main__':
    # Inicializar pygame
    pygame.init()
    # Inicializar pantalla
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    # Creando grupos
    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    '''
    pantalla.blit(mat_imagenes[3][2], [0,0])
    pygame.display.flip()
    '''


    jp = Jugador('tanquedown.png')
    jp.muros = muros
    todos.add(jp)

    pygame.display.flip()
    fin = False
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
                    jp.dir = 3
                if event.key == pygame.K_DOWN:
                    jp.dir = 4

        # pantalla.fill(NEGRO)
        # todos.update()
        # todos.draw(pantalla)
        # pygame.display.flip()
        # reloj.tick(60)

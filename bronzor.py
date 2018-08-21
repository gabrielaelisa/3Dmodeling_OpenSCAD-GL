from initializers import *
from CC3501Utils import *

import os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import uniform


os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


class Bronzor:
    def __init__(self, pos):
        self.pos = pos
        self.angulo = 90

        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        glEnable(GL_COLOR_MATERIAL)

        glBegin(GL_TRIANGLES)

        # cuerpo exterior
        color = [0/250, 50/250, 250/250]  # azul
        glColor3f(color[0], color[1], color[2])
        cilindro(100, 15, Vector(0, 0, 0))

        #cuerpo interior
         # azul
        glColor3f(0, 0, 1)
        cilindro(80, 25, Vector(0, 0, -5))

        #esferas del cuerpo
        color = [0 / 250, 0 / 250, 250 / 250]  # azul
        glColor3f(color[0], color[1], color[2])
        esfera(23, Vector(0, 105, 6))
        esfera(23, Vector(0, -105, 6))
        esfera(23, Vector(-90, 60, 6))
        esfera(23, Vector(90, 60, 6))
        esfera(23, Vector(90, -60, 6))
        esfera(23, Vector(-90, -60, 6))

        #nariz
        color = [0 / 250, 50 / 250, 250 / 250]  # azul
        glColor3f(color[0], color[1], color[2])
        esfera(20, Vector(0, 0, 20))

        #cilindros del cuerpo
        color = [0 / 250, 50 / 250, 250 / 250]  # azul
        glColor3f(color[0], color[1], color[2])
        cilindro(8, 24, Vector(-25, 45, -2))  #superior izquierdo
        cilindro(8, 24, Vector( 25, 45, -2)) #superior derecho
        cilindro(8, 24, Vector(25, -45, -2))
        cilindro(8, 24, Vector(-25, -45, -2))

        #circunferencia interior
        glColor3f(0, 0, 0)#negro
        cilindro(55, 24, Vector(0, 0, -4))
        color = [0 / 250, 0 / 250, 250 / 250]  # azul
        glColor3f(color[0], color[1], color[2])
        cilindro(53, 24, Vector(0, 0, -4))

        #ojos
        glColor3f(1, 1, 1) #blanco
        for i in range(0,20):
            cilindro(8, 25, Vector(-50, -10+i, -2))
            cilindro(8, 25, Vector(50, -10 + i, -2))
        glColor3f(0, 0, 0)  #negro

        for i in range(0, 14):
            cilindro(5.5, 25, Vector(-50, -7.5 + i, -2))
            cilindro(5, 25, Vector(50, -7.5 + i, -2))


        glColor3f(0, 0, 1)
        cilindro(80, 23, Vector(0, 0, -5))
        #arbol
        glColor3f(0 / 250, 50 / 250, 250 / 250)
        for i in range(0, 37, 1):
            i = i - 0.5
            cilindro(0.1+i/2, 23, Vector(0, 0+ i, -8))

        #glTranslate(10,60,0)
        #glRotate(-125, 0, 0, 1)
        glScale(2,2,1)

        # ramas
        glColor3f(0 / 250, 50 / 250, 250 / 250)
        cuadrilatero(Vector(1, 0, -8), Vector(-1, 0, -8), Vector(-1, -25, -8), Vector(1, -25, -8))
        cuadrilatero(Vector(1, -1.5, -8), Vector(15, 0.5, -8), Vector(16, -0.5, -8), Vector(0, -3.5, -8))
        cuadrilatero(Vector(1, -16.5, -8), Vector(15, -14.5, -8), Vector(16, -15.5, -8), Vector(0, -18.5, -8))
        cuadrilatero(Vector(-1, -20.5, -8), Vector(-15, -18.5, -8), Vector(-16, -19.5, -8), Vector(-1, -22.5, -8))
        cuadrilatero(Vector(-1, -5.5, -8), Vector(-15, -3.5, -8), Vector(-16, -4.5, -8), Vector(-1, -7.5, -8))
        for i in range(0, 14, 1): #hojas
            i= i-0.5
            cilindro(max(5.5-i/2, 0.1), 23, Vector(-20 +i, 0 -i/2, -8))
            cilindro(max(5.5 - i / 2, 0.1), 23, Vector(-20 +i, -15 -i/2, -8))

        #glTranslate(10, -10, 0)
        #glRotate(255, 0, 0, 1)
        for i in range(0, 11, 1):
            cilindro(0.1+ i/2, 23, Vector(15 +i, 0 + i/2, -8))
            cilindro(0.1+ i/2, 23, Vector(15 +i, -15 + i/2, -8))

        glEnd()

        glEndList()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(-45, 0, 0, 1)  # Rotacion en torno a eje y
        glRotatef(self.angulo, 1, 0, 0)  # Rotacion en torno a eje x
        #glRotatef(self.angulo, 0, 0, 1)  # Rotacion en torno a eje y
        glCallList(self.lista)
        glPopMatrix()


def main():
    # inicializar
    ancho = 800
    alto = 600
    init(ancho, alto, "ejemplo aux")

    # crear objetos
    clock = pygame.time.Clock()

    # camara
    camPos = Vector(100, 100, 50)  # posicion de la camara
    camAt = Vector(10000, 10000, 0)  # posicion que se enfoca

    # luz
    light = GL_LIGHT0
    l_position = Vector(1000.0, 100.0, 500.0)

    # crear una luz coherente con su color base
    l_diffuse = [1.0, 1.0, 1.0, 1.0]
    l_ambient = [0.2, 0.2, 0.2, 1]
    l_specular = [1.0, 1.0, 1.0, 1.0]

    # otros valores estandar
    l_constant_attenuation = 1.5
    l_linear_attenuation = 0.5
    l_quadratic_attenuation = 0.2

    l_spot_cutoff = 60.0
    l_spot_direction = Vector(-1.0, -1.0, 0.0)  # direccion de rebote de luz
    l_spot_exponent = 2.0

    
    bronzor = []
    p = Bronzor(Vector(500, 500, 0))
    bronzor.append(p)

    # variables de tiempo
    fps = 30
    dt = 1.0 / fps

    run = True
    while run:
        # manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # obtener teclas presionadas
        pressed = pygame.key.get_pressed()

        if pressed[K_UP]:
            camPos = sumar(ponderar(10, normalizar(camAt)), camPos)
        if pressed[K_DOWN]:
            camPos = sumar(ponderar(-10, normalizar(camAt)), camPos)
        if pressed[K_RIGHT]:
            camPos = sumar(ponderar(-10, rotarFi(normalizar(camAt), 90)), camPos)
        if pressed[K_LEFT]:
            camPos = sumar(ponderar(10, rotarFi(normalizar(camAt), 90)), camPos)

        if pressed[K_w]:
            camAt = sumar(Vector(0, 0, 100), camAt)
        if pressed[K_s]:
            camAt = sumar(Vector(0, 0, -100), camAt)
        if pressed[K_d]:
            camAt = rotarFi(camAt, 0.01)
        if pressed[K_a]:
            camAt = rotarFi(camAt, -0.01)

        if pressed[K_r]:
            l_position = Vector(uniform(0, 1000), uniform(0, 1000), uniform(0, 1000))

        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # dibujar objetos
        #eje.dibujar()
        for a in bronzor:
            a.dibujar()

        # camara
        glLoadIdentity()
        gluLookAt(camPos.x, camPos.y, camPos.z,  # posicion
                  camAt.x, camAt.y, camAt.z,  # mirando hacia
                  0.0, 0.0, 1.0)  # inclinacion

        # luz
        glLightfv(light, GL_POSITION, l_position.cartesianas())
        glLightfv(light, GL_AMBIENT, l_ambient)
        glLightfv(light, GL_SPECULAR, l_specular)
        glLightfv(light, GL_DIFFUSE, l_diffuse)
        glLightf(light, GL_CONSTANT_ATTENUATION, l_constant_attenuation)
        glLightf(light, GL_LINEAR_ATTENUATION, l_linear_attenuation)
        glLightf(light, GL_QUADRATIC_ATTENUATION, l_quadratic_attenuation)
        glLightf(light, GL_SPOT_CUTOFF, l_spot_cutoff)
        glLightfv(light, GL_SPOT_DIRECTION, l_spot_direction.cartesianas())
        glLightf(light, GL_SPOT_EXPONENT, l_spot_exponent)

        glEnable(light)

        pygame.display.flip()  # cambiar imagen
        clock.tick(fps)  # esperar 1/fps segundos

    pygame.quit()
    return


main()

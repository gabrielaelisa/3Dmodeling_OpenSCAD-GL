# -*- coding: utf-8 -*-
from OpenGL.GL import *
from math import *

# ----------------------------- CLASE VECTOR ----------------------------------#


class Vector:
    """
    @ Vector: Define un objeto vector en 3D. Contiene los parametros [X,Y,Z] que
    permiten ubicarse en el espacio 3D. Provee metodos para transformar entre
    sistemas de coordenadas esfericas, cilindricas y cartesianas.
    
    @ Param: x, y, z - componentes del vector, enteros o reales.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def fi(self):
        return atan2(self.y, self.x)

    def theta(self):
        return acos(self.z / self.modulo())

    def rho(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def modulo(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def esfericas(self):
        return self.modulo(), self.fi(), self.theta()

    def cilindricas(self):
        return self.rho(), self.fi(), self.z

    def cartesianas(self):
        return self.x, self.y, self.z


# ------------------------------------------------------------------------------#


# ------------------- FUNCIONES PARA MANIPULAR VECTORES ------------------------#


def VectorEsfericas(r, fi, theta):
    """
    @ VectorEsfericas: Crea un nuevo objeto Vector dando sus coordenadas en esfericas
    @ Param: r, fi, theta - coordenadas en esfericas, enteros o reales.
    """
    return Vector(r * sin(theta) * cos(fi), r * sin(theta) * sin(fi), r * cos(theta))


def VectorCilindricas(r, fi, z):
    """
    @ VectorCilindricas: Crea un nuevo objeto Vector dando sus coordenadas cilindricas.
    @ Param: r, fi, z - coordenadas en cilindricas, enteros o reales.
    """
    return Vector(r * cos(fi), r * sin(fi), z)


def sumar(r2, r1):
    return Vector(r2.x + r1.x, r2.y + r1.y, r2.z + r1.z)


def restar(r2, r1):
    return Vector(r2.x - r1.x, r2.y - r1.y, r2.z - r1.z)


def multiplicar(r2, r1):
    return Vector(r2.x * r1.x, r2.y * r1.y, r2.z * r1.z)


def ponderar(a, r):
    return Vector(a * r.x, a * r.y, a * r.z)


def normalizar(r):
    m = r.modulo()
    if m > 0:
        return Vector(r.x / m, r.y / m, r.z / m)  # BUG SOLVED
    else:
        return r


def desplazarRadialmente(r, d):
    return VectorEsfericas(r.modulo() + d, r.fi(), r.theta())


def rotarFi(r, a):
    a2 = r.fi() + a
    if a2 >= 2 * pi:
        a2 -= 2 * pi
    if a2 < 0:
        a2 += 2 * pi
    return VectorCilindricas(r.rho(), a2, r.z)


def rotarTheta(r, a):
    a2 = r.theta() + a
    if a2 >= pi:
        a2 -= 2 * pi
    if a2 < -pi:
        a2 += 2 * pi
    return VectorEsfericas(r.modulo(), r.fi(), a2)


def distancia(r1, r2):
    return restar(r1, r2).modulo()


def punto(r1, r2):
    return r1.x * r2.x + r1.y * r2.y + r1.z * r2.z


def cruz(r1, r2):
    return Vector(r1.y * r2.z - r1.z * r2.y, r1.z * r2.x - r1.x * r2.z, r1.x * r2.y - r1.y * r2.x)


def normal(p1, p2, p3):
    """
    @ Normal: retorna un objeto Vector que es la normal de un triangulo definido por
    tres vectores segun la regla de la mano derecha.
    @ Param: p1, p2, p3 - Objetos de la clase Vector
    """
    n = cruz(restar(p2, p1), restar(p3, p1))
    m = n.modulo()
    if m != 0:
        return ponderar(1.0 / m, n)
    else:
        return n


def promediar(lv):
    n = len(lv)
    r = Vector(0.0, 0.0, 0.0)

    for v in lv:
        r = sumar(r, v)
    r = ponderar(1.0 / n, r)

    return r


# ------------------------------------------------------------------------------#


# ------------------ FUNCIONES PARA DIBUJAR PRIMITIVAS -------------------------#
def triangulo(p1, p2, p3):
    """
    @ triangulo: Genera los vertices para un triangulo.
    @ Param: p1, p2, p3 - Objetos de la clase Vector
    """

    glNormal3fv(normal(p1, p2, p3).cartesianas())
    glVertex3fv(p1.cartesianas())
    glVertex3fv(p2.cartesianas())
    glVertex3fv(p3.cartesianas())


def cuadrilatero(p1, p2, p3, p4):
    """
    @ cuadrilatero: Genera los vertices para un cuadrilatero.
    @ Param: p1, p2, p3, p4: Objetos de la clase Vector
    """
    triangulo(p1, p3, p4)
    triangulo(p1, p2, p3)
    return


def cono(radio, altura, pos=Vector(0, 0, 0)):
    """
    @ cono: Genera los vertices para un cono con base centrada en pos.
    """
    # delta angular, presicion
    dang = 2 * pi / 10

    p0 = sumar(Vector(0, 0, 0), pos)  # centro base
    p1 = sumar(Vector(0, 0, altura), pos)  # punta
    p2 = sumar(VectorCilindricas(radio, 0, 0), pos)  # punto inicial base

    ang = 0
    while ang <= 2 * pi:
        p3 = sumar(VectorCilindricas(radio, ang + dang, 0), pos)  # siguiente punto en la iteracion

        # dibujar seccion del cono
        triangulo(p0, p3, p2)
        triangulo(p1, p2, p3)

        # continuar iterando
        p2 = p3
        ang += dang
    return


def cilindro(radio, altura, pos=Vector(0, 0, 0)):
    """
    @ cilindro: Genera los vertices para un cilindro con base centrada en pos.
    """
    # delta angular, precision
    dang = 2 * pi / 10

    p1 = sumar(Vector(0, 0, 0), pos)  # centro base
    p2 = sumar(VectorCilindricas(radio, 0, 0), pos)  # punto inicial base
    p4 = sumar(Vector(0, 0, altura), pos)  # centro tapa
    p5 = sumar(VectorCilindricas(radio, 0, altura), pos)  # punto inicial tapa

    theta = 0
    while theta <= 2 * pi:
        p3 = sumar(VectorCilindricas(radio, theta + dang, 0), pos)  # siguiente punto en la iteracion
        p6 = sumar(VectorCilindricas(radio, theta + dang, altura), pos)

        # dibujar seccion del cilindro
        triangulo(p2, p1, p3)  # base
        triangulo(p4, p5, p6)  # tapa
        cuadrilatero(p3, p2, p5, p6)  # manto

        # continuar iterando
        p2 = p3
        p5 = p6
        theta += dang
    return


def esfera(radio, pos=Vector(0, 0, 0)):
    """
    @ esfera: Genera los vertices para una esfera centrada en pos.
    """
    dtheta = 2 * pi / 20.0  # definicion
    dfi = 2 * pi / 20.0
    theta = 0  # angulo que cae
    fi = 0  # angulo polar

    while theta <= pi - dtheta:
        while fi <= 2 * pi - dfi:
            p1 = sumar(VectorEsfericas(radio, fi, theta), pos)
            p2 = sumar(VectorEsfericas(radio, fi + dfi, theta), pos)
            p3 = sumar(VectorEsfericas(radio, fi + dfi, theta + dtheta), pos)
            p4 = sumar(VectorEsfericas(radio, fi, theta + dtheta), pos)
            cuadrilatero(p1, p4, p3, p2)
            fi += dfi

        fi = 0  # reinicia el angulo
        theta += dtheta
    return

class Paralelepipedo:
    # Crea un paralelepipedo centrado en 0 con las dimensiones especificadas
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

        self.pos = Vector(0, 0, 0)
        self.angulo = 0

        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)



        # poliedro definido desde el vertice superior izquierdo en sentido antihorario
        # p1-p4 cara superior
        # p5-p8 cara inferior
        p1 = Vector(-self.largo / 2.0, -self.ancho / 2.0, self.alto / 2.0)
        p2 = Vector(-self.largo / 2.0, self.ancho / 2.0, self.alto / 2.0)
        p3 = Vector(self.largo / 2.0, self.ancho / 2.0, self.alto / 2.0)
        p4 = Vector(self.largo / 2.0, -self.ancho / 2.0, self.alto / 2.0)
        p5 = Vector(-self.largo / 2.0, -self.ancho / 2.0, -self.alto / 2.0)
        p6 = Vector(-self.largo / 2.0, self.ancho / 2.0, -self.alto / 2.0)
        p7 = Vector(self.largo / 2.0, self.ancho / 2.0, -self.alto / 2.0)
        p8 = Vector(self.largo / 2.0, -self.ancho / 2.0, -self.alto / 2.0)

        glBegin(GL_TRIANGLES)
        color = [28, 195, 204]  # cafe
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]

        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])  # amarillo
        cuadrilatero(p1, p4, p3, p2)
        cuadrilatero(p5, p6, p7, p8)
        cuadrilatero(p1, p2, p6, p5)
        cuadrilatero(p2, p3, p7, p6)
        cuadrilatero(p3, p4, p8, p7)
        cuadrilatero(p4, p1, p5, p8)

        glEnd()
        glEndList()

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.angulo, 0, 0, 1)  # Rotacion en torno a eje Z
        glCallList(self.lista)
        glPopMatrix()

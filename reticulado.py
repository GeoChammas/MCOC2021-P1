import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    __NNodosInit__ = 100
    def __init__(self):
        super(Reticulado, self).__init__()
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}

    def agregar_nodo(self, x, y, z=0):
        self.xyz.resize((self.Nnodos+1, 3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos += 1
        return()

    def agregar_barra(self, barra):
        self.barras.append(barra)
        return()

    def obtener_coordenada_nodal(self, n):
        posicion = n
        coordenadas = self.xyz[n]
        return(coordenadas)

    def calcular_peso_total(self):
        lista_barras = self.barras
        peso_total = 0
        for barra in lista_barras:
            peso_total += barra.calcular_peso(self)
        return(peso_total)

    def obtener_nodos(self):
        xy = self.xyz
        return(xy)

    def obtener_barras(self):
        lista_barras = self.barras
        return(lista_barras)

    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        #Falta implementar	
        return(0)

    def agregar_fuerza(self, nodo, gdl, valor):
        #Falta implementar	
        return(0)

    def ensamblar_sistema(self):
        #Falta implementar	
        return(0)

    def resolver_sistema(self):
        #Falta implementar	
        return(0)

    def obtener_desplazamiento_nodal(self, n):
        #Falta implementar	
        return(0)

    def obtener_fuerzas(self):
        #Falta implementar	
        return(0)

    def obtener_factores_de_utilizacion(self, f):
        #Falta implementar	
        return(0)

    def rediseñar(self, Fu, ϕ=0.9):
        #Falta implementar	
        return(0)

    def chequear_diseño(self, Fu, ϕ=0.9):
        #Falta implementar	
        return(0)

    def __str__(self):
     
        return "Soy un reticulado :)"

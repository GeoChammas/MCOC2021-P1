import numpy as np
from constantes import g_, ρ_acero, E_acero
from numpy import pi


class Barra(object):
    def __init__(self, ni, nj, seccion):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        

    def obtener_conectividad(self):
        return([self.ni, self.nj])
    
    def calcular_area(self):
        return self.seccion.area()
    
    def calcular_largo(self, reticulado):
        n_i = reticulado.obtener_coordenada_nodal(self.ni)
        n_j = reticulado.obtener_coordenada_nodal(self.nj)
        x, y, z = abs(n_i[0] - n_j[0]), abs(n_i[1] - n_j[1]), abs(n_i[2] - n_j[2])
        L = (x**2 + y**2)**(0.5)
        return(L)

    def calcular_peso(self, reticulado):
        area = self.calcular_area()
        largo = self.calcular_largo(reticulado)
        peso = (area*largo)*ρ_acero*g_
        return(peso)

    def obtener_rigidez(self, ret):
        #Falta implementar  
        return(0)

    def obtener_vector_de_cargas(self, ret):
        #Falta implementar  
        return(0)

    def obtener_fuerza(self, ret):
        #Falta implementar  
        return(0)

    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        #Falta implementar  
        return(0)

    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        #Falta implementar  
        return(0)

    def rediseñar(self, Fu, ret, ϕ=0.9):
        #Falta implementar  
        return(0)
    #hola
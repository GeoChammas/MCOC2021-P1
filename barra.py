import numpy as np
from constantes import g_, ρ_acero, E_acero

class Barra(object):
    def __init__(self, ni, nj, seccion, color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color = color

    def obtener_conectividad(self):
        return([self.ni, self.nj])
    
    def calcular_area(self):
        return (self.seccion.area())
    
    def calcular_largo(self, ret):
        n_i = ret.obtener_coordenada_nodal(self.ni)
        n_j = ret.obtener_coordenada_nodal(self.nj)
        x, y, z = abs(n_i[0] - n_j[0]), abs(n_i[1] - n_j[1]), abs(n_i[2] - n_j[2])
        L = (x**2 + y**2 + z**2)**(0.5)
        return(L)

    def calcular_peso(self, ret):
        area = self.calcular_area()
        largo = self.calcular_largo(ret)
        return((area*largo)*ρ_acero*g_)

    def obtener_rigidez(self, ret):
        area = self.calcular_area()
        largo = self.calcular_largo(ret)
        n_i = ret.obtener_coordenada_nodal(self.ni)
        n_j = ret.obtener_coordenada_nodal(self.nj)
        cos_x = (n_j[0]-n_i[0])/largo
        cos_y = (n_j[1]-n_i[1])/largo
        cos_z = (n_j[2]-n_i[2])/largo
        if ret.Ndimensiones == 2:
            TO = np.array([-cos_x, -cos_y, cos_x, cos_y], dtype=np.double).reshape((4,1))
        else:
            TO = np.array([-cos_x, -cos_y, -cos_z, cos_x, cos_y, cos_z], dtype=np.double).reshape((6,1))
        return(area*E_acero/largo*(TO@TO.T))

    def obtener_vector_de_cargas(self, ret):
        weight = self.calcular_peso(ret)
        return(np.array(ret.fpp)*weight/2)

    def obtener_fuerza(self, ret):
        ue = np.zeros(2*ret.Ndimensiones)
        ue[0:ret.Ndimensiones] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[ret.Ndimensiones:] = ret.obtener_desplazamiento_nodal(self.nj)
        area = self.calcular_area()
        largo = self.calcular_largo(ret)
        n_i = ret.obtener_coordenada_nodal(self.ni)
        n_j = ret.obtener_coordenada_nodal(self.nj)
        cos_x = (n_j[0]-n_i[0])/largo
        cos_y = (n_j[1]-n_i[1])/largo
        cos_z = (n_j[2]-n_i[2])/largo
        if ret.Ndimensiones == 2:
            TO = np.array([-cos_x, -cos_y, cos_x, cos_y], dtype=np.double).reshape((4,1))
        else:
            TO = np.array([-cos_x, -cos_y, -cos_z, cos_x, cos_y, cos_z], dtype=np.double).reshape((6,1))
        return(area*E_acero/largo*(TO.T@ue))

    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        #Falta implementar  
        return(0)

    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        #Falta implementar  
        return(0)

    def rediseñar(self, Fu, ret, ϕ=0.9):
        #Falta implementar  
        return(0)
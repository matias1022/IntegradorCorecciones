import csv

from claseIntegranteProyecto import IntegranteProyecto

from claseProyecto import Proyecto

class ManejadorIntegrantesProyecto:
    listaIntegrantes=[]
    def __init__(self):
        self.__listaIntegrantes = []

    def addIntegrantes(self,proyect):
        if type (proyect)==IntegranteProyecto:
           self.__listaIntegrantes.append(proyect)

    def cargarIntegrantes(self):
         archivo= open ("integrantesProyecto.csv")
         leer= csv.reader(archivo,delimiter=';')
         band = True
         for fila in leer:
             if band:
                " Saltear Cabecera"
                band = False
             else:
                 idProyecto= fila[0]
                 apellidoNombre=fila[1]
                 dni=fila[2]
                 categoriaInvestigacion=fila[3]
                 rol=fila[4]
                 integrante= IntegranteProyecto(idProyecto,apellidoNombre, dni, categoriaInvestigacion,rol)
                 self.addIntegrantes(integrante)
         archivo.close()
    def contar (self,IDProyecto):
        return self.__listaIntegrantes.count(IDProyecto)

        

    def obtenerDirector(self,idProyecto):  
        band=False
        i=0
        categoria=0
        while not band and i<len(self.__listaIntegrantes):
            if self.__listaIntegrantes[i].obtenerID()==idProyecto and self.__listaIntegrantes[i].obtenerRol()=='director' and self.__listaIntegrantes[i].obtenerCategoria() in ('I','II'):
                    band=True
                    categoria=self.__listaIntegrantes[i].obtenerCategoria()
            else:
                i=i+1
        return categoria
    def obtenerCodirector(self,idProyecto):
        band=False
        i=0
        categoria=0
        while not band and i<len(self.__listaIntegrantes):
            if self.__listaIntegrantes[i].obtenerID()==idProyecto and self.__listaIntegrantes[i].obtenerRol()=='codirector' and self.__listaIntegrantes[i].obtenerCategoria() in ('I','II','III'):
                        band=True
                        categoria=self.__listaIntegrantes[i].obtenerCategoria()
            else:
                i=i+1
        return categoria



    def contarDirector(self,idProyecto):
        integrante=IntegranteProyecto()
        band= True
        for integrante in self.__listaIntegrantes:
            if integrante.obtenerID()==idProyecto:
                if integrante.obtenerRol()=="director":
                                band=False
        return band
    def contarCodirector(self,idProyecto):
        integrante=IntegranteProyecto()
        band= False 
        for integrante in self.__listaIntegrantes:
            if integrante.obtenerID()==idProyecto:
                if integrante.obtenerRol()=="codirector":
                                band=True
        return band
    
 
   
    def mostrar(self):
             print  (self.__listaIntegrantes[0],self.__listaIntegrantes[1],self.__listaIntegrantes[2],self.__listaIntegrantes[3],self.__listaIntegrantes[4])

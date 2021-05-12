import csv, os
from claseProyecto import Proyecto

class ManejadorProyecto: 
    __listaProyecto=[]   
    def __init__(self):
        self.__listaProyecto = []
    def addProyecto(self,proyect):

        self.__listaProyecto.append(proyect)

    def cargarProyecto(self):

         archivo= open ("proyectos.csv")
         leer= csv.reader(archivo,delimiter=';')
         band = True
         for fila in leer:
             if band:
                ''' Saltear Cabecera'''
                band = False
             else:
               idProyecto= fila[0]
               titulo=fila[1]
               palabrasClave=fila[2]
               proyecto= Proyecto(idProyecto,titulo,palabrasClave)
               self.addProyecto(proyecto)
               
         archivo.close()
    def calcularPuntaje(self,listaInt):

         for ID in self.__listaProyecto:
             puntaje=0
             print ("El ID del Proyecto es:",ID)
             #A
             cantidad_Integrantes=listaInt.contar(ID)

             if cantidad_Integrantes<3:
                 puntaje=puntaje-20
                 print ("Un Proyecto debe tener como minimo 3 integrantes")
             else: puntaje=puntaje+10
             print(puntaje)
             #B
             categDirector=listaInt.obtenerDirector(ID)
             if categDirector =="I" or categDirector =="II" or categDirector =="III":
                  puntaje=puntaje+10
             else:  
                puntaje=puntaje-5
                print("El Director del Proyecto debe tener categoría I o II ")
             
             print(puntaje)
             #C
             categCoDirector=listaInt.obtenerCodirector(ID)
             print(categCoDirector)
       #      if listaInt.obtenerCodirector(ID)==True:
             if categCoDirector =="I" or categCoDirector =="II" or categCoDirector =="III":
                 puntaje=puntaje+10
             else: 
                puntaje=puntaje-5
                print ("El Codirector del Proyecto debe tener como mínimo categoría III")
             print(puntaje)
             #D
     
             if categDirector==0:         
                 print("El Proyecto debe tener un Director")
             #E
        
             if categCoDirector==0:
               
                 print("El Proyecto debe tener un Codirector")
             #F
             if categCoDirector==0 or categDirector==0:
                 puntaje=puntaje-10
             print("El Proyecto tuvo un puntaje de: ",puntaje)
             print ("----------------------------------")  
             unProyecto = Proyecto()
      
             for unProyecto in self.__listaProyecto:
                if unProyecto.obtenerID() == ID:
                    unProyecto.ponerPuntaje(puntaje)
         print('Proyectos ordenados por Puntaje de Mayor a Menor:\n')
         otroProyecto = Proyecto()
         self.__listaProyecto.sort(reverse=True)
         for otroProyecto in self.__listaProyecto:
                  otroProyecto.mostrar()

    def obtenerListaID(self):
        listaIDP=[]
        unProyecto = Proyecto()
        for unProyecto in self.__listaProyecto:
            listaIDP.append(unProyecto.obtenerID())
        return listaIDP

    def obtenerListaProyectos(self):
        return self.__listaProyecto


    def mostrarDatos(self):
             print  (self.__listaProyecto[0],self.__listaProyecto[1],self.__listaProyecto[2])
   
    def __str__(self):
        a=""
        unProyecto=Proyecto()
        for unProyecto in self.__listaProyecto:
            a= a+unProyecto.__str__() + '\n'
        return a

"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print()
    print()
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar artistas cronologicamente") # R1
    print("3- Consultar adquisiciones cronologicamente") # R2
    print("4- Clasificacion de obras por tecnicas de un artista") # R3
    print("5- Clasificacion de obras por nacionalidad de sus creadores") # R4
    print("6- Costo de transportar un departamento") # R5
    print("7- Proponer nueva exposicion en el museo") # R6
    print("0- Salir")

def printEspacio():
    """
    añade espacios entre funciones 
    """

    print("")
    print("=" * 50)
    print("")


def initCatalog(datatype):
    """
    Inicializa el catalogo de obras
    """
    return controller.initCatalog(datatype)


def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def printArtistasCrono(lista):
    """
    imprime el numero de artistas en un rango de años
    """
    cantidad = lt.size(lista)
    print("Hay " + str(cantidad) + " artistas en el rago seleccioando")
    print()
    print("Top 3 mas viejos: ")
    for x in range(3):
        elemento = lt.getElement(lista, x)
        print(str(x+1) + ") el artista: " + elemento["nombre"] + " nacido en: " + str(elemento["edad"]) + " de nacionalidad: " + elemento["nacionalidad"] + " y de genero: " +  elemento["genero"])

    print()
    print("Top 3 mas viejos: ")
    for x in range(3):
        elemento = lt.getElement(lista, cantidad - x)
        print(str(x+1) + ") el artista: " + elemento["nombre"] + " nacido en: " + str(elemento["edad"]) + " de nacionalidad: " + elemento["nacionalidad"] + " y de genero: " +  elemento["genero"])



def printObrasCronoacq(lista):
    """
    imprime la cantidad de obras adquiridas en un rango de años
    """
    cantidad = lt.size(lista)
    printEspacio()
    print("Hay " + str(cantidad) + " obras adquiridas en el rago seleccioando")
    print()
    print("Top 3 mas jovenes: ")
    for x in range(3):
        elemento = lt.getElement(lista, x)
        print(str(x+1) + ") la obra: " + elemento["name"] + " adquirida en : " + str(elemento["dateacquired"]) + " con medio: " + elemento["medium"] + " y de dimensiones: " +  elemento["dimensions"] +' creada por: ' + str(elemento['artistname']))
        

    print()
    print("Top 3 mas viejos: ")
    for x in range(3):
        elemento = lt.getElement(lista, cantidad-x)
        print(str(x+1) + ") la obra: " + elemento["name"] + " adquirida en : " + str(elemento["dateacquired"]) + " con medio: " + elemento["medium"] + " y de dimensiones: " +  elemento["dimensions"]+ 'creada por: ' + str(elemento['artistname']))




def print3LastElements(Elements,prop):
    '''

    Imprime el nombre de los tres últimos elementos de una lista
    Prop es el atributo del artista u obra (nombre,fecha,técnica,etc)

    '''
    print('1: '+ str(lt.getElement(Elements, 0)[prop]))
    print('2: '+ str(lt.getElement(Elements, 1)[prop]))
    print('3: '+ str(lt.getElement(Elements, 2)[prop]))



def printObrasPorTecnica(TotalObras,TotalTecnicas,TecnicaMasUsada,ObrasArtistaTecnica,nombre): 
    printEspacio()
    if TecnicaMasUsada=='': 
        TecnicaMasUsada='No hay suficiente información '

    if TotalTecnicas==-1:
        TotalTecnicas=0

        
    print('El artista  ' + str(nombre) + ' Tiene un total de  ' + str(TotalObras) + ' obras  y un total de ' + str(TotalTecnicas) + ' distintas   técnicas utilizadas \n \n')
    print('La técnica más utilizada por '+ str(nombre) + ' es: ' + str(TecnicaMasUsada))
    print()

    print('Obras con la técnica más utilizada: ')
    for i in range(lt.size(ObrasArtistaTecnica)): 
        elemento=lt.getElement(ObrasArtistaTecnica,i)
        print(str(i+1) + ')' + ' La obra: ' + str(elemento['name']) + '  con fecha : '  + str(elemento['date']) + '   dimensiones : ' + str(elemento['dimensions']) + 'y técnica : ' + str(elemento['medium']))
    printEspacio()

def Print_nacionalidad_obras(lista):
    printEspacio()

    print("Top 10 de nacionalidades con mas artistas")

    for x in range(1, 11):
        elemento = lt.getElement(lista, x)
        print(elemento["lugar"] + " con " + str(elemento["cantidad"]) + " artistas")

    
    print()

    print("De la nacionalidad con mas artistas el top 3 primeros y ultimos")

    print()

    for x in range(5):
        elemento = lt.getElement(lista, 1)
        obra = lt.getElement(elemento["obras"], x)  
        print("La obra de titulo " + obra["titulo"] + " De artstas " + obra["artistas"] + " Hecha en " + str(obra["fecha"]) + " Con el medio " + obra["medio"] + "Con dimensiones" + obra["dimenciones"])

    print()

    cantidad = lt.size(lt.getElement(lista, 1)["obras"])

    for x in range(5):
        elemento = lt.getElement(lista, 1)
        obra = lt.getElement(elemento["obras"], cantidad - x)  
        print("La obra de titulo " + obra["titulo"] + " De artstas " + obra["artistas"] + " Hecha en " + str(obra["fecha"]) + " Con el medio " + obra["medio"] + "Con dimensiones" + obra["dimenciones"])

    printEspacio()

def printObrasTransporte(TotalObras, TotalPrecio, TotalPeso,TransportePorCosto, TransportePorFecha): 
    printEspacio()
    print('Hay un total de : ' + str(TotalObras) + ' obras por transportarse, con un precio total de transporte de: ' + str(TotalPrecio) + ' USD, por un peso de: ' + str(TotalPeso) + 'kg')
    print( )
    print('Las 5 obras más costosas por transportar son: ')
    print()
    for i in range(5):
        elemento=lt.getElement(TransportePorCosto,i)
        print(str(i+1) + ')' + ' La obra: ' + str(elemento['name']) + '  con fecha : '  + str(elemento['date']) + '   dimensiones : ' + str(elemento['dimensions']) + ', técnica : ' + str(elemento['medium'])+'y costo de transporte aprox: ' + str(round(elemento['cost']))+' USD')

    print()
    print()

    print('Las 5 obras más antiguas para transportarse son: ')
    print()
    for i in range(5):
        elemento=lt.getElement(TransportePorFecha,i)
        print(str(i+1) + ')' + ' La obra: ' + str(elemento['name']) + '  con fecha : '  + str(elemento['date']) + '   dimensiones : ' + str(elemento['dimensions']) + ', técnica : ' + str(elemento['medium'])+'y costo de transporte aprox: ' + str(round(elemento['cost']))+' USD')
    print()
    print()


def printObrasNuevaEX(lista):

    printEspacio()

    print("se llena el espacio con " + str(lt.size(lista) -1) + " obras y " + str(lt.getElement(lista, 0)) + " espcio") 
    
    print()
    print("primeras 5:")

    for x in range(2 ,7):
        obra = lt.getElement(lista, x)
        print("La obra de titulo " + str(obra["titulo"]) + " hecha por " + obra["nombre"] + " Hecha en " + str(obra["fecha"]) + " Con el medio " + obra["medio"] + " Con dimensiones " + str(obra["dimensiones"]))

    print()
    print("ultimas 5:")

    for x in range(lt.size(lista) - 5 ,lt.size(lista)):
        obra = lt.getElement(lista, x)
        print("La obra de titulo " + str(obra["titulo"]) + " hecha por " + obra["nombre"] + " Hecha en " + str(obra["fecha"]) + " Con el medio " + obra["medio"] + " Con dimensiones " + str(obra["dimensiones"]))
    

    

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        datatype=input('Seleccione el tipo de tipo de estructura para los datos (ARRAY_LIST, LINKED_LIST)')

        printEspacio()
        print("Cargando información de los archivos ....")
        catalog=initCatalog(datatype)
        loadData(catalog)

        print('Obras de arte cargadas ' + str(lt.size(catalog['artworks'])))
        print('Artistas cargados ' + str(lt.size(catalog['artists'])))
        
        print('Úlitmas 3 obras cargadas: ')
        print3LastElements(controller.get3LastElements(catalog['artworks']),'name')
        print('Últimos 3 artistas cargados: ')
        print3LastElements(controller.get3LastElements(catalog['artists']),'name')
        printEspacio()
        
        
        

    elif int(inputs[0]) == 2:

        printEspacio()
        Año_inicial = int(input("Desde que año quieres buscar?:  "))
        Año_fin = int(input("Hasta que año quieres buscar?:  "))
        

        cantidadArtistas = controller.artistasCronologico(catalog, Año_inicial, Año_fin)
        printArtistasCrono(cantidadArtistas)
        printEspacio()
        
        

    elif int(inputs[0]) == 3:
        FechaInicial = input("desde que fecha quieres buscar?(AAAA-MM-DD):   ")
        FechaFin = input("hasta que fecha quieres buscar?(AAAA-MM-DD):   ")
        printEspacio()

        CantidadObras=controller.obrasCronologicoacq(catalog,FechaInicial,FechaFin)
        printObrasCronoacq(CantidadObras)
        printEspacio()




    elif int(inputs[0]) == 4:
        nombre = input("de que artista deseas buscar?: ")
        TotalObras,TotalTecincas,TecnicaMasUsada,ObrasArtistaTecnica=controller.ObrasArtista(catalog,nombre)
        printObrasPorTecnica(TotalObras,TotalTecincas,TecnicaMasUsada,ObrasArtistaTecnica,nombre)


    elif int(inputs[0]) == 5:
        print("Cargando...")
        Nacionalidad_obras = controller.Nacionalidad_obras(catalog)
        Print_nacionalidad_obras(Nacionalidad_obras)


    elif int(inputs[0]) == 6:
        depa = input("Que departamento deseas transportar?: ")
        TotalObras, TotalPrecio,TotalPeso, TransportePorCosto, TransportePorFecha=controller.Transporte(catalog,depa)
        printObrasTransporte(TotalObras, TotalPrecio,TotalPeso,TransportePorCosto, TransportePorFecha)
        

    elif int(inputs[0]) == 7:
        Año_inicial = input("desde que año inician las obras?: ")
        Año_fin = input("hasta que año van las obras?: ")
        espacio = input("Cual es el area disponible?: ")
        obrasNuevaEx = controller.ObrasNuevaEx(catalog, Año_inicial, Año_fin, espacio)
        printObrasNuevaEX(obrasNuevaEx)


    else:
        sys.exit(0)
sys.exit(0)

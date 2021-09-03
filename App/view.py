﻿"""
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


def initCatalog():
    """
    Inicializa el catalogo de obras
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def printArtistasCrono(numero):
    """
    imprime el numero de artistas en un rango de años
    """
    print("EL numero de artistas en este rango es: " + str(numero))



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        printEspacio()
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData(catalog)

        print('Obras de arte cargadas ' + str(lt.size(catalog['artworks'])))
        print('Artistas cargados ' + str(lt.size(catalog['artists'])))
        
        print('úlitmas 3 obras cargadas: ')
        controller.get3LastElements(catalog['artworks'])
        print('últimos 3 artistas cargados: ')
        controller.get3LastElements(catalog['artists'])
        printEspacio()
        
        
        

    elif int(inputs[0]) == 2:

        printEspacio()
        Año_inicial = int(input("desde que año quieres buscar?: "))
        Año_fin = int(input("hasta que año quieres buscar?: "))

        cantidadArtistas = controller.artistasCronologico(catalog, Año_inicial, Año_fin)
        printArtistasCrono(cantidadArtistas)
        printEspacio()
        
        

    elif int(inputs[0]) == 3:
        fecha_inicial = input("desde que fecha quieres buscar?(AAAA-MM-DD): ")
        fecha_fin = input("hasta que fecha quieres buscar?(AAAA-MM-DD): ")

    elif int(inputs[0]) == 4:
        nombre = input("de que artista deseas buscar?: ")

    elif int(inputs[0]) == 5:
        print("Cargando...")

    elif int(inputs[0]) == 6:
        depa = input("Que departamento deseas transportar?: ")

    elif int(inputs[0]) == 7:
        Año_inicial = input("desde que año inician las obras?: ")
        Año_fin = input("hasta que año van las obras?: ")

    else:
        sys.exit(0)
sys.exit(0)

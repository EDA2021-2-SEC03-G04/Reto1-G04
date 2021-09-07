"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(): 
    """
    Inicializa el catálogo de obras de arte. Crea una lista vacia para guardar
    todas las obras, adicionalmente, crea una lista vacia para los artistas.Retorna el catalogo inicializado.
    """
    catalog={'artworks': None, 'artists': None}

    catalog['artworks']=lt.newList()
    catalog['artists']=lt.newList('ARRAY_LIST', cmpfunction=compareartists)

    return catalog



# Funciones para agregar informacion al catalogo


def addArtwork(catalog,artwork): 
    #Se adiciona la obra  a la lista de obras
    new=newArtwork(artwork['Title'],artwork['DateAcquired'])
    lt.addLast(catalog['artworks'],new)
    


def addArtist(catalog,artist): 
    #Se adiciona el artista  a la lista de artistas
    new=newArtist(artist['DisplayName'],artist['BeginDate'],artist['EndDate'])

    lt.addLast(catalog['artists'],new)
   





# Funciones para creacion de datos

def newArtwork(name,dateacquired):
    '''
    Crea un nuevo objeto de obra de arte con atributos de nombre, fecha de adquisición 
    '''

    #Separamos la string de la fecha de adquisición con '-' y lo convertimos a foramto datetime
    #Si la entrada es vacia entonces se pone feha 1-1-1
    if dateacquired:
        datelst=dateacquired.split('-')
        dateacquired2=datetime.date(int(datelst[0]),int(datelst[1]),int(datelst[2]))
    else:
        dateacquired2=datetime.date(1,1,1)
    



    artwork={'name':'','dateacquired':''}
    artwork['name']=name
    artwork['dateacquired']=dateacquired2
    return artwork

def newArtist(name,begindate,enddate):
    '''
    Crea un nuevo objeto de obra de artista con atributos de nombre,fecha de inicio, fecha final
    '''
    artist={'name':'','begindate':'','enddate':''}
    artist['name']=name
    artist['begindate']=begindate
    artist['enddate']=enddate
    

    return artist

# Funciones de consulta

def get3LastElements(lista):

    """
    Retorna los 3 últimos elementos de una lista
    """

    pos=lt.size(lista)-2
    return lt.subList(lista, pos, 3)
        


def artistasCronologico(lista, inicio, final):

    artistas = lista["artists"]
    cont = 0

    joven1 = [9999, ""] # edad, nombre
    joven2 = [9999, ""]
    joven3 = [9999, ""]

    mayor1 = [0, ""]
    mayor2 = [0, ""]
    mayor3 = [0, ""]


    for x in range(lt.size(artistas)):

        grupo = lt.getElement(artistas, x)
        edad = int(grupo["begindate"])
        nombre = grupo["name"]

        if edad != 0 and edad >= inicio and edad <= final:
            cont += 1

            # comparacion joven

            if edad < joven3[0]:
                if edad < joven2[0]:
                    if edad < joven1[0]:
                        cambio1 = joven1[0] #cambio de top
                        cambio2 = joven2[0]
                        cambio1Nom = joven1[1]
                        cambio2Nom = joven2[1]

                        joven1[0] = edad
                        joven1[1] = nombre

                        joven2[0] = cambio1
                        joven2[1] = cambio1Nom

                        joven3[0] = cambio2
                        joven3[1] = cambio2Nom
                    else:
                        cambio = joven2[0] #cambio entre 2 y 3
                        cambioNom = joven2[1]

                        joven2[0] = edad
                        joven2[1] = nombre
                        joven3[0] = cambio 
                        joven3[1] = cambioNom
                else:
                    joven3[0] = edad
                    joven3[1] = nombre 
            
            # comparacion mayores

            if edad > mayor3[0]:
                if edad > mayor2[0]:
                    if edad > mayor1[0]:
                        cambio1 = mayor1[0] #cambio de top
                        cambio2 = mayor2[0]
                        cambio1Nom = mayor1[1]
                        cambio2Nom = mayor2[1]

                        mayor1[0] = edad
                        mayor1[1] = nombre

                        mayor2[0] = cambio1
                        mayor2[1] = cambio1Nom

                        mayor3[0] = cambio2
                        mayor3[1] = cambio2Nom
                    else:
                        cambio = mayor2[0] #cambio entre 2 y 3
                        cambioNom = mayor2[1]

                        mayor2[0] = edad
                        mayor2[1] = nombre
                        mayor3[0] = cambio 
                        mayor3[1] = cambioNom
                else:
                    mayor3[0] = edad
                    mayor3[1] = nombre 

        
    return [cont, joven1, joven2, joven3, mayor1, mayor2, mayor3]


# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistname1,artist):
    '''
    Crea una función de comparación para el TAD lista de artista
    '''
    if (artistname1.lower() in artist['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento



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
    new=newArtwork(artwork['Title'])
    lt.addLast(catalog['artworks'],new)
    


def addArtist(catalog,artist): 
    #Se adiciona el artista  a la lista de artistas
    new=newArtist(artist['DisplayName'],artist['BeginDate'],artist['EndDate'])

    lt.addLast(catalog['artists'],new)
   





# Funciones para creacion de datos

def newArtwork(name):
    '''
    Crea un nuevo objeto de obra de arte con atributo de nombre (por ahora)
    '''
    artwork={'name':''}
    artwork['name']=name
    return artwork

def newArtist(name,begindate,enddate):
    '''
    Crea un nuevo objeto de obra de artista con atributo de nombre (por ahora)
    '''
    artist={'name':'','begindate':'','enddate':''}
    artist['name']=name
    artist['begindate']=begindate
    artist['enddate']=enddate
    artist['name']=name

    return artist

# Funciones de consulta

def get3LastElements(lista):

    """
    Retorna los 3 últimos elementos de una lista
    """

    pos=lt.size(lista)-2
    return lt.subList(lista, pos, 3)
        

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistname1,artist):
    '''
    Crea una función de comparación para el TAD lista de artista
    '''
    if (artistname1.lower() in artist['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento



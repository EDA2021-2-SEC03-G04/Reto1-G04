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
from DISClib.Algorithms.Sorting import shellsort as shsort
from DISClib.Algorithms.Sorting import insertionsort as insort
from DISClib.Algorithms.Sorting import mergesort as mrgsort
from DISClib.Algorithms.Sorting import quicksort as qcksort
import time


assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(datatype): 
    """
    Inicializa el catálogo de obras de arte. Crea una lista vacia para guardar
    todas las obras, adicionalmente, crea una lista vacia para los artistas.Retorna el catalogo inicializado.
    """

    catalog={'artworks': None, 'artists': None}

    catalog['artworks']=lt.newList(datatype)
    catalog['artists']=lt.newList(datatype, cmpfunction=compareartists)

    return catalog



# Funciones para agregar informacion al catalogo


def addArtwork(catalog,artwork): 
    #Se adiciona la obra  a la lista de obras
    new=newArtwork(artwork['Title'],artwork['DateAcquired'],artwork['ConstituentID'],artwork['Date'],artwork['Medium'],artwork['Dimensions'],artwork['Department'],artwork['CreditLine'],artwork['Classification'])
    lt.addLast(catalog['artworks'],new)
    


def addArtist(catalog,artist): 
    #Se adiciona el artista  a la lista de artistas
    new=newArtist(artist['DisplayName'],artist['BeginDate'],artist['EndDate'],artist['Nationality'],artist['Gender'],artist['ConstituentID'])

    lt.addLast(catalog['artists'],new)
   





# Funciones para creacion de datos

def newArtwork(name,dateacquired,constituentid,date,medium,dimensions,department,creditline,classification):
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
    



    artwork={'name':'','dateacquired':'','constituentid':'','date':'','medium':'','dimensions':'','department':'','creditline':'','classification':''}
    artwork['name']=name
    artwork['dateacquired']=dateacquired2
    artwork['constituentid']=constituentid
    artwork['date']=date
    artwork['medium']=medium
    artwork['dimensions']=dimensions
    artwork['department']=department
    artwork['creditline']=creditline
    artwork['classification']=classification 


    return artwork

def newArtist(name,begindate,enddate,nationality,gender,constituentid):
    '''
    Crea un nuevo objeto de obra de artista con atributos de nombre,fecha de inicio, fecha final
    '''
    artist={'name':'','begindate':'','enddate':'','nationality':'','gender':'','constituentid':''}
    artist['name']=name
    artist['begindate']=begindate
    artist['enddate']=enddate
    artist['nationality']=nationality
    artist['gender']=gender
    artist['constituentid']=constituentid
    

    return artist

# Funciones de consulta

def get3LastElements(lista):

    """
    Retorna los 3 últimos elementos de una lista
    """

    pos=lt.size(lista)-2
    return lt.subList(lista, pos, 3)
        


def artistasCronologico(lista, inicio, final):
    """
    Retorna una lista con los artistas ordenados por epoca
    """

    artistas = lista["artists"]
    cont = 0
    retorno = lt.newList()


    for x in range(lt.size(artistas)):

        grupo = lt.getElement(artistas, x)
        edad = int(grupo["begindate"])
        nombre = grupo["name"]
        muerte = int(grupo["enddate"])
        genero = grupo["gender"]
        nacionalidad = grupo["nationality"]

        if edad != 0 and edad != None and edad >= inicio and edad <= final:
            
            agregar = {"nombre" : nombre, "edad" : edad, "muerte" : muerte, "genero" : genero, "nacionalidad" : nacionalidad}
            lt.addLast(retorno, agregar)
    
    shsort.sort(retorno, compArtistasByBegindate)

    return retorno

def obrasCronologicoacq(lista,inicio,final,metodo,sizesublista): 
    """
    Retorna una lista con las obras ordenadas por fecha de adquisición 
    """
    obras = lista["artworks"]
    retorno = lt.newList()


    for x in range(round(lt.size(obras)*sizesublista)):

        grupo = lt.getElement(obras, x)
        dateacquired = grupo["dateacquired"]
        name = grupo["name"]
        medium = grupo["medium"]
        dimensions = grupo["dimensions"]
        

        if  dateacquired >= inicio and dateacquired <= final:
        
            
            agregar = {"name" : name, "dateacquired" : dateacquired, "medium" : medium, "dimensions" : dimensions}
            lt.addLast(retorno, agregar)
    
    StartTime=time.process_time()
    if metodo=='ShellSort':
        shsort.sort(retorno, cmpArtworkByDateAcquired)
    elif metodo=='InsertionSort':
        insort.sort(retorno, cmpArtworkByDateAcquired)
    elif metodo=='MergeSort':
        mrgsort.sort(retorno, cmpArtworkByDateAcquired)
    else:
        qcksort.sort(retorno,cmpArtworkByDateAcquired)
    StopTime=time.process_time()
    TimeMseg=(StopTime-StartTime)*1000

    print(f'El ordenamiento {metodo} tardó {TimeMseg} miliseg')


    return retorno




# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistname1,artist):
    '''
    Crea una función de comparación para el TAD lista de artista
    '''
    if (artistname1.lower() in artist['name'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1,artwork2): 
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1['dateacquired']<artwork2['dateacquired']

    

def compArtistasByBegindate(art1, art2):
    """
    compara artistas por su fecha de nacmiento 
    """
    return art1["edad"] < art2["edad"]


# Funciones de ordenamiento



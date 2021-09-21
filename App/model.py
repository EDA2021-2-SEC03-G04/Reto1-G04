﻿"""
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


from os import defpath
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
    new=newArtwork(artwork['Title'],artwork['DateAcquired'],artwork['ConstituentID'],artwork['Date'],artwork['Medium'],artwork['Dimensions'],
    artwork['Department'],artwork['CreditLine'],artwork['Classification'], artwork['Circumference (cm)'],artwork['Depth (cm)'],artwork['Diameter (cm)'],
    artwork['Height (cm)'],artwork['Length (cm)'],artwork['Weight (kg)'],artwork['Width (cm)'])

    lt.addLast(catalog['artworks'],new)
    


def addArtist(catalog,artist): 
    #Se adiciona el artista  a la lista de artistas
    new=newArtist(artist['DisplayName'],artist['BeginDate'],artist['EndDate'],artist['Nationality'],artist['Gender'],artist['ConstituentID'])

    lt.addLast(catalog['artists'],new)
   





# Funciones para creacion de datos

def newArtwork(name,dateacquired,constituentid,date,medium,dimensions,department,creditline,classification,circumference,depth,diameter,height,length,weight,width):
    '''
    Crea un nuevo objeto de obra de arte con atributos de nombre, fecha de adquisición 
    '''

    #Separamos la string de la fecha de adquisición con '-' y lo convertimos a foramto datetime
    #Si la entrada es vacia entonces se pone feha de hoy
    if dateacquired:
        datelst=dateacquired.split('-')
        dateacquired2=datetime.date(int(datelst[0]),int(datelst[1]),int(datelst[2]))
    else:
        dateacquired2=datetime.date.today()

    if date:
        date=int(date)
    else:
        date=3000
    
    



    artwork={'name':'','dateacquired':'','constituentid':'','date':'','medium':'','dimensions':'','department':''
    ,'creditline':'','classification':'','circumference':'','depth':'','diameter':'','height':'','length':'','weight':'','width':''}

    artwork['name']=name
    artwork['dateacquired']=dateacquired2
    artwork['constituentid']=constituentid
    artwork['date']=date
    artwork['medium']=medium
    artwork['dimensions']=dimensions
    artwork['department']=department
    artwork['creditline']=creditline
    artwork['classification']=classification 
    artwork['circumference']=circumference
    artwork['depth']=depth
    artwork['diameter']=diameter
    artwork['height']=height
    artwork['length']=length
    artwork['weight']=weight
    artwork['width']=width



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
    
    mrgsort.sort(retorno, compArtistasByBegindate)

    return retorno

def obrasCronologicoacq(lista,inicio,final,metodo,sizesublista): 
    """
    Retorna una lista con las obras ordenadas por fecha de adquisición 
    """
    #Lista con todas las obras
    obras = lista["artworks"]
    #La lista que se va a retornar de obras en el rango deseado
    retorno = lt.newList()

    #Recorre toda slas obras
    for x in range(round(lt.size(obras)*sizesublista)):
        #Toma la obra
        grupo = lt.getElement(obras, x)
        #Extrae los datos de la obra
        dateacquired = grupo["dateacquired"]
        name = grupo["name"]
        medium = grupo["medium"]
        dimensions = grupo["dimensions"]
        
        
        #Chequea si la obra fue adquirida en el rango de fechas deseado
        if  dateacquired >= inicio and dateacquired <= final:
        
            #Agrega la obra a la lista a retornar
            agregar = {"name" : name, "dateacquired" : dateacquired, "medium" : medium, "dimensions" : dimensions}
            lt.addLast(retorno, agregar)
    
    #Ordena la lista a retornar por fecha de adquisición
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


def ObrasArtista(catalog, nombre):
    """
    Retorna el total de obras de un artista, el total de técnicas usadas por el artista, la técnica más usada y una lista con las obras de dicha técnica
    """

    #Toma todas las obras y artistas
    Obras=catalog['artworks']
    Artistas=catalog['artists']

    #Obtiene el constituent ID del artista buscado
    Artista=lt.getElement(Artistas,lt.isPresent(Artistas,nombre))
    Constid=Artista['constituentid']
    #Lista Para guardar las obras de la tecinca más usada por el artista buscado
    ObrasArtistaTecnica=lt.newList()
    #Lista de todas las Obras del artista buscado
    ObrasArtista=lt.newList()
    #Diccionario para contar cuantas obras hay de cada técnica
    Tecnicas={}

    #Recorre todas las obras para ver cuales son del artista buscado
    for i in range(lt.size(Obras)): 
        Obra=lt.getElement(Obras,i)
        #Procesamiento del string de constituent id (una obra puede tener varios artistas)
        TecnicaObra=Obra['medium']
        ConstidObra=Obra['constituentid']
        ConstidObra=ConstidObra.translate({ord(i): None for i in '[]'})
        ConstidObra=ConstidObra.split(',')
        #Agrega las listas del artista a ObrasArtista
        if Constid in ConstidObra:  
            Tecnicas[TecnicaObra] = Tecnicas.get(i, 0) + 1
            lt.addLast(ObrasArtista,Obra)

    #Encuentra cuál es la técnica más usada y cúantas técnicas hay
    TotalTecnicas=len(Tecnicas)
    if TotalTecnicas==0:
        maxim=0
        TecnicaMasUsada=''

    else:
        maxim=max(Tecnicas.values())
        TecnicaMasUsada=str(list(Tecnicas.keys())[list(Tecnicas.values()).index(maxim)])

    
    #Crea la lista de obras del artista con la técnica más usada
    for i in range(lt.size(ObrasArtista)):
        Obra=lt.getElement(ObrasArtista,i) 
        if Obra['medium']==TecnicaMasUsada:
            lt.addLast(ObrasArtistaTecnica,Obra)

    TotalObras=lt.size(ObrasArtista)


    return TotalObras,TotalTecnicas-1,TecnicaMasUsada, ObrasArtistaTecnica

    
def Nacionalidad_obras(catalog):
    """
    Lista con la nacionalidad
    """

    General = lt.newList()
    Obras=catalog['artworks']
    Artistas=catalog['artists']
    NacioYaRegistradas = lt.newList()

    for x in range(lt.size(Obras)):

        obra = lt.getElement(Obras, x)
        Iden = obra['constituentid']
        Iden = Iden.translate({ord(i): None for i in '[]'})
        Iden = Iden.split(',')
        titulo = obra["name"]
        fecha = obra["date"]
        medio = obra["medium"]
        dimenciones = obra["dimensions"]

        nacionalidades = lt.newList()
        nombres = ""

        for y in range(lt.size(Artistas)):

            art = lt.getElement(Artistas, y)
            idenArt = art['constituentid']
            nacionalidadArt = art["nationality"]
            nomArt = art["name"]
            if idenArt in Iden and nacionalidadArt != "":

                lt.addLast(nacionalidades, nacionalidadArt)
                nombres = nombres + nomArt + " "

        for z in range(lt.size(nacionalidades)):

            nan = lt.getElement(nacionalidades, z)

            if lt.isPresent(NacioYaRegistradas, nan) == 0:

                #Agregar diccionarios
                lt.addLast(NacioYaRegistradas, nan)
                listaObrasMom = lt.newList()
                obraEspe = {"titulo" : titulo, "artistas" : nombres, "fecha" : fecha , "medio" : medio, "dimenciones" : dimenciones}
                lt.addLast(listaObrasMom ,obraEspe)
                agregado = {"lugar" : nan, "cantidad" : 1, "obras" : listaObrasMom}
                lt.addLast(General, agregado)    
            else:
                
                for x1 in range(lt.size(General)):
                    elemento = lt.getElement(General, x1)
                    if elemento["lugar"] == nan:
                        cantidadNueva = elemento["cantidad"] + 1
                        elemento["cantidad"] = cantidadNueva
                        lt.changeInfo(General, x1, elemento)

    mrgsort.sort(General, compNacionalidadByCantidad)

    return General



def Transporte(catalog,depa): 

    '''
    Calcula el costo e inforación asociada a transportar un departamento del museo
    '''
    #Obtiene las obras del catalogo
    Obras=catalog['artworks']
    #Crea una nueva lista para las obras del departamento a transportar
    ObrasDepto=lt.newList()
    #Acumulación del precio de transporte por obra
    TotalPrecio=0
    #Acumulación del peso total de las obras
    TotalPeso=0
    #Recorre todas las obras del catálogo para ver si están en el departamento a transportar
    for i in range(lt.size(Obras)):
        #Obtiene la obra
        Obra=lt.getElement(Obras,i)
        #Revisa si la obra pertenece al departamento a transportar
        if Obra['department'].lower()==depa.lower():
            #Función que calcula el costo de transporte de una obra
            costo=CalcularCosto(Obra)
            #Función que calcula el peso de una obra
            peso=CalcularPeso(Obra)
            #Se le añade el atributo 'costo' a cada obra
            Obra['cost']=costo
            #Se acumulan el precio y el peso
            TotalPrecio+=costo
            TotalPeso+=peso
            #Se añade la obra a la lista de obras del departamento buscado 
            lt.addLast(ObrasDepto,Obra)

    #Los ordena de forma DESCENDENTE por fecha en una lista y en la otra por costo de transporte
    TransportePorCosto=mrgsort.sort(ObrasDepto,compPrecio)
    TransportePorFecha=mrgsort.sort(ObrasDepto,compFecha)
    #Calcula el total de obras del departamento 
    TotalObras=lt.size(ObrasDepto)

    return TotalObras, TotalPrecio,TotalPeso,TransportePorCosto, TransportePorFecha


    

        









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

def compNacionalidadByCantidad(coso1, coso2):
    """
    Compara por cantidad de artistas con nacionalidad
    """
    return coso1["cantidad"] > coso2["cantidad"]

def compPrecio(obra1,obra2):
    '''
    Compara por precio de transporte en orden descendente 
    '''
    return obra1['cost'] > obra2["cost"]

def compFecha(obra1,obra2):
    '''
    Compara por precio de transporte en orden descendente 
    '''
    return int(obra1['date']) < int(obra2["date"])



# Funciones de ordenamiento

def CalcularCosto(Obra):

    '''
    Retorna el costo aproximado de transpotar una obra de arte
    '''

    circumference=Obra['circumference']
    depth=Obra['depth']
    diameter=Obra['diameter']
    height=Obra['height']
    lenght=Obra['length']
    weight=Obra['weight']

    return 1

def CalcularPeso(Obra): 
    '''
    Retorna el peso aproximado de una obra 
    '''

    return 1


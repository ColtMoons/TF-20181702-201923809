# Problema de la ruta más corta
**WV72 - Trabajo Final de Complejidad Algorítmica 2022-01**

## Integrantes
------
- Miner Lozano Becerra
- Antony Sthif Carrasco Cunya
- Prado Valer Luis Eduardo

## Resumen Ejecutivo
------
El problema de la ruta más corta consiste en encontrar la ruta más óptimo para llegar de un punto en la ciudad a otro punto en la ciudad. En este caso, estos puntos en la ciudad serán representados por los vértices, los cuales representan intersecciones entre calles en una ciudad. Por ello, se tendrán en cuenta los datos de las dos ubicaciones que se necesitan, la ubicación de inicio y la ubicación de destino.

Ante la problematica, hemos representado una ciudad como una zona de muestra, la cual esta compuesta por 1500 intersecciones entre calles de una ciudad. Debido a esto, cada una de las intersecciones será representado por un vértice y las calles que conectan a cada una de las intersecciones será representado por una arista que unirá a cada vertice respectivamente. Debido a ello, se generará un grafo en base a estos datos y a este grafo se le podra implementar los algoritmos de búsqueda del camino más corto que nos ayudará a encontrar el camino más óptimo entre dos vértices.

Al desarrollar los algoritmos, podremos hacer mejor uso de estos para resolver problemas de igual o mayor dificultad, además, obtendremos mayor conocimiento sobre el funcionamiento y la importancia de los algoritmos en problemas reales.

Para esto se plantean los siguientes objetivos:
-	Desarrollar las competencias del curso haciendo uso de técnicas y herramientas acorde a los objetivos del curso.
-	Desarrollar los algoritmos que resuelvan el problema de manera eficiente.
-	Determinar la importancia de la aplicación de algoritmos eficientes a la hora de resolver algún problema.
-	Analizar la eficiencia y complejidad de los algoritmos planteados.

## Imagen estática de la ciudad 
-------
Para el presente proyecto se eligio la ciudad de Manhattan y su imagen estática es la siguiente:

![Manhattan](/Pictures/Manhattan-Static-Photo.jpg)

## Descripción de los datos consignados por calle
----------
Se ha implementado la ciudad de manhattan y los datos que hemos agregado a las calles de esta ciudad han sido: 

- Nombre de la calle 
- ID de la calle
- Posición en el eje X inicio
- Posición en el eje Y inicio
- Posición en el eje X final
- Posicion en el eje Y final 

![utm](/Pictures/UTM.jpg)

Se hará uso de la latitud y longitud para generar los datos en UTM como se muestra en la imagen. En el caso del presente proyecto, se usará estos datos para brindarle unas coordenadas de inicio y final a nuestras aristas.

## Descripción de la información consignada por intersección
----
Se ha implementado la ciudad de Manhattan y los datos que hemos agregado en relación con las intersecciones son:

-	ID de la intersección
-	ID de calles que poseen intersección
-	posición en el eje X
-	posición en el eje Y

## Explicación de la elaboración del grafo
---
El grafo generado tiene el propósito de representar a la ciudad Manhattan, por ello, sus atributos como tal representan un atributo de una ciudad sus calles, intersecciones, distancias entre estas, etc. 

Grafo: Representa una porción de la ciudad manhattan 
Aristas: Representan la distancia entre intersecciones de la ciudad manhattan
Vértices: Representan las intersecciones de las distintas calles 

Para el desarrollo del grafo se hizo uso de un archivo .ipynb en donde se crearon una clase point que obtendría el valor del nodo en la que se encuentra sus posiciones x,y. Además, se crea una función para la lectura de datos de un .csv en donde nos retornan los datos de los nodos para luego entrar a la función donde se crea el grafo.

````
def readNodes(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines.pop(0)
        arr = []
        for l in lines:
            lista = l.strip().split(sep=",")
            arr.append(Point(int(lista[1]),int(lista[2]),int(lista[0])))
    return arr

def createGrah(n):
    g=[[] for _ in range(len(n))]
    for i in range(len(n)):
        if  n[i].getID()-1 >= 0 and n[i].getID() % 1000!=0:
            g[i].append(((n[i].getID()-1),10))
        if n[i].getID()+1 < len(n) and n[i].getID() % 1000 != 999:
            g[i].append(((n[i].getID()+1),10))
        if n[i].getID()+1000<len(n):
            g[i].append(((n[i].getID()+1000),15))
        if n[i].getID()-1000 >= 0:
            g[i].append(((n[i].getID()-1000),15))
    return g

nodos= readNodes("Nodos.csv")
grafo=createGrah(nodos)
````
## Exposición Trabajo Pacial
----

Enlace https://www.youtube.com/watch?app=desktop&v=7886otI_7fM&feature=youtu.be

## Exposición Trabajo Final 
----

Enlace: 

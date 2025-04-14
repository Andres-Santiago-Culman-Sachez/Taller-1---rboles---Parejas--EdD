import bigtree as BT
from bigtree import Node

raizPrincipal = Node("a", dato = 20)    #primer parametro es el nombre del nodo, el segundo es el dato que contiene

#Creación de otros nodos que mediante 'parent = ...' hace que raizPrincipal sea su raíz
nodoB = Node("b", dato = 32, parent = raizPrincipal)
nodoC = Node("c", dato = 23, parent = raizPrincipal)

#Hijos de 'raizPrincipal'
raizPrincipal.children

# el atributo '.depth' muestra en nivel en que se encuentra el nodo
raizPrincipal.depth, nodoB.depth

#Muestra el orden del arbol
raizPrincipal.max_depth

#Muestra lo que contiene dato en todos los nodos
raizPrincipal.show(attr_list=["dato"])

#Muestra graficamente el arbol mediante la terminal
raizPrincipal.hshow()

#Muestra el camino por pasos y organiza cada paso en un vector
print(raizPrincipal.go_to(nodoC))

nodoD = Node("d", dato = 45, parent = nodoB)
print(raizPrincipal.go_to(nodoD))

raizPrincipal.show(attr_list=["dato"])

nodoE = Node("e", dato = 50, parent = nodoB)
nodoF = Node("f", dato = 60, parent = nodoB)
raizPrincipal.hshow()

print(f"los hijos de {nodoB.name} son: {nodoB.children}")

#Es arbol?
esRaizNodoB = nodoB.is_root
print(esRaizNodoB)
print(raizPrincipal.is_root)
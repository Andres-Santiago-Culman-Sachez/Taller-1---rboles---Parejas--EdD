# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Taller 1 - Árboles - Parejas
# ===========================================
#Fecha 15/04/2025
#Estudiantes:
#Kevin David Basto Quintero 2222974
#Andres Santiago Culman Sanchez 2241929

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None

class Arbol:
    def __init__(self, dato):
        self.cabeza = dato
        self.contador = 1
        self.nodos = [dato]


    def asignarPadre(self, datoPadre, datoHijo):
        datoHijo.anterior = datoPadre
    # Evitar agregar nodos duplicados
        if datoHijo not in self.nodos:
            self.nodos.append(datoHijo)
            self.contador += 1
        return True



    def peso(self):
        return self.contador


    def altura(self, hoja):
        actual = hoja
        cont = 1
        #print(actual)
        while actual.anterior:
            cont += 1
            actual = actual.anterior
        return cont

    def orden(self):
        orden = 0
        for nodo in self.nodos:
            altura = self.altura(nodo)
            if altura > orden:
                orden = altura
        return orden



#Instanciacion
nodo1 = Nodo("gato")
nodo2 = Nodo("perro")
nodo3 = Nodo("animales")
nodo4 = Nodo("mascotas")
nodo5 = Nodo("salvajes")
nodo6 = Nodo("leon")
nodo7 = Nodo("hijoLeon")
arbol = Arbol(nodo3)

#Asignación
arbol.asignarPadre(nodo3, nodo1)
arbol.asignarPadre(nodo3, nodo2)
arbol.asignarPadre(nodo4, nodo3)
arbol.asignarPadre(nodo4, nodo5)
arbol.asignarPadre(nodo5, nodo6)
arbol.asignarPadre(nodo6, nodo7)

#Metodos
print(arbol.peso())
#Alturas
print(f"Altura del nodo {nodo2.dato}: {arbol.altura(nodo2)}")
print(f"Altura del nodo {nodo1.dato}: {arbol.altura(nodo1)}")
print(f"Altura del nodo {nodo3.dato}: {arbol.altura(nodo3)}")
print(f"Altura del nodo {nodo4.dato}: {arbol.altura(nodo4)}")
print(f"Altura del nodo {nodo5.dato}: {arbol.altura(nodo5)}")
print(f"Altura del nodo {nodo6.dato}: {arbol.altura(nodo6)}")
#Orden
print(f"El orden del arbol es:{arbol.orden()}")
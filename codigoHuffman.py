import heapq
from collections import defaultdict, Counter

class NodoHuffman:
    def __init__(self, char,frec):
        self.char = char
        self.frec = frec
        self.left = None
        self.right = None

    def __lt__(self, otro):
        return self.frec < otro.frec

def arbolHuffman(frec):
    #Crear un heap  (cola de prioridad)
    heap= [NodoHuffman(char,frec) for char,frec in frec.items()]
    heapq.heapify(heap)

#Combinamos los nodos con menor frecuencia

    while len(heap) > 1:
        lef=heapq.heappop(heap)
        rig=heapq.heappop(heap)
        nodo_interno=NodoHuffman(None, lef.frec+rig.frec)
        nodo_interno.left=lef
        nodo_interno.right=rig
        heapq.heappush(heap, nodo_interno)

    return heap[0]

def generar_codigo_Huffman(nodo, prefijo="", codigos=defaultdict()):
    if nodo:
        if nodo.char is not None:
            codigos[nodo.char]= prefijo
        generar_codigo_Huffman(nodo.left, prefijo+"0", codigos)
        generar_codigo_Huffman(nodo.right, prefijo+"1", codigos)
    return codigos


frecuencias={
    "a":5,
    "b":9,
    "c":12,
    "d":13,
    "e":16,
    "f":45,
}

arbolDeHuffman=arbolHuffman(frecuencias)
codigos=generar_codigo_Huffman(arbolDeHuffman)

for caracter,codigo in codigos.items():
    print(f"{caracter}: {codigo}")
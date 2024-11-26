from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}  
    def agregar_vertice(self, v):
        if v not in self.grafo:
            self.grafo[v] = []
    def agregar_arco(self, v1, v2, peso=1):
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        self.grafo[v1].append((v2, peso))
        self.grafo[v2].append((v1, peso))  
    def recorrido_en_anchura(self, nodo_inicio):
        if nodo_inicio not in self.grafo:
            print(f"El nodo {nodo_inicio} no existe en el grafo.")
            return  
        visitados = set()
        cola = deque([nodo_inicio])
        
        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                print(nodo, end=" ")
                visitados.add(nodo)
                for vecino, _ in self.grafo[nodo]:
                    if vecino not in visitados:
                        cola.append(vecino)
        print()
    def recorrido_en_profundidad(self, nodo_inicio):
        if nodo_inicio not in self.grafo:
            print(f"El nodo {nodo_inicio} no existe en el grafo.")
            return
        
        visitados = set()
        self.dfs_recursivo(nodo_inicio, visitados)
        print()

    def dfs_recursivo(self, nodo, visitados):
        visitados.add(nodo)
        print(nodo, end=" ")
        for vecino, _ in self.grafo[nodo]:
            if vecino not in visitados:
                self.dfs_recursivo(vecino, visitados)

    def buscar_vertice(self, vertice):
        return vertice in self.grafo

    def distancia_entre_nodos(self, nodo_origen, nodo_destino):
        if nodo_origen not in self.grafo or nodo_destino not in self.grafo:
            print(f"Uno o ambos nodos no existen en el grafo.")
            return None
        
        cola = deque([(nodo_origen, 0)])  
        visitados = set()

        while cola:
            nodo, distancia = cola.popleft()

            if nodo == nodo_destino:
                return distancia
            
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino, peso in self.grafo[nodo]:
                    if vecino not in visitados:
                        cola.append((vecino, distancia + peso))
        
        return None  # Si no se encuentra el nodo destino
def mostrar_menu():
    print("\nMenú:")
    print("1. Recorrido en Anchura (BFS)")
    print("2. Recorrido en Profundidad (DFS)")
    print("3. Buscar Vértice")
    print("4. Distancia entre dos nodos")
    print("5. Salir")
def ejecutar_grafo():
    grafo.agregar_arco('A', 'B', 1)
    grafo.agregar_arco('A', 'C', 4)
    grafo.agregar_arco('B', 'C', 2)
    grafo.agregar_arco('B', 'D', 5)
    grafo.agregar_arco('C', 'D', 1)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nodo_inicio = input("Ingrese el nodo de inicio para BFS: ")
            grafo.recorrido_en_anchura(nodo_inicio)
        
        elif opcion == "2":
            nodo_inicio = input("Ingrese el nodo de inicio para DFS: ")
            grafo.recorrido_en_profundidad(nodo_inicio)
        
        elif opcion == "3":
            vertice = input("Ingrese el vértice a buscar: ")
            encontrado = grafo.buscar_vertice(vertice)
            if encontrado:
                print(f"El vértice {vertice} fue encontrado.")
            else:
                print(f"El vértice {vertice} no fue encontrado.")
        
        elif opcion == "4":
            nodo_origen = input("Ingrese el nodo de origen: ")
            nodo_destino = input("Ingrese el nodo de destino: ")
            distancia = grafo.distancia_entre_nodos(nodo_origen, nodo_destino)
            if distancia is not None:
                print(f"La distancia entre {nodo_origen} y {nodo_destino} es: {distancia}")
            else:
                print("No se encontró un camino entre los nodos.")
        
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    ejecutar_grafo()

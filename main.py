import networkx as nx
import matplotlib.pyplot as plt
import os


# Parcial #2 IA, metodo anchura

def crear_grafo():
    G = nx.DiGraph()
    G.add_edge("Colon", "Chiriqui", weight=2300)
    G.add_edge("Cocle", "Veraguas", weight=1500)
    G.add_edge("Veraguas", "Los Santos", weight=2000)
    G.add_edge("Veraguas", "Chiriqui", weight=1500)
    G.add_edge("Veraguas", "Herrera", weight=1500)
    G.add_edge("Los Santos", "Chiriqui", weight=2000)
    G.add_edge("Panamá", "Cocle", weight=1500)
    G.add_edge("Panamá", "Veraguas", weight=2400)
    G.add_edge("Panamá", "Colon", weight=1300)
    G.add_edge("Colon", "Bocas del toro", weight=2000)
    G.add_edge("Colon", "Cocle", weight=1000)
    return G


def propiedades_grafo():
    pos = nx.circular_layout(Grafo)
    nx.draw(Grafo, pos, node_size=5000, edge_color='grey', node_color='w', arrowsize=10, width=3.5, with_labels=True,
            arrowstyle="->")


def bfs():
    Visitados = {node: False for node in Grafo.nodes}
    Cola = [NodoInicio]
    Visitados[NodoInicio] = True
    Ruta = []
    while Cola:
        nodoActual = Cola.pop(0)
        Ruta.append(nodoActual)
        for node in Grafo.neighbors(nodoActual):
            if not Visitados[node]:
                if node == NodoMeta:
                    Cola.clear()
                    Ruta.append(node)
                    break
                Cola.append(node)
                Visitados[node] = True

    print('\n\tParcial #2\n\tDavid Gómez\n\tBúsqueda en anchura')
    print("\n\tRuta: ", " -> ".join(Ruta))


def imprimir_grafo():
    x = plt.gca()
    x.margins(0.1)
    plt.axis("off")
    plt.title('Parcial #2 David Gómez')
    plt.show()


def cls():
    os.system('cls')


if __name__ == '__main__':
    Grafo = crear_grafo()
    propiedades_grafo()
    NodoInicio = "Panamá"
    NodoMeta = "Chiriqui"
    bfs()
    imprimir_grafo()

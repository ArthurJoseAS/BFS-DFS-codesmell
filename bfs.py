import sys
import pydot

def ler_grafo_dot(arquivo):
    graphs = pydot.graph_from_dot_file(arquivo)
    g = graphs[0]
    
    nodes = [n.get_name() for n in g.get_nodes() if n.get_name() not in ('node', 'graph', 'edge')]

    for edge in g.get_edges():
        src = edge.get_source()
        dst = edge.get_destination()
        if src not in nodes:
            nodes.append(src)
        if dst not in nodes:
            nodes.append(dst)

    n = len(nodes)
    nodes.sort()

    indice = {}

    for i in range(n):
        indice[nodes[i]] = i


    matriz = [[0] * n for _ in range(n)]


    for edge in g.get_edges():
        u, v = str(edge.get_source()), str(edge.get_destination())
        i, j = indice[u], indice[v]
        matriz[i][j] = 1
        if not g.get_type() == "digraph":
            matriz[j][i] = 1

    return nodes, matriz


def bfs(vertices, matriz):
    n = len(vertices)
    visitados = [False] * n
    ordem = []

    inicio = 0
    fila = [inicio]
    visitados[inicio] = True

    while fila:
        u = fila.pop(0)
        ordem.append(vertices[u])

        vizinhos = [i for i in range(n) if matriz[u][i] == 1]

        for v in vizinhos:
            if not visitados[v]:
                visitados[v] = True
                fila.append(v)

    return ordem


if __name__ == "__main__":
    arquivo = sys.argv[1]
    vertices, matriz = ler_grafo_dot(arquivo)

    print("Matriz de Adjacência:")
    for linha in matriz:
        print(linha)

    resultado = bfs(vertices, matriz)
    print("\nOrdem da BFS:", " -> ".join(resultado))
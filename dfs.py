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


    for i in range(n):
        indice[nodes[i]] = i

    adj_list = [[] for _ in range(n)]
    for edge in g.get_edges():
        
        u, v = str(edge.get_source()), str(edge.get_destination())
        i, j = indice[u], indice[v]

        if v not in adj_list[i]:
            adj_list[i].append(v)
        
        if not g.get_type() == "digraph":
            if u not in adj_list[j]:
                adj_list[j].append(u)
    return nodes, adj_list

qtd_vertices = 0
indice = {}
tempo_chegada = []
tempo_saida = []
predecessores = []
visitado: list
time: int = 0

def dfs(vertices: list[str], adj_list: list[list]):
    
    for v in vertices:
        visitado[indice[v]] = False    
    for v in vertices:
        if not visitado[indice[v]]:
            predecessores[indice[v]] = "NIL"
            dfs_visit(v, adj_list)
ordem = []

def dfs_visit(v, adj_list):
    global time
    ordem.append(v)
    visitado[indice[v]] = True
    time += 1
    tempo_chegada[indice[v]] = time
    
    adj_list[indice[v]].sort()
    for a in adj_list[indice[v]]:
        if not visitado[indice[a]]:
            predecessores[indice[a]] = v
            dfs_visit(a, adj_list)
    
    time += 1
    tempo_saida[indice[v]] = time

if __name__ == "__main__":
    arquivo = sys.argv[1]
    vertices, adj_list = ler_grafo_dot(arquivo)
    qtd_vertices = len(vertices)
    visitado = [None] * qtd_vertices
    tempo_chegada = [None] * qtd_vertices
    tempo_saida = [None] * qtd_vertices
    predecessores = [None] * qtd_vertices 
    dfs(vertices, adj_list)
    for i in ordem:
        print(">" + str(i) + "-"  , end = "")
    print("")
    for v in vertices:
        print(str(v) + " " + str(tempo_chegada[indice[v]]) + "/" + str(tempo_saida[indice[v]]))
    print(predecessores)
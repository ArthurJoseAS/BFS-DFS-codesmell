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

indice = {}
tempo_chegada = []
tempo_final = []
predecessores = []
visitado = []
time = 0

def dfs(vertices: list[str], adj_list: list[list]):
    for v in vertices:
        visitado[v] = False    
    for v in vertices:
        if not visitado[v]:
            dfs_visit(v, adj_list)

def dfs_visit(v, adj_list):
    visitado[v] = True
    tempo += 1
    adj_list[indice[v]].sort()
    for a in adj_list[indice[v]]:
        if not visitado[a]:
            dfs_visit(a, adj_list)
    tempo += 1
    return

if __name__ == "__main__":
    arquivo = sys.argv[1]
    vertices, adj_list = ler_grafo_dot(arquivo)

    resultado = dfs(vertices, adj_list)
    print("\nOrdem da DFS:", " -> ".join(resultado))

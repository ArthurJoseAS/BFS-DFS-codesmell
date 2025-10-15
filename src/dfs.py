import sys
import pydot


"""
Fills the nodes list with the graph read from the .dot file
"""
def populate_nodes_list(nodes, g):
    for edge in g.get_edges():
        src = edge.get_source()
        dst = edge.get_destination()
        if src not in nodes:
            nodes.append(src)
        if dst not in nodes:
            nodes.append(dst)
    nodes.sort()

"""
Fills adjacency list with the edges read from the .dot file
"""
def fill_adj_list(adj_list, g):
    for edge in g.get_edges():
        
        u, v = str(edge.get_source()), str(edge.get_destination())
        i, j = indice[u], indice[v]

        if v not in adj_list[i]:
            adj_list[i].append(v)
        
        if not g.get_type() == "digraph":
            if u not in adj_list[j]:
                adj_list[j].append(u)


"""
Reads a .dot file and returns a node list and an adjacency list that represents the read graph
"""
def read_dot_graph(arquivo):
    graphs = pydot.graph_from_dot_file(arquivo)
    g = graphs[0]
    
    nodes = [n.get_name() for n in g.get_nodes() if n.get_name() not in ('node', 'graph', 'edge')]


    populate_nodes_list(nodes, g)
    n = len(nodes)

    for i in range(n):
        indice[nodes[i]] = i

    
    adj_list = [[] for _ in range(n)]
    fill_adj_list(adj_list, g)

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
            export_graph.add_edge(pydot.Edge(v, a))
            dfs_visit(a, adj_list)
    
    time += 1
    tempo_saida[indice[v]] = time

export_graph = pydot.Dot("output_graph", graph_type="graph")

if __name__ == "__main__":
    arquivo = sys.argv[1]
    vertices, adj_list = read_dot_graph(arquivo)
    for v in vertices:
        export_graph.add_node(pydot.Node(v))
    
    qtd_vertices = len(vertices)
    visitado = [None] * qtd_vertices
    tempo_chegada = [None] * qtd_vertices
    tempo_saida = [None] * qtd_vertices
    predecessores = [None] * qtd_vertices 
    dfs(vertices, adj_list)
    print("Ordem da DFS:", " -> ".join(ordem))
    for v in vertices:
        print(str(v) + ": " + str(adj_list[indice[v]]) + "  " + str(tempo_chegada[indice[v]]) + "/" + str(tempo_saida[indice[v]])
              + "  Predecessor: " + str(predecessores[indice[v]]))
    nome_arquivo: str = sys.argv[1][:sys.argv[1].rindex(".")]
    export_graph.write(nome_arquivo + "dfstree.dot")
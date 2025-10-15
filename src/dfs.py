import sys
import pydot

def read_dot_graph(filepath):
    """
    Reads a graph from a .dot file and represents it as an adjacency list.
    """
    graphs = pydot.graph_from_dot_file(filepath)
    graph = graphs[0]
    
    nodes = [n.get_name() for n in graph.get_nodes() if n.get_name() not in ('node', 'graph', 'edge')]

    for edge in graph.get_edges():
        src = edge.get_source()
        dst = edge.get_destination()
        if src not in nodes:
            nodes.append(src)
        if dst not in nodes:
            nodes.append(dst)

    node_count = len(nodes)
    nodes.sort()

    for i in range(node_count):
        vertex_indices[nodes[i]] = i

    adjacency_list = [[] for _ in range(node_count)]
    for edge in graph.get_edges():
        
        u, v = str(edge.get_source()), str(edge.get_destination())
        i, j = vertex_indices[u], vertex_indices[v]

        if v not in adjacency_list[i]:
            adjacency_list[i].append(v)
        
        if not graph.get_type() == "digraph":
            if u not in adjacency_list[j]:
                adjacency_list[j].append(u)
                
    return nodes, adjacency_list

# Global variables for DFS
vertex_count = 0
vertex_indices = {}
discovery_time = []
finish_time = []
predecessors = []
visited: list
time: int = 0
traversal_order = []

def dfs(vertices: list[str], adjacency_list: list[list]):
    """
    Initializes and runs the Depth-First Search algorithm.
    """
    for v in vertices:
        visited[vertex_indices[v]] = False
        
    for v in vertices:
        if not visited[vertex_indices[v]]:
            predecessors[vertex_indices[v]] = "NIL"
            dfs_visit(v, adjacency_list)

def dfs_visit(v, adjacency_list):
    """
    The recursive core of the DFS algorithm.
    """
    global time
    traversal_order.append(v)
    visited[vertex_indices[v]] = True
    time += 1
    discovery_time[vertex_indices[v]] = time
    
    adjacency_list[vertex_indices[v]].sort()
    for neighbor in adjacency_list[vertex_indices[v]]:
        if not visited[vertex_indices[neighbor]]:
            predecessors[vertex_indices[neighbor]] = v
            export_graph.add_edge(pydot.Edge(v, neighbor))
            dfs_visit(neighbor, adjacency_list)
    
    time += 1
    finish_time[vertex_indices[v]] = time

export_graph = pydot.Dot("output_graph", graph_type="graph")

if __name__ == "__main__":
    filepath = sys.argv[1]
    vertices, adjacency_list = read_dot_graph(filepath)
    
    for v in vertices:
        export_graph.add_node(pydot.Node(v))
    
    vertex_count = len(vertices)
    visited = [None] * vertex_count
    discovery_time = [None] * vertex_count
    finish_time = [None] * vertex_count
    predecessors = [None] * vertex_count
    
    dfs(vertices, adjacency_list)
    
    print("DFS Order:", " -> ".join(traversal_order))
    
    for v in vertices:
        idx = vertex_indices[v]
        print(f"{v}: {adjacency_list[idx]}  {discovery_time[idx]}/{finish_time[idx]}  Predecessor: {predecessors[idx]}")

    filename_base = filepath[:filepath.rindex(".")]
    export_graph.write(filename_base + "_dfstree.dot")
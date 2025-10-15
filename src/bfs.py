import sys
import pydot


"""
Fills the adjacency matrix with the edges from the .dot graph
"""
def fill_adj_matrix(graph, node_index_map, adjacency_matrix):
    for edge in graph.get_edges():
        source_vertex, destination_vertex = str(edge.get_source()), str(
            edge.get_destination()
        )
        source_index, destination_index = (
            node_index_map[source_vertex],
            node_index_map[destination_vertex],
        )
        adjacency_matrix[source_index][destination_index] = 1
        if not graph.get_type() == "digraph":
            adjacency_matrix[destination_index][source_index] = 1

"""
Fills the nodes list with the graph read from the .dot file
"""
def populate_nodes_list(nodes, graph):
    for edge in graph.get_edges():
        source = edge.get_source()
        destination = edge.get_destination()
        if source not in nodes:
            nodes.append(source)
        if destination not in nodes:
            nodes.append(destination)

"""
Reads a .dot file and returns a node list and an adjacency matrix that represents the read graph
"""
def read_dot_graph(arquivo):
    graphs = pydot.graph_from_dot_file(arquivo)
    graph = graphs[0]

    nodes = [
        node.get_name()
        for node in graph.get_nodes()
        if node.get_name() not in ("node", "graph", "edge")
    ]
    populate_nodes_list(nodes, graph)
    # for edge in graph.get_edges():
    #     source = edge.get_source()
    #     destination = edge.get_destination()
    #     if source not in nodes:
    #         nodes.append(source)
    #     if destination not in nodes:
    #         nodes.append(destination)

    node_count = len(nodes)
    nodes.sort()

    node_index_map = {}

    for source_index in range(node_count):
        node_index_map[nodes[source_index]] = source_index

    adjacency_matrix = [[0] * node_count for _ in range(node_count)]

    fill_adj_matrix(graph ,node_index_map, adjacency_matrix)

    # for edge in graph.get_edges():
    #     source_vertex, destination_vertex = str(edge.get_source()), str(
    #         edge.get_destination()
    #     )
    #     source_index, destination_index = (
    #         node_index_map[source_vertex],
    #         node_index_map[destination_vertex],
    #     )
    #     adjacency_matrix[source_index][destination_index] = 1
    #     if not graph.get_type() == "digraph":
    #         adjacency_matrix[destination_index][source_index] = 1

    return nodes, adjacency_matrix


distance_list: list


def bfs(vertices, adjacency_matrix):
    vertex_count = len(vertices)
    visited = [False] * vertex_count
    visit_order = []
    start_vertex = 0
    queue = [start_vertex]
    visited[start_vertex] = True
    distance_list[0] = 0
    while queue:
        u = queue.pop(0)
        visit_order.append(vertices[u])

        neighbours = [i for i in range(vertex_count) if adjacency_matrix[u][i] == 1]

        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                distance_list[neighbour] = distance_list[u] + 1
                export_graph.add_edge(pydot.Edge(vertices[u], vertices[neighbour]))

    return visit_order


export_graph = pydot.Dot("output_graph", graph_type="graph")


if __name__ == "__main__":
    input_file = sys.argv[1]
    vertices, adjacency_matrix = read_dot_graph(input_file)

    for vertex in vertices:
        export_graph.add_node(pydot.Node(vertex))

    distance_list = [None] * len(vertices)
    result = bfs(vertices, adjacency_matrix)
    print("Ordem da BFS:", " -> ".join(result))
    print("\nMatriz de Adjacência:")

    for i, vertex in enumerate(vertices):
        print(
            str(vertex)
            + ": "
            + str(adjacency_matrix[i])
            + "  Distance: "
            + str(distance_list[i])
        )
    output_filename: str = sys.argv[1][: sys.argv[1].rindex(".")]
    export_graph.write(output_filename + "_bfstree.dot")

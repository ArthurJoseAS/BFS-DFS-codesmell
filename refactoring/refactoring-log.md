# Log de Refatorações

## Refatoração #1: Rename Variable/Method (BFS)

- **Data**: 14/10/2025
- **Code Smell**: Poor Naming
- **Técnica Aplicada**: Rename Variable/Method
- **Arquivos Afetados**: `bfs.py`
- **Justificativas**: Nomes em português e abreviados dificultam a compreensão e manutenção
- **Mudanças**:
  - `ler_grafo_dot → read_dot_graph`
  - `g → graph`
  - `n → node ; node_count ; vertex_count`
  - `src → source`
  - `dst → destination`
  - `indice → node_index_map`
  - `matriz → adjacency_matrix`
  - `u → source_vertex`
  - `v → destination_vertex ; neighbour ; vertex`
  - `i → source_index`
  - `j → destination_index`
  - `dist_list → distance_list`
  - `visitados → visited`
  - `ordem → visit_order`
  - `inicio → start_vertex`
  - `fila → queue`
  - `vizinhos → neighbours`
  - `arquivo → input_file`
  - `resultado → result`
  - `nome_arquivo → output_filename`
- **Impacto**: Código mais legível e seguindo convenções internacionais.

## Refatoração #2: Replace range(len()) with enumerate

- **Data**: 14/10/2025
- **Code Smell**: C0200 (Pylint) - Consider using enumerate
- **Técnica Aplicada**: Replace Loop with Built-in
- **Arquivos Afetados**: `bfs.py`
- **Justificativas**: Uso de `range(len(sequence))` é menos Pythonico e mais verboso que `enumerate(sequence)`

**Antes:**

```python
for i in range(len(vertices)):
    print(
        str(vertices[i])
        + ": "
        + str(adjacency_matrix[i])
        + "  Distance: "
        + str(distance_list[i])
    )
```

**Depois:**

```python
for i, vertex in enumerate(vertices):
    print(
        str(vertex)
        + ": "
        + str(adjacency_matrix[i])
        + "  Distance: "
        + str(distance_list[i])
    )
```  

- **Mudanças**: `range(len(vertices)) → enumerate(vertices)`; `vertices[i] → vertex (acesso direto ao elemento)`; Eliminação de indexação desnecessária.

## Refatoração #3: Breaking up the read_dot_graph into smaller functions

- **Data**: 14/10/2025
- **Code Smell**: Long Method
- **Técnica Aplicada**: Breaking up method in smaller ones
- **Arquivos Afetados**: `dfs.py` & `bfs.py`
- **Justificativas**: Método muito longo e com muitas responsabilidades

**Antes**

```python
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
```

```python
    for edge in graph.get_edges():
        source = edge.get_source()
        destination = edge.get_destination()
        if source not in nodes:
            nodes.append(source)
        if destination not in nodes:
            nodes.append(destination)
```

**Depois**

```python
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
```

```python
def populate_nodes_list(nodes, graph):
    for edge in graph.get_edges():
        source = edge.get_source()
        destination = edge.get_destination()
        if source not in nodes:
            nodes.append(source)
        if destination not in nodes:
            nodes.append(destination)
```

## Refatoração #4: Rename Variable/Method (DFS)

- **Data**: 14/10/2025
- **Code Smell**: Poor Naming
- **Técnica Aplicada**: Rename Variable/Method
- **Arquivos Afetados**: `dfs.py`
- **Justificativas**: Nomes das variáveis e funções em português e nomes abreviados, dificultam a leitura e identificação de métodos no código.
- **Mudanças**:
- `ler_grafo_dot → read_dot_graph`
- `g → graph`
- `n → node_count`
- `adj_list → adjacency_list`
- `qtd_vertices → vertex_count`
- `tempo_chegada → discovery_time`
- `tempo_saida → finish_time`
- `predecessores → predecessors`
- `indice → vertex_indices`
- `visitado → visited`
- `ordem → traversal_order`
- `arquivo → filepath`
- `a → neighbour`
- `nome_arquivo → filename_base`
- `arquivo → filepath`

- **Impacto**: Código mais legível, autoexplicativo e seguindo convenções internacionais, facilitando colaborações futuras.

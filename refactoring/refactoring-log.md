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

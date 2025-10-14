# Code Smells Identificados

## Análise do Arquivo: `bfs.py`

### 1. **Long Method**

- **Arquivo**: `bfs.py`
- **Linhas**: 5-40
- **Descrição**: A função `ler_grafo_dot()` possui 35 linhas e múltiplas responsabilidades
- **Severidade**: Alta
- **Problemas Específicos**:
  - Lê arquivo DOT
  - Extrai nós do grafo
  - Processa arestas
  - Constrói matriz de adjacência
  - Ordena nós
- **Ferramenta**: pylint (função muito complexa)
- **Status**: Pendente

### 2. **Poor Naming (Nomenclatura Pobre)**

- **Arquivo**: `bfs.py`
- **Linhas**: Em todo o código
- **Descrição**: Nomes de variáveis e funções não descritivos e em português
- **Severidade**: Alta
- **Exemplos**:
  - `g` → `graph`
  - `n` → `node_count`
  - `matriz` → `adjacency_matrix`
  - `fila` → `queue`
  - `vizinhos` → `neighbors`
  - `ler_grafo_dot` → `read_dot_graph`
- **Status**: Pendente

### 3. **Global Variables (Variáveis Globais)**

- **Arquivo**: `bfs.py`
- **Linhas**: 43, 75
- **Descrição**: Uso de variáveis globais `dist_list` e `export_graph`
- **Severidade**: Alta
- **Problemas**:
  - Dificulta teste unitário
  - Causa acoplamento entre funções
  - Possível estado inconsistente
- **Status**: Pendente

### 4. **Magic Number (Número Mágico)**

- **Arquivo**: `bfs.py`
- **Linhas**: 52
- **Descrição**: Uso de índice fixo `inicio = 0` sem explicação
- **Severidade**: Média
- **Problema**: Não fica claro por que o vértice 0 é sempre o início
- **Status**: Pendente

### 5. **Duplicate Code (Código Duplicado)**

- **Arquivo**: `bfs.py`
- **Linhas**: 13-19, 78-79
- **Descrição**: Lógica de extração de nós repetida em diferentes contextos
- **Severidade**: Baixa
- **Status**: Pendente

### 6. **Feature Envy (Inveja de Funcionalidade)**

- **Arquivo**: `bfs.py`
- **Linhas**: 45-70
- **Descrição**: Função `bfs()` modifica `export_graph` que não é seu parâmetro
- **Severidade**: Média
- **Problema**: A função BFS deveria ser pura e não ter efeitos colaterais de exportação
- **Status**: Pendente

### 7. **Dead Code (Código Morto)**

- **Arquivo**: `bfs.py`
- **Linha**: 43
- **Descrição**: Declaração `dist_list: list` sem inicialização adequada
- **Severidade**: Baixa
- **Status**: Pendente

### 8. **No Error Handling (Falta de Tratamento de Erros)**

- **Arquivo**: `bfs.py`
- **Linhas**: 7, 81
- **Descrição**: Nenhum tratamento para arquivo não encontrado ou formato inválido
- **Severidade**: Alta
- **Status**: Pendente

### 9. **Mixed Abstractions (Abstrações Misturadas)**

- **Arquivo**: `bfs.py`
- **Linhas**: 45-70
- **Descrição**: Função `bfs()` mistura algoritmo BFS com manipulação de gráficos de exportação
- **Severidade**: Média
- **Status**: Pendente

## Análise do Arquivo: `dfs.py`

### 1. **Lorem Ipsum**

- **Arquivo**: `bfs.py`
- **Linhas**: 
- **Descrição**: 
- **Severidade**: 
- **Status**: 

**Total de Code Smells Identificados**: 9

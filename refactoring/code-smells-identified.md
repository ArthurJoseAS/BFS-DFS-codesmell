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

### 10. **Long Method**

- **Arquivo**: `dfs.py`
- **Linhas**: 3-30
- **Descrição**: A função `ler_grafo_dot()` possui 27 linhas com múltiplas responsabilidades
- **Severidade**: Alta
- **Problemas Específicos**:
  - Lê arquivo DOT
  - Extrai nós do grafo
  - Processa arestas
  - Constrói lista de adjacência
  - Ordena nós
- **Ferramenta**: pylint (função muito complexa)
- **Status**: Pendente

### 11. **Poor Naming (Nomenclatura Pobre)**

- **Arquivo**: `dfs.py`
- **Linhas**: Em todo o código
- **Descrição**: Nomes de variáveis e funções não descritivos e em português
- **Severidade**: Alta
- **Exemplos**:
  - `g` → `graph`
  - `n` → `node_count`
  - `adj_list` → `adjacency_list`
  - `qtd_vertices` → `vertex_count`
  - `tempo_chegada` → `discovery_time`
  - `tempo_saida` → `finish_time`
- **Status**: Pendente

### 12. **Global Variables (Variáveis Globais)**

- **Arquivo**: `dfs.py`
- **Linhas**: 33-39, 58
- **Descrição**: Uso extensivo de variáveis globais (`qtd_vertices`, `indice`, `tempo_chegada`, `tempo_saida`, `predecessores`, `visitado`, `time`, `ordem`, `export_graph`)
- **Severidade**: Alta
- **Problemas**:
  - Estado compartilhado perigoso
  - Dificulta teste unitário
  - Causa acoplamento entre funções
- **Status**: Pendente

### 13. **Global State Modification**

- **Arquivo**: `dfs.py`
- **Linhas**: 42-46
- **Descrição**: Uso de `global time` para controle de estado
- **Severidade**: Alta
- **Problema**: Variável global modificada dentro da função `dfs_visit`
- **Status**: Pendente

### 14. **Mixed Abstractions (Abstrações Misturadas)**

- **Arquivo**: `dfs.py`
- **Linhas**: 48-60
- **Descrição**: Função `dfs_visit` mistura algoritmo DFS com manipulação de gráficos de exportação
- **Severidade**: Média
- **Problema**: A função DFS deveria focar apenas na travessia do grafo
- **Status**: Pendente

### 15. **Feature Envy (Inveja de Funcionalidade)**

- **Arquivo**: `dfs.py`
- **Linhas**: 55
- **Descrição**: Função `dfs_visit` modifica `export_graph` que não é seu parâmetro
- **Severidade**: Média
- **Status**: Pendente

### 16. **No Error Handling (Falta de Tratamento de Erros)**

- **Arquivo**: `dfs.py`
- **Linhas**: 4, 63
- **Descrição**: Nenhum tratamento para arquivo não encontrado ou formato inválido
- **Severidade**: Alta
- **Status**: Pendente

### 17. **Inconsistent Initialization**

- **Arquivo**: `dfs.py`
- **Linhas**: 33-39, 68-71
- **Descrição**: Variáveis globais declaradas em locais diferentes e inicializadas tardiamente
- **Severidade**: Média
- **Problema**: Dificulta o entendimento do fluxo de inicialização
- **Status**: Pendente

### 18. **Poor Function Structure**

- **Arquivo**: `dfs.py`
- **Linhas**: 42-46
- **Descrição**: Função `dfs` tem responsabilidade dupla - inicialização e execução do algoritmo
- **Severidade**: Média
- **Status**: Pendente

### 19. **Duplicate Code (Código Duplicado)**

- **Arquivo**: `dfs.py`
- **Linhas**: 7-13, 16-22
- **Descrição**: Lógica de extração de nós idêntica à do `bfs.py`
- **Severidade**: Baixa
- **Status**: Pendente

## Resumo por Severidade

| Severidade | BFS | DFS | Total |
|------------|-----|-----|-------|
| Alta       | 4   | 5   | 9     |
| Média      | 3   | 4   | 7     |
| Baixa      | 2   | 1   | 3     |

**Total de Code Smells Identificados**: 19

## Prioridade de Correção

### 🟥 Alta Prioridade (9 smells)

- Long Method em ambas as funções `ler_grafo_dot`
- Poor Naming em todos os arquivos
- Global Variables em ambos os arquivos
- No Error Handling em ambos os arquivos
- Global State Modification no DFS

### 🟧 Média Prioridade (7 smells)

- Mixed Abstractions
- Feature Envy
- Inconsistent Initialization
- Poor Function Structure
- Magic Number

### 🟩 Baixa Prioridade (3 smells)

- Duplicate Code
- Dead Code


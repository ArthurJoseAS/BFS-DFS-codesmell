# BFS-DFS
Implementação da Busca em Largura e Busca em Profundidade em python com a leitura de um arquivo .dot

## Como Rodar
Idealmente, usa-se a ferramenta uv para sincronizar bibliotecas python.
Para sincronizar apenas execute ``uv sync`` na raiz do projeto
Para rodar a bfs utilize ``uv run python3 src/bfs.py {nome do arquivo do grafo}.dot``. A dfs é rodada de forma analoga

Caso não esteja utilizando o uv, é preciso ter a biblioteca pydot instalada e rodar o comando acima **sem** a parte do ``uv run``

## Saída do programa

A BFS exibe a ordem de busca, a matriz de adjacência e as distâncias do vértice inicial para cada vértice do grafo. Além disso ela exibe a árvore de BFS gerada pela bfs como um arquivo chamado bfstree.dot no diretório em que está localizado o arquivo .dot original

A DFS exibe a ordem de busca, as listas de adjacências de cada vértice, o tempo de chegada e saída de cada vértice e os predecessores. Além disso ela exibe a árvore DFS gerada pela busca como um arquivo .dot assim como na BFS

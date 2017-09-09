# Questão 3: Qual ou quais as diferenças entre lista e matriz de adjacências para grafos sem peso nas arestas e grafos com pesos nas arestas?

## Para grafos sem peso nas arestas:

A matriz de adjacência contém, na coluna j, linha i, um valor, ou 0 ou 1. 1 diz que existe uma conexão entre os vértices i e j, 0 diz que a conexão não existe.
A lista de adjacência apenas contém as conexões existentes, em ordem crescente, na numeração dos vértices do grafo.

## Para grafos com peso nas arestas:

A matriz de adjacências pode ser alterada para, em vez de conter um 1 quando houver conexão entre vértices, conter o gasto para essa aresta.
A lista de adjacências pode ser alterada para, além de conter a conexão existente, o valor da aresta.

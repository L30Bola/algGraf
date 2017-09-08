<meta charset="UTF-8">
# Questão 1: Descreva um algoritmo (o mais eficiente possível) que, dado um grafo por sua matriz de adjacências, determina sua lista de adjacências. Qual é a complexidade desse algoritmo? Ele funciona para digrafos?
    
Ideia do algoritmo:
```
listaAdj = lista adjacências
para cada linha I na matriz:
	para cada coluna J na linha i:
		se matriz[linhaI][colunaJ] != 0:
                        adjList[linhaI].append(colunaJ)
```

Ele não está o mais otimizado para facilitar a visualização. Sua complexidade é linear; O(n). Sim, funciona para grafos direcionados e para grafos não direcionados.

## [Código](codigo/questao1.py)

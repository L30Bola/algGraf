#!/usr/bin/env python
def matrizAdj2listaAdj(matriz):
    listaAdj = []
    posLinha = posColuna = 0
    for linha in range(len(matriz)):
        listaAdj.append([])
    for linha in matriz:
        posColuna = 0
        for coluna in linha: 
            if matriz[posLinha][posColuna] != 0:
                listaAdj[posLinha].append({posColuna: coluna})
            posColuna += 1
        posLinha += 1
    print listaAdj

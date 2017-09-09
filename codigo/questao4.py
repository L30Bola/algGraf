#!/usb/bin/env python

def backtracking(palavras, palavrasUsadas, pos, qtd, ultimaPalavra, ordenadas):
    sol = False
    if int(pos) == int(qtd):
        for i in ordenadas:
            print(i)
        return True
    for i in range(int(qtd)):
	if sol == False:
		if (pos == 0):
		    palavrasUsadas[i] = 1
		    ordenadas.append(palavras[i])
		    sol = backtracking(palavras, palavrasUsadas, pos+1, qtd, palavras[i], ordenadas)
		    palavrasUsadas[i] = 0
		    ordenadas.pop(pos)	    
		elif (palavrasUsadas[i] == 0) and (palavras[i][0] == ultimaPalavra[-1]):
		    palavrasUsadas[i] = 1
		    ordenadas.append(palavras[i])
		    sol = backtracking(palavras, palavrasUsadas, pos+1, qtd, palavras[i], ordenadas)
		    palavrasUsadas[i] = 0
		    ordenadas.pop(pos)
    return sol

def head2tail():
    palavras = []
    ordenadas = []
    palavrasUsadas = []
    qtnd = raw_input()
    for i in range(int(qtnd)):
        palavra = raw_input()
        palavras.append(palavra)
	palavrasUsadas.append(0)
    if not (backtracking(palavras, palavrasUsadas, 0, qtnd, None, ordenadas)):
        print(-1)

head2tail()

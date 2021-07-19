from random import randint as rd
import numpy as np

anterior = [1, 2, 3, 4, 5, 7, 8, 10, 12, 17, 20, 21, 23, 24, 25]
contaJogos = 1
pacoteSeven = []
pacoteEight = []
pacoteNine = []

while contaJogos <= 12:
    novoJogo = []
    contaNumeros = 1
    while contaNumeros <= 15:
        numero = rd(1, 25)
        if numero not in novoJogo:
            novoJogo.append(numero)
            contaNumeros += 1
    
    # Valida quantos numeros repetidos do sorteio anterior
    contaAnterior = 0
    for n in novoJogo:
        for an in anterior:
            if n == an:
                contaAnterior += 1

    # Verifica se o pacote está vazio, caso esteja adiciona o primeiro jogo.
    if pacoteSeven == []:
        pacoteSeven.append(novoJogo)
        contaJogos += 1
    else:
        for jogo in pacoteSeven:
            jogo.sort()
            novoJogo.sort()

            # Verifica se existe um jogo igual dentro do pacote para poder adicionar.
            isEqual = np.array_equal(jogo, novoJogo)
            if isEqual == False:
                pacoteSeven.append(novoJogo)
                contaJogos += 1
                break            

for jogo in pacoteSeven:
    print(jogo)


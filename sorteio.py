from random import randint as rd
import numpy as np

class Sorteio:
    '''Classe para gerar os jogos'''
    contaJogos = 1
    packageSeven = []
    packageEight = []
    packageNine = []

    # Método para gerar os jogos
    @classmethod
    def gerarJogos(cls, anterior):
        while cls.contaJogos <= 12:
            novoJogo = []
            contaNumeros = 1
            while contaNumeros <= 15:
                numero = rd(1, 25)
                if numero not in novoJogo:
                    novoJogo.append(numero)
                    contaNumeros += 1

            novoJogo.sort()
            repetidos = cls.contaDezenasRepetidas(novoJogo, anterior)

            if repetidos == 7:
                # Verifica se o jogo pode ser adicionado no packageSeven.
                cls.adicionarInPakage(cls.packageSeven, novoJogo)

            elif repetidos == 8:
                # Verifica se o jogo pode ser adicionado no packageEight.
                cls.adicionarInPakage(cls.packageEight, novoJogo)

            elif repetidos == 9:
                # Verifica se o jogo pode ser adicionado no packageNine.
                cls.adicionarInPakage(cls.packageNine, novoJogo)

    # Adiciona jogo ao pacote

    @classmethod
    def adicionarInPakage(cls, package, novoJogo):
        # Verifica se o pacote está vazio, caso esteja adiciona o primeiro jogo.
        package = package
        if package == []:
            package.append(novoJogo)
            cls.contaJogos += 1
        else:
            result = cls.isEqual(novoJogo)
            if result == False:
                package.append(novoJogo)
                cls.contaJogos += 1

    # Função para verificar se o jogo é valido para adicionar no pacote.
    @classmethod
    def isEqual(cls, novoJogo) -> bool:
        resultado = True
        for jogo in cls.packageSeven:

            resultado = np.array_equal(jogo, novoJogo)

            if resultado == True:
                return resultado

        return resultado

    # Valida quantos numeros repetidos do sorteio anterior
    @classmethod
    def contaDezenasRepetidas(cls, novoJogo, anterior):
        contaAnterior = 0
        for n in novoJogo:
            for an in anterior:
                if n == an:
                    contaAnterior += 1
        return contaAnterior

    @classmethod
    def imprimir(cls, qtdRepetidos):
        if qtdRepetidos == 7:
            print('--- Jogos com sete dezenas repetidas do anterior ---')
            for jogo in cls.packageSeven:
                print(jogo)

        elif qtdRepetidos == 8:
            print('--- Jogos com oito dezenas repetidas do anterior ---')
            for jogo in cls.packageEight:
                print(jogo)

        elif qtdRepetidos == 9:
            print('--- Jogos com 9 dezenas repetidas do anterior ---')
            for jogo in cls.packageNine:
                print(jogo)

#!/usr/bin/env python3
import time

def main(cant_dados_atacante = 3,cant_dados_defensor = 3):
    resultado_absoluto = {}
    for atacante in dados(cant_dados_atacante):
        for defensor in dados(cant_dados_defensor):
            resultadillo = traducir_a_resultado(batalla_simple(atacante,defensor))
            if resultadillo in resultado_absoluto:
                resultado_absoluto[resultadillo] += 1
            else:
                resultado_absoluto[resultadillo] = 1
    print(resultado_absoluto)
    return resultado_absoluto

def print_resultados(d):
    for key in d:
        print("{0} {1:.2f}".format(key, d[key]*100/sum(d.values())))


def dados(cant_dados):
    resultados = [1]*cant_dados
    yield resultados
    while True:
        resultados = inc_dados(resultados)
        yield resultados[:]
        if resultados == [6]*cant_dados:
            break
        

def inc_dados(dados):
    dados[-1] += 1
    for i in range(1,len(dados)+1):
        if dados[-i] == 7:
            dados[-(i+1)] += 1
            dados[-i] = 1
    return dados


def batalla_simple(atacante,defensor):

    resultado = []
    atacante = ordenar_dados(atacante)
    defensor = ordenar_dados(defensor)
    for atacante_dado,defensor_dado in zip(atacante,defensor):
        if defensor_dado < atacante_dado:
            resultado.append("def")
        else:
            resultado.append("ata")
    return resultado

def traducir_a_resultado(entrada):
    perdidas_def,perdidas_ata = 0,0
    for result in entrada:
        if result == "def":
            perdidas_def += 1
        elif result == "ata":
            perdidas_ata += 1
    return str(perdidas_ata) + "x" + str(perdidas_def)

def ordenar_dados(d):
    d.sort()
    d.reverse()
    return d

if __name__=='__main__':
    main()

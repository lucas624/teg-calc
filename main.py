#!/usr/bin/env python3
import sys

def batalla_main(ejercitos_atacante,ejercitos_defensor, resultado_absoluto, probabilidades, depth = 0):
    print("-"*depth+"atacante: ", ejercitos_atacante, " defensor:", ejercitos_defensor)
    if ejercitos_atacante == 0:
        resultado_absoluto["defensor_gana"] += probabilidades
        return None
    if ejercitos_defensor == 0:
        resultado_absoluto["atacante_gana"]  += probabilidades
        return None
    resultados = {}
    cont = 0
    for atacante in dados(cant_dados(ejercitos_atacante)):
        for defensor in dados(cant_dados(ejercitos_defensor)):
            #print(atacante,defensor)
            resultadillo = traducir_a_resultado(batalla_simple(atacante,defensor))
            #print(resultadillo)
            if resultadillo in resultados:
                resultados[resultadillo] += 1
            else:
                resultados[resultadillo] = 1
    suma = sum(resultados.values())
    for key in resultados:
        resultados[key] = resultados[key]/suma
    for key in resultados:
        #print(ejercitos_atacante,"-", key[0], "==", ejercitos_atacante - int(key[0]), "con key =", key)
        #if ejercitos_defensor - int(key[2]) == -1:
        #    print("ERRORES!!!!")
        #    print(ejercitos_defensor,"-", key[2], "==", ejercitos_defensor - int(key[2]), "con key =", key, "| depth = ", depth)
        #    print(resultados)
        #    print("FIN DE ERRORES!!!!")
        batalla_main(ejercitos_atacante - int(key[0]), ejercitos_defensor - int(key[2]), resultado_absoluto, probabilidades * resultados[key], depth + 1)
    print(resultado_absoluto)
    return resultado_absoluto

def print_resultados(d):
    for key in d:
        print("atacante pierde:{} y defensor pierde:{}  {:.2f}".format(key[0], key[2], d[key]*100/sum(d.values())))

def cant_dados(ejercitos):
    if ejercitos > 2:
        return 3
    else:
        return ejercitos 

def dados(cant_dados):
    resultados = [1]*cant_dados
    yield resultados[:]
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
    batalla_main(int(sys.argv[1]), int(sys.argv[2]), {"atacante_gana":0,"defensor_gana":0}, 1)


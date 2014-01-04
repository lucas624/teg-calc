#!/usr/bin/env python3
import sys

count_returns = 0
count_iterate = 0

def calcular_probabilidades():
    resultado_absoluto = {}
    for cant_dados_atacante in range(1,4):
        for cant_dados_defensor in range(1,4):            
            resultados = {}
            for atacante in dados(cant_dados_atacante):
                for defensor in dados(cant_dados_defensor):
                    resultadillo = traducir_a_resultado(batalla_simple(atacante,defensor))
                    if resultadillo in resultados:
                        resultados[resultadillo] += 1
                    else:
                        resultados[resultadillo] = 1
            suma = sum(resultados.values())
            for key in resultados:
                resultados[key] = resultados[key]/suma
            resultado_absoluto[str(cant_dados_atacante)+"vs"+str(cant_dados_defensor)] = dict(resultados)
    return dict(resultado_absoluto)

def batalla_main(ejercitos_atacante,ejercitos_defensor, resultado_absoluto, probabilidades, depth = 0):
    print("{:.2f} {} atacante: {} defensor: {}".format(sum(resultado_absoluto.values())*100, "--"*depth, ejercitos_atacante, ejercitos_defensor))
    if ejercitos_atacante == 0:
        resultado_absoluto["defensor_gana"] += probabilidades
        return None
    if ejercitos_defensor == 0:
        resultado_absoluto["atacante_gana"]  += probabilidades
        return None
    global super_probabilidades
    resultados = super_probabilidades[str(cant_dados(ejercitos_atacante))+"vs"+str(cant_dados(ejercitos_defensor))]
    #print("atacante:",ejercitos_atacante)
    #print("defensor:",ejercitos_atacante)
    #print(resultados)
    for key in resultados:
        batalla_main(ejercitos_atacante - int(key[0]), ejercitos_defensor - int(key[2]), resultado_absoluto, probabilidades * resultados[key], depth + 1)
    #global count_returns
    #count_returns += 1
    return resultado_absoluto

def print_resultados(d):
    for key in d:
        print("atacante pierde:{} y defensor pierde:{}  {:.2f}".format(key[0], key[2], d[key]*100/sum(d.values())))

def print_resultado_absoluto(d):
    print("atacante gana :{:.2f}% y defensor gana:{:.2f}%".format(d["atacante_gana"]*100,d["defensor_gana"]*100))

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
    while True:
        try:
            index = dados.index(7)
        except ValueError:
            return dados
        dados[index]   = 1
        dados[index-1] += 1

def batalla_simple(atacante,defensor):
    #global count_iterate
    #count_iterate += 1
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
    count_returns = 0
    count_iterate = 0
    super_probabilidades = calcular_probabilidades()
    resultado = batalla_main(int(sys.argv[1]), int(sys.argv[2]), {"atacante_gana":0,"defensor_gana":0}, 1)
    print_resultado_absoluto(resultado)
    #print("cosas devueltas", count_returns)
    #print("veces entradas a la batalla simple", count_iterate)



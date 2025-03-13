#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

#repeticao do app
while True:
    area = 0
    while True:
        try:
            area = int(input('Insira a area em metros quadrados da plantacao (somente numeros):'))
            continue_inputs = True
            break
        except:
            resposta1 = int(input('O valor escolhido invalido, aperte 0 para escolher novamente e 1 para sair:'))
            if resposta1 == 1:
                continue_inputs = False
                break

    while type(area) == int and continue_inputs:
        try:
            cultura = int(input('Escolha a cultura: 1 - Batata | 2 - Morango:'))
            if cultura == 1 or cultura == 2:
                break
        except:
            resposta2 = int(input('O valor escolhido invalido, aperte 0 para escolher novamente e 1 para sair'))
            if resposta2 == 1:
                break

    print("\nDados registrados com sucesso!")
    print(f"Área: {area} m²")
    print(f"Cultura: {'Batata' if cultura == 1 else 'Morango'}")

    #Log de entrada (VETOR)
    log = []
    log.append(area)
    log.append(cultura)
    print(log)

    #calculos
    #batata 700mL/1m de fertilizante de fosfato forma da area: quadrado
    #5 ruas para pulverizar com trator
    quantidade_insumo_batata = (math.sqrt(area) * 0.7)*2
    quantidade_por_aplicacao_batata = quantidade_insumo_batata/5

    #morango 450mL/1m inseticida Organofosforado forma da area: quadrado
    #5 ruas para pulverizar com trator
    quantidade_insumo_morango = (math.sqrt(area)* 0.45)*2
    quantidade_por_aplicacao_morango = quantidade_insumo_morango/5

    #saidas precisa formatar e deixar apresentavel os valores
    print(quantidade_insumo_batata)
    print(quantidade_por_aplicacao_batata)
    print(quantidade_insumo_morango)
    print(quantidade_por_aplicacao_morango)
    
    resposta3 = int(input('aperte 0 para escokher novamente e 1 para sair'))
    if resposta3 == 1:
            break


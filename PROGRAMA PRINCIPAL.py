#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
#Log de resultados (VETOR)
logs = []
    
#Realiza a entrada de dados, efetua cálculos e retorna um dicionário com os registros.
def cadastrar_dados():
  # Entrada da área
    while True:
        try:
            area = int(input('\nInsira a area em metros quadrados da plantacao (somente números): '))
            break
        except ValueError:
            print('\nValor escolhido invalido, tente novamente')
                
    # Entrada da cultura          
    while True:
        try:
            cultura = int(input('\nEscolha a cultura: 1 - Batata | 2 - Morango: '))
            if cultura in [1,2]:
                break
        except ValueError:
            print('\nValor escolhido invalido, tente novamente')
    
    print("\nDados registrados com sucesso!")
    print(f"Área: {area} m²")
    cultura_str = "Batata" if cultura == 1 else "Morango"
    print(f"Cultura: {cultura_str}")

    #calculos
    
    #batata 5L/1m de fertilizante de fosfato forma da area: QUADRADO
    #5 ruas para pulverizar com trator
    quantidade_insumo_batata_aplicacao = (math.sqrt(area) * 5)/1000
    quantidade_insumo_batata_total = quantidade_insumo_batata_aplicacao * 5
    
    
    #morango 2.5L/1m inseticida Organofosforado forma da area: quadrado
    #5 ruas para pulverizar com trator
    quantidade_insumo_morango_aplicacao = (math.sqrt(area)* 2.5)/1000
    quantidade_insumo_morango_total = quantidade_insumo_morango_aplicacao * 5
   
    
    #saidas
    if cultura == 1:
        print(f"Quantidade insumo Batata: {quantidade_insumo_batata_total:.2f}L")
        print(f"Quantidade por aplicação Batata: {quantidade_insumo_batata_aplicacao:.2f}L")
    else:
        print(f"Quantidade insumo Morango: {quantidade_insumo_morango_total:.2f}L")
        print(f"Quantidade por aplicação Morango: {quantidade_insumo_morango_aplicacao:.2f}L")
    
     # Cria o registro como um dicionário
    registro = {
        "area": area,
        "cultura": cultura,
        "quant_insumo_batata": quantidade_insumo_batata_total,
        "quant_aplicacao_batata": quantidade_insumo_batata_aplicacao,
        "quant_insumo_morango": quantidade_insumo_morango_total,
        "quant_aplicacao_morango": quantidade_insumo_morango_aplicacao
    }
    return registro

def exibir_registros():
    if not logs:
        print("\nNenhum registro disponível.")
    else:
        print("\nRegistros acumulados:")
        for idx, reg in enumerate(logs):
            cultura_str = "Batata" if reg["cultura"] == 1 else "Morango"
            print(f"\nRegistro {idx}:")
            print(f"  Área: {reg['area']:.2f} m²")
            print(f"  Cultura: {cultura_str}")
            if  reg["cultura"] == 1:
                print(f"  Insumo Batata: {reg['quant_insumo_batata']:.2f}")
                print(f"  Aplicação Batata: {reg['quant_aplicacao_batata']:.2f}")
            else:
                print(f"  Insumo Morango: {reg['quant_insumo_morango']:.2f}")
                print(f"  Aplicação Morango: {reg['quant_aplicacao_morango']:.2f}")

def atualizar_registro():
    if not logs:
        print("\nNenhum registro para atualizar.")
        return
    try:
        idx = int(input("\nDigite o número do registro que deseja atualizar: "))
        if idx < 0 or idx >= len(logs):
            print("\nRegistro inválido.")
            return
    except ValueError:
        print("\nEntrada inválida.")
        return

    # Atualizando os dados do registro
    try:
        nova_area = int(input("\nDigite a nova área (somente números): "))
    except ValueError:
        print("\nEntrada inválida para área.")
        return

    try:
        nova_cultura = int(input("\nDigite a nova opção para cultura (1 - Batata, 2 - Morango): "))
        if nova_cultura not in [1, 2]:
            print("\nOpção inválida para cultura.")
            return
    except ValueError:
        print("\nEntrada inválida para cultura.")
        return

    # Atualiza os valores e recalcula os insumos
    logs[idx]["area"] = nova_area
    logs[idx]["cultura"] = nova_cultura
    logs[idx]["quant_insumo_batata"] = (math.sqrt(nova_area) * 5) / 1000
    logs[idx]["quant_aplicacao_batata"] = logs[idx]["quant_insumo_batata"] * 5
    logs[idx]["quant_insumo_morango"] = (math.sqrt(nova_area) * 2.5) / 1000
    logs[idx]["quant_aplicacao_morango"] = logs[idx]["quant_insumo_morango"] / 5

    print("\nRegistro atualizado com sucesso!")
    
def remover_registro():
    logs.pop(int(input("\nDigite o número do registro que deseja remover: "))) 
    
    print('\nRegistro removido!')

def main():
    """
    Menu principal para gerenciar o cadastro, exibição e atualização dos dados.
    """
    while True:
        print("\nMenu Principal:")
        print("1. Registrar novos dados")
        print("2. Exibir registros (Saída de dados)")
        print("3. Atualizar um registro")
        print("4. Remover registro")
        print("5. Sair do programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registro = cadastrar_dados()
            if registro:
                logs.append(registro)
        elif opcao == "2":
            exibir_registros()
        elif opcao == "3":
            atualizar_registro()
        elif opcao == "4":
            remover_registro()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()






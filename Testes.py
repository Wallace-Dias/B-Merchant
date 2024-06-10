from random import choice, randint


from random import randint





bag = []

loja = {'maça': randint(1,10), 'banana': randint(1, 10), 'pera': randint(1, 10), 'uva': randint(1,10)}



while True:
    for index, (k, v) in enumerate(loja.items(), start=1):
        print(f"{index}:{k}: {v}")
    
    opc = int(input("\nOPC: "))
    if opc == 0:
        break

    elif 1 <= opc <= len(loja):
        bag.append(loja.items()[opc -1])
        #bag.append(item)
    
    elif opc == 999:
        print(bag)
    












""" barato = []
caro = []

loja = {'maçã': randint(1, 10), 'banana': randint(1, 10), 'pera': randint(1, 10), 'uva': randint(1, 10)}

while True:
    print("Itens na loja:")
    for index, (k, v) in enumerate(loja.items(), start=1):
        print(f"{index}. {k}: {v}")

    print("\nDigite o número do item para selecionar ou 0 para sair:")
    opc = int(input("OPC: "))

    if opc == 0:
        break
    elif 1 <= opc <= len(loja):
        item_selecionado = list(loja.items())[opc - 1]
        k, v = item_selecionado
        print(f"Item selecionado: {k}: {v}\n")
    else:
        print("Opção inválida. Tente novamente.\n")



 """
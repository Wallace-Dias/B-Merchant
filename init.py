from random import choice, randint
from time import sleep
print('='*50)
print("B-Merchant".center(50))
print('='*50)

gold = 100
player = []
itens = []
loja = {'Maçã': randint(1, 100), 'galho': randint(1, 100), 'Poção': randint(1,100)}
#print(choice(itens))

print(f"Bem vindo Mercador! Voce tem atualmente {gold} de Gold\n O que gostaria de fazer?\n")
sleep(1)

nome = 'Wallace'
lvl = 1
player.append(nome)
player.append(lvl)


#menu
print("[1] - Status \n[2] - Itens \n[3] - Explorar")

while True:
    opc = int(input("Opção: "))
    if opc == 1:
        print("Status".center(50))
        print(f'Nome: {player[0]} \nLvl: {player[1]}')

        print("Itens".center(50))
        for index, i in enumerate (itens, start=1):
            print(f'{index}: {i}')
        print('='*50)
        
    if opc == 3:
        print("Você se encontrou com um mercador, o que gostaria de fazer?")
        print("[1] - Comprar \n[2] - Vender")
        opc = int(input("Opção: "))
        if opc == 1:
            cont = 0
            for index, c in enumerate(loja, start = 1):
                print(f'{index}: {c}')
                cont +=1
                if cont == len(loja):
                    buy = int(input("Buy: "))
                    if 1 <= buy <= len(loja):#and gold <= loja.values() :
                        item_comprado = loja[buy - 1]
                        itens.append(item_comprado)
                        loja.remove(item_comprado)
    
    if opc == 5:
        print("Saindo . . .")
        sleep(1)
        print("="*50)
        print("Programa Encerrado".center(50))
        print("="*50)
        break
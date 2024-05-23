from random import choice
from time import sleep
print('='*50)
print("B-Merchant".center(50))
print('='*50)

gold = 0
player = []
itens = []
loja = ['Maçã', 'galho', 'Poção']
#print(choice(itens))

print(f"Bem vindo Mercador! Voce tem atualmente {gold} de Gold\n O que gostaria de fazer?\n")
sleep(1)

#menu
print("[1] - Status \n[2] - Itens \n[3] - Explorar")

while True:
    opc = int(input("Opção: "))
    if opc == 1:
        print("Status".center(50))
        print('='*50)
        
    
    if opc == 5:
        print("Saindo . . .")
        sleep(1)
        print("="*50)
        print("Programa Encerrado".center(50))
        print("="*50)
        break
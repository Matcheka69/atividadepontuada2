import os
os.system("clear")


soma=0
while True:
    print("""
Código \t Nome \t\t\t Valor
      
1 \t Picanha \t\t R$75,00
2 \t Fraldinha \t\t R$53,00
3 \t Ancho argentinon\t R$73,00
4 \t Maminha \t\t R$60,00
5 \t Linguiça \t\t R$35,00
6 \t Sorvete \t\t R$17,00
7 \t Petit gateau \t\t R$23,00
0 \t Encerrar programa  \t   
""")

    opçao = int(input("Digite o código do prato que deseja: "))
    match opçao:
        case 1:
            print("Seu prato foi picanha.")
            valor= 75,00
        case 2:
            print("Seu prato foi fraldinha.")
            valor=53,00
        case 3:
            print("Seu prato foi ancho argentino.")
            valor= 73,00
        case 4:
            print("Seu prato foi maminha.")
            valor=60,00
        case 5:
            print("Seu prato foi linguiça.")
            valor=35,00
        case 6: 
            print ("Seu prato foi sorvete.")
            valor= 17,00
        case 7:
            print("Seu prato foi petit gateau.")
            valor= 23,00
    
        case 0: exit ("Programa finalizado.")

        case _:
            print("Opção invalida, digite um código válido.")
            

    soma += valor
    resposta = (input("Deseja adicionar mais algum pedido? \nDigite 'S' ou '0' para sair: ")).lower()

    if resposta == "0":
        print(f"A soma é {soma}")
        break   

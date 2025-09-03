inteira = 30
meia = 15
estudante = meia
valor = 0
valor_total = 0
pedidos = " "


print("-=-=-=-=-= Sistema Cine Ágil =-=-=-=-=--=-=- \n")


while True:

    print("\nPara encerrar sua compra digite -1")
    print()
    idade =  int(input("informe sua idade: "))
   
    if idade == -1:
        break

    elif idade >= 12:
        est = input("É estudante? Digite S para sim e N para não: ").upper()
        if est == "N":
            valor = inteira
            print(f"\nPreço normal: {inteira:.2f},")
            print("Ingresso Normal adicionado!")
            valor_total += valor
        else:
            valor = meia
            print(f"\nPreço Estudante: R${meia:.2f}")
            print("Ingresso Estudante adicionado!")
            valor_total += valor
    
    else:
        
        valor = meia
        print(f"\nPreço infantil: R${meia:.2f}")
        print("Ingresso Infantil adicionado!")

        valor_total += valor


print(f"\nO valor total dos seus ingressos R$ {valor_total}")
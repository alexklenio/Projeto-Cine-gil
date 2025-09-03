inteira = 30
meia = 15
estudante = meia
valor = 0
valor_total = 0
total_ingressos = 0


print("\n-=-=-=-=-= Sistema Cine Ágil =-=-=-=-=--=-=- \n")


ingressos = int(input("Quantos ingressos você deseja comprar"))

for ingresso in range(ingressos):
    print("\nPara encerrar sua compra digite -1")
    print()
    idade =  int(input("informe sua idade: "))
   
 

    if idade >= 12:
            est = input("É estudante? Digite 'S' para sim e 'N' para não: ").upper().strip()
            if est == "N":
                valor = inteira
                print(f"\nPreço normal: {inteira:.2f},")
                print("Ingresso Normal adicionado!")
               

            else:
                valor = meia
                print(f"\nPreço Estudante: R${meia:.2f}")
                print("Ingresso Estudante adicionado!")
                
    else:
    
        valor = meia
        print(f"\nPreço infantil: R${meia:.2f}")
        print("Ingresso Infantil adicionado!")
           
          
    valor_total += valor
    total_ingressos +=1

    

print(f"\nO valor total dos seus ingressos é R$ {valor_total:.2f}")
print(f"Total de ingressos comprados: {total_ingressos}\n")
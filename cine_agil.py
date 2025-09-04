# --- INICIALIZAÇÃO DE VARIÁVEIS ---
# Define os valores dos ingressos.
inteira = 30
meia = 15
estudante = meia  # A variável 'estudante' recebe o mesmo valor de 'meia', facilitando a leitura do código.
valor = 0  # Variável temporária para armazenar o valor do ingresso atual, antes de ser somado.
valor_total = 0  # Variável para acumular o custo total de todos os ingressos.
total_ingressos = 0  # Contador para o número de ingressos comprados.

# Exibe uma mensagem de boas-vindas ao sistema.
print("\n-=-=-=-=-= Sistema Cine Ágil =-=-=-=-=--=-=- \n")

# --- COLETA DE INFORMAÇÕES INICIAIS ---
# Solicita ao usuário a quantidade de ingressos que ele deseja comprar.
qtd_ingressos = int(input("Quantos ingressos você deseja comprar? "))

# --- LOOP PRINCIPAL ---
# O loop 'for' é usado para iterar um número fixo de vezes, determinado por 'qtd_ingressos'.
# Cada iteração (repetição) do loop representa a compra de um ingresso.
for ingresso in range(qtd_ingressos):
    
    # Solicita a idade do cliente.
    # Esta informação é crucial para determinar o tipo de ingresso.
    idade = int(input("Informe a idade para o ingresso #" + str(ingresso + 1) + ": "))
    
    # --- LÓGICA DE VALOR DO INGRESSO ---
    # Verifica se a idade é maior ou igual a 12 anos.
    if idade >= 12:
        # Se for, pergunta se a pessoa é estudante.
        est = input("É estudante ( S / N) ").upper().strip()
        
        # Se a resposta for 'N' (Não), o valor é o da inteira.
        if est == "N":
            valor = inteira
            print(f"\nPreço normal: R${inteira:.2f}")
            print("Ingresso Normal adicionado!")
        # Se a resposta for diferente de 'N' (ex: 'S', 's', 'Estudante', etc), o valor é a meia-entrada.
        else:
            valor = meia
            print(f"\nPreço Estudante: R${meia:.2f}")
            print("Ingresso Estudante adicionado!")
            
    # Se a idade for menor que 12 anos, o valor do ingresso é sempre a meia-entrada (infantil).
    else:
        valor = meia
        print(f"\nPreço infantil: R${meia:.2f}")
        print("Ingresso Infantil adicionado!")
           
    # --- ATUALIZAÇÃO DOS TOTAIS ---
    # Ao final de cada iteração, o valor do ingresso atual é somado ao valor total.
    valor_total += valor
    # O contador de ingressos é incrementado.
    total_ingressos += 1
    
# --- RESULTADOS FINAIS ---
# Após o loop 'for' terminar (todos os ingressos terem sido processados),
# o programa exibe o valor total da compra e a quantidade de ingressos.
print(f"\nO valor total dos seus ingressos é R$ {valor_total:.2f}")
print(f"Total de ingressos comprados: {total_ingressos}\n")
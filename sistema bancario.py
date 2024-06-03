MENSAGEM_FINAL = " Obrigado por utilizar nossos serviços! ".center(60, "*")
OPCAO_INVALIDA = " A opção selecionada é inválida! ".center(60, "*")
FINALIZAR = " Operação finalizada! ".center(60, "*")
LIMITE_SAQUE = 500
QUANTIDADE_LIMITE_SAQUE = 3
MENSAGEM_OPCAO_GERAL = "Digite {E} para confirmar, {C} para corrigir e informar um novo valor ou {S} para finalizar a operação.\n"

saldo = 0
quantidade_saque = 0
extrato = ""
valor_total_sacado = 0
opcao_corrigir_deposito, opcao_corrigir_saque, limite_excedido = False, False, False

depositos, saques = [], []

opcao_geral = {"E":"E", "C":"C", "S":"S"}
menu = """
Escolha uma das opções abaixo\n:
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> \n"""

def get_opcao():
    if limite_excedido:
        return "q"
    
    elif opcao_corrigir_deposito:
        return "d"

    elif opcao_corrigir_saque:
        return "s"

    else:
        return input(menu)

def validar_regras_saque(valor):
    if saldo <= 0:
        print(f"Seu saldo de R$ {saldo} não lhe permite efetuar um saque!\n")
        return False
    
    elif valor_total_sacado >= LIMITE_SAQUE * QUANTIDADE_LIMITE_SAQUE:
        print(f"Você atingiu o valor limite diário no valor de {LIMITE_SAQUE * QUANTIDADE_LIMITE_SAQUE} e não poderá mais efetuar novos saques!\nEscolha outra operação.")
        return False
    
    elif valor_total_sacado + valor > LIMITE_SAQUE * QUANTIDADE_LIMITE_SAQUE:
        print(f"Você atingirá o valor limite diário no valor de {LIMITE_SAQUE * QUANTIDADE_LIMITE_SAQUE}! Escolha um valor menor.\n")
        return False
    
    elif valor > LIMITE_SAQUE:
        print(f"Não é possível sacar uma valor maior que {LIMITE_SAQUE}! Escolha um valor menor.\n")
        return False
    
    elif quantidade_saque >= QUANTIDADE_LIMITE_SAQUE:
        print("Você atingiu o número máximo de saques diários!\nEscolha outra operação.")
        return False
    
    return True

def getBye():
    print(f"{FINALIZAR}\n{MENSAGEM_FINAL}")

while True:
    
    opcao = get_opcao().lower()

    if opcao == "d":
        opcao_corrigir_deposito = False
        valor = float(input("Digite o valor que deseja depositar:\n"))
        if valor > 0:
            print(f"Você informou o valor {valor}!\n")
            nova_opcao = input(MENSAGEM_OPCAO_GERAL.format(**opcao_geral)).upper()
            
            if nova_opcao == opcao_geral.get("E"):
                print(f"Depósito no valor de {valor} foi efetivado!\n")
                depositos.append(valor)
                saldo += valor

            elif nova_opcao == opcao_geral.get("C"):
                opcao_corrigir_deposito = True
                continue

            elif nova_opcao == opcao_geral.get("S"):
                getBye()
                break

            else:
                print(f"{OPCAO_INVALIDA}")
                getBye()
                break

        else:
            print(f"Você informou o valor {valor}!\n Somente é permitido depositar um valor maior que zero.\n")
            getBye()
            break

    elif opcao == "s":
        opcao_corrigir_saque = False
        valor_total_sacado = 0
        for valor in saques:
            valor_total_sacado += float(valor)

        if validar_regras_saque(valor_total_sacado):
            valor = float(input("Digite o valor que deseja sacar:\n"))
            if validar_regras_saque(valor):
                print(f"Você informou o valor {valor}!\n")
                nova_opcao = input(MENSAGEM_OPCAO_GERAL.format(**opcao_geral)).upper()
                
                if nova_opcao == opcao_geral.get("E"):
                    if validar_regras_saque(valor):
                        print(f"Saque no valor de {valor} foi efetivado!\n")
                        saques.append(valor)
                        quantidade_saque += 1
                        saldo -= valor

                    else:
                        limite_excedido = True

                elif nova_opcao == opcao_geral.get("C"):
                    opcao_corrigir_saque = True
                    continue

                elif nova_opcao == opcao_geral.get("S"):
                    getBye()
                    break

                else:
                    print(f"{OPCAO_INVALIDA}")
                    getBye()
                    break
            else:
                opcao_corrigir_saque = True


    elif opcao == "e":
        cabecalho_rodape = " Extrato ".center(60, "*")
        if not depositos:
            print("Sem movimentações para serem exibidas no extrato!\n")
            
        else:
            print(cabecalho_rodape)
            for valor in depositos:
                print(f"Deposito no valor de {valor:.2f}\n")

            for valor in saques:
                print(f"Saque no valor de {valor:.2f}\n")

            print(f"\nSaldo da conta: {saldo:.2f}")
            print(cabecalho_rodape)

    elif opcao == "q":
        getBye()
        break

    else:
        print(f" Selecione uma das seguintes opções: {menu}")
        
        
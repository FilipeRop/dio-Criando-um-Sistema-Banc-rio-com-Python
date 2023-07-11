menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ''
numeroSaques = 0
limiteSaques = 3

while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
        
        else:
            print('Operação falhou! Valor inválido.')
        
    elif opcao.lower() == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeuSaldo = valor > saldo
        excedeuLimite = valor > limite
        excedeuSaques = numeroSaques >= limiteSaques

        if excedeuSaldo:
            print('Operação Falhou!')
            print('Saldo Insuficiente!')

        elif excedeuLimite:
            print('Operação Falhou!')
            print('Valor do saque excede o limite!')

        elif excedeuSaques:
            print('Operação Falhou!')
            print('Número máximo de saques foi atingido!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numeroSaques += 1

        else:
            print('Operação Falhou! Valor inválido.')
    
    elif opcao.lower() == 'e':
        print('\n----------Extrato----------')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('-'*28)

    elif opcao.lower() == 'q':
        break

    else:
        print('Operação inválida!')
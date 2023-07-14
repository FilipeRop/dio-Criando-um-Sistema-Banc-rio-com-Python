import textwrap

def menu():
    menu = """
    ----------MENU----------
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [l] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        print('\nDepósito Realizado com Sucesso')
    else:
        print('\nOperação falhou!')
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):

    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaque = numeroSaques >= limiteSaques

    if excedeuSaldo:
        print('Operação Falhou! Saldo insuficiente.')
    elif excedeuLimite:
        print('Operação falhou! O valor excede o limite diário.')
    elif excedeuSaque:
        print('Operação Falhou! Execeu o número máximo de saques.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}'
        numeroSaques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Operação falhou!')
    
    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print('EXTRATO')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}')

def criarUsuario(usuario):
    cpf = input('Informe o seu CPF (apenas números): ')
    usuario = filtrarUsuario(cpf, usuario)

    if usuario:
        print('CPF já cadastrado!')
        return
    
    nome = input('Nome completo: ')
    dataNascimento = input('Data de nascimento (dd-mm-aaaa): ')
    endereco = input('Endereço: (logradouro, N°, Bairro, Cidade, UF)')

    usuario.append({'nome': nome, 'dataNascimento': dataNascimento, 'cpf': cpf, 'endereco':endereco})

    print('Usuario criado')

def filtrarUsuario(cpf, usuario):
    usuarioFiltrado = [user for user in usuario if user['cpf'] == cpf]
    return usuarioFiltrado[0] if usuarioFiltrado else None

def criarConta(agencia, numeroConta, usuario):
    cpf = input('Informe o seu CPF: ')
    user = filtrarUsuario(cpf, usuario)

    if user:
        print('Conta criada')
        return {'agencia':agencia, 'numeroConta':numeroConta, 'usuario': user}
    
    print('Usuário não encontrado!')

def listarContas(contas):

    for conta in contas:
        linha = f"""
        Agência; {conta['agencia']}
        C/C: {conta['numeroConta']}
        Titular: {conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))
            

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numeroSaques = 0
    limiteSaques = 3
    usuario = []
    contas = []
    agencia = '0001'

    while True:

        opcao = menu()

        if opcao.lower() == 'd':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao.lower() == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numeroSaques = numeroSaques,
                limiteSaques = limiteSaques
            )
        
        elif opcao.lower() == 'e':
            exibirExtrato(saldo, extrato=extrato)

        elif opcao.lower() == 'nu':
            criarUsuario(usuario)
        
        elif opcao.lower() == 'nc':
            numeroConta = len(contas) + 1
            conta = criarConta(agencia, numeroConta, usuario)

            if conta:
                contas.append(conta)

        elif opcao.lower() == 'l':
            listarContas(contas)

        elif opcao.lower() == 'q':
            break

        else:
            print('Operação inválida!')

main()
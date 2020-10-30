def calculadora_simples():
    operacao = input('''
Por favor digite uma das 4 operacoes matematicas, para completarmos o resultado:
+ para soma
- para subtração
* for multiplicação
/ for divisão
''')

    numero_1 = int(input('Entre com o primeiro numero: '))
    numero_2 = int(input('Entre com o segundo numero: '))

    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_1_2)

    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operacao == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(numero_1 / numero_2)

    else:
        print('voce digitou um operador invalido, por favor rode o programa novamente.')

    # Adicionando a funcao novamente() para a funcao da calculadora_simpleste()
    novamente()

def novamente():
    calc_novamente = input('''Voce deseja fazer novo cálculo?
Digite S for SIM or N for NAO.
''')

    if calc_novamente.upper() == 'S':
        calculadora_simples()
    elif calc_novamente.upper() == 'N':
        print('Obrigado.')
    else:
        novamente()

calculadora_simples()
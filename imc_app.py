# entrada de dados 

from ast import Continue


while True:
    nome = str(input('Informe seu nome:'))
    peso = str(input('Informe seu peso:')).replace(',','.')
    altura = str(input('Informe sua altura:')).replace(',','.')

    # conversão para float
    peso = float(peso)
    altura = float(altura)

    # calcule imc
    imc = peso/(altura ** 2)

    # mostrar o valor do imc
    print(f'IMC de {nome}: {imc:,.2f}.')

    # condicionais
    if imc >40:
        print(f'O seu imc é obesidade grau 3.')
    elif imc >=35:
        print(f'O seu imc é obesidade grau 2.')
    elif imc >=30:
        print(f'O seu imc é obesidade grau 1.')
    elif imc >=25:
        print(f'O seu imc é sobrepeso.')
    elif imc >=20:
        print(f'O seu imc é peso normal.')
    else:
        print(f'Você está abaixo do peso.')

    # verificar se o usuário deseja continuar
    Continuar = input('Deseja continuar (s/n)?').lower

    # verificar a opção escolhida pelo usuário
    if Continuar == 's':
        continue
    else:
        break

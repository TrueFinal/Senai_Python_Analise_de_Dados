def imc_funcionarios ():
    for i in range(1, 11):
        altura = float(input(f'Altura {i}:'))
        peso = float(input(f'Peso {i}:'))
        if altura == 0 or peso == 0:
            print('Nenhum dos valores podem ser zero (0)!')
            return
        imc = peso / (altura**2)
        print(f'Seu IMC é {i}: {imc:2f}')

imc_funcionarios()
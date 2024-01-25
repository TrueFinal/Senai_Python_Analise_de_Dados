def imcs(peso, altura):
    if (peso==0) or (altura==0):
        print('Nenhum dos valores pode ser zero (0)!')
    else:
        imc = peso/(altura**2)
        print('Este é seu IMC:',imc)

imcs(60, 1.73)
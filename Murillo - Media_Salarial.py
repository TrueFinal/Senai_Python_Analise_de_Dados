def media_salarial():
    acumulador = 0,
    contador = 0,
    atemedia = 0,
    acimamedia = 0,
    while True:
        salario = int(input("DIgite o valor do salário ou zero para sair:"))
        if salario == 0:
            if contador>0:
                media = acumulador / contador
            print("----------------------------------------------------------")
            print("O solário médio é:", media)
            print("----------------------------------------------------------")
            while True:
                salario = int(input("Digite o valor do salario ou zero para sair:"))
                if salario == 0:
                    print(atemedia, "Ganham até a média salárial")
                    print(acimamedia, "Ganham acima da média salárial")
                    break
                else:
                    if salario<=media:
                        atemedia +=1
                    else:
                        acimamedia +=1
            break
        else:
            acumulador += salario
            contador += 1
def media_altura():
    maioraltura = -1
    menoraltura = 1000
    contador_de_homens = 0
    contador_de_mulheres = 0
    soma_altura_mulheres = 0
    x = 1
    while x <11:
        altura = int(input("Informe a altura da pessoa:"))
        sexo = str(input("Informe o sexo da pessoa (M ou F):"))
        if altura > maioraltura:
            maioraltura = altura
        if altura < menoraltura:
            menoraltura = altura
        if sexo == "M":
            contador_de_homens +=1
        else:
            contador_de_mulheres +=1
            contador_de_mulheres += altura
        x += 1
        if x == 11:
            print("-------------------------------------------------------------")
            print("A maior altura do grupo é:", maioraltura)
            print("A menos altura do grupo é:", menoraltura)
            print("-------------------------------------------------------------")
            if contador_de_mulheres > 0:
                media = soma_altura_mulheres / contador_de_mulheres
                print("A média de altura das mulheres é", media)
                print("---------------------------------------------------------")
            break

media_altura()
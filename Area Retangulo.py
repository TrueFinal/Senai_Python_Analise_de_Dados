def area_retangulo(b, h):
    if (b==0) or (h==0):
        print('Nenhum dos números pode ser zero (0)!')
    else:
        if b==h:
            print('Os valores do lado e altura do retângulo não podem ser iguais!')
        else:
            area = b*h
            print('Esta é a área do retângulo:',area)

area_retangulo(10, 0)
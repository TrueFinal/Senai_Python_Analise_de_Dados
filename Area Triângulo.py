def area_circulo(b, h):
    if (b==0) or (h==0):
        print('Nenhum dos valores pode ser zero!')
    else:
        area = b*h/2
        print('Esta é a área do triângulo:',area)

area_circulo(9, 3)
def area_circulo(r):
    pi = 3.1416
    if r==0:
        print('O valor do raio do círculo não pode ser zero (0)!')
    else:
        area = pi*(r**2)
        print('Esta é a área do círculo:',area)

area_circulo(3)
def area_quadrado(l1, l2):
        if (l1==0) or (l2==0):
            print('Nenhum dos valores pode ser zero (0)!')
        else:
            if l1 != l2:
                print('Os valores dos lados do quadrado devem ser iguais!')
            else:
                area = l1*l2
                print('Esta é a área do quadrado:',area)

area_quadrado(10, 10)
def area_t (h, b):
    while True:
        if h>0:
            if b>0:
                area = h*b/2
                print('Esta é a área do triângulo:',area)
            else:
                print('Nenhum dos valores poder ser zero (0)!')
            break
            
area_t(300.25, 10.000)
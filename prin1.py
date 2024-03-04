if __name__ == '__main__':
    print('Por favor ingresa 3 enteros')
    a = int(input('1er numero: '))
    while a < 0:
        print('El numero no es entero positivo')
        a = int(input('1er numero: '))
    b = int(input('2er numero: '))
    while b < 0:
        print('El numero no es entero positivo')
        a = int(input('2er numero: '))
    c = int(input('3er numero: '))
    while c < 0:
        print('El numero no es entero positivo')
        a = int(input('3er numero: '))
    
    print(f'La suma de los numeros es {a + b + c}') 
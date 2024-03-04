if __name__ == '__main__':
    matrix = [0,0,0,0,0,0,0,0]
    meanOdd = 0
    meanEven = 0
    def addPos(value):
        try:
            value = int(value)
            global meanOdd
            global meanEven
            x = 1
            if not value > 0:
                return
            else:
                matrix[0] += x
                if not value % 2 == 0:
                    matrix[1] += x
                    meanOdd = mean(meanOdd, value)
                    matrix[3] = meanOdd
                elif value % 2 == 0:
                    matrix[2] += x
                    meanEven = mean(meanEven, value)
                    matrix[4] = meanEven
                    
                if value < 10:
                    matrix[5] += x
                elif 20 <= value <= 50:
                    matrix[6] += x
                elif value > 100:
                    matrix[7] += x
                addPos(int(input('Ingresa un numero ')))
        except ValueError:
            print("Numero no valido")
            addPos(input('Ingresa un numero '))

                   
    def mean(prevMean, x):
        if not x == 0:
            return (x + prevMean) / 2 if prevMean != 0 else x
    
    addPos(input('Ingresa un numero '))
    print(f'Total de numeros agregados: {matrix[0]} ')
    print(f'La cantidad de numeros impares son {matrix[1]} ')
    print(f'la cantidad de numeros pares son {matrix[2]} ')
    print(f'El promedio de los numeros impares es {matrix[3]} ')
    print(f'El promedio de los numeros pares es {matrix[4]} ')
    print(f'Hay {matrix[5]} valores menores que 10')
    print(f'Hay {matrix[6]} valores entre 20 y 50')
    print(f'Hay {matrix[7]} valores mayores de 100')

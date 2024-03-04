if __name__ == '__main__':
    matrix = []
    case = [0,0,0,0,0,0]
    def rgtrCamper(i):
        i += 1
        stdn = []
        stdn.append(input(f'nombre del estudiante {i}: ')) 
        stdn.append(input('edad del estudiante: '))
        height = float(input('altura del estudiante: '))
        while height < 0:
            print('El valor no es positivo')
            height = float(input('altura del estudiante: '))
        mass = float(input('peso del estudiante: '))
        while mass < 0:
            print('El valor no es positivo')
            mass = float(input('altura del estudiante: '))
        stdn.append(float(mass)/(float(height)**2))
        if stdn[2] < 18.5:
            stdn.append(-1)
        elif (stdn[2] >= 18.5) and (stdn[2] < 24.9):
            stdn.append(0)
        elif (stdn[2] >= 25) and (stdn[2] < 29.9):
            stdn.append(1)
        elif (stdn[2] >= 30) and (stdn[2] < 34.9):
            stdn.append(2)
        elif (stdn[2] >= 35)and (stdn[2] < 39.9):
            stdn.append(3)
        elif stdn[2] >= 40:
            stdn.append(4)
        matrix.append(stdn)

    
    def addIMC(i):
        category = case
        imc = matrix[i-1][3] 
        if imc == -1:
            case[0] = category[0] + 1
        elif imc == 0:
            case[1] = category[1] + 1
        elif imc == 1:
            case[2] = category[2] + 1
        elif imc == 2:
            case[3] = category[3] + 1
        elif imc == 3:
            case[4] = category[4] + 1
        elif imc == 4:
            case[5] = category[5] + 1
    
    for i in range(3):
        rgtrCamper(i)
    for i in range(3):
        addIMC(i)
    print(f'El numero de estudiantes por debajo del peso ideal es {case[0]}')
    print(f'El numero de estudiantes en peso saludable es {case[1]}')
    print(f'El numero de estudiantes con sobrepeso es {case[2]}')
    print(f'El numero de estudiantes con obesidad I {case[3]}')
    print(f'El numero de estudiantes con obesidad II {case[4]}')
    print(f'El numero de estudiantes con obesidad III {case[5]}')



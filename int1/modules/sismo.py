matrix = []
meanV = 0
cate = ''
def rgstCty():
    matrix.append([input(' ingrese el nombre de la ciudad ')])
    if len(matrix) > 0:
        for i in range(len(matrix[0])-1):
            matrix[len(matrix)-1].append(input(f'Ingrese la escala del sismo N°{i+1} para la ciudad {matrix[len(matrix)-1][0]} '))

def rgstSsm():
    for i in range(len(matrix)):
        matrix[i].append(input(f'Ingrese la escala del sismo para la ciudad {matrix[i][0]} '))
def srchSsm():
    print(matrix)
    x = input('Ingrese el nombre de la ciudad ')
    for i in range(len(matrix)):
        if x in matrix[i]:
            index = matrix[i].index(x)
            print(matrix[i])

def evalCty():
    global meanV
    global cate
    for i in range(len(matrix)):
        for j in range(len(matrix[0])-1):
                meanV = mean(meanV, float(matrix[i][j+1]))
        cate = risk(meanV)
        print(f'El promedio de la ciudad {matrix[i][0]} es de {meanV} siendo de categoria {cate} ')

def mean(prevMean, x):
        if not x == 0:
            return (x + prevMean) / 2 if prevMean != 0 else x
    

def risk(x):
    if x < 2.5:
        return('Amarillo (Sin aiesgo) ')
    elif 2.6 <= x <= 4.5:
        return('Naranja (Riesgo medio) ')
    else:
         return('Rojo (Riesgo alto) ')
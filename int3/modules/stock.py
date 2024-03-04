
from tabulate import tabulate
matrix = []
colums = ['Codigo','Nombre','Stocks','valor compra','valor venta','stock minimo','stock maximo','nombre proveedor']
log = {}
moment = []

def rgstPrdcs():
    x = 0
    hold = []
    code = input('Ingresa el codigo del producto ')
    hold.append(code)
    hold.append(input('Ingresa el nombre del producto '))
    hold.append(float(input('Ingresa el numero de stocks ')))
    hold.append(float(input('Ingresa el valor de compra del producto ')))
    hold.append(float(input('Ingresa el valor de venta del producto ')))
    hold.append(float(input('Ingresa el stock minimo permitido ')))
    hold.append(float(input('Ingresa el stock maximo permitido ')))
    hold.append(input('Ingresa el nombre del proveedor del producto '))
    matrix.append(hold)
    log.update({code: []})
    moment.append(matrix[x][2])
    moment.append(matrix[x][3])
    log[matrix[x][0]].append(moment)
    x += 1
    
def show():
    print(tabulate(matrix, headers=colums))
    
def updtStk():
    x = 0
    y = 0
    name = input('Codigo del stock que deseas actualizar ')
    for i in range(len(matrix)):
        if name in matrix[i]:
            op = input('Desea comprar o vender? ')
            if op == 'comprar' or 'Comprar':
                x = float(input('Ingrese el numero de stocks a comprar '))
                y = matrix[i][2]
                if matrix[i][5] < x + y < matrix[i][6]: 
                    matrix[i][2] += x
                    moment.append(x)
                    moment.append(matrix[i][3])
                    log[matrix[i][0]].append(moment)
                    print('si compra')
                    break
                else:
                    pass
            elif op == 'vender' or 'Vender':
                x = float(input('Ingrese el numero de stocks a vender '))
                y = matrix[i][2]
                if matrix[i][5] < y - x < matrix[i][6]:
                    matrix[i][2] -= x
                    print('si venta')
                    break
                else:
                    pass
            else:
                print('respuesta no identificada ')
                updtStk()
        else:
            print('El codigo no es correcto ')
            updtStk()
    
def updtVl():
    for i in range(len(matrix)):
        x = float(input(f'Valor de compra para el producto {matrix[i][1]} '))
        matrix[i][3] = x
        y = float(input(f'Valor de venta para el producto {matrix[i][1]} '))
        matrix[i][4] = y

def shwCrt():
    crt = float(input('Ingresa el limite minimo de stocks estables '))
    whole = []
    product = []
    for i in range(len(matrix)):
        product = []
        if matrix[i][2] < crt:
             product.append(matrix[i][0])
             product.append(matrix[i][1])
             product.append(matrix[i][2])
             whole.append(product)
        else:
            pass
    print(tabulate(whole, headers=['Codigo','Nombre','Numero de Stocks']))
    
def calcPtnc():
    global x
    global y
    global z
    global w
    x = 0
    y = 0
    z = 0 
    w = 0
    for code, transactions in log.items():
        for transaction in transactions:
            x = transaction[0] * transaction[1]
            y += x
            z += transaction[0]
        w = y / z
        print(f'La ganancia potencial de {code} es de {w} USD')
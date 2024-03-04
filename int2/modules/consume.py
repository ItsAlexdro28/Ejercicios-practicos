from tabulate import tabulate
matrix = []
blueprint = {}
total = {}
def rgstDpncy():
    blueprint = {
    'dep': '',
    'CnsmStndr': 0,
    'CnsmVhcl': [],
    'CnsmDsptv': []
}
    dependency = input('Nombre de la dependencia: ')
    hashMap = blueprint
    hashMap['dep'] = dependency
    matrix.append(hashMap)
    print(matrix)

def rgstCnsm(idx, id):
    id = int(id)
    match idx:
        case 1:
            x = float(input('Ingresa el consumo de kWh mensual '))
            y = 0.374
            matrix[id-1]['CnsmStndr'] = x * y
        case 2:
            z = int(input('Cuantos vehiculos vas a ingresar? '))
            for i in range(z):
                x = float(input('Ingresa los kilometros recorridos'))
                y = 0.374
                matrix[id-1]['CnsmVhcl'].append(x * y)
        case 3:
            z = int(input('Cuantos diferentes dispositivos vas a ingresar? '))
            for i in range(z):
                w = float(input('cuantos dispositivos hay para este tipo? '))
                x = float(input('Ingresa la potencia del dispositivo en W (watts)'))
                y = float(input('Ingresa el tiempo de uso en horas mensual'))
                matrix[id-1]['CnsmDsptv'].append(((x * y)/1000 * w) * 0.374)
        case _ :
            print("nooo")         

#0.374

def lkCO2():
    global total
    total = {}
    x = 0
    for i in range(len(matrix)):
        x = 0
        x += matrix[i]['CnsmStndr']         
        for j in range(len(matrix[i]['CnsmVhcl'])):
            x += matrix[i]['CnsmVhcl']     
        for j in range(len(matrix[i]['CnsmDsptv'])):
            x += matrix[i]['CnsmDsptv'][j]
        
        total.update({matrix[i]['dep']: x} )
    print(total)  

def hghstCnsm():
    highest = 0
    highestName = ''
    for v, k in total.items():
        if k > highest:
            highest = k
            highestName = v
    print(f'La dependencia con mas consumo fue {highestName} con {highest} tCO2eq/MWh')

def show():
    for i in range(len(matrix)):
        value = matrix[i]['dep']
        print(f'{i+1}. {value}')
    x = float(input("ingresa el ID de la dependencia "))
    if x > len(matrix):
        print('El ID no existe')
        show()
    return x

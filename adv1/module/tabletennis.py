from tabulate import tabulate
scores = {
    'novato': [],
    'intermedio': [],
    'avanzado': []
}
# [id, name, age, jugados, ganados, perdidos, empatados, favor, total]
def rgstPlyr():
    hold = []
    hold.append(int(input('Ingresa el codigo del participante ')))
    hold.append(input('Ingresa el nombre del participante '))
    hold.append(int(input('Ingresa la edad del participante ')))
    for i in range(6):
        x = 0
        hold.append(x)
    age = hold[2]
    if age == 15 or age == 16:
        scores['novato'].append(hold)
    elif age == 17 or age == 18 or age == 19 or age == 20:
        scores['intermedio'].append(hold)
    elif age >= 21:
        scores['avanzado'].append(hold)
    else:
        print('El participante no tiene la edad minima ')
        rgstPlyr()

def rgstMtch():
    cat = input('Ingresa la categoria novato, intermedio o avanzado: ').lower()
    if len(scores[cat]) < 5:
        print(f'La categoria {cat} todavia no cumple con los 5 inscritos minimos')
        return
    print(f'--- Jugadores inscritos en la categoría {cat} ---')
    removed_players = []
    for i, player in enumerate(scores[cat], 1):
        if i not in removed_players: 
            print(f'{i}. {player[1]}')
    playerIndex1 = int(input('Escribe el número del jugador 1: '))
    if playerIndex1 > len(scores[cat]) or playerIndex1 in removed_players:
        print('El jugador no se encuentra')
        return
    removed_players.append(playerIndex1)
    print(f'--- Jugadores restantes en la categoría {cat} ---')
    for i, player in enumerate(scores[cat], 1):
        if i not in removed_players: 
            print(f'{i}. {player[1]}')
    playerIndex2 = int(input('Escribe el número del jugador 2: '))
    if playerIndex2 > len(scores[cat]) or playerIndex2 in removed_players:
        print('El jugador no se encuentra')
        return
    score = input('Escribe el resultado del partido (jugador 1 - jugador 2): ')
    goals = list(map(int, score.split('-')))
    favor = abs(goals[0] - goals[1])
    result = 1 if favor > 0 else (2 if favor < 0 else 3)
    v = playerIndex1 - 1
    k = playerIndex2 - 1
    scores[cat][v][3] += 1
    scores[cat][k][3] += 1
    if result == 1:
        scores[cat][v][4] += 1
        scores[cat][k][5] += 1
        scores[cat][v][7] += favor
        scores[cat][v][8] += 2
    elif result == 2:
        scores[cat][k][4] += 1
        scores[cat][v][5] += 1
        scores[cat][k][7] += favor
        scores[cat][k][8] += 2
    else:
        scores[cat][k][6] += 1
        scores[cat][v][6] += 1
    
def shwCtgry():
    cat = input('Ingresa la categoria novato, intermedio o avanzado: ').lower()
    print(tabulate(scores[cat], headers=['id', 'nombre', 'edad', 'partidos jugados', 'partidos ganados', 'partidos perdidos', 'partidos empatados', 'favor', 'total']))

def shwPrtcpnt():
    two = []
    cat = input('Ingresa la categoria ')
    cat.lower()
    for i in range(len(scores[cat])):
        print(f'{i+1}. {scores[cat][i][1]}')
    x = int(input('Escriba el numero del jugador que quisiera revisar '))
    two.append([0,0,0,0,0,0,0,0,0])
    two.append(scores[cat][x], headers=['id', 'nombre', 'edad', 'partidos jugados', 'partidos ganados', 'partidos perdidos', 'partidos empatados', 'favor', 'total'])
    print(tabulate(two))

def wnnr():
    global y
    for category, players in scores.items():
        best = {}
        maxPoints = 0
        for player in players:
            points = player[8]
            if points >= maxPoints:
                name = player[1]
                if points > maxPoints:
                    best = {}
                    maxPoints = points
                favor = player[7]
                best[name] = [points, favor]
        if best:
            print(f'El deportista que ganó en la categoría {category} es {list(best.keys())[0]}')



                    


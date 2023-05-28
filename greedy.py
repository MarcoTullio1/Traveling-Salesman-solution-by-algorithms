import time
from typing import DefaultDict
INT_MAX = 2147483647

def greedy(matriz):
    num_cidades = len(matriz)
    cidades = list(range(num_cidades))
    visitadas = [False] * num_cidades

    # Inicia a rota na cidade 0
    rota = [0]
    visitadas[0] = True

    # Inicializa o tempo de execução
    tempo_inicial = time.time()

    # Enquanto houver cidades não visitadas
    while len(rota) < num_cidades:
        cidade_atual = rota[-1]
        distancia_minima = float('inf')
        proxima_cidade = None

        # Encontra a cidade mais próxima não visitada
        for cidade in cidades:
            if not visitadas[cidade] and matriz[cidade_atual][cidade] < distancia_minima:
                distancia_minima = matriz[cidade_atual][cidade]
                proxima_cidade = cidade

        # Marca a próxima cidade como visitada e adiciona à rota
        visitadas[proxima_cidade] = True
        rota.append(proxima_cidade)

    # Calcula a distância total da rota
    distancia_total = sum(matriz[rota[i]][rota[i+1]] for i in range(num_cidades - 1))
    distancia_total += matriz[rota[-1]][rota[0]]  # Considera a distância de retorno à cidade inicial

    # Calcula o tempo de execução
    tempo_execucao = (time.time() - tempo_inicial) * 1000

    # Retorna a rota, a distância mínima e o tempo de execução
    return rota, distancia_total, tempo_execucao

# Function to find the minimum cost path for all the paths
def greedy2(tsp):
    # Inicializa o tempo de execução
    tempo_inicial = time.time()
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)

    # Starting from the 0th indexed
    # city i.e., the first city
    visitedRouteList[0] = 1
    route = [0] * len(tsp)

    # Traverse the adjacency
    # matrix tsp[][]
    while i < len(tsp) and j < len(tsp[i]):

        # Corner of the Matrix
        if counter >= len(tsp[i]) - 1:
            break

        # If this path is unvisited then
        # and if the cost is less then
        # update the cost
        if j != i and (visitedRouteList[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1

        j += 1

        # Check all paths from the
        # ith indexed city
        if j == len(tsp[i]):
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1

    # Update the ending city in array
    # from city which was last visited
    i = route[counter - 1] - 1

    for j in range(len(tsp)):

        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1

    sum += min

    # Calcula o tempo de execução
    tempo_execucao = (time.time() - tempo_inicial) * 1000

    return 0, sum, tempo_execucao

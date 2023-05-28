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
import numpy as np
import itertools
import time
from sys import maxsize
from itertools import permutations
V = 4


def brute_force(matriz):
    # Cria uma lista com os índices das cidades
    cidades = list(range(len(matriz)))

    # Cria todas as permutações possíveis das cidades
    permutacoes = itertools.permutations(cidades)

    # Inicializa a distância mínima como infinito
    distancia_minima = float('inf')
    melhor_rota = None

    # Inicia a contagem do tempo de execução
    inicio = time.time()

    # Itera sobre todas as permutações e calcula a distância total
    for rota in permutacoes:
        distancia_total = 0
        cidade_anterior = None

        # Calcula a distância total da rota atual
        for cidade in rota:
            if cidade_anterior is not None:
                distancia_total += matriz[cidade_anterior][cidade]
            cidade_anterior = cidade

        # Considera a distância de retorno para a cidade inicial
        distancia_total += matriz[cidade][rota[0]]

        # Verifica se a rota atual é a melhor encontrada até o momento
        if distancia_total < distancia_minima:
            distancia_minima = distancia_total
            melhor_rota = rota

    # Finaliza a contagem do tempo de execução
    fim = time.time()

    # Calcula o tempo de execução em milissegundos
    tempo_execucao = (fim - inicio) * 1000

    # Retorna a melhor rota, a distância mínima encontrada e o tempo de execução
    return melhor_rota, distancia_minima, tempo_execucao


def brute_force2(graph, s):
	# Inicializa o tempo de execução
    tempo_inicial = time.time()
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
        
	# Calcula o tempo de execução
    tempo_execucao = (time.time() - tempo_inicial) * 1000

    return 0, min_path, tempo_execucao

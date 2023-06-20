import numpy as np
import time


def tsp_dynamic_programming(matriz):
    n = len(matriz)
    # Cria uma tabela para armazenar os subproblemas
    # O valor dp[i][mask] representa a menor distância de percorrer todas as cidades do conjunto 'mask' e terminar em i
    dp = np.full((n, 1 << n), -1)  # Inicializa todas as células com -1 (valor inválido)

    # Inicializa o caso base para a cidade inicial
    dp[0][1] = 0

    # Inicia a contagem do tempo de execução
    inicio = time.time()

    # Preenche a tabela dinâmica
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i) != 0:  # Verifica se a cidade i está no conjunto 'mask'
                for j in range(n):
                    if i != j and mask & (1 << j) != 0:  # Verifica se a cidade j também está no conjunto 'mask'
                        # Calcula a distância mínima para chegar em i a partir de outras cidades
                        submask = mask ^ (1 << i)  # Remove a cidade i do conjunto 'mask'
                        if dp[j][submask] != -1:
                            if dp[i][mask] == -1 or dp[j][submask] + matriz[j][i] < dp[i][mask]:
                                dp[i][mask] = dp[j][submask] + matriz[j][i]

    # Encontra a melhor rota e a distância mínima
    cidade_final = 0
    distancia_minima = float('inf')
    for i in range(1, n):
        if dp[i][(1 << n) - 1] != -1 and matriz[i][0] != -1:
            if dp[i][(1 << n) - 1] + matriz[i][0] < distancia_minima:
                cidade_final = i
                distancia_minima = dp[i][(1 << n) - 1] + matriz[i][0]

    # Reconstrói a melhor rota
    rota = [cidade_final]
    mask = (1 << n) - 1
    while mask != 1:
        for i in range(n):
            if i != cidade_final and mask & (1 << i) != 0 and dp[cidade_final][mask] == dp[i][mask ^ (1 << cidade_final)] + matriz[i][cidade_final]:
                rota.append(i)
                mask ^= (1 << cidade_final)
                cidade_final = i
                break
    rota.append(0)  # Adiciona a cidade inicial à rota

    # Finaliza a contagem do tempo de execução
    fim = time.time()

    # Calcula o tempo de execução em milissegundos
    tempo_execucao = (fim - inicio) * 1000

    # Retorna a melhor rota, a distância mínima encontrada e o tempo de execução
    return rota[::-1], distancia_minima, tempo_execucao


def ler_grafo_de_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
    matriz = []
    for linha in linhas:
        valores = [int(valor) if valor != '-1' else -1 for valor in linha.strip().split(';')]
        matriz.append(valores)
    return np.array(matriz)


# Leitura do grafo de um arquivo
matriz_distancias = ler_grafo_de_arquivo('grafo.txt')

# Chamada da função de programação dinâmica
melhor_rota, distancia_minima, tempo_execucao = tsp_dynamic_programming(matriz_distancias)

# Imprimir resultados
print("Melhor Rota:", melhor_rota)
print("Distância mínima:", distancia_minima)
print("Tempo de execução:", tempo_execucao, "ms")

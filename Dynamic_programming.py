import numpy as np
import time

def dynamic_programming(matriz):
    n = len(matriz)
    # Inicializa a tabela de memoização com valores infinitos
    memo = np.full((n, 2**n), float('inf'))

    # Inicializa a tabela para o caso base (nenhuma cidade visitada, exceto a cidade inicial)
    for i in range(n):
        if i != 0:
            memo[i][0] = matriz[i][0]

    # Função auxiliar para calcular a distância mínima para visitar todas as cidades
    def tsp_dp_util(mask, pos):
        # Se todas as cidades foram visitadas, retorna a distância para voltar à cidade inicial
        if mask == (1 << n) - 1:
            return matriz[pos][0]

        # Verifica se o resultado já foi calculado anteriormente
        if memo[pos][mask] != float('inf'):
            return memo[pos][mask]

        # Calcula a distância mínima para visitar as cidades não visitadas
        for cidade in range(n):
            if (mask >> cidade) & 1 == 0:  # Verifica se a cidade ainda não foi visitada
                nova_distancia = matriz[pos][cidade] + tsp_dp_util(mask | (1 << cidade), cidade)
                memo[pos][mask] = min(memo[pos][mask], nova_distancia)

        return memo[pos][mask]

    # Inicia a contagem do tempo de execução
    inicio = time.time()

    # Chama a função auxiliar para calcular a distância mínima
    distancia_minima = tsp_dp_util(1, 0)  # Começa na cidade inicial (0) e visita apenas ela

    # Finaliza a contagem do tempo de execução
    fim = time.time()

    # Calcula o tempo de execução em milissegundos
    tempo_execucao = (fim - inicio) * 1000

    return distancia_minima, tempo_execucao

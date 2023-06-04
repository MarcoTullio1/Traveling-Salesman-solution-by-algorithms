import time

def backtracking(matriz):
    
    cidades = list(range(len(matriz)))

    distancia_minima = float('inf')
    melhor_rota = None

    
    inicio = time.time()

    
    def backtrack(rota_atual, cidades_disponiveis, distancia_parcial):
        nonlocal distancia_minima, melhor_rota

        if distancia_parcial > distancia_minima:
            return

        if not cidades_disponiveis:
            distancia_total = distancia_parcial + matriz[rota_atual[-1]][rota_atual[0]]

            if distancia_total < distancia_minima:
                distancia_minima = distancia_total
                melhor_rota = rota_atual
            return

        for cidade in cidades_disponiveis:
            nova_rota = rota_atual + [cidade]

            novas_cidades_disponiveis = cidades_disponiveis.copy()
            novas_cidades_disponiveis.remove(cidade)

            nova_distancia_parcial = distancia_parcial
            if rota_atual:
                cidade_anterior = rota_atual[-1]
                nova_distancia_parcial += matriz[cidade_anterior][cidade]

            backtrack(nova_rota, novas_cidades_disponiveis, nova_distancia_parcial)

    backtrack([], cidades, 0)

    fim = time.time()

    tempo_execucao = (fim - inicio) * 1000

    return melhor_rota, distancia_minima, tempo_execucao

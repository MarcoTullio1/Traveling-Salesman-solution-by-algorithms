import decimal
import time
import pandas as pd
import numpy as np
from Backtracking import backtracking
from Dynamic_programming import dynamic_programming
from BF import brute_force

class Test:
    def generate_random_graph(self, n):
        graph = np.random.randint(0, 10, (n, n))
        return graph

    def question_b(self):
        data_results = {
            'vértice': [],
            'tempo_execução_médio_backtracking': [],
            'tempo_execução_médio_programação_dinâmica': [],
            'tempo_execução_médio_força_bruta': [],
            'acurácia_backtracking': [],
            'acurácia_programação_dinâmica': [],
        }
        df_results = pd.DataFrame(data_results)

        data_backtracking = {
            'vértice': [],
            'tempo_execução': [],
            'solução': [],
            'rota': []
        }
        df_backtracking = pd.DataFrame(data_backtracking)

        data_dynamic_programming = {
            'vértice': [],
            'tempo_execução': [],
            'solução': []
        }
        df_dynamic_programming = pd.DataFrame(data_dynamic_programming)

        data_brute_force = {
            'vértice': [],
            'tempo_execução': [],
            'solução': [],
            'rota': []
        }
        df_brute_force = pd.DataFrame(data_brute_force)

        inicialização_vértices = 5

        for i in range(5):
            print(f"Executando iteração {i+1}...")
            contador_acertos_bt = 0
            contador_acertos_dp = 0
            tempo_total_bt = 0
            tempo_total_dp = 0
            tempo_total_bf = 0

            for j in range(1000):
                grafo = self.generate_random_graph(inicialização_vértices)

                # Algoritmo de backtracking
                rota_bt, solução_bt, tempo_execução_bt = backtracking(grafo)
                tempo_total_bt += tempo_execução_bt

                # Algoritmo de programação dinâmica
                solução_dp, tempo_execução_dp = dynamic_programming(grafo)
                tempo_total_dp += tempo_execução_dp

                # Algoritmo de força bruta
                rota_bf, solução_bf, tempo_execução_bf = brute_force(grafo)
                tempo_total_bf += tempo_execução_bf

                # Comparação das soluções
                if solução_bt == solução_bf:
                    contador_acertos_bt += 1

                if solução_dp == solução_bf:
                    contador_acertos_dp += 1

                # Armazenar resultados
                df_backtracking = pd.concat([df_backtracking, pd.DataFrame({'vértice': [inicialização_vértices],
                                                                            'tempo_execução': [tempo_execução_bt],
                                                                            'solução': [solução_bt],
                                                                            'rota': [rota_bt]})])
                df_dynamic_programming = pd.concat([df_dynamic_programming, pd.DataFrame({'vértice': [inicialização_vértices],
                                                                                            'tempo_execução': [tempo_execução_dp],
                                                                                            'solução': [solução_dp]})])
                df_brute_force = pd.concat([df_brute_force, pd.DataFrame({'vértice': [inicialização_vértices],
                                                                          'tempo_execução': [tempo_execução_bf],
                                                                          'solução': [solução_bf],
                                                                          'rota': [rota_bf]})])

            # Calcular tempo médio
            tempo_médio_bt = tempo_total_bt / 1000
            tempo_médio_dp = tempo_total_dp / 1000
            tempo_médio_bf = tempo_total_bf / 1000

            # Calcular acurácia em porcentagem
            acurácia_bt = contador_acertos_bt / 10
            acurácia_dp = contador_acertos_dp / 10

            # Armazenar resultados médios
            df_results = pd.concat([df_results, pd.DataFrame({'vértice': [inicialização_vértices],
                                                              'tempo_execução_médio_backtracking': [tempo_médio_bt],
                                                              'tempo_execução_médio_programação_dinâmica': [tempo_médio_dp],
                                                              'tempo_execução_médio_força_bruta': [tempo_médio_bf],
                                                              'acurácia_backtracking': [acurácia_bt],
                                                              'acurácia_programação_dinâmica': [acurácia_dp]})])

            # Incrementar o número de vértices para a próxima iteração
            inicialização_vértices += 5

        # Salvar resultados em arquivos CSV
        df_backtracking.to_csv('resultados_backtracking.csv', index=False)
        df_dynamic_programming.to_csv('resultados_programação_dinâmica.csv', index=False)
        df_brute_force.to_csv('resultados_força_bruta.csv', index=False)
        df_results.to_csv('resultados_comparativos.csv', index=False)

        # Exibir resultados
        print("Resultados Backtracking:")
        print(df_backtracking)
        print("\nResultados Programação Dinâmica:")
        print(df_dynamic_programming)
        print("\nResultados Força Bruta:")
        print(df_brute_force)
        print("\nResultados Comparativos:")
        print(df_results)

    def executar_testes(self):
        self.question_b()

Test().executar_testes()

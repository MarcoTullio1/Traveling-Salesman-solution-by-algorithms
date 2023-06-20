import decimal
import time
import pandas as pd
import numpy as np
from Backtracking import backtracking
from Dynamic_programming import dynamic_programming

class Test:
    def generate_random_graph(self, n):
        graph = np.random.randint(0, 10, (n, n))
        return graph

    def question_b(self):
        data_results = {
            'vertice': [],
            'average_time_execution_backtracking': [],
            'average_time_execution_dynamic_programming': [],
            'same_solution_count': []
        }
        df_results = pd.DataFrame(data_results)

        data_backtracking = {
            'vertice': [],
            'execution_time': [],
            'solution': [],
            'route': []
        }
        df_backtracking = pd.DataFrame(data_backtracking)

        data_dynamic_programming = {
            'vertice': [],
            'execution_time': [],
            'solution': []
        }
        df_dynamic_programming = pd.DataFrame(data_dynamic_programming)

        vertex_initialization = 5

        for i in range(5):
            same_solution_count = 0
            total_time_bt = 0
            total_time_dp = 0

            for j in range(1000):
                graph = self.generate_random_graph(vertex_initialization)

                # Algoritmo de backtracking
                route_bt, solution_bt, execution_time_bt = backtracking(graph)
                total_time_bt += execution_time_bt

                # Algoritmo de programação dinâmica
                solution_dp, execution_time_dp = dynamic_programming(graph)
                total_time_dp += execution_time_dp

                # Comparação das soluções
                if solution_bt == solution_dp:
                    same_solution_count += 1

                # Armazenar resultados
                df_backtracking = pd.concat([df_backtracking, pd.DataFrame({'vertice': [vertex_initialization],
                                                                            'execution_time': [execution_time_bt],
                                                                            'solution': [solution_bt],
                                                                            'route': [route_bt]})])
                df_dynamic_programming = pd.concat([df_dynamic_programming, pd.DataFrame({'vertice': [vertex_initialization],
                                                                                            'execution_time': [execution_time_dp],
                                                                                            'solution': [solution_dp]})])

            # Calcular tempo médio
            average_time_bt = total_time_bt / 1000
            average_time_dp = total_time_dp / 1000

            # Armazenar resultados médios
            df_results = pd.concat([df_results, pd.DataFrame({'vertice': [vertex_initialization],
                                                              'average_time_execution_backtracking': [average_time_bt],
                                                              'average_time_execution_dynamic_programming': [average_time_dp],
                                                              'same_solution_count': [same_solution_count]})])

            # Incrementar o número de vértices para a próxima iteração
            vertex_initialization += 5

        # Salvar resultados em arquivos CSV
        df_backtracking.to_csv('backtracking_results.csv', index=False)
        df_dynamic_programming.to_csv('dynamic_programming_results.csv', index=False)
        df_results.to_csv('comparison_results.csv', index=False)

        # Exibir resultados
        print("Backtracking Results:")
        print(df_backtracking)
        print("\nDynamic Programming Results:")
        print(df_dynamic_programming)
        print("\nComparison Results:")
        print(df_results)

    def run_tests(self):
        self.question_b()

Test().run_tests()

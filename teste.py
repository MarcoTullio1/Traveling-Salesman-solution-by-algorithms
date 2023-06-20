import decimal
import time
import pandas as pd
import numpy as np
from BF import brute_force
from Backtracking import backtracking
from greedy import greedy
from Dynamic_programming import dynamic_programming

global greedy_execution_time
global bf_execution_time
global same_solution_count


class Test:

    def generate_random_graph(self, n):
        graph = np.random.randint(0, 10, (n, n))
        return graph

    def question_a(self):
        vertex_count = 5
        total_time_bf = 0
        total_time_g = 0
        total_time_bt = 0

        for i in range(1000):
            for i in range(70):
                graph = self.generate_random_graph(vertex_count)
                route_bf, solution_bf, execution_time_bf = brute_force(graph)
                route_g, solution_g, execution_time_g = greedy(graph)
                route_bt, solution_bt, execution_time_bt = backtracking(graph)
                route_dp, solution_dp = dynamic_programming(graph)  # Teste com programação dinâmica

                total_time_bf += execution_time_bf
                total_time_g += execution_time_g
                total_time_bt += execution_time_bt

            # Verifica se o tempo de execução foi maior do 4 minutos
            if (total_time_bf > 240000 or total_time_g > 240000):
                print("Tamanho maximo de grafo encontrado! N = " + str(vertex_count - 1))
                break
            
            print("Grafo de tamanho " + str(vertex_count) + " processado!")
            vertex_count+=1

    def question_b(self):
        data_results = {
            'vertice': [],
            'average_time_execution_bf': [],
            'average_time_execution_greedy': [],
            'average_time_execution_backtracking': [],
            'average_time_execution_dynamic_programming': [],  # Adicione esta coluna
            'same_solution_count': []
        }
        df_results = pd.DataFrame(data_results)

        data_bf = {
            'vertice': [],
            'execution_time': [],
            'solution': [],
            'route': []
        }
        df_bf = pd.DataFrame(data_bf)

        data_greedy = {
            'vertice': [],
            'execution_time': [],
            'solution': [],
            'route': []
        }
        df_greedy = pd.DataFrame(data_greedy)

        data_backtracking = {
            'vertice': [],
            'execution_time': [],
            'solution': [],
            'route': []
        }
        df_backtracking = pd.DataFrame(data_backtracking)

        data_dynamic_programming = {  # Adicione este bloco
            'vertice': [],
            'solution': []
        }
        df_dynamic_programming = pd.DataFrame(data_dynamic_programming)

        vertex_inicialization = 5

        for i in range(5):

            same_solution_count = 0
            total_time_bf = 0
            total_time_g = 0
            total_time_bt = 0
            total_time_dp = 0  # Adicione esta variável

            for i in range(1000):
                graph = self.generate_random_graph(vertex_inicialization)

                route_bf, solution_bf, execution_time_bf = brute_force(graph)
                route_g, solution_g, execution_time_g = greedy(graph)
                route_bt, solution_bt, execution_time_bt = backtracking(graph)
                route_dp, solution_dp = dynamic_programming(graph)  # Teste com programação dinâmica

                total_time_bf += execution_time_bf
                total_time_g += execution_time_g
                total_time_bt += execution_time_bt
                total_time_dp += solution_dp  # Adicione esta linha

                if (solution_bf == solution_g):
                    same_solution_count += 1

                df_bf = pd.concat([df_bf, pd.DataFrame({'vertice': [vertex_inicialization],
                                                        'execution_time': [execution_time_bf],
                                                        'solution': [solution_bf],
                                                        'route': [route_bf]
                                                        })])

                df_greedy = pd.concat([df_greedy, pd.DataFrame({'vertice': [vertex_inicialization],
                                                                'execution_time': [execution_time_g],
                                                                'solution': [solution_g],
                                                                'route': [route_g]
                                                                })])
                
                df_backtracking = pd.concat([df_backtracking, pd.DataFrame({'vertice': [vertex_inicialization],
                                                                'execution_time': [execution_time_bt],
                                                                'solution': [solution_bt],
                                                                'route': [route_bt]
                                                                })])

                df_dynamic_programming = pd.concat([df_dynamic_programming, pd.DataFrame({'vertice': [vertex_inicialization],
                                                                                          'solution': [solution_dp]
                                                                                          })])  # Adicione esta linha

                df_greedy.to_csv("./greedy.csv", index=False)
                df_bf.to_csv("./brute_force.csv", index=False)
                df_backtracking.to_csv("./backtracking.csv", index=False)
                df_dynamic_programming.to_csv("./dynamic_programming.csv", index=False)  # Adicione esta linha

            df_results = pd.concat([df_results, pd.DataFrame({'vertice': [vertex_inicialization],
                                                              'average_time_execution_bf': [total_time_bf / 1000],
                                                              'average_time_execution_greedy': [total_time_g / 1000],
                                                              'average_time_execution_backtracking': [total_time_bt / 1000],
                                                              'average_time_execution_dynamic_programming': [total_time_dp / 1000],  # Adicione esta coluna
                                                              'same_solution_count': [same_solution_count]})])

            print("Grafo de tamanho " +
                  str(vertex_inicialization) + " processado.")
            df_results.to_csv("./results.csv", index=False)
            vertex_inicialization += 1


if __name__ == "__main__":
    Test().question_a()
    time.sleep(5)
    Test().question_b()

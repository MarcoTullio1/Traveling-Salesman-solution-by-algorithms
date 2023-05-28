import decimal
import pandas as pd
import numpy as np
from BF import brute_force
from greedy import greedy
import threading

global greedy_execution_time 
global bf_execution_time
global same_solution_count


class Test:

    def generate_random_graph(self, n):
        graph = np.random.randint(0, 10, (n, n))
        return graph

    def question_a(self):
        data_results = {
            'vertice': [],
            'average_time_execution_bf': [],
            'average_time_execution_greedy': [],
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

        vertex_inicialization = 5

        for i in range(5):

            same_solution_count  = 0
            total_time_bf = 0
            total_time_g = 0
        
            for i in range(1000):
                graph = self.generate_random_graph(vertex_inicialization)

                route_bf, solution_bf, execution_time_bf = brute_force(graph)
                route_g, solution_g, execution_time_g = greedy(graph)

                total_time_bf += execution_time_bf
                total_time_g += execution_time_g
                
                if(solution_bf == solution_g):
                    same_solution_count+=1

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

                df_greedy.to_csv("./greedy.csv", index=False)
                df_bf.to_csv("./brute_force.csv", index=False)

            df_results = pd.concat([df_results, pd.DataFrame({'vertice': [vertex_inicialization],
                                                               'average_time_execution_bf': [total_time_bf / 1000],
                                                               'average_time_execution_greedy': [total_time_g / 1000],
                                                               'same_solution_count': [same_solution_count]})])

            print("Grafo de tamanho " + str(vertex_inicialization) + " processado.")
            df_results.to_csv("./results.csv", index=False)
            vertex_inicialization += 1
        

if __name__ == "__main__":
    Test().question_a()

import decimal
import pandas as pd
import numpy as np
from BF import brute_force
from greedy import greedy
import threading

global greedy_solution
global greedy_execution_time 
global bf_solution
global bf_execution_time


class Test:

    def generate_random_graph(self, n):
        graph = np.random.randint(0, 10, (n, n))
        return graph

    def question_a(self):
        data_results = {
            'vertice': [],
            'average_time_execution_bf': [],
            'average_time_execution_greedy': [],
            'greedy_solution': []
        }
        df_results = pd.DataFrame(data_results)

        data_bf = {
            'vertice': [],
            'average_time_execution': []
        }
        df_bf = pd.DataFrame(data_bf)

        data_greedy = {
            'vertice': [],
            'average_time_execution': [],
            'accuracy': []
        }
        df_greedy = pd.DataFrame(data_greedy)

        vertex_inicialization = 5

        for i in range(4): 
            n = vertex_inicialization
            t1 = threading.Thread(target=self.test_bf(n))
            t2 = threading.Thread(target=self.test_greedy(n))

            t1.start()
            t2.start()

            t2.join()
            t1.join()

            df_results = pd.concat([df_results, pd.DataFrame({'vertice': [n],
                                                               'average_time_execution_bf': [bf_execution_time],
                                                               'average_time_execution_greedy': [greedy_execution_time],
                                                               'greedy_solution': [greedy_solution],
                                                               'brute_force_solution': [bf_solution],
                                                               'same_solution': [bf_solution == greedy_solution]
            })])

            if bf_solution == 0:  
                df_results.to_csv("./results.csv", index=False)
                break
            
            vertex_inicialization += 1

        df_results.to_csv("./results.csv", index=False)

    def test_bf(self, n):
        global bf_solution
        global bf_execution_time
        total_time = 0

        for i in range(70):
            graph = self.generate_random_graph(n)
            route, solution, execution_time = brute_force(graph)
            total_time += execution_time

        #verifica se o tempo de execucao foi maior do que 4 minutos
        if total_time > 240000:
            bf_solution = 0
            bf_execution_time = decimal.Decimal(total_time / 70)

        bf_solution =  solution
        bf_execution_time = decimal.Decimal(total_time / 70)

    def test_greedy(self, n):
        total_time = 0
        global greedy_solution
        global greedy_execution_time
        global greedy_solution

        for i in range(70):
            graph = self.generate_random_graph(n)
            route, solution, execution_time = greedy(graph)
            total_time += execution_time

        #verifica se o tempo de execucao foi maior do que 4 minutos
        if total_time > 240000:
            greedy_solution = 0
            greedy_execution_time = decimal.Decimal(total_time / 70)

        greedy_solution =  solution
        greedy_execution_time = decimal.Decimal(total_time / 70)


if __name__ == "__main__":
    Test().question_a()

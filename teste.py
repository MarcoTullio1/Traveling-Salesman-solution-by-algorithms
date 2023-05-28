import decimal
import math
import pandas as pd
import numpy as np
from BF import travellingSalesmanProblem
from greedy import findMinRoute
import time


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

        time_execution = 0
        vertex_inicialization = 5
        start_time = time.time()

        while time_execution < 240:  # 4 minutos = 240 segundos
            n = vertex_inicialization - 1
            average_time_execution_bf = self.test_bf(n)
            average_time_execution_greedy, greedy_solution, accuracy = self.test_greedy(n)

            df_results = pd.concat([df_results, pd.DataFrame({'vertice': [n],
                                                               'average_time_execution_bf': [average_time_execution_bf],
                                                               'average_time_execution_greedy': [average_time_execution_greedy],
                                                               'greedy_solution': [greedy_solution]})])

            df_bf = pd.concat([df_bf, pd.DataFrame({'vertice': [n],
                                                     'average_time_execution': [average_time_execution_bf]})])

            df_greedy = pd.concat([df_greedy, pd.DataFrame({'vertice': [n],
                                                             'average_time_execution': [average_time_execution_greedy],
                                                             'accuracy': [accuracy]})])

            end_time = time.time()
            time_execution = end_time - start_time
            time_execution = math.floor(time_execution)
            vertex_inicialization += 1

        df_results.to_csv("./results.csv", index=False)
        df_bf.to_csv("./brute_force_execution.csv", index=False)
        df_greedy.to_csv("./greedy_execution.csv", index=False)

    def test_bf(self, n):
        total_time_execution_size = 0

        for repetition in range(1, 71):
            graph = self.generate_random_graph(n)
            s = 0
            start_time = time.time()
            result = travellingSalesmanProblem(graph, s)
            end_time = time.time()
            final_time = end_time - start_time
            total_time_execution_size += final_time

        average_time_execution = decimal.Decimal(total_time_execution_size / 70)
        return average_time_execution

    def test_greedy(self, n):
        total_time_execution_size = 0
        total_correct_solutions = 0

        for repetition in range(1, 71):
            graph = self.generate_random_graph(n)
            start_time = time.time()
            greedy_solution = findMinRoute(graph)
            end_time = time.time()
            final_time = end_time - start_time
            total_time_execution_size += final_time

            # Verificar se a solução do algoritmo guloso é a mesma da força bruta
            bf_solution = travellingSalesmanProblem(graph, 0)
            if greedy_solution == bf_solution:
                total_correct_solutions += 1

        average_time_execution = decimal.Decimal(total_time_execution_size / 70)
        accuracy = total_correct_solutions / 70
        return average_time_execution, greedy_solution, accuracy


if __name__ == "__main__":
    Test().question_a()

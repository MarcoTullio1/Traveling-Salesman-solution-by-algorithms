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
            'graph_number': [],
            'vertices': [],
            'brute_force_solution': [],
            'greedy_solution': [],
            'greedy_time_execution': []
        }

        data_bf_execution = {
            'vertices': [],
            'average_time_execution': []
        }

        data_greedy_execution = {
            'vertices': [],
            'average_time_execution': [],
            'matched_solutions': []
        }

        df_results = pd.DataFrame(data_results)
        df_bf_execution = pd.DataFrame(data_bf_execution)
        df_greedy_execution = pd.DataFrame(data_greedy_execution)

        vertex_inicialization = 5
        graph_number = 1

        brute_force_solutions = []
        greedy_solutions = []
        matched_solutions = []

        for _ in range(1000):
            n = vertex_inicialization - 1
            graph = self.generate_random_graph(n)
            brute_force_solution, brute_force_time = self.test_bf(graph)
            greedy_solution, greedy_time = self.test_greedy(graph)

            brute_force_solutions.append(brute_force_solution)
            greedy_solutions.append(greedy_solution)
            matched_solutions.append(greedy_solution == brute_force_solution)

            df_results = pd.concat([df_results, pd.DataFrame({'graph_number': [graph_number],
                                                              'vertices': [n],
                                                              'brute_force_solution': [brute_force_solution],
                                                              'greedy_solution': [greedy_solution],
                                                              'greedy_time_execution': [greedy_time]})])

            df_bf_execution = pd.concat([df_bf_execution, pd.DataFrame({'vertices': [n],
                                                                        'average_time_execution': [brute_force_time]})])

            df_greedy_execution = pd.concat([df_greedy_execution, pd.DataFrame({'vertices': [n],
                                                                                'average_time_execution': [greedy_time],
                                                                                'matched_solutions': [greedy_solution == brute_force_solution]})])

            vertex_inicialization += 1
            graph_number += 1

        df_results.to_csv("./results.csv", index=False)
        df_bf_execution.to_csv("./brute_force_execution.csv", index=False)
        df_greedy_execution.to_csv("./greedy_execution.csv", index=False)

        # Armazenar resultados em um arquivo separado
        results = {
            'brute_force_solutions': brute_force_solutions,
            'greedy_solutions': greedy_solutions,
            'matched_solutions': matched_solutions
        }
        np.savez('./results.npz', **results)

    def test_bf(self, graph):
        s = 0
        start_time = time.time()
        brute_force_solution = travellingSalesmanProblem(graph, s)
        end_time = time.time()
        brute_force_time = end_time - start_time
        return brute_force_solution, brute_force_time

    def test_greedy(self, graph):
        start_time = time.time()
        greedy_solution = findMinRoute(graph)
        end_time = time.time()
        greedy_time = end_time - start_time
        return greedy_solution, greedy_time

if __name__ == "__main__":
    Test().question_a()

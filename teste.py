import decimal
import math
import pandas as pd
import numpy as np
from BF import travellingSalesmanProblem
from greedy import findMinRoute
import time


class Test:
    def question_a(self):
        data = {
            'vertice': [],
            'average_time_execution': []
        }
        df = pd.DataFrame(data)

        time_execution = 0
        vertex_inicialization = 5
        start_time = time.time()

        while time_execution < 240:  # 4 minutos = 240 segundos
            n = np.random.randint(vertex_inicialization, vertex_inicialization + 1)
            graph = np.random.randint(0, 10, (n, n))
            average_time_execution = self.test_bf(graph, n)
            df = pd.concat([df, pd.DataFrame({'vertice': [n], 'average_time_execution': [average_time_execution]})])
            end_time = time.time()
            time_execution = end_time - start_time
            time_execution = math.floor(time_execution)
            vertex_inicialization += 1

        df.to_csv("./brute_force_execution.csv")

    def test_bf(self, graph, n):
        total_time_execution_size = 0

        for repetition in range(1, 71):
            s = 0
            start_time = time.time()
            result = travellingSalesmanProblem(graph, s)
            end_time = time.time()
            final_time = end_time - start_time
            total_time_execution_size += final_time

        average_time_execution = decimal.Decimal(total_time_execution_size / 70)
        return average_time_execution

    def test_greedy(self, graph):
        findMinRoute(graph)


if __name__ == "__main__":
    question_a = Test().question_a()
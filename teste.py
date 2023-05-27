import decimal
import math
import pandas as pd
import numpy as np
from BF import travellingSalesmanProblem
import time

class Test:
    def generate_random_graph(self, n):
        graph = np.random.randint(0, 10, (n, n))
        return graph

    def question_a(self):
        data = {
            'vertice': [],
            'average_time_execution': []
        }
        df = pd.DataFrame(data)

        vertex_inicialization = 5

        #for _ in range(1000):
        for _ in range(100):
            n = vertex_inicialization - 1
            average_time_execution = self.test_bf(n)
            df = pd.concat([df, pd.DataFrame({'vertice': [n], 'average_time_execution': [average_time_execution]})])
            vertex_inicialization += 1

        df.to_csv("./brute_force_execution.csv")

    def test_bf(self, n):
        total_time_execution_size = 0

        for _ in range(70):
            graph = self.generate_random_graph(n)
            s = 0
            start_time = time.time()
            result = travellingSalesmanProblem(graph, s)
            end_time = time.time()
            final_time = end_time - start_time
            total_time_execution_size += final_time

        average_time_execution = decimal.Decimal(total_time_execution_size / 70)
        return average_time_execution

if __name__ == "__main__":
    Test().question_a()

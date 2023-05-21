import decimal
import math
import pandas as pd
import numpy as np
from BF  import travellingSalesmanProblem
from greedy import  findMinRoute
import time
class Test:

    def question_a(self):
        ''' function responsible for calculate the number of maximum vertex that
        can be executed in 4 minutes related to brute-force algorithm'''
        data = {
            'vertice': [],
            'average_time_execution': []
        }
        df = pd.DataFrame(data)

        time_execution = 0
        vertex_inicialization = 5
        start_time = time.time()
        while time_execution < 240: # 4 minutoes = 240 seconds
                ''' n is the number of vertices in the graph. 
                graph is a adjacency matrix on n vertices'''
                n = np.random.randint(vertex_inicialization, vertex_inicialization + 1)
                graph = np.random.randint(0, 10, (n, n))
                avarage_time_execution = self.test_bf(graph,n) #return the avarege time execution of a vertice
                df = df.append({'vertice': n, 'average_time_execution': avarage_time_execution},
                               ignore_index=True)
                end_time = time.time()
                time_execution = end_time - start_time # calculate the time of execution
                time_execution = math.floor(time_execution)
                vertex_inicialization = vertex_inicialization + 1 # increments the number of vertices setting
        df.to_csv("./brute_force_execution.csv")



    def test_bf(self,graph,n): # function responsible for call the execution of the  brute-force algorithm
        total_time_execution_size = 0
        for repetition in range(1, 71):
                s = 0
                start_time = time.time()  # in seconds
                result = travellingSalesmanProblem(graph, s)
                end_time = time.time()  # em segundos
                final_time = end_time-start_time
                total_time_execution_size = total_time_execution_size + final_time # time of solution

        avarage_time_execution = decimal.Decimal(total_time_execution_size/70) # average solution time sum all running time and divide by the number of times the solution was found

        return avarage_time_execution


    def test_greedy(self,graph): # function responsible for call the execution of the algorithm greedy
        findMinRoute(graph)





if __name__ == "__main__":
    quation_a = Test().question_a()

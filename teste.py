import numpy as np
from BF  import travellingSalesmanProblem
from greedy import  findMinRoute
import time
class Teste:

    def graph_generator(self):

        for i in range (5,50):
            n = np.random.randint(i, i + 1)
            graph = np.random.randint(0, 10, (n, n))
            #print(graph)
            #self.test_greedy(graph)
            self.test_bf(graph,n)

    def test_bf(self,graph,n):
        size = n
        total_time_execution_size = 0
        number_solutions = 0

        for repetition in range(1, 71):
                s = 0
                start_time = time.time()  # em segundos
                print(travellingSalesmanProblem(graph, s))
                number_solutions= number_solutions +1
                end_time = time.time()  # em segundos
                final_time = end_time-start_time
                total_time_execution_size = total_time_execution_size + final_time # tempo de solução
                # tempo médio de solução soma todos os total time execution e divide pelo número de vezes que a solução foi encontrada
                #total_time_execution_size
                #media_time = total_time_execution_size
        print("number_solutions",number_solutions)
        print(total_time_execution_size)
        avarage_time_execution = float(total_time_execution_size)/float(70)
        print(float(avarage_time_execution))





    def test_greedy(self,graph):
        #size = n
        tempo_inicial = time.time() # em segundos
        findMinRoute(graph)
        tempo_final = time.time() # em segundos
        print(tempo_final-tempo_inicial)




if __name__ == "__main__":
    my = Teste().graph_generator()

    #print(travellingSalesmanProblem(my,s))
    #findMinRoute(my)



'''The question is a little open-ended, so please clarify if this isn't what you want.

import numpy as np 
#n is the number of vertices in the graph.  
adjacency = np.random.randint(0,2,(n,n)) 
That's it. You now have the adjacency matrix of a random graph on n vertices. That means adjacency[i,j]=1 if there is an edge between vertices i and j and is 0 otherwise. You can choose n randomly too if you want.

n=np.random.randint(1,N+1) 
where N is the largest number of vertices allowed'''
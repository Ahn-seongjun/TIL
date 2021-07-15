class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

A, B, C, D = 0, 1, 2, 3
G1 = Graph(4)
G1.graph[A][B] = 1; G1.graph[A][C] = 1; G1.graph[A][D] = 1
G1.graph[B][A] = 1; G1.graph[B][C] = 1
G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1
G1.graph[D][A] = 1; G1.graph[D][C] = 1

for i in range(4):
    for j in range(4) :
        print(G1.graph[i][j], end=' ')
    print()
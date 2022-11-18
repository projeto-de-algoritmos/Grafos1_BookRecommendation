class Graph:
 
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.adjacency_matrix = [[] for _ in range(num_vertex)]
 

    def dfs(self, temp, v, visited):
 
        visited[v] = True
        temp.append(v)
        
        for i in self.adjacency_matrix[v]:
            if visited[i] == False:
                temp = self.dfs(temp, i, visited)
        return temp
 

    def add_edge(self, v, w):
        self.adjacency_matrix[v].append(w)
        self.adjacency_matrix[w].append(v)
 

    def connected_components(self):
        visited = []
        c_components = []
        
        visited = [False for _ in range(self.num_vertex)]
        for v in range(self.num_vertex):
            if visited[v] == False:
                temp = []
                c_components.append(self.dfs(temp, v, visited))
        return c_components

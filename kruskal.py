class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

   
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    
    def find(self, parent, i):

        if parent[i] == i:
            return i

        return self.find(parent, parent[i])

    
    def union(self, parent, rank, x, y) -> None:

        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    
    def kruskal_mst(self):

        result = []

        i = 0
        e = 0

        
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

       
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        
        while e < self.V - 1:

            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            
            if x != y:

                e += 1

                result.append([u, v, w])

                self.union(parent, rank, x, y)

       
        print("Edges in MST:")

        total_cost = 0

        for u, v, w in result:
            total_cost += w
            print(f"{u} -- {v} == {w}")

        print("Total Cost =", total_cost)



g = Graph(5)

g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.kruskal_mst()
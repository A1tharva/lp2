import sys


V = 5


graph = [
    [0, 10, 0, 5, 0],
    [10, 0, 1, 2, 0],
    [0, 1, 0, 0, 4],
    [5, 2, 0, 0, 2],
    [0, 0, 4, 2, 0]
]



def min_distance(dist, visited):

    minimum = sys.maxsize
    min_index = 0

    for v in range(V):

        if dist[v] < minimum and visited[v] == False:
            minimum = dist[v]
            min_index = v

    return min_index



def dijkstra(src):

    dist = [sys.maxsize] * V

    visited = [False] * V

    dist[src] = 0

    for _ in range(V):

        u = min_distance(dist, visited)

        visited[u] = True

        for v in range(V):

            if (graph[u][v] > 0 and
                visited[v] == False and
                dist[v] > dist[u] + graph[u][v]):

                dist[v] = dist[u] + graph[u][v]

    
    print("Vertex \t Distance from Source")

    for i in range(V):
        print(i, "\t\t", dist[i])



dijkstra(0)
import sys
V = 5

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

def min_key(key, mst_set):

    minimum = sys.maxsize
    min_index = -1

    for v in range(V):

        if key[v] < minimum and mst_set[v] == False:
            minimum = key[v]
            min_index = v

    return min_index

def prim_mst():

    parent = [0] * V

    key = [sys.maxsize] * V

    mst_set = [False] * V

    key[0] = 0
    parent[0] = -1

    for _ in range(V):

        u = min_key(key, mst_set)

        mst_set[u] = True

        for v in range(V):

            if graph[u][v] > 0 and mst_set[v] == False and key[v] > graph[u][v]:

                key[v] = graph[u][v]

                parent[v] = u

    print("Edge \tWeight")

    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


prim_mst()
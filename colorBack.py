V = 4


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]


m = 3


color = [0] * V



def is_safe(v, c):

    for i in range(V):

        if graph[v][i] == 1 and color[i] == c:
            return False

    return True



def solve(v):

    
    if v == V:
        return True


    for c in range(1, m + 1):

        if is_safe(v, c):

            color[v] = c

            if solve(v + 1):
                return True

            
            color[v] = 0

    return False



if solve(0):

    print("Solution Exists")

    for i in range(V):
        print(f"Vertex {i} ---> Color {color[i]}")

else:
    print("No Solution")
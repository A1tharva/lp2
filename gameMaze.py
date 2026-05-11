from queue import PriorityQueue

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]


start = (0, 0)
goal = (4, 4)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]



def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def a_star(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    pq = PriorityQueue()

    pq.put((0, 0, start, [start]))

    visited = set()

    while not pq.empty():

        f, g, current, path = pq.get()

       
        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        x, y = current

        
        for dx, dy in moves:

            nx, ny = x + dx, y + dy

            
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0:

                    neighbor = (nx, ny)

                    if neighbor not in visited:

                        new_g = g + 1

                        new_f = new_g + heuristic(neighbor, goal)

                        pq.put((new_f, new_g, neighbor, path + [neighbor]))

    return None



path = a_star(maze, start, goal)

if path:
    print("Shortest Path:")
    print(path)
else:
    print("No path found")
# 1. Breadth First Search (BFS)

## Theory

Breadth First Search explores a graph level by level.
It first visits all neighboring nodes of the current node before moving deeper.

It uses a **Queue (FIFO)** data structure.

Applications:

* Shortest path in unweighted graphs
* Web crawling
* Network broadcasting
* Social networks

## Algorithm

1. Start from source node.
2. Mark source as visited.
3. Insert source into queue.
4. Repeat until queue becomes empty:

   * Remove front node.
   * Visit all unvisited adjacent nodes.
   * Mark them visited and enqueue them.

## Time Complexity

For graph with `V` vertices and `E` edges:

[
O(V + E)
]

## Space Complexity

[
O(V)
]

(for queue and visited array)

---

# 2. Depth First Search (DFS)

## Theory

Depth First Search explores as deep as possible before backtracking.

It uses:

* Stack
  or
* Recursion

Applications:

* Topological sorting
* Cycle detection
* Connected components
* Maze solving

## Algorithm

1. Start from source node.
2. Mark node as visited.
3. Visit an unvisited adjacent node recursively.
4. Backtrack when no unvisited node remains.

## Time Complexity

[
O(V + E)
]

## Space Complexity

[
O(V)
]

(recursion stack + visited array)

---

# 3. A* Algorithm for 8-Puzzle

## Theory

A* (A-Star) is a heuristic search algorithm used for optimal pathfinding.

It evaluates nodes using:

f(n)=g(n)+h(n)

Where:

* (g(n)) = actual cost from start
* (h(n)) = heuristic estimate to goal
* (f(n)) = total estimated cost

Common heuristic for 8-puzzle:

* Manhattan Distance
* Misplaced Tiles

Applications:

* AI games
* Robotics
* Route finding

## Algorithm

1. Put initial state in priority queue.
2. Compute heuristic value.
3. Select state with minimum (f(n)).
4. Expand neighboring states.
5. Repeat until goal state found.

## Time Complexity

Worst case:

[
O(b^d)
]

Where:

* (b) = branching factor
* (d) = depth of solution

### What is branching factor?

The number of child nodes generated from one node.

### What is depth of solution?

The number of steps required to reach the goal state from the start state.

## Space Complexity

[
O(b^d)
]

---

# 4. Pathfinding in Maze

## Theory

Maze pathfinding finds a valid route from source to destination.

Algorithms used:

* BFS → shortest path
* DFS → any path
* A* → optimized shortest path

Applications:

* Video games
* Robot navigation
* GPS systems

## BFS-Based Maze Algorithm

1. Start from source cell.
2. Visit neighboring valid cells.
3. Store visited cells.
4. Continue until destination reached.

## Time Complexity

For maze of size (N \times M):

[
O(N×Mlog(N×M))]

## Space Complexity

[
O(N×M)
]

---

# 5. Greedy Algorithms

Greedy algorithms make the locally optimal choice at each step.

---

# 5(a). Selection Sort

## Theory

Selection Sort is a simple comparison-based sorting algorithm that repeatedly selects the smallest element from the unsorted part of the array and places it at the correct position.

It divides the array into:

Sorted part
Unsorted part

Initially:

Sorted part is empty
Entire array is unsorted

At every iteration:

minimum element is selected
swapped with current position

## Algorithm

1. Start from first index.
2. Find minimum element in remaining array.
3. Swap minimum with current index.
4. Repeat for all elements.

## Time Complexity

Best, Average, Worst:

$$
[
O(n^2)
]

$$
## Space Complexity

$$
[
O(1)
]

$$
---

# 5(b). Prim’s Minimum Spanning Tree Algorithm

## Theory

Prim’s Algorithm is a greedy graph algorithm used to find the Minimum Spanning Tree (MST) of a weighted connected graph.

The algorithm starts from any vertex and repeatedly adds the minimum-weight edge that connects:

a visited vertex
to
an unvisited vertex.

It grows the MST step by step until all vertices are included.

Applications:

* Network design
* Road construction

## Working

1. Start from any vertex.
2. Mark it visited.
3. Find minimum-weight edge connecting visited and unvisited vertices.
4. Add edge to MST.
5. Repeat until all vertices are visited.

## Algorithm
1. Initialize:
    * visited array
    * MST edge list
2. Select starting vertex.
3. Repeat until all vertices included:
    * Find minimum edge from visited → unvisited vertex
    * Add edge to MST
    * Mark new vertex visited

## Time Complexity

Using Priority Queue:

$$
[
O(Elog V)
]
$$

## Space Complexity

$$
[
O(V)
]
$$

---

# 5(c). Kruskal’s Minimum Spanning Tree Algorithm

## Theory

Kruskal’s Algorithm is a greedy graph algorithm used to find the Minimum Spanning Tree (MST) of a weighted connected graph.
The algorithm selects edges in increasing order of weight and adds them to the spanning tree only if they do not form a cycle.
It follows the Greedy approach because at every step it chooses the smallest available edge

* What is Minimum Spanning Tree (MST)?
A Minimum Spanning Tree is:
A subset of graph edges
Connects all vertices
Contains no cycles
Has minimum total edge weight
For a graph with V vertices:
Number of MST edges=V−1

Uses:

* Greedy method
* Union-Find structure

## Algorithm

1. Sort all edges in ascending order of weight.
2. Select the smallest edge.
3. Check whether it forms a cycle.
4. If no cycle:
      include edge in MST
5. Otherwise:
      discard edge
6. Repeat until MST contains V−1 edges.

## Time Complexity
$$
[
O(ElogE)
]
$$
## Space Complexity
$$

[
O(V)
]

$$

# 5(d). Dijkstra’s Shortest Path Algorithm

## Theory

Dijkstra’s Algorithm is a greedy graph search algorithm used to find the shortest path from a source vertex to all other vertices in a weighted graph.

It works only for graphs with:

Non-negative edge weights

The algorithm repeatedly selects the vertex with the minimum temporary distance and updates the distances of its neighboring vertices.

It follows the Greedy approach because at every step it chooses the locally optimal vertex (minimum distance vertex).

## Algorithm

1. Assign infinite distance to all vertices.
2. Set source distance = 0.
3. Pick minimum distance vertex.
4. Update adjacent distances.
5. Repeat.

## Time Complexity

Using Priority Queue:

[
O((V + E)log V)
]

## Space Complexity

[
O(V)
]

---

# 9. N-Queens Problem using CSP, Backtracking and Branch & Bound

## Theory

N-Queens problem places N queens on chessboard such that:

* No two queens share same row
* Same column
* Same diagonal

CSP (Constraint Satisfaction Problem):

* Variables → queen positions
* Constraints → non-attacking conditions

Backtracking:

* Try placing queen row by row
* Backtrack if conflict occurs

Branch & Bound:

* Prune invalid branches early

## Algorithm

1. Start from first row.
2. Place queen in safe column.
3. Recur for next row.
4. If no safe position, backtrack.
5. Continue until all queens placed.

## Time Complexity

Worst case:

[
O(N!)
]

## Space Complexity

[
O(N)
]

(recursion stack)

---

# 10. Graph Coloring using CSP, Backtracking and Branch & Bound

## Theory

Graph coloring assigns colors to vertices such that adjacent vertices have different colors.

CSP Representation:

* Variables → vertices
Variables are the unknowns that need values
* Domain → available colors
Domain is the set of possible values each variable can take.
* Constraints → adjacent vertices differ
Constraints are rules that must be satisfied.

Backtracking:

* Assign colors recursively
* Undo invalid assignments

Branch & Bound:

* Prune states violating constraints

Applications:

* Register allocation
* Scheduling
* Map coloring

## Algorithm

1. Select a vertex.
2. Assign valid color.
3. Recur for next vertex.
4. Backtrack if no color possible.

## Time Complexity

Worst case:

[
O(m^V)
]

Where:

* (m) = number of colors
* (V) = vertices

## Space Complexity

[
O(V)
]
### Backtracking
* Definition: Backtracking is a problem-solving technique where we build a solution step by step and remove choices when they lead to an invalid solution.
It is a recursive search method.
* Working of Backtracking
Choose a possible solution.
Check whether it is valid.
If valid → continue.
If invalid → go back (backtrack) and try another choice.

### Branch and Bound
* Definition: Branch and Bound is an optimization technique that divides a problem into smaller subproblems (branching) and removes unnecessary paths using bounds.
* Working
1. Branching
Divide problem into smaller subproblems.
2. Bounding
Calculate upper/lower bound.
3. Pruning
Discard branches that cannot produce optimal solution

# 11. Elementary Chatbot System for Customer Interaction

## Theory (AI Perspective)

A chatbot is an Artificial Intelligence application designed to simulate human conversation and provide automatic responses to user queries. An elementary chatbot uses simple AI techniques such as rule-based processing and keyword matching to interact with users.

The chatbot accepts user input in natural language, analyzes the keywords or patterns in the sentence, and generates predefined responses. Unlike advanced AI chatbots that use machine learning and deep learning, elementary chatbots rely on manually defined rules and decision logic.

The system is useful for handling:

* Product information
* Service inquiries
* Frequently Asked Questions (FAQs)
* Customer support requests

In Artificial Intelligence, this type of chatbot falls under:

* Natural Language Processing (basic level)
* Expert Systems
* Rule-Based Intelligent Systems

### Working Principle

1. User enters a query.
2. System processes text input.
3. Keywords or rules are identified.
4. Matching response is selected.
5. Response is displayed to the user.

### AI Techniques Used

* Keyword Matching
* Pattern Recognition
* Rule-Based Decision Making
* If-Else Logic
* String Processing

### Advantages

* Fast response generation
* Easy to implement
* Low computational cost
* Useful for repetitive customer queries

### Limitations

* Cannot understand complex language
* No self-learning capability
* Responses are limited to predefined rules
* Cannot handle ambiguous queries effectively

### Applications

* E-commerce support
* Banking help systems
* College inquiry systems
* Online service portals

---

# 12. Rule-Based Elementary Chatbot using Basic AI Techniques

## Theory (AI Perspective)

A rule-based chatbot is a basic Artificial Intelligence system that responds to user queries using predefined rules and conditions. The chatbot works by comparing user input with stored keywords or patterns and then generating suitable responses.

The chatbot does not actually “understand” language like humans. Instead, it uses simple AI methods to identify important words and map them to corresponding replies.

This approach represents one of the earliest forms of conversational AI systems and is widely used in simple customer interaction applications.

## Artificial Intelligence Concepts Involved

### 1. Natural Language Processing (NLP)

Basic NLP techniques are used to process user text input by:

* Converting text to lowercase
* Removing unnecessary symbols
* Splitting sentences into words

### 2. Knowledge Base

The chatbot contains a predefined database of:

* Questions
* Keywords
* Responses

### 3. Rule-Based Inference Engine

The inference engine checks user input against stored rules and selects the appropriate response.

Example:

* If input contains “price” → show product pricing
* If input contains “service” → display service details

### 4. Pattern Matching

The chatbot identifies patterns or keywords in user messages and generates related outputs.

## Working of the System

1. User enters message.
2. Chatbot preprocesses input.
3. System searches for matching keywords/rules.
4. Appropriate response is retrieved.
5. Output is displayed.

## Features

* Interactive customer communication
* FAQ handling
* Simple and efficient design
* Real-time response generation

## Advantages

* Easy implementation
* Minimal memory usage
* Faster execution
* Suitable for small-scale applications

## Disadvantages

* No learning capability
* Limited conversational ability
* Depends completely on predefined rules

## Applications

* Customer care systems
* Online shopping assistants
* Railway/airline inquiry systems
* Educational help desks

## Conclusion

Rule-based chatbots are simple AI systems designed for automated customer interaction. They use predefined rules, keyword matching, and basic NLP techniques to generate responses. Although limited compared to modern intelligent chatbots, they provide an efficient and economical solution for handling common customer queries and FAQs.

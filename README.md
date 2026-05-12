# Salesforce Practical Executions & Lightning App Development
This repository contains Salesforce Apex anonymous execution codes for basic operations and a step-by-step guide to create a custom Lightning Application in Salesforce.
---
# 🚀 How to Run Apex Code (Execute Anonymous Window)
## Steps:
- Go to Setup  
- Open Developer Console  
- Navigate to:

Debug → Open Execute Anonymous Window

- paste the required code  
- click Execute  
---
# ➕ 1. Addition
```apex
Integer ans = AdditionDemo.addNumbers(10, 20);
System.debug('Addition is: ' + ans);

⸻

➖ 2. Subtraction

Integer ans = SubtractionDemo.subtractNumbers(20, 10);
System.debug('Subtraction is: ' + ans);

⸻

✖️ 3. Multiplication

Integer ans = MultiplicationDemo.multiplyNumbers(10, 5);
System.debug('Multiplication is: ' + ans);

⸻

➗ 4. Division

Decimal ans = DivisionDemo.divideNumbers(20, 5);
System.debug('Division is: ' + ans);

⸻

🧮 5. Calculator

Integer add = CalculatorDemo.addNumbers(10, 5);
Integer sub = CalculatorDemo.subtractNumbers(10, 5);
Integer mul = CalculatorDemo.multiplyNumbers(10, 5);
Decimal div = CalculatorDemo.divideNumbers(10, 5);
System.debug('Addition: ' + add);
System.debug('Subtraction: ' + sub);
System.debug('Multiplication: ' + mul);
System.debug('Division: ' + div);

⸻

🔢 6. Table of 5 — Executable Input

TableOfFive.displayTable();

⸻

🔟 7. Table of 10 — Executable Input

TableOfTen.displayTable();

⸻

👋 8. Welcome Message — Executable Input

WelcomeMessage.displayMessage();

⸻

☁️ 9. Design and Develop Custom Application using Salesforce Cloud (Lightning Platform)

⸻

Step 1: Login to Salesforce

Open:
Salesforce Login
Login using your username and password.

⸻

Step 2: Open Setup

* Click ⚙️ Gear Icon (top-right)
* Click:

Setup

⸻

Step 3: Open App Manager

* In Setup search bar, type:

App Manager

* Click:

App Manager

⸻

Step 4: Create Lightning App

* Click:

New Lightning App

⸻

Step 5: Enter App Details

Field	Value
App Name	StudentApp

Developer Name auto-fills automatically.

Click:

Next

⸻

Step 6: App Options

* Navigation Style:

Standard Navigation

* Leave other settings default.
    Click:

Next

⸻

Step 7: Utility Items

* Leave empty
    Click:

Next

⸻

Step 8: Navigation Items

Add these from Available Items → Selected Items:

* Accounts
* Contacts
* Reports

Click:

Next

⸻

Step 9: User Profiles

* Select:

System Administrator

* Move to Selected Profiles
* Click:

Save & Finish

⸻

Step 10: Open the App

* Click App Launcher (9 dots icon)
* Search:

StudentApp

* Open the app

⸻

Step 11: Create Account Record

* Click:

Accounts

* Click:

New

* Enter:
    * Account Name → Test Account
* Click:

Save

⸻

Step 12: Create Contact

* Inside Test Account click:

New Contact

* Enter:
    * First Name → Atharva
    * Last Name → Yadav
* Click:

Save

⸻

Step 13: Create Note

* Click:

New Note

* Enter:

Salesforce Practical Demo

* Save

⸻

Step 14: Demonstrate Search

Use top search bar:

Test Account

Explain:

* “Salesforce provides global search functionality.”

---

AI : to run - python3 fileName.py

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. A* Algorithm for 8-Puzzle
4. Pathfinding in Maze
5. Greedy Algorithms

5(a). Selection Sort
5(b). Prim’s Minimum Spanning Tree Algorithm
5(c). Kruskal’s Minimum Spanning Tree Algorithm
5(d). Dijkstra’s Shortest Path Algorithm

9. N-Queens Problem using CSP, Backtracking and Branch & Bound - nQBack : backtracking ; nQBranch : Branch & Bound
10. Graph Coloring using CSP, Backtracking and Branch & Bound - Backtracking and Branch & Bound : colorBack.py ( same code for both )
11. Elementary Chatbot System for Customer Interaction : bot.py ( same as 12 )
12. Rule-Based Elementary Chatbot using Basic AI Techniques : bot.py ( same as 11 )

-----

CC : SalesForce & Trigger Example 

Real-Life Example: Online Shopping Website

Imagine you order a phone from an online shopping app.

The moment you place the order, many things happen automatically:

1. Your order gets saved.
2. Stock quantity decreases.
3. You receive a confirmation email.
4. Delivery team gets notified.
5. Invoice is generated.

Nobody does this manually every time.

A system automatically reacts when a new order is created.

That automatic reaction is similar to a Trigger in Salesforce.

⸻

Salesforce Example

Suppose a company stores customer data in Salesforce.

When a new customer is added:

* Salesforce automatically sends a welcome email.
* Assigns a sales representative.
* Creates a follow-up reminder.

This automatic process can be written using an Apex Trigger.


----

AI :

I'll walk you through everything in this file, topic by topic, in plain simple language.

---

## 1. BFS (Breadth First Search)

Imagine you're finding a friend in a crowd. You first check everyone standing right next to you, then everyone a little farther, then farther still. That's BFS — it explores **level by level**.

It uses a **Queue** (like a line at a shop — first in, first out).

**Steps:** Start at a node → mark it visited → add neighbors to queue → keep processing until queue is empty.

**When to use:** Finding the shortest path in a map or game (unweighted).

---

## 2. DFS (Depth First Search)

Imagine exploring a maze by always going as deep as possible down one path before turning back. That's DFS — go **deep first, backtrack later**.

It uses a **Stack** or **Recursion**.

**Steps:** Start at a node → go deep into one neighbor → when stuck, backtrack → try another path.

**When to use:** Detecting cycles, solving mazes, topological sorting.

Both BFS and DFS have the same complexity: **O(V+E)** — V for vertices, E for edges.

---

## 3. A* Algorithm (for 8-Puzzle)

The 8-puzzle is a sliding tile game. A* is a smart search that doesn't just blindly explore — it **estimates which path looks most promising** and goes that way first.

It uses the formula: **f(n) = g(n) + h(n)**
- **g(n)** = how far you've already traveled
- **h(n)** = your best guess of how far the goal is (the "heuristic")
- **f(n)** = total estimated cost

Common heuristics: count misplaced tiles, or measure Manhattan distance (how many moves each tile needs).

**When to use:** Games, GPS navigation, robotics.

---

## 4. Maze Pathfinding

Finding a route from start to end in a grid/maze.

- **BFS** → gives the **shortest** path
- **DFS** → gives **any** path (not necessarily shortest)
- **A\*** → gives the **optimal** path smartly

The maze is treated as a grid of cells, and you visit neighboring valid cells until you reach the destination.

---

## 5. Greedy Algorithms

A greedy algorithm always picks **the best-looking option right now**, without worrying about the future. It's fast but doesn't always give the globally best answer.

### 5a. Selection Sort
Repeatedly find the **minimum element** from the unsorted part and put it in its correct place.

Example: `[5, 3, 1, 4]` → find min (1), put first → `[1, 3, 5, 4]` → repeat.

Complexity: always **O(n²)** — slow for large data.

### 5b. Prim's Algorithm (Minimum Spanning Tree)
Goal: connect all cities with **minimum total road length**, no loops.

Strategy: start from any city → always pick the **cheapest edge** that connects a new unvisited city → repeat until all cities are connected.

Complexity: **O(E log V)** with a priority queue.

### 5c. Kruskal's Algorithm (Minimum Spanning Tree)
Same goal as Prim's, different strategy: sort **all edges by weight** → pick the cheapest edge that doesn't create a cycle → repeat until you have V-1 edges.

Uses **Union-Find** to detect cycles efficiently.

Complexity: **O(E log E)**.

### 5d. Dijkstra's Shortest Path
Find the **shortest distance from one source to all other nodes** in a weighted graph (no negative weights allowed).

Strategy: always process the **closest unvisited node** next → update its neighbors' distances → repeat.

Think of it like a GPS finding the fastest route.

Complexity: **O((V+E) log V)**.

---

## 9. N-Queens Problem

Place N chess queens on an N×N board so **no two queens attack each other** (no shared row, column, or diagonal).

- **CSP framing:** each queen's column is a variable, constraints say no two can clash
- **Backtracking:** place a queen row by row → if a conflict is found, go back and try the next column
- **Branch & Bound:** skip (prune) entire branches early if they're already invalid

Worst case complexity: **O(N!)** — gets very slow for large N.

---

## 10. Graph Coloring

Assign colors to graph nodes so that **no two connected nodes share a color**. Classic example: coloring a map so neighboring countries are different colors.

- **Variables** = nodes, **Domain** = available colors, **Constraints** = adjacent nodes differ
- **Backtracking:** assign a color → check constraint → if violated, undo and try next color
- **Branch & Bound:** prune invalid branches early to save time

Used in: CPU register allocation, exam scheduling, map coloring.

Worst case: **O(mᵛ)** where m = colors, V = vertices.

**Backtracking** in simple terms: try → fail → undo → try something else.

**Branch & Bound** in simple terms: split the problem into parts, calculate bounds to skip paths that can't possibly be optimal.

---

## 11 & 12. Rule-Based Chatbot

A basic chatbot that responds to users using **hardcoded rules**, not real AI learning.

**How it works:**
1. User types a message
2. Chatbot converts it to lowercase, cleans it up (basic NLP)
3. Looks for keywords like "price", "service", "help"
4. Matches them to a predefined response
5. Shows the reply

**AI concepts used:** keyword matching, pattern recognition, if-else logic — no machine learning involved.

**Pros:** simple, fast, cheap to build.
**Cons:** can't learn, can't handle complex questions, only knows what you programmed in.

**Used in:** basic customer support portals, FAQ bots, college inquiry systems.

---

That covers the entire file! The topics progress from **graph search** (BFS/DFS/A*) → **greedy optimization** (sorting, MST, shortest path) → **constraint solving** (N-Queens, graph coloring) → **basic AI systems** (chatbots).














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














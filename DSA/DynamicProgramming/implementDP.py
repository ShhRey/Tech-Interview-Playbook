"""
#======================================================= What is Dynamic Programming? ====================================================#
Dynamic Programming is an algorithmic technique used to solve complex problems by breaking them down into smaller sub-problems. 
It is applicable when a problem exhibits the following two properties:
- Overlapping sub problems: Same sub problems are being solved multiple times.
- Optimal Substructure: Optimal solution to the local problem can be constructed from optimal solitions of its sub problems.


#========================================================== What is Memoization? Top-down Approach =======================================================#
Memoization is a technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again.
- It is the idea to remember the computation of each smaller operation and compute its value atmost once. 
- We achieve this by storing the computational value as a memo (by initializing an empty dictionary).
When a sub-problem is encountered, we first check if there is any matching memo entry in the dictionary, if so no computation is required (Lookup in O(1))
If not, comput ethe results, store it in the memo, and then return the same.


#======================================================= What is Tabulation? Bottom-up Approach ====================================================#
Tabulation solves all possible related sub problems first, and uses those results to build up to the solution of the largest problem.
- We achieve this by filling up an n-dimentional table (array).
- Define the base case, and use iterative loops to fill the table based on recurrence relation.
- Final answer is usually the last element in the table

We need to put some thoughts in the order in which we solve sub problems:
- Its important to solve dependencies on a sub problem first, therefore we have to solve them in a topological sorting order.
""" 
# Dynamic Programming
* **Q: What is Dynamic Programming?**

  **Ans:**
    * **It is basically optimized(faster) recursion using a technique called _memoization_.**
  * Every DP algorithm has 2 important component:
    1. Base Case
    2. Recurrence relation

* In recursion, find the solution to the sub-problem multiples time, but in dp we avoid the multiple computations, using a technique
called **memoization**.

* **Q: How is memoization done?**

    **Ans:**
  * In this technique, basically, once we find the answer to a sub-problem, we cache the answer **usually** in a **hashmap (could also be an array)**.
  * And then if the sub-problem appears again then instead of calculating the answer, we first look for the result in the hashmap
  * and if it is present in the hashmap then we return then answer
  * or if it is not present in the hashmap, we calculate the answer and store the result in the hashmap and then return the result from the hashmap.

* **Q: How does memoization help in speeding up the recursion?**

    **Ans:** When we already have the answer to a sub-problem in the hashmap, we don't compute the answer to the sub-problem again but instead look for
it in the hashmap in O(1) time complexity.

## Dynamic Programming can be solved using 2 Approaches:
### 1. Top-Down Approach
* This involves using **memoization** technique.
* Here, we start from the original problem and then move down towards the sub-problems in each recursive call.
### 2. Bottom-Up Approach
* This involves using **tabulation** technique.
* Here, we start from the base case solution and move up towards the original problem.

**Note 1: Every DP problem can be solved using both approaches as above.**

**Note 2: The top-down and bottom-up approaches are same in the terms of time complexity.**

**Note 3: The bottom-up approach is better than top-down approach in terms of space complexity.**

## When should we use Dynamic Algorithm?
Most of the DP problems have 2 important characteristics:
1. **The problem will be asking for an optimal value (max/longest or min/shortest) of doing something**

   **OR the number of ways to do something.**

**Examples:**
* What is the minimum cost of doing ...
* What is the maximum profit of ...
* How many ways are there to ...
* What is the longest possible ...
2. At each step of the problem, we would need to decide something and this decision would affect the future decisions.
* A decision could be picking between two elements
* Decisions affecting future decisions could be something like "if you take an element `x`, then you can't take an element `y` in the future"

## Difference between Greedy Algorithm and Dynamic Programming Algorithm
In the Greedy Algorithm, **we always pick the local optimal solution** whereas in the DP Algorithm, that is not the case.

## State
**Q: What is a State?**

**Ans:** **A state is a set of variables** that fully defines a sub-problem or a scenario.

Most common state variables are:
1. An **index** of the input array or a number. This will be a state variable for all the DP problems.
   1. For input array, index i represents the subarray from 0 to i (including)
2. A second index of the input array or string.
   1. If there are 2 indices in the state variable, then these i and j represent the subarray from i to j (both inclusive)
3. Numerical constraint given in the problem.
   1. This is usually given as the input to the problem
4. A boolean to describe a status.

#### Important 1: The first step of creating a DP Algorithm is defining the necessary state variables
#### Important 2: The number of state variables define the dimensionality of the DP Algorithm.

### Steps to Solve a Problem using DP Algorithm (Top-Down Approach)
1. Determine if the problem is about finding the optimal solution or number of solutions.
2. Define the **function** that computes the solution of the sub-problem. We should also determine what is the function is returning.
3. Define the **State variables** for the sub-problem.
4. The arguments to the function are the state variables defined in the step 3.
5. **A recurrence relation for the problem.**
   1. For example: With Fibonacci, the recurrence relation was **_Fn = F n−1 +  Fn−2_**
   2. **This is the most tricky part of the DP Algorithm**
6. **Base Cases** of the problem

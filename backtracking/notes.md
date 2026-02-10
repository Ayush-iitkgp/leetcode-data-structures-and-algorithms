# Backtracking

* Backtracking is an **optimized way to solve a problem** that involves exploring all the possible solutions.
* It **involves an optimization where we stop exploring a possible solution** once we establish that the
possible solution will not lead to the desired solution.
* Abandoning a solution is also called **pruning**.

**Question: What is the difference between exhaustive search and backtracking?**

**Ans:** **In exhaustive search**, we first generate all the possible solutions and then check if they belong to a solution or not.
Where as, in backtracking, we don't explore all the possible solutions.

**Note:** Use backtracking, when we want to explore all the possible solutions.

**Note:** If the size of the input is very small (n <= 15), then backtracking is most likely the solution.

**Note:** The time complexity of a backtracking algorithm is **exponential or factorial**.

## Implementation

* Backtracking is always implemented using **recursion**.
* **Backtracking algorithms are always visualised using Tree**.
* In backtracking, after calling the same function with the child node, **there is always a
next line of code** and this new line is the key to backtracking.
* Usually, the root node in the backtrack algo is **an empty array or an empty string**.

```python
# curr represent the thing you are building
# it could be an array or a combination of state variables

function backtrack(curr) {
    if (base case) {
        Increment or add to answer
        return
    }

    for (iterate over input) {
        Modify curr
        backtrack(curr)
        Undo whatever modification was done to curr
    }
}
```

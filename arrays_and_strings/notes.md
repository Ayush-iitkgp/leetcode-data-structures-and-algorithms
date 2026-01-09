# Arrays and Strings

They represent an **ordered** iterable.

**Question: What is an Ordered Iterable?**
**Ans**: List, Tuple and String are Ordered Iterable where as Dict is an un-ordered iterable.

**_Important:_**
1. Array are **MUTABLE** where as Strings are **IMMUTABLE** in Python.
```
arr = ["b", "c", "d"]
arr[1] = "x" # This is OK
str = "bcd"
str[1] = "x" # This would result in an error.
 ```
2. **Appending and deleting (pop) from the end of the array is O(1).**

**Arrays and Strings problems are usually solved using:**
1. Two Pointers Approach
2. Sliding Window Approach
3. Prefix Sum

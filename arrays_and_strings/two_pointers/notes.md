# Two Pointers Approach

This approach involves having two integer variables that both move along an iterable.

The 2 most use case of this approach is:
1. The two variables point to the start and the end of a single iterable.
2. The two variables point to the start/end of two different iterables.

## Use Case 1: The two variables point to the start and the end of a single iterable
**Summary: Start the pointers at the edges of the input. Move them towards each other until they meet.**
1. Start one pointer `(name left)` at the first index 0 and the other pointer `(named right)` at the last index. 
2. Use a while loop until the pointers are equal to each other. 
3. At each iteration of the loop, move the pointers towards each other. This means either increment the left, decrement right, or both. 
**Note:** Deciding which pointers to move will depend on the problem we are trying to solve.

#### Examples: 
1. Given a string s, return true if it is a palindrome, false otherwise.
2. Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

## Use Case 2: The two variables point to the start/end of two different iterables.
**Summary: Move along both inputs simultaneously until all elements have been checked.**
1. Create two pointers, one for each iterable. Each pointer should start at the first index.
2. Use a while loop until one of the pointers reaches the end of its iterable.
3. At each iteration of the loop, move the pointers forward. This means incrementing either one of the pointers or both of the pointers. 
**Note:** Deciding which pointers to move will depend on the problem we are trying to solve.
**Note:** Because our while loop will stop when one of the pointers reaches the end, the other pointer will not be at the end of its respective iterable when the loop finishes. Sometimes, we need to iterate through all elements - if this is the case, you will need to write extra code here to make sure both iterables are exhausted.

#### Examples:
1. Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
2. Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

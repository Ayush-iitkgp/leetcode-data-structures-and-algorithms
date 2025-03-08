# Prefix Sum

* Can be used on arrays of numbers (int/float).
* The idea is to have **pre-processing** step where we create another array called **prefix** where prefix[i]
is the sum of all the elements upto index i (inclusive) of the original array.
* Prefix sum allows us to find the sum of the subarray in O(1).
* Now, if we want to calculate the sum of the subarray from index i to index j, it is `prefix[j] - prefix[i] + array[i]`

**Note 1: Prefix sum is used when the problem involves sum/product of subarrays.**

**Note 2:** Prefix sum usually **reduces** the time complexity of a problem by O(n).

**Note 3:** Prefix sum also uses O(n) space.

### Examples
1. Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array
that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit,
or false otherwise.
2. **Number of Ways to Split Array**: Given an integer array nums, find the number of ways to split the array into two
parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
3. Running Sum of 1d Array

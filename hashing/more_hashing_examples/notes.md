# More hashing Examples

1. **Group Anagrams**

2. **Minimum Consecutive Cards to Pick Up**
**Problem Statement:** _Given an integer array cards, find the length of the shortest subarray that 
contains at least one duplicate. If the array has no duplicates, return -1._

**Solution 1:** Can we solved using Sliding Window but time complexity is O(n^2)

**Solution 2:** Can be solved using **Hash Map** in O(n)
Approach: Find the indices of each unique cards and store it in a hashmap. The answer would be the minimum of the shortest distance.


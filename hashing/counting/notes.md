# Counting

## Use Case 1: Counting/Frequency
* If you need to count anything/find frequency, think of using hash map or set.

## Examples
1. Longest substring that contains at most k distinct characters (Sliding Window + Counting)
2. **[Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/description/)**
3. **[Check if All Characters Have Equal Number of Occurrences](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/)**

## Use Case 2: Count the number of sub-arrays with an "EXACT" constraint
* This is different from using sliding window to find number of sub-arrays that fit a constraint.
* **For example:**
  1. Finding number of sub-arrays whose **sum is less than K** given **the input is only positive integers** is solved using **Sliding Window.**
  2. But finding number of sub-arrays whose **sum is exactly equal to K** given the input could be positive or negative integer is solved using **HashMaps.**

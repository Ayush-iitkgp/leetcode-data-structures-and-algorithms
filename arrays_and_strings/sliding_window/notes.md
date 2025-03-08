# Sliding Window

This approach also involves having 2 pointers.

This approach mostly applies to Sub-arrays.

**Q: What is a Subarray?**

Ans: A subarray is a small part of the array where the elements in it are in the same order as the original array and they are contiguous to each other in the original array.

A sub-array can be defined by 2 pointers left and right. This subarray is called **window**.

## When should we use Sliding Window?
1. It is used for the problems where a constraint is defined about a subarray and it is asked to **find a valid subarray**.
2. It is the used for the problem for **finding the number of valid sub-arrays**.

## Use Case 1: Find the best (longest) valid subarray
**Summary: Start left and right at the start of the original array. And then iterate over right and find the left for each right where the array becomes valid.**
1. Start the `left` and the `right` pointer at index 0 of the original array.
2. Iterate right from 0 to len(input array).
3. For each iteration, include right in the subarray and re-calculate the constraint.
4. If the subarray becomes invalid, we need to remove elements from the subarray which is done by increasing the `left` pointer (one or multiple times).
5. We will use while loop to increase left as long as the new window (subarray) satisfies the constraint.
6. For each value of `right`, The subarray becomes valid after `left` has been incremented or while lop has been completed.

**Note:** If the subarray becomes invalid we might have to increase left onr or more times.

#### Examples:
1. Find the longest subarray with a sum less than or equal to k
2. Find the smallest subarray with a sum greater than or equal to k
3. Find the longest substring that has at most one "0"
4. Find the subarray of size K with the highest sum/average

## Use Case 2: Find number of valid sub-arrays

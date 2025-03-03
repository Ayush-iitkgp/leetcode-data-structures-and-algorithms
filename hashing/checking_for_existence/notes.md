# Checking for existence

One of the most common applications of a hash table or set is determining if an element exists in O(1). Usually,
the problem would be solved in O(n^2) but with hashing we can solve it in O(n)

This approach involves iterating over the array and building a hash map that will be used for existence.

#### Examples: 
1. **Two Sum:** Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target.
2. **First Letter to Appear Twice:** Given a string s, return the first character to appear twice.
3. Check if a sentence is a Pangram

**Important:**
**Anytime you find your algorithm running `if ... in ...`, use hash map or set**
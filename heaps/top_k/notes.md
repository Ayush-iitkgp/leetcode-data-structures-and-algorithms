# Top K

* Heap is also used in the problem statement where we are asked to find **top (best) K** elements based on the criteria defined in the problem statement.
* The easiest way is to sort the elements and pick the top K elements which has time complexity of `O(n log n)`.
* However, using heap we can solve the problem is `O(n log k)`.

## How to use Heap to find Top K elements?
1. Create a max/min heap at the start.
2. Iterate over the input while pushing every element on the heap (according to the problem's criteria)
3. Pop from the heap once the size exceeds K.
4. Since, we are popping the worst elements from the heap, at the end top K elements remain in the heap.

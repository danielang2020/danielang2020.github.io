# Grokking Algorithms
## 1. Introduction to Algorithms
### Binary Search
> the high performance method to get the middle value between low and high is to use **(low + high) >>> 1** instead of (low + high) / 2, because the former is faster and doesn't cause overflow.

> In general, for any list of n, binary search will take **$\log_2 n$** steps to run in the worst case, whereas simple search will take n steps.

> Binary search only works on when your list is sorted.

```java
Arrays.binarySearch(list, item);
Collections.binarySearch(list, item);
```

```python
bisect.bisect_left(list, item);
```

### Big O Notation
> Big O notation is special notation that tells you how fast an algorithm is.

> Big O notation is about the worst-case scenario.

## 2. Selection Sort
> O(n) time means you touch every element in a list once.

## 3. Recursion
> There's no performance benefit to using recursion; in fact, loops are sometimes better for performance.

### The Stack
> This stack, used to save the variables for multiple functions, is called the call stack.

> Using the stack is convenient, but there's a cost: saving all that info can take up a lot of memory.

## 4. Quicksort
### Quicksort
> Quicksort is a sorting algorithm. It's much faster than selection sort and is frequently used in real life.

> If you always choose a random element in the array as the pivot, quicksort will complete in O(n log n) time on average.

## 5. Hash Tables
### Hash Functions
> A hash function is a function where you put in a string and you get back a number.

## 6. Breadth-First Search
> There are the two questions that breadth-first search can answer for you:
>1. Is there a path from node A to node B?
>2. What is the shortest path from node A to node B?

> if you have a problem like "find the shortest X," try modeling your problem as a graph, and use breadth-first search to solve.

## 7. Dijkstra's Algorithm

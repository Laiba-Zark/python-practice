# Array Practice Problems (Beginner → Advanced)
## Complete 60-Problem Set with Samples, Explanations & Use Cases

---

## 🟢 BEGINNER LEVEL (Problems 1–20)

### Problem 1: Reverse the Array
**Problem Description**
Given an array of integers, reverse the order of its elements.

**Input Format**
- Line 1: Integer n (array size)
- Line 2: n space-separated integers

**Output Format**
Print the reversed array as space-separated integers.

**Sample Input**
```
5
1 2 3 4 5
```

**Sample Output**
```
5 4 3 2 1
```

**Explanation**
The first element becomes the last and the last becomes the first. Each element's position is mirrored around the center.

**Where it is used**
Undo operations, reversing logs, preprocessing data, browser history reversal.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 2: Find the Maximum Element
**Problem Description**
Find the largest element present in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the maximum value.

**Sample Input**
```
6
3 7 2 9 4 1
```

**Sample Output**
```
9
```

**Explanation**
9 is greater than all other elements. Iterate through the array and track the maximum.

**Where it is used**
Leaderboards, analytics, sensor monitoring, peak detection.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 3: Find the Minimum Element
**Problem Description**
Find the smallest element in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the minimum value.

**Sample Input**
```
5
8 6 4 10 2
```

**Sample Output**
```
2
```

**Explanation**
2 is smaller than all other elements. Track the minimum as you iterate.

**Where it is used**
Risk analysis, minimum cost calculations, threshold detection.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 4: Sum of Array Elements
**Problem Description**
Calculate the sum of all elements in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the sum.

**Sample Input**
```
4
5 10 15 20
```

**Sample Output**
```
50
```

**Explanation**
5 + 10 + 15 + 20 = 50. Accumulate all values.

**Where it is used**
Finance totals, scoring systems, batch processing, average calculations.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 5: Count Even Numbers
**Problem Description**
Count how many even numbers exist in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the count of even numbers.

**Sample Input**
```
6
1 2 3 4 5 6
```

**Sample Output**
```
3
```

**Explanation**
Even numbers: 2, 4, 6 = 3 total. Check if each element modulo 2 equals 0.

**Where it is used**
Data filtering, statistics, partitioning algorithms.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 6: Count Odd Numbers
**Problem Description**
Count how many odd numbers exist in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the count of odd numbers.

**Sample Input**
```
5
1 3 5 2 4
```

**Sample Output**
```
3
```

**Explanation**
Odd numbers: 1, 3, 5 = 3 total. Check if each element modulo 2 equals 1.

**Where it is used**
Classification tasks, parity checking, algorithm analysis.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 7: Find the Runner-Up Score
**Problem Description**
Find the second highest distinct element in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the second maximum distinct value.

**Sample Input**
```
5
2 3 6 6 5
```

**Sample Output**
```
5
```

**Explanation**
Distinct values sorted descending: 6, 5, 3, 2. The second highest is 5.

**Where it is used**
Ranking systems, leaderboards, competition scoring.

**Time Complexity:** O(n log n) | **Space Complexity:** O(n)

---

### Problem 8: Check if Array is Sorted
**Problem Description**
Check whether the array is sorted in non-decreasing order.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print "True" if sorted, "False" otherwise.

**Sample Input**
```
5
1 2 2 4 6
```

**Sample Output**
```
True
```

**Explanation**
Each element is ≥ the previous. All conditions met: 1 ≤ 2 ≤ 2 ≤ 4 ≤ 6.

**Where it is used**
Sorting optimizations, validation checks, binary search prerequisites.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 9: Linear Search
**Problem Description**
Search for a given element in the array and return its index (or -1 if not found).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer x (element to search)

**Output Format**
Print the index of the element if found, else -1.

**Sample Input**
```
5
4 2 7 1 9
7
```

**Sample Output**
```
2
```

**Explanation**
Element 7 is at index 2 (0-indexed). Iterate and compare until found.

**Where it is used**
Unsorted data lookups, cache searches, small dataset searches.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 10: Count Frequency of an Element
**Problem Description**
Count how many times a given value appears in the array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer x (element to count)

**Output Format**
Print the frequency of x.

**Sample Input**
```
6
1 2 3 2 2 4
2
```

**Sample Output**
```
3
```

**Explanation**
2 appears 3 times. Count all occurrences of the target element.

**Where it is used**
Histograms, voting systems, data analysis, mode calculation.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 11: Rotate Array Left by One
**Problem Description**
Rotate the array left by one position (first element moves to end).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the rotated array.

**Sample Input**
```
5
1 2 3 4 5
```

**Sample Output**
```
2 3 4 5 1
```

**Explanation**
Element at index 0 moves to the end, all others shift left.

**Where it is used**
Queue simulations, circular buffer operations, carousel effects.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 12: Rotate Array Right by One
**Problem Description**
Rotate the array right by one position (last element moves to front).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the rotated array.

**Sample Input**
```
5
1 2 3 4 5
```

**Sample Output**
```
5 1 2 3 4
```

**Explanation**
Last element moves to the front, all others shift right.

**Where it is used**
Circular buffers, deque operations, right-shift algorithms.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 13: Copy an Array
**Problem Description**
Copy all elements from one array to another.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the copied array.

**Sample Input**
```
4
10 20 30 40
```

**Sample Output**
```
10 20 30 40
```

**Explanation**
Create a new array with identical elements in the same order.

**Where it is used**
Backups, cloning data, state preservation, deep copying.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 14: Replace All Elements with Zero
**Problem Description**
Replace every element in the array with zero.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the array with all zeros.

**Sample Input**
```
5
5 10 15 20 25
```

**Sample Output**
```
0 0 0 0 0
```

**Explanation**
Set each element to 0.

**Where it is used**
Memory reset, cache clearing, initialization routines.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 15: Count Positive and Negative Numbers
**Problem Description**
Count positive and negative numbers separately (zero is neither).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print count of positive and negative numbers.

**Sample Input**
```
7
5 -3 0 -2 7 0 -1
```

**Sample Output**
```
Positive: 2
Negative: 3
```

**Explanation**
Positives: 5, 7 (count=2). Negatives: -3, -2, -1 (count=3). Zeros ignored.

**Where it is used**
Profit/loss analysis, financial statements, sign classification.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 16: Print Alternate Elements
**Problem Description**
Print every alternate element starting from index 0 (indices 0, 2, 4, ...).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print alternate elements.

**Sample Input**
```
7
10 20 30 40 50 60 70
```

**Sample Output**
```
10 30 50 70
```

**Explanation**
Elements at indices 0, 2, 4, 6 are printed.

**Where it is used**
Sampling techniques, downsampling, pattern extraction.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 17: Check Palindrome Array
**Problem Description**
Check whether the array reads the same forward and backward.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print "True" if palindrome, "False" otherwise.

**Sample Input**
```
5
1 2 3 2 1
```

**Sample Output**
```
True
```

**Explanation**
Array reads same in both directions. Compare from both ends inward.

**Where it is used**
Pattern detection, symmetry checking, validation.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 18: Sum of Even Indexed Elements
**Problem Description**
Calculate the sum of elements at even indices (0, 2, 4, ...).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the sum.

**Sample Input**
```
6
10 20 30 40 50 60
```

**Sample Output**
```
90
```

**Explanation**
Indices 0, 2, 4: values 10, 30, 50. Sum = 90.

**Where it is used**
Subset calculations, even-position aggregation, weighted sums.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 19: Sum of Odd Indexed Elements
**Problem Description**
Calculate the sum of elements at odd indices (1, 3, 5, ...).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the sum.

**Sample Input**
```
6
10 20 30 40 50 60
```

**Sample Output**
```
120
```

**Explanation**
Indices 1, 3, 5: values 20, 40, 60. Sum = 120.

**Where it is used**
Subset calculations, odd-position aggregation.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 20: Find Index of Maximum Element
**Problem Description**
Print the index of the maximum element (0-indexed).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the index of the maximum element.

**Sample Input**
```
6
3 7 2 9 4 1
```

**Sample Output**
```
3
```

**Explanation**
Maximum element is 9 at index 3.

**Where it is used**
Peak detection, argmax operations, pivot selection.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

## 🟡 INTERMEDIATE LEVEL (Problems 21–45)

### Problem 21: Move All Zeros to End
**Problem Description**
Move all zeros to the end while maintaining the relative order of non-zero elements.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the array with zeros at the end.

**Sample Input**
```
7
1 0 2 0 3 4 0
```

**Sample Output**
```
1 2 3 4 0 0 0
```

**Explanation**
Non-zero elements maintain order; all zeros move to end.

**Where it is used**
Sparse array optimization, matrix operations, data compaction.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 22: Remove Duplicates from Sorted Array
**Problem Description**
Remove duplicate elements from a sorted array and return the count of unique elements.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated sorted integers

**Output Format**
Print the count of unique elements and the modified array.

**Sample Input**
```
8
1 1 2 2 2 3 4 4
```

**Sample Output**
```
Count: 4
1 2 3 4
```

**Explanation**
Unique elements: 1, 2, 3, 4. Duplicates removed.

**Where it is used**
Database normalization, set operations, duplicate handling.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 23: Two Sum Problem
**Problem Description**
Check if two elements in the array sum to a given target value.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer target

**Output Format**
Print "True" if pair exists, "False" otherwise.

**Sample Input**
```
6
2 7 11 15 3 6
9
```

**Sample Output**
```
True
```

**Explanation**
Pair (2, 7) sums to 9. Can also be (3, 6).

**Where it is used**
Fraud detection, reconciliation, two-pointer problems.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 24: Merge Two Sorted Arrays
**Problem Description**
Merge two sorted arrays into one sorted array.

**Input Format**
- Line 1: Integer n (size of first array)
- Line 2: n space-separated sorted integers
- Line 3: Integer m (size of second array)
- Line 4: m space-separated sorted integers

**Output Format**
Print the merged sorted array.

**Sample Input**
```
3
1 3 5
4
2 4 6 8
```

**Sample Output**
```
1 2 3 4 5 6 8
```

**Explanation**
Use two pointers to merge while maintaining sorted order.

**Where it is used**
Merge sort, database joins, stream processing.

**Time Complexity:** O(n + m) | **Space Complexity:** O(n + m)

---

### Problem 25: Majority Element
**Problem Description**
Find the element appearing more than n/2 times (guaranteed to exist).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the majority element.

**Sample Input**
```
7
3 3 4 2 3 3 3
```

**Sample Output**
```
3
```

**Explanation**
3 appears 5 times, which is > 7/2. Use Boyer-Moore voting.

**Where it is used**
Elections, consensus protocols, dominant pattern detection.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 26: Find Missing Number (1 to n)
**Problem Description**
Find the missing number in a sequence from 1 to n.

**Input Format**
- Line 1: Integer n (range 1 to n, one missing)
- Line 2: n-1 space-separated integers

**Output Format**
Print the missing number.

**Sample Input**
```
5
1 2 3 5
```

**Sample Output**
```
4
```

**Explanation**
Expected sum of 1 to n is n*(n+1)/2. Subtract actual sum to find missing.

**Where it is used**
Data integrity checks, gap detection, reconciliation.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 27: Prefix Sum Array
**Problem Description**
Construct a prefix sum array where each element is the sum of all elements up to that index.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the prefix sum array.

**Sample Input**
```
5
1 2 3 4 5
```

**Sample Output**
```
1 3 6 10 15
```

**Explanation**
prefix[0]=1, prefix[1]=1+2=3, prefix[2]=1+2+3=6, etc.

**Where it is used**
Range queries, cumulative frequency, sliding window.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 28: Range Sum Query
**Problem Description**
Answer multiple range sum queries using a prefix sum array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer q (number of queries)
- Next q lines: Two integers l, r (left and right indices)

**Output Format**
For each query, print the sum of elements from index l to r.

**Sample Input**
```
5
1 2 3 4 5
3
0 2
1 3
2 4
```

**Sample Output**
```
6
9
12
```

**Explanation**
Query 1: sum(0 to 2) = 1+2+3 = 6. Build prefix array first for O(1) per query.

**Where it is used**
Analytics, report generation, 2D matrix operations.

**Time Complexity:** O(n + q) | **Space Complexity:** O(n)

---

### Problem 29: Kadane's Algorithm
**Problem Description**
Find the maximum sum of a contiguous subarray.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the maximum subarray sum.

**Sample Input**
```
6
-2 1 -3 4 -1 2
```

**Sample Output**
```
5
```

**Explanation**
Subarray [4, -1, 2] has max sum 5. Track max_sum and current_sum.

**Where it is used**
Stock trading, portfolio optimization, time-series analysis.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 30: Longest Increasing Subarray
**Problem Description**
Find the length of the longest subarray where each element is strictly greater than the previous.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the length of the longest increasing subarray.

**Sample Input**
```
8
1 3 4 2 5 6 7 1
```

**Sample Output**
```
4
```

**Explanation**
Subarray [2, 5, 6, 7] is longest strictly increasing with length 4.

**Where it is used**
Trend detection, growth analysis, monotonic sequences.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 31: Intersection of Two Arrays
**Problem Description**
Find all elements that appear in both arrays.

**Input Format**
- Line 1: Integer n (size of first array)
- Line 2: n space-separated integers
- Line 3: Integer m (size of second array)
- Line 4: m space-separated integers

**Output Format**
Print common elements (no duplicates).

**Sample Input**
```
4
1 2 3 4
5
3 4 5 6 7
```

**Sample Output**
```
3 4
```

**Explanation**
Elements 3 and 4 are in both arrays.

**Where it is used**
Set operations, matching records, data comparison.

**Time Complexity:** O(n + m) | **Space Complexity:** O(min(n, m))

---

### Problem 32: Union of Two Arrays
**Problem Description**
Find all unique elements from both arrays combined.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer m
- Line 4: m space-separated integers

**Output Format**
Print all unique elements.

**Sample Input**
```
4
1 2 3 4
5
3 4 5 6 7
```

**Sample Output**
```
1 2 3 4 5 6 7
```

**Explanation**
All unique elements from both arrays in sorted order.

**Where it is used**
Combining datasets, aggregate analysis, set theory.

**Time Complexity:** O(n + m) | **Space Complexity:** O(n + m)

---

### Problem 33: Sort Array of 0s, 1s, and 2s
**Problem Description**
Sort an array containing only 0s, 1s, and 2s in O(n) time (Dutch National Flag problem).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers (0, 1, or 2)

**Output Format**
Print the sorted array.

**Sample Input**
```
8
0 1 2 1 0 2 1 0
```

**Sample Output**
```
0 0 0 1 1 1 2 2
```

**Explanation**
Three pointers: partition by moving 0s left and 2s right.

**Where it is used**
Quicksort partitioning, flag-based sorting, tri-state systems.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 34: Longest Subarray with Sum K
**Problem Description**
Find the length of the longest subarray with a given sum K.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer k (target sum)

**Output Format**
Print the length of the longest subarray.

**Sample Input**
```
7
15 2 4 8 9 5 10
12
```

**Sample Output**
```
2
```

**Explanation**
Subarray [2, 4, 8] has sum 14 (not 12). Subarray [4, 8] sums to 12 with length 2.

**Where it is used**
Window-based queries, anomaly detection, balance tracking.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 35: Product of Array Except Self
**Problem Description**
For each index i, compute the product of all elements except arr[i].

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the result array.

**Sample Input**
```
4
1 2 3 4
```

**Sample Output**
```
24 12 8 6
```

**Explanation**
result[0] = 2*3*4 = 24, result[1] = 1*3*4 = 12, etc. Use left-right prefix products.

**Where it is used**
Tensor operations, polynomial evaluation, scaled metrics.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 36: Find Peak Element
**Problem Description**
Find an element that is greater than its neighbors (local maximum).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the peak element.

**Sample Input**
```
5
1 3 4 2 5
```

**Sample Output**
```
4
```

**Explanation**
4 is greater than neighbors 3 and 2. Use binary search for O(log n).

**Where it is used**
Signal processing, mountain peaks, optimization problems.

**Time Complexity:** O(log n) | **Space Complexity:** O(1)

---

### Problem 37: Rearrange Array Alternately (Max-Min)
**Problem Description**
Rearrange array so elements alternate between largest and smallest remaining.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the rearranged array.

**Sample Input**
```
6
1 2 3 4 5 6
```

**Sample Output**
```
6 1 5 2 4 3
```

**Explanation**
Max (6), Min (1), Max (5), Min (2), Max (4), Min (3).

**Where it is used**
Data shuffling, aesthetic arrangement, alternating patterns.

**Time Complexity:** O(n log n) | **Space Complexity:** O(n)

---

### Problem 38: Subarray with Maximum Product
**Problem Description**
Find the maximum product of a contiguous subarray.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the maximum product.

**Sample Input**
```
6
2 3 -2 4 -1 2
```

**Sample Output**
```
24
```

**Explanation**
Subarray [2, 3, -2, 4] has product 2*3*(-2)*4 = -48. Subarray [4, -1] = -4. Best is subarray [-2, 4, -1, 2] ending at 2: -2*4 = -8, then -8*-1 = 8, then 8*2 = 16. Or [3, -2] = -6. Track both max and min (negatives can flip).

**Where it is used**
Growth rate analysis, compounding calculations.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 39: Leaders in an Array
**Problem Description**
Find elements that are greater than all elements to their right.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print leaders from left to right.

**Sample Input**
```
6
16 17 4 3 5 2
```

**Sample Output**
```
17 5 2
```

**Explanation**
17 > all to right. 5 > 2. 2 is last (always leader). Iterate right to left.

**Where it is used**
Hierarchy detection, domination analysis, threshold crossing.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 40: Minimum Number of Jumps to Reach End
**Problem Description**
Given array where each element is max jump length, find minimum jumps to reach last index.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers (jump lengths)

**Output Format**
Print the minimum number of jumps.

**Sample Input**
```
6
2 3 1 1 4 1
```

**Sample Output**
```
2
```

**Explanation**
Jump 1 step to index 1 (value 3), then 3 steps to index 4 (value 4), reach index 5. Total: 2 jumps.

**Where it is used**
Game level design, pathfinding, energy optimization.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 41: Find Duplicate Number
**Problem Description**
Find a duplicate number in array of n+1 integers (range 1 to n).

**Input Format**
- Line 1: Integer n
- Line 2: n+1 space-separated integers

**Output Format**
Print the duplicate number.

**Sample Input**
```
5
1 3 4 2 2
```

**Sample Output**
```
2
```

**Explanation**
2 appears twice. Use Floyd's cycle detection (tortoise-hare).

**Where it is used**
Data integrity, error detection, constraint validation.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 42: Find All Subarrays with Zero Sum
**Problem Description**
Find all subarrays that sum to zero.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print count of subarrays with zero sum.

**Sample Input**
```
6
15 -2 2 -8 1 7
```

**Sample Output**
```
2
```

**Explanation**
Subarray [-2, 2] sums to 0. Subarray [-8, 1, 7] sums to 0. Count = 2.

**Where it is used**
Anomaly detection, balance tracking, portfolio hedging.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 43: Count Subarrays with Given Sum
**Problem Description**
Count subarrays that sum to a target value.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer target_sum

**Output Format**
Print the count.

**Sample Input**
```
5
1 1 1 1 1
3
```

**Sample Output**
```
3
```

**Explanation**
Subarrays: [1,1,1] at positions (0-2), (1-3), (2-4). Count = 3.

**Where it is used**
Analytics, financial reconciliation, prefix-sum queries.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 44: Kth Smallest Element
**Problem Description**
Find the kth smallest element in an unsorted array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer k

**Output Format**
Print the kth smallest element.

**Sample Input**
```
6
3 2 1 5 6 4
2
```

**Sample Output**
```
2
```

**Explanation**
Sorted: [1, 2, 3, 4, 5, 6]. 2nd smallest is 2. Use quickselect for O(n) average.

**Where it is used**
Percentile calculations, selection problems, streaming data.

**Time Complexity:** O(n) average, O(n²) worst | **Space Complexity:** O(1)

---

### Problem 45: Equilibrium Index
**Problem Description**
Find indices where sum of left elements equals sum of right elements.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print all equilibrium indices.

**Sample Input**
```
7
-7 1 5 2 -4 3 0
```

**Sample Output**
```
3 6
```

**Explanation**
At index 3: left sum = -7+1+5 = -1... Actually: At index 3 (value 2): left = -7+1+5 = -1, right = -4+3+0 = -1. At index 6: left sum = -7+1+5+2-4+3 = 0, right = 0.

**Where it is used**
Balance point detection, center-of-mass calculations.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

## 🔴 ADVANCED LEVEL (Problems 46–60)

### Problem 46: Trapping Rain Water
**Problem Description**
Calculate total water trapped after raining on an elevation map (array heights).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers (heights)

**Output Format**
Print total trapped water.

**Sample Input**
```
9
0 1 0 2 1 0 1 3 2 1 2 1
```

**Sample Output**
```
6
```

**Explanation**
Use two pointers tracking left/right max. Water at position i = min(left_max, right_max) - height[i].

**Where it is used**
Simulation, urban planning models, fluid mechanics, geographical analysis.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 47: Container With Most Water
**Problem Description**
Find two lines that together with the x-axis form a container holding maximum water.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers (heights)

**Output Format**
Print the maximum water capacity.

**Sample Input**
```
9
1 8 6 2 5 4 8 3 7
```

**Sample Output**
```
49
```

**Explanation**
Lines at indices 1 (height 8) and 8 (height 7), distance = 7, capacity = min(8,7) * 7 = 49.

**Where it is used**
Optimization problems, two-pointer algorithms, geometric computations.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 48: Maximum Circular Subarray Sum
**Problem Description**
Find maximum sum subarray in a circular array (can wrap around).

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the maximum sum.

**Sample Input**
```
5
5 -3 5 -1 8
```

**Sample Output**
```
15
```

**Explanation**
Circular subarray [8, 5, -3, 5] has sum 15. Use Kadane + total_sum approach.

**Where it is used**
Ring buffer analysis, circular data processing, round-robin scheduling.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 49: Kth Largest Element
**Problem Description**
Find the kth largest element in an unsorted array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer k

**Output Format**
Print the kth largest element.

**Sample Input**
```
6
3 2 1 5 6 4
2
```

**Sample Output**
```
5
```

**Explanation**
Sorted descending: [6, 5, 4, 3, 2, 1]. 2nd largest is 5. Use min-heap of size k.

**Where it is used**
Leaderboards, top-k problems, streaming percentiles.

**Time Complexity:** O(n log k) with heap | **Space Complexity:** O(k)

---

### Problem 50: Median of Two Sorted Arrays
**Problem Description**
Find the median of two sorted arrays.

**Input Format**
- Line 1: Integer n (size of first array)
- Line 2: n space-separated sorted integers
- Line 3: Integer m (size of second array)
- Line 4: m space-separated sorted integers

**Output Format**
Print the median (as float if even length).

**Sample Input**
```
2
1 3
2
2 4
```

**Sample Output**
```
2.5
```

**Explanation**
Merged: [1, 2, 3, 4]. Median = (2 + 3) / 2 = 2.5. Use binary search.

**Where it is used**
Statistical analysis, data aggregation, streaming statistics.

**Time Complexity:** O(log(min(n, m))) | **Space Complexity:** O(1)

---

### Problem 51: Count Inversions
**Problem Description**
Count pairs (i, j) where i < j but arr[i] > arr[j].

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the count of inversions.

**Sample Input**
```
5
1 3 5 2 4
```

**Sample Output**
```
3
```

**Explanation**
Inversions: (3,2), (5,2), (5,4). Use merge sort for O(n log n).

**Where it is used**
Ranking systems, bubble sort analysis, disorder measurement.

**Time Complexity:** O(n log n) | **Space Complexity:** O(n)

---

### Problem 52: Merge Intervals
**Problem Description**
Merge overlapping intervals.

**Input Format**
- Line 1: Integer n (number of intervals)
- Next n lines: Two integers start, end

**Output Format**
Print merged intervals.

**Sample Input**
```
4
1 3
2 6
8 10
15 18
```

**Sample Output**
```
1 6
8 10
15 18
```

**Explanation**
[1,3] and [2,6] overlap, merge to [1,6]. Sort by start, then merge greedily.

**Where it is used**
Calendar scheduling, meeting room problems, event management.

**Time Complexity:** O(n log n) | **Space Complexity:** O(n)

---

### Problem 53: Find All Triplets with Zero Sum
**Problem Description**
Find all unique triplets that sum to zero.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print triplets (no duplicates).

**Sample Input**
```
6
-1 0 1 2 -1 -4
```

**Sample Output**
```
-1 -1 2
-1 0 1
```

**Explanation**
Each triplet sums to 0. Sort, fix first element, use two pointers for remaining two.

**Where it is used**
3-sum problems, constraint satisfaction, combinatorial search.

**Time Complexity:** O(n²) | **Space Complexity:** O(n)

---

### Problem 54: Smallest Subarray with Sum ≥ X
**Problem Description**
Find the length of the smallest contiguous subarray with sum ≥ X.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers
- Line 3: Integer x (target sum)

**Output Format**
Print the length, or -1 if impossible.

**Sample Input**
```
6
2 3 1 2 4 3
7
```

**Sample Output**
```
2
```

**Explanation**
Subarray [4, 3] has sum 7 and length 2 (smallest). Use sliding window.

**Where it is used**
Resource allocation, minimum capacity problems, constraint optimization.

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### Problem 55: Longest Consecutive Sequence
**Problem Description**
Find the longest streak of consecutive numbers in an unsorted array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the length of the longest consecutive sequence.

**Sample Input**
```
9
100 4 200 1 3 2 5
```

**Sample Output**
```
4
```

**Explanation**
Consecutive sequence [1, 2, 3, 4] has length 4. Use hash set.

**Where it is used**
Streak detection, sequence analysis, data validation.

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 56: Spiral Matrix Traversal
**Problem Description**
Traverse a 2D matrix in spiral order (clockwise from outside).

**Input Format**
- Line 1: Integer r (rows), Integer c (columns)
- Next r lines: c space-separated integers

**Output Format**
Print elements in spiral order.

**Sample Input**
```
3 3
1 2 3
4 5 6
7 8 9
```

**Sample Output**
```
1 2 3 6 9 8 7 4 5
```

**Explanation**
Right → Down → Left → Up, shrinking boundaries.

**Where it is used**
Image processing, grid games, matrix operations.

**Time Complexity:** O(r * c) | **Space Complexity:** O(r * c)

---

### Problem 57: Rotate Matrix by 90 Degrees
**Problem Description**
Rotate a square matrix 90 degrees clockwise in-place.

**Input Format**
- Line 1: Integer n (size of n×n matrix)
- Next n lines: n space-separated integers

**Output Format**
Print the rotated matrix.

**Sample Input**
```
3
1 2 3
4 5 6
7 8 9
```

**Sample Output**
```
7 4 1
8 5 2
9 6 3
```

**Explanation**
Transpose then reverse each row. Or rotate layer by layer.

**Where it is used**
Image rotation, graphics processing, coordinate transformations.

**Time Complexity:** O(n²) | **Space Complexity:** O(1)

---

### Problem 58: Set Matrix Zeroes
**Problem Description**
Set entire row and column to zero if an element is zero (in-place).

**Input Format**
- Line 1: Integer r, Integer c
- Next r lines: c space-separated integers

**Output Format**
Print the modified matrix.

**Sample Input**
```
3 3
1 1 1
1 0 1
1 1 1
```

**Sample Output**
```
1 0 1
0 0 0
1 0 1
```

**Explanation**
Element at (1,1) is 0, so row 1 and column 1 become 0. Use first row/column as markers.

**Where it is used**
Matrix modifications, graph algorithms, constraint propagation.

**Time Complexity:** O(r * c) | **Space Complexity:** O(1)

---

### Problem 59: Search in Rotated Sorted Array
**Problem Description**
Search for a target in a rotated sorted array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers (rotated sorted)
- Line 3: Integer target

**Output Format**
Print the index if found, else -1.

**Sample Input**
```
7
4 5 6 7 0 1 2
0
```

**Sample Output**
```
4
```

**Explanation**
Array is rotated at pivot 7. 0 is at index 4. Use binary search on rotated array.

**Where it is used**
Search optimization, modified binary search, system design.

**Time Complexity:** O(log n) | **Space Complexity:** O(1)

---

### Problem 60: Minimum Swaps to Sort Array
**Problem Description**
Find the minimum number of swaps needed to sort an array.

**Input Format**
- Line 1: Integer n
- Line 2: n space-separated integers

**Output Format**
Print the minimum swaps.

**Sample Input**
```
5
2 8 5 4 1
```

**Sample Output**
```
3
```

**Explanation**
Map to positions, find cycles in permutation, swap cycle size - 1 times.

**Where it is used**
Sorting optimization, permutation analysis, algorithmic efficiency.

**Time Complexity:** O(n log n) | **Space Complexity:** O(n)

---

## ✅ Summary: Quick Reference

| Problem | Difficulty | Topic | Time | Space |
|---------|-----------|-------|------|-------|
| 1-20 | 🟢 Beginner | Basics, Iteration, Indexing | O(n) | O(1) |
| 21-25 | 🟡 Intermediate | Two Pointers, Sorting, Hash Maps | O(n²) to O(n log n) | O(n) |
| 26-35 | 🟡 Intermediate | Prefix Sums, Dynamic Window, Math | O(n) to O(n log n) | O(n) |
| 36-45 | 🟡 Intermediate | Search, Patterns, Optimization | O(n) to O(n log n) | O(1) to O(n) |
| 46-50 | 🔴 Advanced | Water Trapping, Medians, Heaps | O(n) to O(log n) | O(1) to O(k) |
| 51-60 | 🔴 Advanced | Inversions, Sorting, 2D Arrays | O(n²) to O(n log n) | O(n) |

## 🚀 Recommended Progression

**Week 1 (Days 1-5):** Problems 1-10 (Basic Iteration & Single Pass)
**Week 1 (Days 6-7):** Problems 11-20 (Indexing & Manipulation)

**Week 2 (Days 8-12):** Problems 21-30 (Sorting, Hashing, Two Pointers)
**Week 2 (Days 13-14):** Problems 31-40 (Advanced Iteration & Dynamic Programming)

**Week 3 (Days 15-19):** Problems 41-50 (Cycle Detection, Stacks, Heaps)
**Week 3 (Days 20-21):** Problems 51-60 (Matrix & Advanced Search)

---

## 🔗 Topics Covered

- **Linear Traversal:** Problems 1-10, 16, 27
- **Two Pointers:** Problems 8, 23, 24, 31, 33, 37, 46, 47
- **Hashing/Sets:** Problems 10, 22, 31, 32, 41, 42, 43, 55
- **Sorting:** Problems 7, 22, 24, 25, 33, 37, 49, 51, 52, 59, 60
- **Prefix Sums:** Problems 4, 18, 19, 27, 28, 34, 42, 43, 45
- **Sliding Window:** Problems 21, 28, 30, 34, 40, 54
- **Binary Search:** Problems 36, 44, 49, 50, 59
- **Dynamic Programming:** Problems 29, 30, 38, 40, 48
- **Matrix Operations:** Problems 56, 57, 58
- **Greedy:** Problems 37, 39, 46, 47, 52, 54

---

## 💡 Pro Tips

1. **Always clarify input/output format** before coding
2. **Use auxiliary space wisely** - sometimes O(n) space saves O(n²) time
3. **Think of edge cases** - empty arrays, single elements, all duplicates
4. **Practice both iterative and recursive** approaches where applicable
5. **Track min/max and prefix/suffix** simultaneously for optimization
6. **Two pointers is powerful** - try it for sorted arrays first
7. **Hash maps/sets convert O(n²) → O(n)** - use freely in intermediate problems


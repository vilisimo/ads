# Algorithms &amp; Data Structures

## Algorithms

### Computation Algorithms
* Euclid's Algorithm for GCD: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/computations/EuclidsAlgorithm.java)

### Searching Algorithms
* Binary Search: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/searching/BinarySearch.java), [Python](../../blob/master/python/algorithms/searching/binary.py)
* Binary Search (recursive): [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/searching/RecursiveBinarySearch.java), [Python](../../blob/master/python/algorithms/searching/recursiveBinary.py)
* Linear Search: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/searching/LinearSearch.java), [Python](../../blob/master/python/algorithms/searching/linear.py)

### Sorting Algorithms
* Bubble sort: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/BubbleSort.java), [Python](../../blob/master/python/algorithms/sorting/bubble.py)
* Insertion Sort: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/InsertionSort.java), [Python](../../blob/master/python/algorithms/sorting/insertion.py)
* Merge Sort: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/MergeSort.java), [Python](../../blob/master/python/algorithms/sorting/mergesort.py)
* Selection Sort: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/SelectionSort.java), [Python](../../blob/master/python/algorithms/sorting/selection.py)
* Quicksort: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/QuickSort.java), [Python](../../blob/master/python/algorithms/sorting/quicksort.py)
* Quicksort (in-place): [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/QuickSortInPlace.java), [Python](../../blob/master/python/algorithms/sorting/quicksort.py#L33)
* Quicksort (in-place, 2): [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/sorting/QuickSortPivotFirst.java), [Python](../../blob/master/python/algorithms/sorting/quicksort.py#L70)

### Transforming Algorithms
* Integer to Roman Numeral (1-3999): [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/transforming/RomanNumerals.java#L20), [Python](../../blob/master/python/algorithms/transforming/roman.py#L19)
* Roman Numeral to Integer (1-3999): [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/algorithms/transforming/RomanNumerals.java#L40), [Python](../../blob/master/python/algorithms/transforming/roman.py#L35)

## Data structures

### Linear Data Structures
* Stack: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/structures/stack), [Python](../../blob/master/python/structures/stack.py)
* Queue: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/structures/queue), [Python](../../blob/master/python/structures/queue.py)

## LeetCode Exercises

### Easy
* [Exercise 0001](https://leetcode.com/problems/two-sum/) - Two Sum: [Python](../../blob/master/python/leetcode/easy/ex0001.py)
* [Exercise 0009](https://leetcode.com/problems/palindrome-number/) - Palindrome Number: [Python](../../blob/master/python/leetcode/easy/ex0009.py)
* [Exercise 0013](https://leetcode.com/problems/roman-to-integer/) - Roman to Integer: [Python](../../blob/master/python/leetcode/easy/ex0013.py)
* [Exercise 0014](https://leetcode.com/problems/longest-common-prefix) - Longest Common Prefix: [Python](../../blob/master/python/leetcode/easy/ex0014.py)
* [Exercise 0020](https://leetcode.com/problems/valid-parentheses/) - Valid Parentheses: [Python](../../blob/master/python/leetcode/easy/ex0020.py)
* [Exercise 0021](https://leetcode.com/problems/merge-two-sorted-lists/) - Merge Two Sorted Lists: [Python](../../blob/master/python/leetcode/easy/ex0021.py)
* [Exercise 0026](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Remove Duplicates from Sorted Array: [Python](../../blob/master/python/leetcode/easy/ex0026.py)
* [Exercise 0027](https://leetcode.com/problems/remove-element/) - Remove Element: [Python](../../blob/master/python/leetcode/easy/ex0027.py)
* [Exercise 0028](https://leetcode.com/problems/implement-strstr/) - Implement strStr: [Python](../../blob/master/python/leetcode/easy/ex0028.py)
* [Exercise 0035](https://leetcode.com/problems/search-insert-position/) - Search Insert Position: [Python](../../blob/master/python/leetcode/easy/ex0035.py)
* [Exercise 0053](https://leetcode.com/problems/maximum-subarray) - Maximum Subarray: [Python](../../blob/master/python/leetcode/easy/ex0053.py)
* [Exercise 0058](https://leetcode.com/problems/length-of-last-word/) - Length of Last Word: [Python](../../blob/master/python/leetcode/easy/ex0058.py)
* [Exercise 0066](https://leetcode.com/problems/plus-one/) - Plus One: [Python](../../blob/master/python/leetcode/easy/ex0066.py)
* [Exercise 0067](https://leetcode.com/problems/add-binary/) - Add Binary: [Python](../../blob/master/python/leetcode/easy/ex0067.py)
* [Exercise 0069](https://leetcode.com/problems/sqrtx/) - Sqrt(x): [Python](../../blob/master/python/leetcode/easy/ex0069.py)
* [Exercise 0070](https://leetcode.com/problems/climbing-stairs/) - Climbing stairs: [Python](../../blob/master/python/leetcode/easy/ex0070.py)
* [Exercise 0771](https://leetcode.com/problems/jewels-and-stones/) - Jewels and Stones: [Python](../../blob/master/python/leetcode/easy/ex0771.py)

## Books
* *Algorithms* (2011) by Robert Sedgewick & Kevin Wayne: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/books/algorithms)

Note that only those exercises that seem to be interesting and require a bit of coding are included.

## Launching Tests

### Python
Easiest way to launch tests is to run the following command:

~~~
cd python/
pytest
~~~

For that, the expectation is that the environment is initialized and `pytest`
is installed:

~~~
python3.10 -m venv env
source env/bin/activate
pip install -r requirements.txt
~~~

### Java
Project uses Gradle as a build tool. Hence, running tests is as easy as:

~~~
./gradlew clean test
~~~

Alternatively, tests can be run in IntelliJ. To do so, import the project as a
Gradle project, right click on `test` directory and select `Run 'All Tests'`.

## Dependencies
With exception of JUnit for Java code, there are no other dependencies.
* For Python examples, 3.10.0+ version should be used, although in many cases
lower versions will be sufficient.
* For Java code, Java 11 was used. Code was written in plain Java with
an exception of [JUnit 4.12](http://junit.org/junit4/), which was used for
tests.

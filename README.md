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
* Exercise 771 - Jewels and Stones: [Python](../../blob/master/python/leetcode/ex771.py)

## Books
* *Algorithms* (2011) by Robert Sedgewick & Kevin Wayne: [Java](../../blob/master/java/src/main/java/com/vilisimo/ads/books/algorithms)

Note that only those exercises that seem to be interesting and require a bit of coding are included.

## Launching Tests

### Python
Easiest way to launch tests is to do that via PyCharm. Alternatively, they
can be launched by issuing this command in `ads/python/` directory:

~~~
python3 -m unittest
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
* For Python examples, 3.6.0+ version should be used, although in many cases
lower versions will be sufficient.
* For Java code, Java 11 was used. Code was written in plain Java with
an exception of [JUnit 4.12](http://junit.org/junit4/), which was used for
tests.

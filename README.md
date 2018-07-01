# Algorithms &amp; Data Structures

## Algorithms

### Searching Algorithms
* Binary Search: [Java](../../blob/master/java/src/algorithms/searching/BinarySearch.java), [Python](../../blob/master/python/algorithms/searching/binary.py)
* Binary Search (recursive): [Java](../../blob/master/java/src/algorithms/searching/RecursiveBinarySearch.java), [Python](../../blob/master/python/algorithms/searching/recursiveBinary.py)
* Linear Search: [Java](../../blob/master/java/src/algorithms/searching/LinearSearch.java), [Python](../../blob/master/python/algorithms/searching/linear.py)

### Sorting Algorithms
* Bubble sort: [Java](../../blob/master/java/src/algorithms/sorting/BubbleSort.java), [Python](../../blob/master/python/algorithms/sorting/bubble.py)
* Insertion Sort: [Java](../../blob/master/java/src/algorithms/sorting/InsertionSort.java), [Python](../../blob/master/python/algorithms/sorting/insertion.py)
* Merge Sort: [Java](../../blob/master/java/src/algorithms/sorting/MergeSort.java), [Python](../../blob/master/python/algorithms/sorting/mergesort.py)
* Selection Sort: [Java](../../blob/master/java/src/algorithms/sorting/SelectionSort.java), [Python](../../blob/master/python/algorithms/sorting/selection.py)
* Quicksort: [Java](../../blob/master/java/src/algorithms/sorting/QuickSort.java), [Python](../../blob/master/python/algorithms/sorting/quicksort.py)
* Quicksort (in-place): [Java](../../blob/master/java/src/algorithms/sorting/QuickSortInPlace.java), [Python](../../blob/master/python/algorithms/sorting/quicksort.py#L33)
* Quicksort (in-place, 2): [Java](../../blob/master/java/src/algorithms/sorting/QuickSortPivotFirst.java), [Python](../../blob/master/python/algorithms/sorting/quicksort.py#L70)

## Data structures

### Linear Data Structures
* Stack: [Java](../../blob/master/java/src/structures/stack), [Python](../../blob/master/python/structures/stack.py)
* Queue: [Java](../../blob/master/java/src/structures/queue), [Python](../../blob/master/python/structures/queue.py)



## Launching Tests
### Python
Easiest way to launch tests is to do that via PyCharm. Nevertheless, it is 
possible to run tests through terminal, too.

First of all, set the correct `PYTHONPATH`. For example, on Linux it might
look something like this: `/home/username/dev/ads/python`. To export the
path, simply issue this command in your terminal:

~~~
PYTHONPATH=$PYTHONPATH:/home/username/dev/ads/python
~~~

Don't forget to adjust the path to your needs. 

### Java
Project uses Gradle as a build tool. Hence, running tests is as easy as:

~~~
./gradlew test
~~~

On the other hand, it is also very easy to run tests in IntelliJ. Simply
import the project as a Gradle project, right click on `test` directory
and select `Run 'All Tests'`.

## Dependencies
With exception of JUnit for Java code, there are no other dependencies. 
* For Python examples, 3.6.0+ version should be used, although in same cases
lower versions will be sufficient. 
* For Java code, Java 9 was used. Code was written in plain Java with
an exception of [JUnit 4.12](http://junit.org/junit4/), which was used for
tests.

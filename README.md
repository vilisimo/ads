# Algorithms &amp; Data Structures

## Algorithms

### Searching Algorithms
* [Binary Search](../../tree/master/algorithms/searching/binary/)
* [Binary Search (recursive)](../../tree/master/algorithms/searching/recursive/binary/)
* [Linear Search](../../tree/master/algorithms/searching/linear/)

### Sorting Algorithms
* [Insertion Sort](../../tree/master/algorithms/sorting/insertion/)
* [Selection Sort](../../tree/master/algorithms/sorting/selection/)


## Launching Tests
### Python
Easiest way to launch tests is to do that via PyCharm. Nevertheless, it is 
possible to run tests through terminal, too.

First of all, set the correct `PYTHONPATH`. For example, on Linux it might look 
something like this: `/home/username/dev/ads/`. To export the path, simply issue 
this command in your terminal:
~~~
PYTHONPATH=$PYTHONPATH:/home/username/dev/ads/
~~~
Don't forget to adjust the path to your needs. 

### Java
Easiest way to launch tests is to do that via IntelliJ. Nevertheless, it is 
possible to run tests through terminal, too. It is a bit more involved than 
Python, however.

First of all, you will need to download [JUnit 4.12](http://junit.org/junit4/).
Once this is done, follow the [instructions](https://github.com/junit-team/junit4/wiki/Getting-started#run-the-test)
on how to run the tests.

Note that you will need to add path to the root folder to `CLASSPATH`, i.e.:
~~~
CLASSPATH=$CLASSPATH:/home/username/dev/ads/
~~~
Otherwise the files will not compile.

Provided that you have `Hamcrest`, `JUnit` and root directory on a `CLASSPATH`,
running of the tests should look something like this:
~~~
javac file.java
java java org.junit.runner.JUnitCore full.package.path.to.desired.file
~~~
Again, running tests through IntelliJ is much less hassle.

## Dependencies
With exception of JUnit for Java code, there are no special dependencies. 
* For Python examples, 3.6.0+ version should be used, although in same cases 
  lower versions should be sufficient. Other than that, the code is written in 
  plain Python.
* For Java code, Java 8 was utilized. Code is written in plain Java. 
  [JUnit 4.12](http://junit.org/junit4/) is used for tests.
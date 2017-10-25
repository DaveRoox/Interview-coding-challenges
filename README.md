# Interview coding challenges
This repository collects coding challenges assigned during technical interviews in big tech companies such as Google, Facebook, Apple and so on.<br>
I will propose my own solution in different languages (mainly C++, Python and Java) and, for each problem, different approaches will be evaluated, stating spatial and time complexity, what are the limits and how to design a better solution.

# Why?
I started this project with the hope to be a good starting point for everyone that is training in order to face a technical interview in the best way, or just for everyone that wants to have fun with some tricky problems.<br>
Also, this is a good opportunity for me too to keep training, so not why, but <b>why not?</b>

# Where are these interviews from?
<ul>
  <a href="https://glassdoor.com/">Glassdoor</a>
</ul>

# Challenges
<ul>
  <a href="https://github.com/DaveRoox/Interview-coding-challenges/blob/master/README.md#search-in-sorted-rotated-array">Search in sorted rotated array</a>
</ul>

<b>---------------------------------------------------------------------------</b>

<b><h2>Search in sorted rotated array</h2></b>
Find a target number in sorted array with rotation.<br>
Example: the array is [5, 7, 8, 1, 3]<br>
Find the index of the number 7, the output is 1.<br>

<b><h4>Brute force approach</h4></b>
A brute force solution consists in a linear search over the array.<br>
If the element is matched, the function returns the current index

```python
def linear_search(array, a, b, target):
    if target < array[a] or target > array[b]:
        return False, None, 1

    n = len(array)
    iterations = 1

    for i in range(n):
        if array[i] == target:
            return True, i, iterations
        iterations += 1

    return False, None, iterations
```

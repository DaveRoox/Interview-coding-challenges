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
  <li><a href="https://github.com/DaveRoox/Interview-coding-challenges/blob/master/README.md#search-in-sorted-rotated-array">Search in sorted rotated array</a></li>
</ul>

<b>---------------------------------------------------------------------------</b>

<b><h2>Search in sorted rotated array</h2></b>
Find a target number in sorted array with rotation.<br>
Example: the array is [5, 7, 8, 1, 3]<br>
Find the index of the number 7, the output is 1.<br>

<b><h4>Brute force approach</h4></b>
A brute force solution consists in a linear search over the array.<br>
If the element is matched, the function returns the current index.

```python
def linear_search(array, low, high, target):

    n = len(array)
    iterations = 1

    for i in range(n):
        if array[i] == target:
            return True, i, iterations
        iterations += 1

    return False, None, iterations
```
In this case we do not even need to know the index of the minimum, <i>low</i>, and the index of the maximum element, <i>high</i>.<br>
The solution looks simple and clear but, unfortunately, when it comes to the performance it does not result in the best approach possible.<br>
Infact, due to we iterate over the whole array, in the worst case (the target number is not present) the algorithm performs <b>n</b> iterations. The average case, however, is not different from the worst case, because, supposing that we define the "average case" when the target number is in the middle of the array, it turns out to performs an average number of iterations that is <b>n/2</b>.<br>
So:
<ul>
  <li>The time complexity is O(n), where n is the size of the array</li>
  <li>The space complexity is O(1), because we don't need to allocate extra space depending on the size of the array</li>
</ul>

<b><h4>Binary search based approach</h4></b>
A consistently better solution can be obtained taking into account that we are managing a pre-ordered array, but rotated.
In this case we could imagine it as a circular data structure, where just changing the initial position from 0 to that of the minimum element and the final position from (n-1) to that of the maximum element we can apply the binary search algorithm.

```python
def logarithmic_search(array, low, high, target):

    if target < array[low] or target > array[high]:
        return False, None, 1

    n = len(array)
    mid = ((low + high + n) // 2) % n if high < low else (low + high) // 2
    iterations = 1

    while array[mid] != target and low != high:
        if array[mid] < target:
            low = (mid + 1) % n
        else:
            high = (mid - 1 + n) % n
        mid = ((low + high + n) // 2) % n if high < low else (low + high) // 2
        iterations += 1

    return array[mid] == target, mid if array[mid] == target else None, iterations
```
The main difference between the standard algorithm and our case is that for us having <i>low</i> > <i>high</i> is a perfectly suitable case.<br>
Infact, we could have:<br>
// DISEGNI
We can spot two cases:
<ul>
  <li><b>low < high</b> this is what we have in the standard algorithm. In this case we can get the middle element just evaluating the integer part of <b>(low + high) / 2</b></li>
  <li>high > low</li>
</ul>
For this approach, we have:
<ul>
  <li>The time complexity is O(log(n)), where n is the size of the array</li>
  <li>The space complexity is O(1), because we don't need to allocate extra space depending on the size of the array</li>
</ul>

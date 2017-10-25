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
In fact, since we iterate over the whole array, in the worst case (that is when the target number is not present) the algorithm performs <b>n</b> iterations. The average case, however, is not different from the worst case, because, supposing that we define the "average case" when the target number is in the middle of the array, it turns out to performs an average number of iterations that is <b>n/2</b>.<br>
So:
<ul>
  <li>The time complexity is O(n), where n is the size of the array</li>
  <li>The space complexity is O(1), because we don't need to allocate extra space depending on the size of the array</li>
</ul>

<b><h4>Binary search based approach</h4></b>
A consistently better solution can be obtained taking into account that we are managing a pre-ordered array, but rotated.
In this case we could imagine it as a circular data structure, where just changing the initial position from 0 to that of the minimum element and the final position from (n-1) to that of the maximum element we can apply the binary search algorithm.<br>

The main difference between the standard algorithm and our case is that for us having <i>low</i> > <i>high</i> is a perfectly suitable case.<br>
Infact, we can spot two cases:
<ul>
  <li><b>low < high</b>: this is what we have in the standard algorithm. In this case we can get the middle element just evaluating the integer part of <b>(low + high) / 2</b><br>
    <b>middle = floor((low + high) / 2)</b>
    </li>
  <li><b>high > low</b>: in this case the main idea is to "transform" this case into the previous one. This can be done adding the length of the array, <i>n</i>, to <i>high</i> and getting the result modulo <i>n</i><br><br>
    Let's suppose to have the following array:<br><br>
    <img align='middle' src='https://user-images.githubusercontent.com/23279650/32007673-788856ce-b9aa-11e7-9614-916dc30875a4.png'/><br><br>
    Adding <i>n</i> to <i>high</i> would mean thinking about the array as it has an "extension" and evaluating the middle index would pick the element as shown:<br><br>
    <img align='middle' src='https://user-images.githubusercontent.com/23279650/32007674-78a77b76-b9aa-11e7-8dcb-e242ebd002db.png'/><br><br>
    At this point what has left to do is to get the index of the middle back to the original interval [0, n-1]. This is easily done by applying the modulo operator:<br><br>
    <img src='https://user-images.githubusercontent.com/23279650/32007675-78c5a420-b9aa-11e7-871e-8790a1e9d442.png'/><br><br>
    So:<br>
    <b>middle = floor((low + high + n) / 2) % n</b>
  </li>
</ul>
If the target is present into the array, iterating the evaluation of the current middle point as shown, and checking for its element until the target has not been found and updating <i>low</i> and <i>high</i> according to the original algorithm, will get the index of the target.<br>
Otherwise we will know that the target is not present into the array if <i>low = high AND array[middle] = array[low] = array[high] != target</i>.<br>
Hence, the condition to verify to keep iterating is that <i>array[middle] != target AND low != high</i>.<br><br>
The code is:<br>
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
For this algorithm:
<ul>
  <li>The time complexity is O(log(n)), where n is the size of the array</li>
  <li>The space complexity is O(1), because we don't need to allocate extra space depending on the size of the array</li>
</ul>

# Interview coding challenges
This repository collects coding challenges assigned during technical interviews in big tech companies such as Google, Facebook, Apple and so on.<br>
I will propose my own solution in different languages (mainly C++, Python and Java) and, for each problem, different approaches will be evaluated, stating spatial and time complexity, what are the limits and how to design a better solution.

# Why?
I started this project with the hope that it could be a good starting point for everyone that is training in order to face a technical interview, or just for everyone that wants to have fun with some tricky problems.<br>
Also, this is a good opportunity for me too to keep training, so not why, but <b>why not?</b>

# Where are these interviews from?
<ul>
  <a href="https://glassdoor.com/">Glassdoor</a>
</ul>

# Challenges
<ul>
  <li><a href="https://github.com/DaveRoox/Interview-coding-challenges/blob/master/README.md#search-in-sorted-rotated-array">Search in sorted rotated array</a></li>
  <li><a href="https://github.com/DaveRoox/Interview-coding-challenges/blob/master/README.md#big-integers">Big integers</a></li>
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
The solution looks simple and clear but, unfortunately, when it comes to the performance it does not result the best approach.<br>
In fact, since we iterate over the whole array, in the worst case (that is when the target number is not present) the algorithm performs <b>n</b> iterations. The average case, however, is not different from the worst case, because, supposing that we define the "average case" when the target number is in the middle of the array, it turns out to perform an average number of iterations that is <b>n/2</b>.<br>
So:
<ul>
  <li>The time complexity is O(n), where n is the size of the array</li>
  <li>The space complexity is O(1), because we don't need to allocate extra space that depends on the size of the array</li>
</ul>

<b><h4>Binary search based approach</h4></b>
A consistently better solution can be obtained taking into account that we are managing a pre-ordered array, but rotated.
In this case we could imagine it as a circular data structure, where just changing the initial position from 0 to that of the minimum element and the final position from (n-1) to that of the maximum element we can apply the binary search algorithm.

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
    At this point all that's left to do is to get the index of the middle back to the original interval [0, n-1]. This is easily done by applying the modulo operator:<br><br>
    <img src='https://user-images.githubusercontent.com/23279650/32007675-78c5a420-b9aa-11e7-871e-8790a1e9d442.png'/><br><br>
    So:<br>
    <b>middle = floor((low + high + n) / 2) % n</b>
  </li>
</ul>
If the target is present into the array, iterating the evaluation of the current middle point as shown, checking if its element matches the target and updating <i>low</i> and <i>high</i> according to the original algorithm, will get the index of the target.<br>
Otherwise we will know that the target is not present into the array if <i>low == high (= middle) AND array[middle] != target</i>.<br>
Hence, the condition to satisfy in order to keep iterating is: <i>array[middle] != target AND low != high</i>.<br><br>

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
  <li>The space complexity is O(1), because we don't need to allocate extra space that depends on the size of the array</li>
</ul>

<b>---------------------------------------------------------------------------</b>

<b><h2>Big integers</h2></b>
Multiply two big integers which don't fit into an built-in integer type.<br>
How would you represent big numbers as a data structure?<br>
Write the function to multiply two big integers.

<b><h4>Representation</h4></b>
<b>Hypothesis</b>: having a string <i>s</i> representing the number.<br>

The first representation that I am going to propose is based on an array allocated dynamically.<br>
This approach is both quick and easy to implement, has a good memory usage and could result in a good choice in terms of performance.<br>
However, two constraints to take into account when adopting this solution are the contiguity of the elements and the fixed size of the memory allocated:<br>
<ul>
<li>The contiguity of the elements could be a problem when we need to manage <b>very</b> large numbers.</li>
<li>The fixed size is a problem when we need to add or remove dynamically one or more elements, that is a situation that we could possibily face in the implementation of mutating operators. This can be solved first freeing the current memory and then allocating a new one of the right size.</li>
</ul><br><br>

The second representation is based on a linked list.<br>
Every digit of the original number is contained in a node that is linked to another one containing the <i>next</i> digit of the number, and so on.<br>
Let's suppose that our number N is 681, this representation would end up in the following data structure:<br><br>
<img src='https://user-images.githubusercontent.com/23279650/32132943-c2685ef4-bbcd-11e7-88e6-cf474d04ee48.png' />

The choice of a linked list is optimal for its flexibility, since operations of adding and/or removing nodes are performed easily and with low overhead.
These operations are necessary when mutating operators (+=, -=, /=, *=, %=, etc.) are requested to be implemented efficiently. In fact, modifying in-place, removing or adding new nodes is generally better than creating a new list, executing the operations needed according to the operator we are implementing, discarding the original list and assigning the new one, because in this last case we discard the whole previous list, no matter what we are doing, if a division by 10 or just adding 1.<br><br>

Anyway, the main downside of using a linked list is the memory usage, because they need also to store the pointers of each node.

```c++
struct BigIntNode {

	short digit;
	BigIntNode *next;

	BigIntNode(short _digit, BigIntNode *_next = nullptr): digit(_digit), next(_next) {}

	~BigIntNode() {
		if(next)
			delete next;
	}

};
```

For this algorithm:
<ul>
  <li>The time complexity is O(log(n)), where n is the size of the array</li>
  <li>The space complexity is O(1), because we don't need to allocate extra space that depends on the size of the array</li>
</ul>

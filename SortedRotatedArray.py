# Brute-force approach:
# Time complexity: O(n)
# Space complexity: O(1)
def linear_search(array, low, high, target):

    n = len(array)
    iterations = 1
	
    for i in range(n):
        if array[i] == target:
            return True, i, iterations
        iterations += 1

    return False, None, iterations

# Binary search based approach:
# Time complexity: O(lgn)
# Space complexity: O(1)
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


# Main program to test the functions.
# Creating the array and filling in positions shifted by an offset
n, offset = 100, 78
array = [0 for _ in range(n)]
for i in range(n):
    array[(i + offset) % n] = i * 2

# Printing the array
for n in array:
    print(n, end='\t')
print()
for n in range(len(array)):
    print(n, end='\t')
print()

# Searching for a target number
target = 20 # present
found, index, iterations = logarithmic_search(array, low=offset, high=offset - 1, target=target)
if found:
    print('%d found at index %d [%d iterations]' % (target, index, iterations))
else:
    print('%d not found [%d iterations]' % (target, iterations))
	
target = 19 # not present
found, index, iterations = logarithmic_search(array, low=offset, high=offset - 1, target=target)
if found:
    print('%d found at index %d [%d iterations]' % (target, index, iterations))
else:
    print('%d not found [%d iterations]' % (target, iterations))

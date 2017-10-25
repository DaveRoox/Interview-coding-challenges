# Brute-force approach:
# Time complexity: O(n)
# Space complexity: O(1)
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

# Binary search based approach:
# Time complexity: O(lgn)
# Space complexity: O(1)
def logarithmic_search(array, a, b, target):

	if target < array[a] or target > array[b]:
        return False, None, 1

    n = len(array)
    c = ((a + b + n) // 2) % n if b < a else (a + b) // 2
    iterations = 1

    while array[c] != target and a != b:
        if array[c] < target:
            a = (c + 1) % n
        else:
            b = (c - 1 + n) % n
        c = ((a + b + n) // 2) % n if b < a else (a + b) // 2
        iterations += 1

    return array[c] == target, c if array[c] == target else None, iterations


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
found, index, iterations = rotated_binary_search(array, a=offset, b=offset - 1, target=target)
if found:
    print('%d found at index %d [%d iterations]' % (target, index, iterations))
else:
    print('%d not found [%d iterations]' % (target, iterations))
	
target = 19 # not present
found, index, iterations = rotated_binary_search(array, a=offset, b=offset - 1, target=target)
if found:
    print('%d found at index %d [%d iterations]' % (target, index, iterations))
else:
    print('%d not found [%d iterations]' % (target, iterations))

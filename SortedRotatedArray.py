def linear_search(array, a, b, target):

	if target < array[a] or target > array[b]:
        return 'Not found'

    n = len(array)
    for i in range(n):
		if array[i] == target:
			return i

    return 'Not found'

def logarithmic_search(array, a, b, target): # Based on the binary search

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


n, offset = 100, 78
target = 20
array = [0 for _ in range(n)]
for i in range(n):
    array[(i + offset) % n] = i * 2

for n in array:
    print(n, end='\t')
print()
for n in range(len(array)):
    print(n, end='\t')
print()

found, index, iterations = rotated_binary_search(array, a=offset, b=offset - 1, target=target)
if found:
    print('%d found at index %d [%d iterations]' % (target, index, iterations))
else:
    print('%d not found [%d iterations]' % (target, iterations))

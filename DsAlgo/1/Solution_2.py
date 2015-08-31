# Reuse the input array this time
def getAbsoluteMinAndMax(array, start, end):
	delta = end - start
	if delta <= 0: # catch cases where range is <= 0
		return (None, None)
	elif delta > 2: # divide and conquer
		half = delta//2
		(leftMin, leftMax) = getAbsoluteMinAndMax(array, start, start + half)
		(rightMin, rightMax) = getAbsoluteMinAndMax(array, start + half, end)
		return (min(leftMin, rightMin), max(leftMax, rightMax))
	elif delta == 1: # odd
		return (array[start], array[start])
	elif delta == 2: # even
		return (min(array[start], array[end - 1]), max(array[start], array[end - 1]))
array = [3, 1, 5, 12, 9, 0, 5]
(absoluteMin, absoluteMax) = getAbsoluteMinAndMax(array, 0, len(array))
print(absoluteMin, absoluteMax)
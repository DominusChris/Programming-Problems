def getAbsoluteMinAndMax(array):
	if not array: # catch case where n = 0
		return (None, None)
	lengthArray = len(array)
	if lengthArray > 2: # divide and conquer
		half = len(array)//2
		(leftMin, leftMax) = getAbsoluteMinAndMax(array[:half])
		(rightMin, rightMax) = getAbsoluteMinAndMax(array[half:])
		return (min(leftMin, rightMin), max(leftMax, rightMax))
	elif lengthArray == 1: # odd
		return (array[0], array[0])
	elif lengthArray == 2: # even
		return (min(array), max(array))
(absoluteMin, absoluteMax) = getAbsoluteMinAndMax([3, 1, 5, 12, 9, 0, 5])
print(absoluteMin, absoluteMax)
def quickSort(arr):
	# Break condition
	if len(arr) <= 1:
		return arr
	N = len(arr)
	pivot = arr[ N // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quickSort(left) + middle + quickSort(right)


print(quickSort([2,-1,86,44,12,0,-87,78]))
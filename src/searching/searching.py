def linear_search(arr, target):
    # check each index in the array
    for i in range(0, len(arr)):
        # if the value at that index and the target match return it
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # instantiate our left and right halves of the array
    left = 0
    right = len(arr) - 1

    #iterate loop as long as left is less than or equal to right
    while left <= right:
        midpoint = (right + left) // 2

        # if target at midpoint, we have index
        if arr[midpoint] == target:
            return midpoint
        # otherwise check whether midpoint is greater or lesser than target,
        # and reassign the corresponding variable to cut our array in half   
        elif arr[midpoint] > target:
            right = midpoint - 1 #by setting right below the midpoint, we cut our array into just the left half
        else:
            left = midpoint + 1

    # return -1 if not in array
    return -1

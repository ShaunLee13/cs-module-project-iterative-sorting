# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # this will be where we start each loop. since sorting small to large,
        # we won't have any values below boundary
        boundary = i
        num_small = boundary

        # on each cycle, compare our current smallest value (which starts at boundary index) to the value at each concurrent index
        for j in range(boundary + 1, len(arr)):

            # if a smaller value is found, set it to smallest
            if arr[j] < arr[num_small]:
                num_small = j

        # when we've gone through the array, sort the smallest value into the list by swapping it with our boundary position
        arr[num_small], arr[boundary] = arr[boundary], arr[num_small]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr): 
    n = len(arr) 
   
    # Iterate over each element in array
    for i in range(n): 
        swapped = False
  
        # Since we're bubbling large to small, our boundary is pulled back each cycle
        for j in range(0, n-i-1): 
   
            # loop and compare from beginning of array to the last unsorted element
            # and if our current position is larger than the next, swap positions
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # if j loop doesn't make any changes in this cycle, break out of the algorithm early
        if swapped == False: 
            break

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm? O(n+r) (number of elements + range)
'''
def counting_sort(arr, maximum=None):
    # first ensure our array has length
    if len(arr) == 0:
        return arr
    # then check for negative numbers
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"

    # determine the highest value of our list
    maximum = max(arr) + 1 

    # create a new list to store the position values of our input
    counter = [0] * maximum
    #increment each of our positional index values by 1 to give us a list to reference
    for item in arr:
        counter[item] += 1

    # starting at 0 index; in our first loop, we compare values up to our max
    # in our second, for each counter item at the index represented by that value:
    i = 0
    for val in range(maximum):
        for item in range(counter[val]):

            # update the value at arr[i] with our val
            # then increment i while inside this loop
            arr[i] = val
            i += 1
            # this will input one instance of val for every instance that was originally added into our counter list

    return arr

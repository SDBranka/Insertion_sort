#Build an algorithm for insertion sort. Please watch the video here to understand how insertion sort works and implement the code. Basically, this sort works by starting at index 1, shifting that value to the left until it is sorted relative to all values to the left, and then moving on to the next index position and performing the same shifts until the end of the list is reached. 

#tends to be faster than bubble sort or selection sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i-1] > arr[i] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr


x = [6, 3, 0, 5, 2, 1, 4]
print(insertion_sort(x))


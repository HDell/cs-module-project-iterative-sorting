def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) # -1 would also work, but would move to the left size of an even min
    mid = (high + low) // 2
    while high > low:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            mid = (high + low) // 2
        else: #arr[mid] > target
            high = mid # -1 would also work, but would move to the left size of an even min
            mid = (high + low) // 2

    return -1  # not found

## Merge Sort 
def merge(n, arr):  # Merge Sort function, takes size and array as input
    # Recursive merge sort function
    def ms(arr, low, high):
        if low == high:
            return  # Base case: if only one element, already sorted
        mid = (low + high) // 2  # Find mid point
        ms(arr, low, mid)        # Recursively sort left half
        ms(arr, mid + 1, high)   # Recursively sort right half
        sort(arr, low, mid, high)  # Merge the two halves
    # Function to merge two sorted halves
    def sort(arr, low, mid, high):
        i = low        # Start of left half
        j = mid + 1    # Start of right half
        k = []         # Temp array to store sorted elements
        # Merge elements from both halves in sorted order
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                k.append(arr[i])
                i += 1
            else:
                k.append(arr[j])
                j += 1
        # Copy remaining elements from left half, if any
        while i <= mid:
            k.append(arr[i])
            i += 1
        # Copy remaining elements from right half, if any
        while j <= high:
            k.append(arr[j])
            j += 1
        # Copy merged sorted elements back to original array
        for ind, val in enumerate(k):
            arr[ind + low] = val
    low = 0
    high = n - 1
    ms(arr, low, high)
    return arr

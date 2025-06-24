## Quick Sort
def quicksort(arr):  
    # Recursive helper function for quick sort
    def qs(arr, low, high):
        # Only sort if more than one element
        if low < high:
            # Partition the array and get pivot index
            pIndex = partition(arr, low, high)

            # Recursively sort left sub-array
            qs(arr, low, pIndex - 1)

            # Recursively sort right sub-array
            qs(arr, pIndex + 1, high)

    # Partitioning function to place pivot at correct position
    def partition(arr, low, high):
        i = low          # Left pointer
        j = high         # Right pointer
        pivot = arr[low] # Choosing the first element as pivot

        # Continue while left pointer is less than right
        while i < j:
            # Move i until an element > pivot is found
            while arr[i] <= pivot and i < high:
                i += 1
            # Move j until an element < pivot is found
            while arr[j] >= pivot and j > low:
                j -= 1
            # Swap if valid indices
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in its correct sorted position
        arr[low], arr[j] = arr[j], arr[low]

        # Return final index of pivot
        return j

    # Set initial low and high indices
    n = len(arr)
    low = 0
    high = n - 1

    # Call recursive quicksort
    qs(arr, low, high)

    # Return the sorted array
    return arr

# Read input from user
arr = list(map(int, input("Enter array elements: ").split()))

# Print the sorted result
print("Sorted array using Quick Sort:", quicksort(arr))

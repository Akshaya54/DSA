## Subsequence sum k

# 1.Brute Force – Generate All Subsets and Filter Size k
# Recursive function to generate all subsets
def generate(ind, curr_arr, ans, nums, k):
    if ind == len(nums):  # Base case: reached end of the list
        ans.append(curr_arr.copy())  # Save a copy of the current subset
        return
    
    # Include the current element
    curr_arr.append(nums[ind])
    generate(ind + 1, curr_arr, ans, nums, k)
    
    # Backtrack: Remove the last element and move forward without it
    curr_arr.pop()
    generate(ind + 1, curr_arr, ans, nums, k)

# Wrapper function
def subsets(nums: list[int], k: int) -> list[list[int]]:
    ind = 0
    curr_arr = []
    ans = []
    generate(ind, curr_arr, ans, nums, k)  # Generate all subsets
    
    # Check all subsets and return the first one of size k
    for lst in ans:
        if len(lst) == k:
            return lst  # Return first matching subset
    return "No"  # If no such subset exists



# 2. Optimal Solution – Subset Sum Problem (Sum = k)

# Recursive function to check if any subset sums up to k
def c(ind, arr, k):
    # Base case: found a subset whose sum is k
    if k == 0:
        return True
    # If we’ve used all elements or the remaining sum is negative
    if ind == len(arr):
        return False

    # Take the current element and reduce k
    path1 = c(ind + 1, arr, k - arr[ind])
    if path1:
        return True  # Early return if we found the solution

    # Don’t take the current element
    path2 = c(ind + 1, arr, k)

    # Return true if either path leads to a valid solution
    return path1 or path2

# Wrapper function
def sum(arr, k):
    ind = 0
    return c(ind, arr, k)



## Combination Sum III
'''
You are given two integers k and n, and you need to return all possible combinations of k distinct numbers from 1 to 9 that sum to n.
'''

# Recursive function to generate combinations
def generate(k, n, curr, ans):
    # Base Case: If sum becomes 0 and length is k, add valid combination
    if n == 0 and len(curr) == k:
        ans.append(curr.copy())
        return
    # Invalid Cases
    if n < 0 or len(curr) > k:
        return  # Stop recursion if sum is too small or list size exceeds k
    if n == 0 and len(curr) < k:
        return  # If we reach sum 0 but less than k elements → not valid
    # Set starting element
    if len(curr) == 0:
        ele = 1  # Start from 1 if no elements yet
    else:
        ele = curr[-1] + 1  # Ensure increasing order and uniqueness
    # Loop from current element up to 9
    for i in range(ele, 10):
        curr.append(i)  # Choose the number
        generate(k, n - i, curr, ans)  # Recurse with updated sum and combination
        curr.pop()  # Backtrack to try other possibilities
# Wrapper function
def comb3(k: int, n: int):
    curr = []  # Stores current combination
    ans = []   # Final answer list
    generate(k, n, curr, ans)
    return ans


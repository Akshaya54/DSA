### Subset generation

# Function to recursively generate subsets
def generate(ind, curr_arr, ans, nums):
    # Base case: if we reach the end of the array
    if ind == len(nums):
        ans.append(curr_arr.copy())  # Add a copy of the current subset to the answer
        return
    # Include the current element (take)
    curr_arr.append(nums[ind])      # Add nums[ind] to the current subset
    generate(ind + 1, curr_arr, ans, nums)
    curr_arr.pop()                  # Backtrack: remove the last element added
    # Exclude the current element (don't take)
    generate(ind + 1, curr_arr, ans, nums)

# Main function to generate all subsets
def subsets(nums: list[int]) -> list[list[int]]:
    ind = 0                # Starting index
    curr_arr = []          # Current subset being formed
    ans = []               # List to store all subsets
    generate(ind, curr_arr, ans, nums)
    return ans


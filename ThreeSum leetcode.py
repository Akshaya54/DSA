'''
Three Sum Problem Solutions

Given an array nums of n integers, find all unique triplets in the array which gives the sum of zero.

Solutions include:
1. Brute Force Approach
2. Hash Map/Dictionary Approach
3. Two Pointer Optimal Approach
'''

# Solution 1: Brute Force Approach
def three_sum_bruteforce(nums):
    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """
    s = set()
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    s.add(tuple(temp))
    return [list(t) for t in s]




# Solution 2: Hash Map Approach
def three_sum_hashmap(nums):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    s = set()
    n = len(nums)
    for i in range(n-1):
        hashmap = set()
        for j in range(i+1, n):
            k = -(nums[i] + nums[j])
            if k in hashmap:
                temp = tuple(sorted((nums[i], nums[j], k)))
                s.add(temp)
            hashmap.add(nums[j])
    return [list(t) for t in s]




# Solution 3: Two Pointer Optimal Approach
def three_sum(nums):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1) or O(n) depending on sorting
    """
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i+1, n-1
        while j < k:
            sums = nums[i] + nums[j] + nums[k]
            if sums < 0:
                j += 1
            elif sums > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
    return ans

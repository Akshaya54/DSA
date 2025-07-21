## Merge two sorted lists

# Input two sorted lists
nums1 = list(map(int, input("Enter sorted list 1: ").split()))
nums2 = list(map(int, input("Enter sorted list 2: ").split()))
# Initialize pointers for both lists
i = 0  # pointer for nums1
j = 0  # pointer for nums2
# Result list to store merged output
res = []
# Merge both lists until one is exhausted
while i < len(nums1) and j < len(nums2):
    # Compare elements at current positions
    if nums1[i] < nums2[j]:
        res.append(nums1[i])  # smaller element from nums1 is added
        i += 1                # move pointer in nums1
    else:
        res.append(nums2[j])  # smaller (or equal) element from nums2 is added
        j += 1                # move pointer in nums2
# If any elements left in nums1, add them
while i < len(nums1):
    res.append(nums1[i])
    i += 1
# If any elements left in nums2, add them
while j < len(nums2):
    res.append(nums2[j])
    j += 1
print(res)

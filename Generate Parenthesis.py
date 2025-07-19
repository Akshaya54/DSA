## Generate Valid Parentheses
'''
You're given an integer n, and you need to generate all possible combinations of n pairs of balanced parentheses.
Example:
Input: n = 3  
Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
Idea:
Each valid parentheses string must:
Have exactly n opening brackets (
Have exactly n closing brackets )
At no point should the number of ) be more than ( (to remain valid)
'''
# Recursive function to generate valid parenthesis strings
def gen(ind, cur, ans, opening, closing, n):
    # Base Case: when we use all n opening and closing brackets
    if opening == closing and ind == 2 * n:
        ans.append(cur)  # Add the valid string to answer list
        return
    # If we use more than n opening brackets → invalid
    if opening > n:
        return
    # Option 1: Add opening bracket if still allowed
    gen(ind + 1, cur + "(", ans, opening + 1, closing, n)
    # Option 2: Add closing bracket only if openings > closings
    if opening > closing:
        gen(ind + 1, cur + ")", ans, opening, closing + 1, n)

# Wrapper function
def generateparenthesis(n):
    ind = 0           # To keep track of total characters used
    cur = ""          # Current combination string
    ans = []          # Final list to store valid parentheses
    opening = 0       # Count of '(' used
    closing = 0       # Count of ')' used
    gen(ind, cur, ans, opening, closing, n)
    return ans

## Valid Parenthesis 
'''
You're given a string s that contains only:
'(', ')', '{', '}', '[' and ']'
You need to determine whether the input string is valid.
A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Each closing bracket must have a corresponding opening bracket before it.
'''
def valid(s):
    stack = []  # Initialize an empty stack to store opening brackets
    for i in s:
        # If character is an opening bracket, push to stack
        if i in "({[":
            stack.append(i)
        else:
            # If stack is empty but we get a closing bracket → invalid
            if len(stack) == 0:
                return False
            # Pop the last opening bracket from stack
            x = stack.pop()
            # Check if the popped bracket matches the closing one
            if (x == "(" and i == ")") or (x == "{" and i == "}") or (x == "[" and i == "]"):
                continue  # Valid match, continue checking
            else:
                return False  # Mismatch → invalid string
    # If stack is empty after processing all characters → valid
    return len(stack) == 0

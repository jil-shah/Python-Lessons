# Problem 1 --- Valid Parentheses
# LeetCode 20 --- Easy

# "()[]{}" → True
# "([)]"   → False
# Derive It
# For:

# ({[]})

# Brute Force
# Save a new array with the chracters as you go through it, when a close symbol is found, look at the letter before
# and see if it was the open equivalent and then remove the open
# if the character before doesnt match not valid parenthesis


# Faster
# Push values into a stack, when a closed one is found, pop the previous from the stack and see if its the open equivalent 
# O(n) where n is the list of letters O(n) because of the additional stack

def valid(order):
    stack = []
    pairs = {')': '(', '}': '{', ']':'['}

    for c in order:
        if c not in pairs:
            stack.append(c)
            continue
        x = stack[-1]
        # if stack is empty, the last is != pair of the current
        if not stack or x != pairs[c]: 
            return False
        stack.pop()


s = '([)]'
print(valid(s))

            

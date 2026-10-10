# 5. Problem 4 — Generate Parentheses (LC 22)
# Given n pairs of parentheses, write a function to generate all combinations of 
# well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# For n=2:

# (())
# ()()

# generate only valid strings to reduce the iterations
# '(' = 3 ')' = 3
# we want to create all combinations but ensure its valid
# we just need to ensure an opened bracket is closed before the end 

# multiple choices at each step add open, or add closed
# decision tree
# backtracking
# what choice am i making? which character to use 
# lets try 2 opens, 2 closes
# [] -> ( or )
# ( - has to staart with an open 
# state? how many open or close have we used 
# current, opened, closed states
# when can we add (? if both open closed are the same 
# can add open if opened < 0
# close rule? we can only add ) if closed < opened

def genParenthesis(n):
    results = []

    def backtrack(curr, opened, closed):
        if (opened == n and closed == n):
            results.append(curr)
            return
        
        # for open: opened < closed
        if (opened < n):
            backtrack(curr + '(', opened+1, closed)
        # for close: close < opened
        if (closed < opened):
            backtrack(curr + ')', opened, closed+1)

    backtrack("",0,0)
    return results

print(genParenthesis(3))
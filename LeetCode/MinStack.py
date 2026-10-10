# Problem 2 --- Min Stack
# LeetCode 155 --- Medium

# Support push, pop, top, and getMin in O(1).

# Normal minimum search would require scanning: O(n).

# Ask:

# Can I store minimum information as values are pushed?

# Example:
# values: [5, 2, 8, 1]
# mins:   [5, 2, 2, 1]


values= [5, 2, 8, 1]
mins=   [5, 2, 2, 1]

# min stack

# push, pop, top are all O(1) already as there base method push(), pop(), [-1]
# Get Min will not be 

# Brute Force: using the min(stack) will go through each element in the stack O(n)

# Optimize: so what we can do is save the minimum at each additional push. 
# With each additional push, compare against the min if its less than the min is different
# but what happens when a number is popped the min now is different, we would need to go through the list to find the new min
# Improvement: instead store a running list of the minimum 


class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, value):
        self.stack.append(value)
        if not self.stack or not self.mins or self.mins[-1] > value:
            self.mins.append(value)
        else:
            self.mins.append(self.mins[-1])
    def pop(self):
        self.stack.pop()
        self.mins.pop()
    
    def top(self):
        return self.stack[-1]
    
    def GetMin(self):
        return self.mins[-1]


if __name__  == '__main__':
    min_stack = MinStack()

    min_stack.push(5)
    min_stack.push(2)
    min_stack.push(8)
    min_stack.push(1)
    
    print(min_stack.stack)
    print(min_stack.top())

    print(min_stack.GetMin())
    min_stack.pop()

    print(min_stack.stack)
    print(min_stack.GetMin())
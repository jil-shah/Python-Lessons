s="()"
dict = {'(':')','[':']','{':'}'}
stack = []
if len(s)%2:
    print (False)
for i in s:
    if i in dict.keys():
        stack.append(i)
    else:
        if (stack==[]):
            print (False)
        a = stack.pop()
        print(a)
        if (i != dict[a]):
            print(False)
print(stack == [])
    
        

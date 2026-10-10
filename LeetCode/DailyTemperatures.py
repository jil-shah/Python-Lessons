# Problem 3 --- Daily Temperatures
# LeetCode 739 --- Medium

# [73,74,75,71,69,72,76,73]
# →
# [1,1,4,2,1,1,0,0]
# Brute force scans forward from every day → O(n²).
# we would need to scan the future values everytime for each new value

# Better question:
# Which previous days are still waiting for a warmer day?
# The stack stores indices of unresolved days.
# Why indices? Because:
# wait = current_index - previous_index

# so lets try: 
# index 0 - v = 73 -> add to the stack [73]
# index 1 - v = 74 -> compare through the stack. [74>73] = [1]. Update stack with 74 [74]
# index 2 - v = 75 -> [75 > 74] = [1, 1]. Stack = [75]
# index 3 - v = 71 -> [71 < 75] -> skip 71 is not warmer [1, 1, 0]. Stack = [75, 71]
# index 4 - v = 69 -> [69 < 71] -> skip  69 is not warmer [1, 1, 0, 0]. S = [75,71,69]
# this gives an issue how to know how many days have passed, should there be index in the stack 
# index 5 - v = 72 -> [72 > 69] = [1, 1, 0, 0, 1]. ST = [75,71] SI = [2,3]
#                     [72 > 71] = [1, 1, 0, 2, 1]. ST = [75] SI = [2] 5-3 = 2
#                     [72 < 75] -> Skip not warm.  ST = [75,72] SI = [2, 5]
# index 6 - v = 76 -> [76 > 72] = [1, 1, 0, 2, 1, 1]. ST = [75,71] SI = [2,3] 6-5 = 1 
#                     [76 > 75] = [1, 1, 4, 2, 1, 1]. ST = [76] SI = [6] 6 -2 = 4  

# O(n) for both because of the loop, each index is pushed 1 and popped 1, the index is never popped multiple times. 
def DailyTemps(temps):
    StackI = []
    Days = [0] * len(temps)
    for i,t in enumerate(temps):
        t = temps[i]
        while (StackI and t > temps[StackI[-1]]):
            prevI = StackI.pop()
            Days[prevI] = (i - prevI)

        StackI.append(i)
    return Days

t = [73,74,75,71,69,72,76,73]
print(DailyTemps(t))   

            
            





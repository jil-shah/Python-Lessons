# 692. Top K Frequent Words

# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Problem: 
# we need to know the frequency of each word
# the output needs to be ordered from highest frequency to lowest

# Example: 
# i: 2, love:2, leetcode:1, coding:1 k =2
# i, love

# does the capitilization matter? No
# if there are no words in words, what would be the expected reponse? EMPTY LIST

# APPROACH
# HEAP - MAX HEAP we need the top k frequent words
# dictionary which woould help us with storing the word and frequency 

# first step is the dictionary -> frequency O(N)
# second step would be to heapify the dictionary O(N)
# and then the output would just be just by extracting the top k elements

import heapq
def TopKelements(words, k):
    freqs = {}
    for word in words:
        if (word in freqs):
            freqs[word]+=1
        else:
            freqs[word] =1
    heap = []
    for word,freq in freqs.items():
        heapq.heappush(heap,(-1*freq, word))
    results = []
    for i in range (k):
        maxword = heapq.heappop(heap)
        results.append(maxword[1])
    return results
words = ["i","love","leetcode","i","love","coding"]
k = 2

print(TopKelements(words,k))
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(TopKelements(words,k))
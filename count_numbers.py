"""Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive)."""

class Solution(object):
    def countOdds(low, high):
        return int(((high + high%2)-(low - low%2))/2)
    
Solution.countOdds(2, 9)    
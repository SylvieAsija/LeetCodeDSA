'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true


Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''
'''
SOLUTION
Runtime: O(n) -> 7 ms -> beats 97.35%
Memory:          12.09 MB -> beats 13.35%
'''
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    s_index = 0
    if s == "":
        return True
    elif t == "":
        return False
    
    for t_index in range(len(t)):
        if s[s_index] == t[t_index]:
            s_index += 1
            if s_index == len(s):
                return True
    return False
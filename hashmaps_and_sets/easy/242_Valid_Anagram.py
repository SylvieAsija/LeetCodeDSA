'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''
'''
SOLUTION
Runtime: 11ms O(n + m) -> 11ms -> beats 93.18%
Memory:               12.66MB -> beats 67.80%
'''


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    letters = {}

    for letter in s:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    for letter in t:
        if letter not in letters or letters[letter] == 0:
            return False
        else:
            letters[letter] -= 1

    return True

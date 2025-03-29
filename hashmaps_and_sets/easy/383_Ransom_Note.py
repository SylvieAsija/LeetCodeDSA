'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
'''
SOLUTION
Runtime: 30ms O(n + m) -> 30ms -> beats 59.02%
Memory:               12.65MB -> beats 77.15%
'''


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    letters = {}

    for letter in magazine:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    for letter in ransomNote:
        if letter in letters and letters[letter] > 0:
            letters[letter] -= 1
        else:
            return False

    return True

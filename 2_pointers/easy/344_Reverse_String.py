'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''
'''
SOLUTION
Runtime: 3ms O(n) -> 3ms -> beats 55.10%
Memory:               20.28MB -> beats 18.10%
'''


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    start = 0
    end = -1

    for _ in range(len(s)/2):
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1

    return s

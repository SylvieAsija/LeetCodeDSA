'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
'''
SOLUTION
Runtime: O(n) -> 39 ms -> beats 38.59%
Memory:          12.58 MB -> beats 73.86%
'''
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.replace(" ", "").lower()
    s_index = 0
    e_index = len(s) - 1
    while s_index < len(s):
        if (s[s_index].isalpha() or s[s_index].isalnum()):
            if (s[e_index].isalpha() or s[e_index].isalnum()):
                if s[s_index] != s[e_index]:
                    return False
                else:
                    s_index += 1
                    e_index -= 1
            else:
                e_index -= 1
        else:
            s_index += 1

    return True
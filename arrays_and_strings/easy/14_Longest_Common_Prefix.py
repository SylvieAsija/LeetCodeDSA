'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
'''
SOLUTION
Runtime: O(n) -> 15 ms -> beats 70.62%
Memory:          11.97 MB -> beats 22.86%
'''
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) <= 1:
        return strs[0]
    
    strs.sort()
    prefix = 0
    for letter in range(min(len(strs[0]),len(strs[len(strs)-1]))):
        if strs[0][letter] == strs[len(strs)-1][letter]:
            prefix += 1
        else:
            break
    return strs[0][:prefix]
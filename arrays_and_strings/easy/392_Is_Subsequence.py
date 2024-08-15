'''
SOLUTION
Runtime: O(n) -> 7 ms -> beats 97.35%
Memory:          12.09 MB -> beats 13.35%
'''
def isSubsequence(self, s, t):
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
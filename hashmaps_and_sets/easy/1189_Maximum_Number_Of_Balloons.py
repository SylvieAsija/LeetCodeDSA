'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
'''
'''
SOLUTION
Runtime: 4ms O(n + m) -> 4ms -> beats 67.86%
Memory:               12.57MB -> beats 46.73%
'''


def maxNumberOfBalloons(text):
    """
    :type text: str
    :rtype: int
    """
    hashmap = {}
    for letter in "baloon":
        hashmap[letter] = 0

    for letter in text:
        if letter in hashmap:
            hashmap[letter] += 1

    return min(hashmap['b'], hashmap['a'], hashmap['l'] / 2, hashmap['o'] / 2, hashmap['n'])

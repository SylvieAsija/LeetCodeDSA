'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''
'''
SOLUTION
Runtime: 8ms O(n) -> 8ms -> beats 60.69%
Memory:               13.60MB -> beats 90.06%
'''


def maxNumberOfBalloons(self, text):
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

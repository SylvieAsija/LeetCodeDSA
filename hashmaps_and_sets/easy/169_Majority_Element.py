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


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    
    return max(hashmap, key=hashmap.get)
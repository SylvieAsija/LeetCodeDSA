'''
Given an integer array nums of size n, return the number with the value closest to 0 
in nums. If there are multiple answers, return the number with the largest value.

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.


Example 2:
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:
1 <= n <= 1000
-105 <= nums[i] <= 105
'''
'''
SOLUTION
Runtime: O(n) -> 107 ms -> beats 49.32%
Memory:          11.57 MB -> beats 99.46%
'''
def findClosestNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    closest = 1e7
    max_close = -1e7
    for val in nums:
        if abs(val) < closest:
            closest = abs(val)
            max_close = val
        elif abs(val) == closest:
            max_close = max(val, max_close)
    return max_close
    
print(findClosestNumber([-4,-2,1,4,8]))
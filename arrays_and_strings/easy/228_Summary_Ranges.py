'''You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array 
exactly. That is, each element of nums is covered by exactly one of the ranges, and 
there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"


Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''
'''
SOLUTION
Runtime: O(n) -> 8 ms -> beats 88.44%
Memory:          11.62 MB -> beats 53.54%
'''
def summaryRanges( nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) == 0:
        return
    
    ranges = []

    if len(nums) == 1:
        ranges.append(str(nums[0]))
        return ranges
    
    counter = 0
    smallest = nums[0]
    prev = smallest

    for number in nums[1:]:
        if number - 1 == prev:
            counter += 1
            if number == nums[-1]:
                ranges.append(str(smallest) + "->" + str(smallest + counter))
        else:
            if counter:
                range = str(smallest) + "->" + str(smallest + counter)
            else: 
                range = str(smallest)
            counter = 0
            smallest = nums[nums.index(number)]
            ranges.append(range)
            if number == nums[-1] or len(nums) == 1:
                print("here")
                ranges.append(str(smallest))
        prev = number
    
    return ranges
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
profit, return 0.

 
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before 
you sell.


Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104'''
'''
SOLUTION
Runtime: O(n) -> 735 ms -> beats 67.37%
Memory:          20.84 MB -> beats 60.02%
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy_day = 0
    sell_day = len(prices)-1
    profit = 0
    for days in range(len(prices)):
        if prices[days] < prices[buy_day]:
            buy_day = days
            sell_day = days + 1
        elif prices[days] - prices[buy_day] > profit and sell_day > buy_day:
            sell_day = days
            profit = prices[sell_day] - prices[buy_day]
    if profit:
        return profit
    return 0


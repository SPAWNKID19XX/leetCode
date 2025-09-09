'''
Problem: Summer Sale Discount

A shop wants to apply a discount of discount% to the most expensive item purchased by a customer during the sales period.
Only one product (the most expensive one) can benefit from the discount.

You need to implement the function:

    def calculate_total_price(prices, discount):

    -prices: a list of integers representing the prices of products purchased.
    -discount: an integer between 0 and 100, representing the percentage discount applied to the most expensive product.

The function should return the total purchase price as an integer, rounded down if the result is a float.

Constraints:

    -0 ≤ discount ≤ 100
    -0 < price of a product < 100000
    -0 < number of products < 100
'''

class Solution():
    def calculate_total_price(self, prices: list, discount: int) -> int:

        res = 0
        
        if not prices:
            return res

        ex_prod = max(prices)
        discounted = (ex_prod*discount)/100

        res = sum(prices)-discounted

        return int(res)

a = Solution()
print(a.calculate_total_price([20,50,100], 10))
print(a.calculate_total_price([100, 200, 300], 20))
print(a.calculate_total_price([5, 5, 5, 5], 50))
print(a.calculate_total_price([1000], 100))
print(a.calculate_total_price( [10, 20, 30, 40, 50], 25))
print(a.calculate_total_price( [], 25))

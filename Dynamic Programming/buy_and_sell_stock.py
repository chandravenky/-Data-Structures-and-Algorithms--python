

#Inefficient solution
def buy_and_sell_stocks_1(input_array):

  dp = []

  if len(input_array)<=1:
    return 0
    
  for i in range(1, len(input_array)):
    
    buy_min = min(input_array[:i])

    sell = input_array[i]

    profit = max(sell - buy_min, 0)

    dp.append(profit)

  return max(dp)
  
def test_buy_and_sell_stocks(input_function):

  input_array_example_1= [7,1,5,3,6,4]

  input_array_example_2= [7,6,4,3,1]

  expected_amt_example_1= 5

  expected_amt_example_2= 0

  actual_amt_example_1= input_function(input_array_example_1)

  actual_amt_example_2= input_function(input_array_example_2)

  return expected_amt_example_1 == actual_amt_example_1 and expected_amt_example_2 == actual_amt_example_2

#Better solution
def buy_and_sell_stocks(input_array):

  dp = []

  if len(input_array)<=1:
    return 0

  buy_min = input_array[0]
  max_profit =0
    
  for i in range(1, len(input_array)):

    if input_array[i] < buy_min:
      buy_min = input_array[i]

    if input_array[i] - buy_min > max_profit:
      max_profit = input_array[i] - buy_min

  return max_profit

print(test_buy_and_sell_stocks(buy_and_sell_stocks_1))

#Leetcode
class Solution(object):
    
    def maxProfit(self, prices):
        
        dp = []

        if len(prices)<=1:
            return 0

        buy_min = prices[0]
        max_profit =0

        for i in range(1, len(prices)):

            if prices[i] < buy_min:
                buy_min = prices[i]

            if prices[i] - buy_min > max_profit:
                max_profit = prices[i] - buy_min

        return max_profit

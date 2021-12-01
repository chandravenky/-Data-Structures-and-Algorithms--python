


def house_rob_tot_amt(input_array):

  dp = [0, input_array[0]]


  for i in range(1, len(input_array)):
    
    dp.append(max(dp[i], input_array[i] + dp[i-1]))

  return dp[len(input_array)]

def test_house_rob_tot_amt():

  input_array= [2,7,9,3,1]

  expected_amt= 12

  actual_amt= house_rob_tot_amt(input_array)

  return expected_amt == actual_amt

print(test_house_rob_tot_amt())

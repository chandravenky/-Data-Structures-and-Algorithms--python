

def findfibonnaci(number):

  if number== 0:
    return 0

  if number== 1:
    return 1

  return findfibonnaci(number-1) + findfibonnaci(number-2)

def findfibonnaci_test():

  index = 10
  fib_output_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  print(assert findfibonnaci(index)== fib_output_array[index])

findfibonnaci_test()
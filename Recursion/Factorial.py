

def findFactorial(number):

  if number ==1:
    return 1

  return number* findFactorial(number-1)

print(findFactorial(4))

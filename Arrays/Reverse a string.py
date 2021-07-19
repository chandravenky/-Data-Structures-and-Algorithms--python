def reverse(string):

  reversed_string = ''

  for index in range(len(string), 0, -1):

    reversed_string = reversed_string + string[index-1]

  return reversed_string


print(reverse("John"))
print(reverse("The quick brown fox"))




def reverseString(input_string):

  if not len(input_string):
    return ''
  
  string = input_string[len(input_string)-1]
  
  remaining_string = input_string[:len(input_string)-1]

  return string + reverseString(remaining_string)

print(reverseString('hello world'))
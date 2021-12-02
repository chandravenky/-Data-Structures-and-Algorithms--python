

def reverse_string(input_string_array):
  
  if len(input_string_array)<=1:
    return input_string_array

  for i in range(0, len(input_string_array)//2):
    
    char_on_hold = input_string_array[i]

    input_string_array[i] = input_string_array[len(input_string_array)-i-1]

    input_string_array[len(input_string_array)-i-1] = char_on_hold

  return input_string_array

def test_reverse_string():

  input_string_array_1= ["h","e","l","l","o"]
  input_string_array_2= ["H","a","n","n","a","h"]

  expected_ouput_1= ["o","l","l","e","h"]
  expected_ouput_2= ["h","a","n","n","a","H"]

  actual_output_1= reverse_string(input_string_array_1)
  actual_output_2= reverse_string(input_string_array_2)

  return actual_output_1 == expected_ouput_1 and actual_output_2 == expected_ouput_2

print(test_reverse_string())

#For leetcode

class Solution(object):
    
    def reverseString(self, input_string_array):
  
        if len(input_string_array)<=1:
            return input_string_array

        for i in range(0, len(input_string_array)//2):
            
            char_on_hold = input_string_array[i]

            input_string_array[i] = input_string_array[len(input_string_array)-i-1]

            input_string_array[len(input_string_array)-i-1] = char_on_hold

        return input_string_array

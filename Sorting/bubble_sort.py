

def bubble_sort(input_array):

  for i in range(0, len(input_array)):
    for j in range(0, len(input_array)-1):

      if input_array[j]>input_array[j+1]:
        temp = input_array[j]
        input_array[j] = input_array[j+1];
        input_array[j+1] = temp

  return input_array

input_array = [3,4,5,1,2,3,3,9,7]
print(bubble_sort(input_array))

#Test

def bubble_sort_test():

  input_array = [4.2,1.1,7,9,8,4,7]

  expected_output_array = [1.1,4,4.2,7,7,8,9]

  return bubble_sort(input_array) == expected_output_array

print(bubble_sort_test())


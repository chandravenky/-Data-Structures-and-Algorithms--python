

def insertion_sort(input_array):

  for i in range(0, len(input_array)):

    for j in range(i+1, len(input_array)):

      if input_array[j] < input_array[i]:

        temp = input_array[i]

        input_array[i] = input_array[j]
        input_array[j] = temp   

  return input_array

input_array = [3,4,5,1,2,3,3,9,7]
print(insertion_sort(input_array))

def insertion_sort_test():

  input_array = [4.2,1.1,7,9,8,4,7]

  expected_output_array = [1.1,4,4.2,7,7,8,9]

  return selection_sort(input_array) == expected_output_array

print(insertion_sort_test())


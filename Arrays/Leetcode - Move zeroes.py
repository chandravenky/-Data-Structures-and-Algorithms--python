#O(n^2) - Does not run on Leetcode
class Solution(object):
    def moveZeroes(self, input_array):
        
        zero_array = []

        for i in input_array:

            if i ==0:
                zero_array.append(0)
                input_array.remove(i)
        
        
        result = input_array + zero_array
        result = input_array + zero_array
        return zero_array

#O(n) solution
class Solution:
    def moveZeroes(self, input_array):
        
        index = 0

        for i in input_array:

            if i !=0:
                input_array[index] =i
                index = index+ 1

        for i in range(index, len(input_array)):

            input_array[i] = 0

        return input_array
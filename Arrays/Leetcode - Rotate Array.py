class Solution(object):
    def rotate(self, input_array, k):
        
        if len(input_array)<2 or k==0 or k==len(input_array):
            return input_array
        
        if k> len(input_array):
            k= k%len(input_array)
        
        
        first_array = input_array[len(input_array)-k:] 
        second_array = input_array[0:len(input_array)-k]
        
        result_array = first_array + second_array
        
        input_array[:] = result_array
        
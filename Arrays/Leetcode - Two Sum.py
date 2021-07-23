#Brute force
class Solution(object):
    def twoSum(self, input_array, target):
        for i in range(0, len(input_array)):

            for j in range(0, len(input_array)):
                
                if input_array[i] + input_array[j] == target and i!=j:

                    return [i,j]


print(two_sum([3,3], 6)

#Sorted array (positive)
def two_sum(input_array, target):

  i=0;
  j= len(input_array)-1

  while i < len(input_array) and j> 0:

    if(input_array[i]) + (input_array[j]) == target:
      return [i,j]

    if(input_array[i]) + (input_array[j]) >target:

      j=j-1
    
    elif(input_array[i]) + (input_array[j]) <target:

      i=i+1



print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))

#HashMap
class Solution(object):
    def twoSum(self, input_array, target):
        val_index_dict = {}

        for index in range(0, len(input_array)):
            
            val_index_dict[input_array[index]] = index
            
        for index in range(0, len(input_array)):
            
            diff = target - input_array[index]
            
            if diff in val_index_dict and index!=val_index_dict[diff]:
                
                return [index, val_index_dict[diff]]
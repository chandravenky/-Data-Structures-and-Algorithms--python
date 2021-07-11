
def merge_sorted_arrays(array1, array2):

  merged_array = []
  i=0
  j=0

  while i< len(array1) and j< len(array2):

    if array1[i] < array2[j]:
      merged_array.append(array1[i])
      i = i + 1
    
    else:
      merged_array.append(array2[j])
      j=j+1

  return merged_array + array1[i:] + array2[j:]


print(merge_sorted_arrays([0,3,4,31], [4,6,30]))

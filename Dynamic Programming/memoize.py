cache = {}

def memoize_add_to_80(n, cache):

  if n in cache:
    print('cache used')
    return cache[n]
  
  else:
    cache[n] = n+80
    return cache[n]

def test_memoize_add_to_80_cache():

  input_number = 5
  input_cache = {}

  output_number = memoize_add_to_80(input_number, input_cache)

  return input_number in input_cache

print(test_memoize_add_to_80_cache())
print(memoize_add_to_80(5, cache))
print(memoize_add_to_80(5, cache))

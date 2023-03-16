str = 'aabbbbbbbcdeffff'
arr = {}

for element in str:
  if element not in arr.keys():
    arr[element] = 0 # inicjuje element jeśli jeszcze go nie ma w tablicy
  arr[element] += 1
print(arr, arr.keys())
print(max(arr.values()), max(arr, key = arr.get))


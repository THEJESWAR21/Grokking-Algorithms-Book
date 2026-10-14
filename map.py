from functools import reduce
arr1 = [1,2,3,4,5]
arr2 = map(lambda x: 2 * x, arr1)

result = list(arr2)

print(type(arr2))
print(result)

arr3 = reduce(lambda x,y: x+y, arr1)

print(type(arr3))
print(result)

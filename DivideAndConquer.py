def sumarr(arr):
    if arr == []: # Base Case
        return 0
    else:
        return arr[0] + sumarr(arr[1:])

print(sumarr([2,3,4,5,6])) # 20

def countarr(arr):
    if arr == []:
        return 0
    else:
        return 1 + countarr(arr[1:])

print(countarr([2,3,4,5,6])) # 5

def maxnum(arr):
    sorted_list = []
    # Outer Loop: that append the smallest number to the new list
    for i in range(len(arr) - 1): # the final item will be the smallest so comparing against itself is redundant.
        smallest = i
        # Inner Loop: Checking for smallest number in the list
        for x in range(i+1, len(arr)):
            if arr[x] < arr[smallest]:
                smallest = x
        
        smallest_val = arr.pop(smallest)
        arr.insert(i, smallest_val)

    return arr

print(maxnum([2,7,1,9,14])) # 5
print()

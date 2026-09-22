def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    sorted_arr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sorted_arr.append(arr.pop(smallest))

    return sorted_arr

def selectionSort2(arr):
    for i in range(len(arr) - 1): # Outer Loop shifts lowest value to the front of the list
        smallest_i = i # takes the first index
        
        for j in range(i+1, len(arr)): # Inner Loop checks for the smallest number
            if arr[j] < arr[smallest_i]:
                smallest_i = j

        smallest_value = arr.pop(smallest_i)
        arr.insert(i, smallest_value)

    return arr

print(selectionSort([2,5,3,1,4,8,0,9,6,7]))
print(selectionSort2([2,5,3,1,4,8,0,9,6,7]))

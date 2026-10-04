def quicksort(array):
    less = []
    greater = []

    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))

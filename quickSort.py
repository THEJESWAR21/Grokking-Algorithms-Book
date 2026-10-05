from time import sleep

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

def print_items(array):
    for item in array:
        sleep(1)
        print(item)

print_items([1,2,3,4,5,6])

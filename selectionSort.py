def findSmallest(nums):
    smallest = nums[0]
    smallest_index = 0

    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i

    return smallest_index

def selectionSort(nums):
    sortest_nums = []

    for i in range(len(nums)):
        smallest = findSmallest(nums)
        sortest_nums.append(nums.pop(smallest))

    return print(sortest_nums)


selectionSort([2,5,3,1,4,8,0,9,6,7])


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def binarySearch(search_term):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == search_term:
            print("YOU GOT IT")
            print(mid)
            break
        elif guess < search_term:
            low = mid + 1
        else:
            high = mid - 1

binarySearch(20)

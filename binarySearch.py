# alaphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def binarySearch(target):
    low = 0
    high = len(nums) - 1


    while high >= low:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            print(f"Target Found Position: {mid}")
            break
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


binarySearch(25)

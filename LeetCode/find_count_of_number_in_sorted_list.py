#lower bound upper bound logic

def find_count(nums, target):

    #find_left_index
    low = 0
    high = len(nums) - 1
    left_index = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            left_index = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    #find right index
    low = 0
    high = len(nums) - 1
    right_index = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            right_index = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return left_index, right_index


target = int(input())
print(find_count([1,2,2,2,2,3,3,3,4,5,6,7,8,9], target))
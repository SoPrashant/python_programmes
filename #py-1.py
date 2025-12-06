#py-1
#sorted array return start and finish index of the target value


def findFirst(nums,target):
    left = 0
    right = len(nums)-1
    ans = -1

    while left<=right:
        mid = (left+right)//2

        if nums[mid] == target:
            ans = mid
            right = mid-1
        elif nums[mid]<=target:
            left = mid+1
        else:
            right = mid-1
    return ans


def findLast(nums,target):
    left = 0
    right = len(nums)-1
    ans = -1

    while left<=right:
        mid = (left+right)//2

        if nums[mid] == target:
            ans = mid
            left = mid+1
        elif nums[mid]<=target:
            left = mid+1
        else:
            right = mid-1
    return ans            

def searchRange(nums,target):
    return ([findFirst(nums,target),findLast(nums,target)])

nums = [2,2,4,4,5,6,7,7,7,7,8,9,9,9]
target = int(input())
print(searchRange(nums,target))



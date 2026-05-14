# 3. Find missing number in a list
# Nums = [1,2,4,5,7,8,10,12]


def find_missing_number(nums):
    missing_number = []

    for i in range(len(nums)-1):
        current = nums[i]
        next = nums[i+1]

        if next - current > 1:
            for j in range(current+1,next):
                missing_number.append(j)

    return missing_number

print(find_missing_number([1,2,4,5,7,8,10,12]))
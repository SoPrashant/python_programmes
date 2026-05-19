

def freq(target, arr):
    ub = len(arr)-1
    lb = 0
    a = -1
    b = -1
    while lb <= ub:
        if arr[lb] == target:
            a = lb
        else:
            lb += 1
        if arr[ub] == target:
            b = ub
        else:
            ub -= 1

        if a != -1 and b != -1:
            break

    if a == -1:
        return 0

    return (b-a+1)

arr = [1,2,2,2,3,4,5]

print(freq(2, arr))

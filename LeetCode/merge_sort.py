#divide an conquer algorithm merge sort

def merge_sort(arr1, arr2):
    i = j =0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

arr1 = [12,15,26,38]
arr2 = [2,4,78,345]

print(merge_sort(arr1, arr2))
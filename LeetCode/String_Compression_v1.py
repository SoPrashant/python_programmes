
def string_compression(arr):
    result = ""
    count = 1

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            result += arr[i] + str(count)
            count = 1

    result += arr[-1] + str(count)
    return result

strr = "aabbbcddea"

print(string_compression(strr))


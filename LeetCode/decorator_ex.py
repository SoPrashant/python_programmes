def decorator(func):
    def wrapper(*args):
        print("Logging the values of",func,"is",args)
        return func(*args)
    return wrapper

@decorator
def operation(x,y):
    return x+y

operation(3,4)

print(operation(10,20))

print(list(range(10)))


arr1 = [1,2,3,4]
arr2 = arr1
arr3 = arr1[:]
arr1.append(5)
arr2.append(6)
print(arr1)
print(arr2) # [1,2,3,4,5]
print(arr3) # [1,2,3,4]
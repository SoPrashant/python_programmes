def fib(n, value_dict):
    if n ==0 or n == 1:
        return n

    if n in value_dict:
        return value_dict[n]

    value_dict[n] = fib(n-1, value_dict) + fib(n-2, value_dict)
    return value_dict[n]

print(fib(3,{}))
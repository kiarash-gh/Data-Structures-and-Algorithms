def fibonacci(n):
    assert n >= 0 and int(n) == n, "fibonacci number can not be negative or non integer"
    if n in [1, 0]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)



number = int(input("Enter a number to calculate fibonacci: \n"))
print("the answer is {}".format(fibonacci(number)))
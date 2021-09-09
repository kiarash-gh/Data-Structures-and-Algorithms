def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number to calculate factorial: \n"))
print("the factorial of {} is {}".format(number, factorial(number)))
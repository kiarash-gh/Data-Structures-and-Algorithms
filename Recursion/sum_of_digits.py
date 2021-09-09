# Finding the sum of digits of a positive integer number using recursion

def sum_of_digits(n):
    assert n >= 0 and int(n) == n , "The number must be positive integer"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n / 10))


number = int(input("Enter a number to sum the digits \n"))
print("the sum of digits of {} is {}".format(number, sum_of_digits(number)))
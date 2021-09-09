# convertinf a number from decimal to binary using recursion

def decimal_to_binary(n):
    assert int(n) == n, "the number must be integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n / 2))
    

number = int(input("Enter a number: "))
print("the binary form of {} is {}".format(number, decimal_to_binary(number)))
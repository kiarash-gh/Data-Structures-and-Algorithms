# finding GCD of two numbers using recursion
# Euclidean algorithm
# gcd(48, 18)
# step 1: 48/18 = 2 remainder 12
# step 2: 18/12 = 1 remainder 6
# step 1: 12/6 = 2 remainder 0
# gcd is 6

def gcd(num1, num2):
    assert int(num1) == num1 and int(num2) == num2, "The numbers must be integer"
    if num1 < 0 :
        num1 = -1 * num1
    if num2 < 0 :
        num2 = -1 * num2  
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("the GCD is: ",gcd(number1, number2))
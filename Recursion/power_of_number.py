# calculating power of a number using recursi

def power_of_numer(base, exp):
    assert exp >= 0 and int(exp) == exp , "The exponent must be integer and positive"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power_of_numer(base, exp-1)


number = int(input("Enter a number: "))
exponent = int(input("Enter an exponent: "))
print("the answer is: ",power_of_numer(number,exponent))
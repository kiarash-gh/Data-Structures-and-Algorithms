# def recursive_methode(parameters):
#     if exit conditon satisfied:
#         return some value
#     else:
#         recursive_methode(modified parameters)



def recursive_methode(n):
    if n < 1:
        print("{} is less than 1".format(n))
    else:
        recursive_methode(n - 1)
        print(n)


recursive_methode(4)
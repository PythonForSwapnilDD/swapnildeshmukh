def fact(no):
    if(no==0):
        return 1
    return no*fact(no-1)

value=5
ret=fact(value)
print("Factorial of {} is {}".format(value,ret))

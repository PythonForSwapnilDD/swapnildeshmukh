def EvenNum(a):
    i = 1
    j = 1
    while j <= a:
        if i %2 == 0:
            print(i, end=" ")
            j = j + 1
        i = i + 1

a= int(input("Enter number"))
EvenNum(a)

def even (a):
    if a % 2 == 0:
        b = True
        return(b)
    else:
        b = False
        return(b)
r = int(input("Введите число - "))
TF = even(r)
if TF == True:
    print("Число ",r," четное")
else:
    print("Число ",r," нечетное")
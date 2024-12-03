def S(a):
    b = PI*a*a
    return(b)
def C(a):
    b = PI*a*2
    return(b)
PI = 3.14  

r = float(input("Введите радиус круга - "))
square = S(r)
Circle = C(r)
print("Длинна окружности равна с радиусом ",r, " см равна ", Circle)
print("Площадь круга равна с радиусом ",r, " см равна ", square)
def sum(a):
    b = a.split()
    m = 0
    print(b)
    for i in range(0,len(b)):
        m = m + int(b[i])
    return(m)
list = input("Введите список из чисел ")
summ = sum(list)
print("Сумма всех чисел в списке равна", summ)
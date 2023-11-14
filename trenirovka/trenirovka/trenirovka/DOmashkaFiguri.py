def my_function(x):
    return x+x*x
A = float(input("Введите начальную точку A: "))
B = float(input("Введите конечную точку B: "))
while True:

    H = float(input("Введите шаг H (положительное значение): "))
    if H > 0 and A + H <= B:
        break
    elif H <= 0:
        print("Шаг должен быть положительным числом. Пожалуйста, введите корректное значение.")
    else:
        print("Шаг H слишком большой, чтобы достичь B из A. Пожалуйста, введите другое значение.")
if (A - B) % H == 0:
    print("{:<10} {:<10}".format("Значение x", "Значение y"))
    x = A
    while x <= B:
        y = my_function(x)
        print("{:<10} {:<10}".format(x, y))
        x += H
else:
    print("Значение H не подходит. С ним мы не попадём из A в B.")
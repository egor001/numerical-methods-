import math
import random

def Function(x):
    return x * math.atan(x) + (x / 2) * math.cos(x) - 3  # (0,10)


def Diff_Function(x):
    return math.atan(x) + x / (1 + x ** 2) + math.cos(x) / 2 - (x * math.sin(x)) / 2


def Dihtomy(a, b, e, Function):
    count = 0
    left = a
    right = b
    while abs(left - right) > e:
        temp = (left + right) / 2
        count = count + 1
        if (Function(temp) == 0):
            return temp
        elif (Function(temp) * Function(left) < 0):
            right = temp
        elif (Function(temp) * Function(right) < 0):
            left = temp
    N = int(math.log(abs((b - a) / e), 2)) + 1
    print("точность: "+str(e))
    print("количество итераций по циклу: "+str(count))
    print("количество итераций по формуле" + str(N))
    print("нуль функции: "+ str(right))

#res = math.log(abs(x3/1))/math.log(abs(x2))

def Newton(a, b, err, f, diff_f):
    count = 0
    x = (a + b) / 2
    while (abs(f(x)) > err):
        x = x - f(x) / diff_f(x)
        count = count + 1
    print("количество итераций по циклу: "+str(count))
    print("нуль функции: "+ str(x))

def Chord(a,b, f, err):
    count = 0
    x1 = 0
    x2 = 3
    while abs(f(x2)) > err:
        count = count + 1
        temp = x2
        x2 = x1 + f(x1) * (x2-x1) / (f(x2) - f(x1))
        x1 = temp
    print("Метод хорд: " + str(x2))
    print("количество итераций по циклу: " + str(count))

def Convergence_rate(f,diff_f,a,b):
    x = (a + b) / 2
    n = 5
    for i in range(0,n-2):
        x = x - f(x) / diff_f(x)

    x1 = x - f(x) / diff_f(x)
    x2 = x1 - f(x1) / diff_f(x1)
    x3 = x2 - f(x2) / diff_f(x2)
    result = math.log(abs((x3 - x2))) / math.log(abs((x3 - x1)))
    print("скорость сходимости для метода Ньютона: ",result)

err = 10 ** (-3)
Dihtomy(0, 10, err, Function)
Newton(0, 10, err, Function, Diff_Function)
print()

err = 10 ** (-6)
Dihtomy(0, 10, err, Function)
Newton(0, 10, err, Function, Diff_Function)
Chord(0,10,Function,err)
print()

err = 10 ** (-9)
Dihtomy(0, 10, err, Function)
Newton(0, 10, err, Function, Diff_Function)
Convergence_rate(Function,Diff_Function,0,10)

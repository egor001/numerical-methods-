import math
import matplotlib.pyplot as plt
#from sympy import diff , cos, ln, integrate, sin
from sympy import *
import numpy as np
from scipy import integrate
#f(x)=x^5sin(x) [-1;1]
min = -1
step = 0
temp = -1
points = []
number = int(input('введите количество точек '))# вводить две и более точек
step = 2/(number - 1)

for i in range(0,number):
    points.append(temp)
    temp = temp + step

print('точки ', points) #точки
max=points[number-1]
def Function(x):
    result = (x**5)*math.sin(x)
    return result
def Integral(min,max):
    #x =Symbol('x')
    result,err = integrate.quad(Function,min,max)
    return result
def Method_rectangle(arr_x,step,Function,max):
    result=0
    for i in range(0, len(arr_x)-1):
        result= result+step*Function(arr_x[i]+step/2)
    return result

def Method_trapezoid(arr_x,step,Function,max):
    result = 0
    for i in range(0, len(arr_x)-1):
        result = result + step * (Function(arr_x[i]) + Function(arr_x[i+1]))/2
    return result
def Method_Simpson(arr_x,step,Function,max):
    result = 0
    for i in range(0, len(arr_x)):
        if (arr_x[i] != max):
            result = result + step*(1/6) * (Function(arr_x[i])+ 4*Function(arr_x[i] + step / 2)+Function(arr_x[i+1]))
    return result

def Method_Gauss(arr_x,step,Function,max):
    result=0
    for i in range(0,len(arr_x)-1):
        temp1 = (arr_x[i+1]-arr_x[i])/2
        temp2 = (arr_x[i+1]+arr_x[i])/2
        result =result + temp1*1/9*(5*Function(temp2+temp1*(3/5)**(0.5)) + 5*Function(temp2+temp1*(-((3/5)**(0.5)))) +8*Function(temp2))
    return result


def Inaccuracy(Method,name,min):
    arr = np.array([x for x in range(3,100)])
    arr_1 = []
    for i in range(3,100):
        points=[]
        number = i
        step = 2 / (number - 1)
        temp = -1

        for j in range(0, number):
            points.append(temp)
            temp = temp + step
        max = points[len(points) - 1]
        result = abs(Method(points,step,Function,max) - Integral(min,max))
        arr_1.append(result)
    plt.plot(arr, arr_1,label=name )
    plt.grid()
    plt.legend()

def Inaccuracy_log(Method,name):
    arr = []
    arr_1 = []
    for i in range(3, 100):
        points = []
        number = i
        step = 2 / (number - 1)
        temp = -1
        arr.append(ln(step))
        for j in range(0, number):
            points.append(temp)
            temp = temp + step
        max = points[len(points) - 1]
        result = ln(abs(Method(points, step, Function, max) - Integral(min, max)))
        arr_1.append(result)
    plt.plot(arr, arr_1, label=name)
    plt.grid()
    plt.legend()

str="метод прямоугольников"
Inaccuracy(Method_rectangle,str,min)
print(Method_rectangle(points,step,Function,max))
print(Method_trapezoid(points,step,Function,max))
print(Method_Simpson(points,step,Function,max))
print(Method_Gauss(points,step,Function,max))
print(Integral(-1,1))
str="метод трапеции"
Inaccuracy(Method_trapezoid,str,min)
str="метод Симпсона"
Inaccuracy(Method_Simpson,str,min)
str="метод Гаусса"
Inaccuracy(Method_Gauss,str,min)

plt.figure()
plt.title("зависимость ошибки от шага")
str="метод прямоугольников"
Inaccuracy_log(Method_rectangle,str)
str="метод трапеции"
Inaccuracy_log(Method_trapezoid,str)
str="метод Симпсона"
Inaccuracy_log(Method_Simpson,str)
str="метод Гаусса"
Inaccuracy_log(Method_Gauss,str)

plt.show()

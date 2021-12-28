import math
import matplotlib.pyplot as plt
from sympy import diff , cos, ln, sin
import numpy as np
min = -1.5
Max = 1.5
step = 0
temp = -1.5
points = []
number = int(input('введите количество точек '))# вводить две и более точек
step = 3/(number - 1)

for i in range(0,number):
    if temp <= 1.5:
        points.append(temp)
    temp = temp + step
#print(len(points))
#print(number)
print('точки ', points) #точки

def Function(x):
    result = (cos(x))**2 # x =[-1.5 ; 1.5]
    return result

def Function_diff_1(x):
    result = -sin(2*x)
    return result

def Function_diff_2(x):
    result = -2*cos(2*x)
    return result

def Function_diff_1_h(arr_x,step):
    result = []
    Max = arr_x[len(arr_x) - 1]
    for i in range(0, len(arr_x)):
        if(arr_x[i] != Max):
            temp = (Function(arr_x[i+1]) - Function(arr_x[i]))/step
            result.append(temp)
        else:
            temp = (Function(arr_x[i]) - Function(arr_x[i-1]))/step
            result.append(temp)
    return result

def Function_diff_1_h2(arr_x,step):
    result = []
    Max = arr_x[len(arr_x) - 1]
    min = -1.5
    for i in range(0, len(arr_x)):
        if (arr_x[i] == Max):
            temp = (Function(arr_x[i-2]) - 4*Function(arr_x[i-1]) + 3*Function(arr_x[i]))/(step*2)
        elif(arr_x[i] == min):
            temp = (-3*Function(arr_x[i]) + 4 * Function(arr_x[i + 1]) - Function(arr_x[i + 2])) / (step * 2)
        else:
            temp = (Function(arr_x[i + 1]) - Function(arr_x[i-1])) / (step*2)
        result.append(temp)
    return result
def Function_diff_2_h2(arr_x,step):
    result = []
    min=-1.5
    Max = arr_x[len(arr_x) - 1]
    for i in range(0, len(arr_x)):
        if(arr_x[i]== min):
            temp = (2*Function(arr_x[i]) - 5*Function(arr_x[i+1]) + 4*Function(arr_x[i+2]) - Function(arr_x[i+3]))/(step ** 2)
        elif(arr_x[i] == Max):
            temp = (2*Function(arr_x[i]) - 5*Function(arr_x[i-1]) + 4*Function(arr_x[i-2]) - Function(arr_x[i-3]))/(step ** 2)
        else:
            temp = (Function(arr_x[i+1]) - 2*Function(arr_x[i]) + Function(arr_x[i-1]))/(step ** 2)
        result.append(temp)
    return result

def Function_diff_2_h4(arr_x,step):
    result = []
    for i in range(0,len(arr_x)):
        temp = ( -Function(arr_x[i] - 2*step) + 16 * Function(arr_x[i] - step) -30 * Function(arr_x[i]) + 16*Function(arr_x[i]+ step) - Function(arr_x[i]+2*step)) / (12 * step ** 2)
        result.append(temp)
    return result

def Maximum(arr):
    temp = 0
    for i in range(0,len(arr)):
        if(temp<arr[i]):
            temp = arr[i]
    return temp

def Function_arr(arr,function):
    temp_arr = []
    for i in range(0, len(arr)):
        result = function(arr[i])
        temp_arr.append(result)
    return temp_arr

def Inaccuracy(arr_function, arr_lagranz):
    temp_arr= []
    for i in range(0,len(arr_function)):
        temp = abs(arr_function[i] - arr_lagranz[i])
        temp_arr.append(temp)
    return temp_arr
# def Log(Original, Function,name):
#     arr = []
#     arr_1 = []
#     for i in range(10, 100):
#         points_temp = []
#         number_temp = i
#         step_temp = 3 / (number_temp - 1)
#         arr.append(abs(ln((step_temp))))
#         temp = -1.5
#         for i in range(0, number_temp):
#             if temp <= 1.5:
#                 points_temp.append(temp)
#             temp = temp + step_temp
#         max_temp = Maximum(Inaccuracy(Function_arr(points_temp, Original),Function(points_temp,step_temp)))
#         arr_1.append(abs(ln(max_temp)))
#     plt.plot(arr, arr_1, label= name)
#     plt.grid()
#     plt.legend()

def Log():
    arr = []
    arr_1_h = []
    arr_1_h2 = []
    arr_2_h2 = []
    arr_2_h4 = []
    for i in range(10, 100):
        points_temp = []
        number_temp = i
        step_temp = 3 / (number_temp - 1)
        arr.append(abs(ln((step_temp))))
        temp = -1.5
        for i in range(0, number_temp):
            if temp <= 1.5:
                points_temp.append(temp)
            temp = temp + step_temp
        max_temp = Maximum(Inaccuracy(Function_arr(points_temp, Function_diff_1),Function_diff_1_h(points_temp,step_temp)))
        arr_1_h.append(abs(ln(max_temp)))
        max_temp = Maximum(Inaccuracy(Function_arr(points_temp, Function_diff_1), Function_diff_1_h2(points_temp, step_temp)))
        arr_1_h2.append(abs(ln(max_temp)))
        max_temp = Maximum(Inaccuracy(Function_arr(points_temp, Function_diff_2), Function_diff_2_h2(points_temp, step_temp)))
        arr_2_h2.append(abs(ln(max_temp)))
        max_temp = Maximum(Inaccuracy(Function_arr(points_temp, Function_diff_2), Function_diff_2_h4(points_temp, step_temp)))
        arr_2_h4.append(abs(ln(max_temp)))

    plt.plot(arr, arr_1_h, label= "dif_1,h")
    plt.plot(arr,arr_1_h2, label= "dif_1,h2")
    plt.plot(arr,arr_2_h2, label= "dif_2,h2")
    plt.plot(arr,arr_2_h4, label= "dif_2,h4")
    plt.grid()
    plt.legend()



#print(Inaccuracy(Function_arr(points,Function_diff_1),Function_diff_1_h(points)))
plt.title("1-ая производная")
plt.plot(points, Function_arr(points,Function_diff_1), label="original", color= 'blue')
plt.plot(points, Function_diff_1_h(points,step),label = "h", color= 'orange')
plt.plot(points,Function_diff_1_h2(points,step), label="h2", color= 'green')
plt.grid()
plt.legend()

plt.figure()
plt.title("2-ая производная")
plt.plot(points,Function_arr(points,Function_diff_2), label="original", color= 'blue')
plt.plot(points,Function_diff_2_h2(points,step), label="h2", color='orange')
plt.plot(points,Function_diff_2_h4(points,step), label="h4", color='green')
plt.grid()
plt.legend()

plt.figure()
plt.title("погрешность 1-ой производной")
plt.plot(points, Inaccuracy(Function_arr(points,Function_diff_1),Function_diff_1_h(points,step)), label="h", color='orange')
plt.plot(points,Inaccuracy(Function_arr(points,Function_diff_1),Function_diff_1_h2(points,step)), label="h2", color='green')
plt.grid()
plt.legend()

plt.figure()
plt.title("погрешность 2-ой производной")
plt.plot(points, Inaccuracy(Function_arr(points,Function_diff_2),Function_diff_2_h2(points,step)), label="h2", color='orange')
plt.plot(points,Inaccuracy(Function_arr(points,Function_diff_2),Function_diff_2_h4(points,step)), label="h4", color='green')
plt.grid()
plt.legend()

plt.figure()
Log()
plt.grid()
plt.show()
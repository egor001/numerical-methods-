import math
import matplotlib.pyplot as plt
from sympy import diff , cos, ln
import sympy
min = 0
max = 10
step = 0
temp = 0
temp1 = 0
points = []
knots = []
number = int(input('введите количество точек '))
step = 10/number
temp1 = step/2
for i in range(0,number):
    if temp <= 10:
        knots.append(temp)
    temp = temp + step

for i in range(0,number):
    if temp1 <= 10:
        points.append(temp1)
    temp1 = temp1 + step

length = len(points) #количество точек
print('точки ', points) #точки
print('узлы',knots) #узлы


def Function(x):
    result = (10 - math.cos(2*x) + math.log1p(1+x))/(1+x)
    return result

def Function_arr(arr):
    temp_arr = []
    for i in range(0, len(arr)):
        result = (10 - math.cos(2 * arr[i]) + math.log1p(1 + arr[i])) / (1 + arr[i])
        temp_arr.append(result)
    return temp_arr

def my_Lagranz(arr_y,arr_x,t):
    p = 0
    for i in range(0, len(arr_y)):
        temp = 1
        tempp = 1
        for j in range(0, len(arr_x)):
            if i !=j :
                tempp = tempp*(arr_x[i] - arr_x[j])
                temp = temp * (t - arr_x[j])
        p= p+ arr_y[i]*(temp/tempp)

    return p


def Lagranz_arr(arr_y,arr_x, arr_points):
    temp_arr = []
    for i in range(0,len(arr_points)):
        temp_arr.append(my_Lagranz(arr_y,arr_x, arr_points[i]))
    return temp_arr

def Chebushev():
    temp_arr= []
    for i in range(0,length):
        x = (min+max)/2 + ((max-min)*math.cos((2*i+1)*math.pi/(2*length)))/2
        temp_arr.append(x)
    #print(temp_arr)
    return temp_arr

def Inaccuracy(arr_function, arr_lagranz):
    temp_arr= []
    for i in range(0,len(arr_function)):
        temp = abs(arr_function[i] - arr_lagranz[i])
        temp_arr.append(temp)
    return temp_arr

def Task():
    result_arr=[]
    for i in range(2,100):
        number =i
        step = 10 / number
        temp1 = step / 2
        points = []
        knots = []
        temp=0

        for i in range(0, number):
            if temp <= 10:
                knots.append(temp)
            temp = temp + step

        for i in range(0, number):
            if temp1 <= 10:
                points.append(temp1)
            temp1 = temp1 + step

        max1 = FindMax(Inaccuracy(Function_arr(points), Lagranz_arr(Function_arr(knots), knots, points)))
        result_arr.append(max1)
    temp_arr = []
    temp_point = 0
    temp_min=10000
    for i in range(0,98):
        print("max: "+str(result_arr[i])+"точки: "+ str(i+2))
        if(temp_min>result_arr[i]):
            temp_min = result_arr[i]
            temp_point=i+2
        temp_arr.append(i)
    print("минимальный максимум: "+ str(temp_min)+ "в точке: "+ str(temp_point))
    plt.figure()
    plt.title("Задание")
    plt.plot(temp_arr,result_arr)
    plt.grid()
    plt.show()






def FindMax(arr):
    result = 0
    for i in range(0,len(arr)):
        if(arr[i]>result):
            result=arr[i]

    return result



print('значения функции в точках ',Function_arr(points))
print('значение функции в узлах',Function_arr(knots))
#print(len(knots))
#print(len(points))
print('значение функции в точках, используя полином Лагранжа(узлы фикисрованные)',Lagranz_arr(Function_arr(knots),knots, points))
print('значение функции в точках, используя полином Лагранжа(узлы Чебышева)',Lagranz_arr(Function_arr(Chebushev()), Chebushev(), points))
print('ggg', Chebushev())
#print(Inaccuracy(1.5))
#Chebushev()
#print(my_Lagranz(knots, Function_arr(knots), 0.5))
#print(Lagranz(knots, Function_arr(knots), 0.5))
plt.title("Узлы Чебышева")
plt.plot(points, Function_arr(points),color='red',label="original") #строит график по точкам
plt.plot(points,Lagranz_arr(Function_arr(Chebushev()), Chebushev(), points),color= 'blue')
plt.grid()
plt.legend()

plt.figure()
plt.title("С фиксированными узлами")
plt.plot(points, Function_arr(points),color='red', label="original")
plt.plot(points, Lagranz_arr( Function_arr(knots),knots, points), color='blue')
plt.grid()
plt.legend()

plt.figure()
plt.title("Погрешности")
plt.plot(points,Inaccuracy(Function_arr(points), Lagranz_arr(Function_arr(knots),knots, points)), color='red', label="с фикс. узлами")
plt.plot(points,Inaccuracy(Function_arr(points), Lagranz_arr(Function_arr(Chebushev()), Chebushev(), points)), color='blue', label="с узлами Чебышева")
plt.grid()
plt.legend()

#plt.show()
Task()



import math
import matplotlib.pyplot as plt

step = 0.05
a = 0
b = 1


def Function(x, u_0, u_1):
    result = (2+6*x+5*(x**2))/(1+x)**2 - u_1/(1+x) - u_0/(1+x)**2
    return result


def Original(x):
    result = x ** 2 + math.sin(math.log(x + 1))
    return result

def Eler_method1(x_arr, Function,step):
    h = step
    u_0 = 0
    u_1 = 1

    u_0_arr = []
    u_0_arr.append(u_0)
    u_1_arr = []
    u_1_arr.append(u_1)

    for i in range(0,len(x_arr) - 1):
        u_1 = u_1_arr[i] + h * Function(x_arr[i], u_0_arr[i], u_1_arr[i])
        u_0 = u_0_arr[i] + h * u_1_arr[i]
        u_0_arr.append(u_0)
        u_1_arr.append(u_1)

    return u_0_arr

def Runge_Kutta_method1(x_arr, Function, step):
    h = step
    u_0 = 0
    u_1 = 1

    u_0_arr = []
    u_0_arr.append(u_0)
    u_1_arr = []
    u_1_arr.append(u_1)

    for i in range(0,len(x_arr) - 1):
        k1 = Function(x_arr[i], u_0_arr[i], u_1_arr[i])
        q1 = u_1_arr[i]

        k2 = Function(x_arr[i] + h / 2, u_0_arr[i] + (h / 2) * q1, u_1_arr[i] + (h / 2) * k1)
        q2 = u_1_arr[i] + (h / 2) * k1

        k3 = Function(x_arr[i] + h / 2, u_0_arr[i] + (h / 2) * q2, u_1_arr[i] + (h / 2) * k2)
        q3 = u_1_arr[i] + (h / 2) * k2

        k4 = Function(x_arr[i]+h, u_0_arr[i] + h*q3, u_1_arr[i] + h * k3)
        q4 = u_1_arr[i] + h * k3



        u_1 = u_1_arr[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        u_0 = u_0_arr[i] + (h / 6) * (q1 + 2 * q2 + 2 * q3 + q4)

        u_1_arr.append(u_1)
        u_0_arr.append(u_0)

    return u_0_arr

def Adams_method1(x_arr, Function,step):
    h = step
    u_0 = 0
    u_1 = 1

    u_0_arr = []
    u_0_arr.append(u_0)
    u_1_arr = []
    u_1_arr.append(u_1)

    for i in range(0,2):
        k1 = Function(x_arr[i], u_0_arr[i], u_1_arr[i])
        q1 = u_1_arr[i]

        k2 = Function(x_arr[i] + h / 2, u_0_arr[i] + (h / 2) * q1, u_1_arr[i] + (h / 2) * k1)
        q2 = u_1_arr[i] + (h / 2) * q1

        k3 = Function(x_arr[i] + h / 2, u_0_arr[i] + (h / 2) * q2, u_1_arr[i] + (h / 2) * k2)
        q3 = u_1_arr[i] + (h / 2) * q2

        k4 = Function(x_arr[i] + h, u_0_arr[i] + h*q3, u_1_arr[i] + h * k3)
        q4 = u_1_arr[i] + h * q3

        u_1 = u_1_arr[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        u_0 = u_0_arr[i] + (h / 6) * (q1 + 2 * q2 + 2 * q3 + q4)

        u_1_arr.append(u_1)
        u_0_arr.append(u_0)


    for i in range(0,len(x_arr) - 3):
        u_1 = u_1_arr[i + 2] + h * ((23 / 12) * Function(x_arr[i + 2], u_0_arr[i + 2], u_1_arr[i + 2]) - (4 / 3) * Function(x_arr[i + 1], u_0_arr[i + 1], u_1_arr[i + 1]) +(5 / 12) * Function(x_arr[i], u_0_arr[i], u_1_arr[i]))
        u_0 = u_0_arr[i + 2] + h * ((23 / 12) * u_1_arr[i + 2] - (4 / 3) * u_1_arr[i + 1] + (5 / 12) * u_1_arr[i])
        u_1_arr.append(u_1)
        u_0_arr.append(u_0)

    return u_0_arr


def Runge_amendment(x_arr, x_arr_rude,Function,step,original_arr):
    t = 4
    h = 0.1
    
    arr_runge_amend = []
    arr_res_rud = Runge_Kutta_method1(x_arr_rude,Function,h)
    arr_res = Runge_Kutta_method1(x_arr,Function,step)
    for i in range(0,len(x_arr_rude)):
        arr_runge_amend.append(abs(arr_res[i*2] - arr_res_rud[i])/15)

    rk_after = []
    for i in range(0,len(x_arr_rude)):
        rk_after.append(arr_res[i*2] + arr_runge_amend[i])

    err2 = [abs(e - u) for e, u in zip(rk_after, original_arr)]
    err1 = [abs(e - u) for e, u in zip(arr_res_rud, original_arr)]

    print("до", err1)
    print("после", err2)



original_arr = []
x_arr = []
n = int(b/step)
temp = 0
for i in range(0,n):
    original_arr.append(Original(temp))
    x_arr.append(temp)
    temp = temp + step

x_arr_rude = []
original_arr_rude = []
step1 = 0.1
n = int(b/step1)
temp = 0
for i in range(0,n):
    x_arr_rude.append(temp)
    original_arr_rude.append(Original(temp))
    temp = temp + step1

Euler_errors = [abs(e - u)  for e, u  in zip(Eler_method1(x_arr,Function,step), original_arr)]
Runge_errors = [abs(e - u)  for e, u  in zip(Runge_Kutta_method1(x_arr,Function,step), original_arr)]
Adams_errors = [abs(e - u)  for e, u  in zip(Adams_method1(x_arr,Function,step), original_arr)]
print("Euler: ",Euler_errors)
print("Runge-Kutte: ",Runge_errors)
print("Adams: ",Adams_errors)

plt.figure()
plt.plot(x_arr,Adams_errors, label="Adams")
plt.plot(x_arr,Euler_errors, label="Eler")
plt.plot(x_arr,Runge_errors, label="Runge-Kutt")
plt.legend()
plt.grid()

Runge_amendment(x_arr,x_arr_rude,Function,step,original_arr_rude)

plt.figure()
plt.plot(x_arr,Adams_method1(x_arr,Function,step), label="Adams")
plt.plot(x_arr,Eler_method1(x_arr,Function,step), label="Eler")
plt.plot(x_arr,Runge_Kutta_method1(x_arr,Function,step), label="Runge-Kutt")
plt.plot(x_arr,original_arr, label="Original")
plt.legend()
plt.grid()
plt.show()

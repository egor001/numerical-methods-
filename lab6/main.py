import math
import matplotlib.pyplot as plt

step = 0.05
a = 0
b = 1


def p(x):
    return 1 / (1 + x)


def q(x):
    return 1 / (1 + x) ** 2


def f(x):
    return (2 + 6 * x + 5 * x ** 2) / (1 + x) ** 2


def Original(x):
    result = x ** 2 + math.sin(math.log(x + 1))
    return result


def Run_through_method(arr_x, p, q, f, h, arr_orig):
    c0 = (-1 - 2 * h) / ((h * p(arr_x[0]) - 2) * (-1 - 2 * h) - (1 - h * p(arr_x[0]) + h * h * q(arr_x[0])))
    d0 = (1 - h*p(arr_x[0]) + h*h*q(arr_x[0]))*h/(1+2*h) + f(arr_x[0])*h*h
    arr_c = []
    arr_d = []
    arr_c.append(c0)
    arr_d.append(d0)


    for i in range(1,len(arr_x) - 1):
        ci = 1/((h*p(arr_x[i]) - 2) - (1 - h*p(arr_x[i]) + h*h*q(arr_x[i]))*arr_c[i-1])
        di = f(arr_x[i])*h*h - (1 - h*p(arr_x[i]) + h*h*q(arr_x[i]))*arr_c[i-1]*arr_d[i-1]
        arr_c.append(ci)
        arr_d.append(di)

    yn = (arr_c[len(arr_x)-2]*arr_d[len(arr_x)-2] + 7.3015*h)/(1+arr_c[len(arr_x)-2] + 3*h)


    arr_y = []
    arr_y.append(yn)

    for i in range(1,len(arr_x) - 1):
        yi = arr_c[len(arr_x) - 2 - i]*(arr_d[len(arr_x) - 2 - i] - arr_y[i-1])
        arr_y.append(yi)

    y0 = (-1*arr_y[len(arr_y) - 1] + h)/(-1 - 2*h)
    arr_y.append(y0)
    arr_result = []
    arr_err = []

    for i in range(0,len(arr_y)):
        arr_result.append(arr_y[len(arr_y) -1 - i])

    for i in range(0,len(arr_y)):
        arr_err.append(abs(arr_result[i] - arr_orig[i]))

    return  arr_result


def Run_through_method2(arr_x, p, q, f, h, arr_orig):
    c1 = (-1 - 2 * h)/((2*q(arr_x[1])*h*h - 4)*(-1 - 2*h)/(2+h*p(arr_x[1])) - (2 - h*p(arr_x[1]))/(2 + h*p(arr_x[1])))
    d1 = 2*f(arr_x[1])*h*h/(2+p(arr_x[1])*h) + (2 - h*p(arr_x[1]))*(-h)/((2+h*p(arr_x[1]))*(-1-2*h))


    arr_c = []
    arr_d = []
    arr_c.append(0)
    arr_d.append(0)
    arr_c.append(c1)
    arr_d.append(d1)

    for i in range(2, len(arr_x)):
        ci = 1 / ((2*q(arr_x[i])*h*h - 4)/(2+h*p(arr_x[i])) - (2 - h*p(arr_x[i]))*arr_c[i - 1]/(2 + h*p(arr_x[i])))
        di = (2*f(arr_x[i])*h*h)/(2+h*p(arr_x[i])) - (2 - h*p(arr_x[i]))*arr_c[i-1]*arr_d[i-1]/(2+h*p(arr_x[i]))
        arr_c.append(ci)
        arr_d.append(di)


    yn = (2 * 7.3015 * h - (arr_d[i] - arr_c[i - 1] * arr_d[i - 1])) / (6 * h + arr_c[i - 1] - 1 / arr_c[i])


    arr_y = []
    arr_y.append(yn)
    for i in range(1, len(arr_x) - 1):
        yi = arr_c[len(arr_x)  -1- i] * (arr_d[len(arr_x)  -1- i] - arr_y[i - 1])
        arr_y.append(yi)

    y0 = (arr_y[len(arr_y) - 1] - h) / (1 + 2 * h)
    # y0_temp = (-1*arr_orig[1] + h)/(-1 - 2*h)
    # print("ddd ",yn_temp)
    arr_y.append(y0)
    arr_result = []
    arr_err = []
    for i in range(0, len(arr_y)):
        arr_result.append(arr_y[len(arr_y) - 1 - i])
    for i in range(0, len(arr_y)):
        arr_err.append(abs(arr_result[i] - arr_orig[i]))

    return arr_result

arr_x = []
arr_orig = []
n = int(b / step)
temp = 0
for i in range(0, n+1):
    arr_x.append(temp)
    arr_orig.append(Original(temp))
    temp = temp + step

plt.figure()
plt.grid()
plt.plot(arr_x, Run_through_method(arr_x,p,q,f,step,arr_orig), label = "h")
plt.plot(arr_x, arr_orig, label = "original")
plt.plot(arr_x, Run_through_method2(arr_x,p,q,f,step,arr_orig), label = "h2")
plt.legend()

plt.figure()
plt.grid()
err_h = [abs(e - u)  for e, u  in zip(Run_through_method(arr_x,p,q,f,step,arr_orig), arr_orig)]
err_h2 = [abs(e - u)  for e, u  in zip(Run_through_method2(arr_x,p,q,f,step,arr_orig), arr_orig)]
print(err_h)
print(err_h2)
plt.plot(arr_x,err_h, label = "h")
plt.plot(arr_x,err_h2, label = "h2")
plt.legend()


plt.show()
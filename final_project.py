# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни.
# Найти интервалы, на которых функция возрастает.
# Найти интервалы, на которых функция убывает.
# Построить график.
# Вычислить вершину.
# Определить промежутки, на котором f > 0.
# Определить промежутки, на котором f < 0.


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


x = sp.symbols('x')
f = sp.sympify('-12*x^4*sin(cos(x)) - 18*x^3+5*x^2 + 10*x - 30')

begint = -11 # начало интервала
endint = 11 # конец интервала
accuracy = 0.000001 # точность вычислений
step = 0.001

xlist = []
ylist = []
i = begint
xlist.append(i)
ylist.append(f.evalf(subs={x: i}))

while i < endint + step:
    if f.evalf(subs={x: i}) * f.evalf(subs={x: i+step}) <= 0:
        beg = i
        while beg < i + step + accuracy:
            if f.evalf(subs={x: beg}) * f.evalf(subs={x: beg+step}) <= 0:
                xlist.append(beg)
                ylist.append(f.evalf(subs={x: beg}))
                break
            beg += accuracy
    elif f.evalf(subs={x: i}) > f.evalf(subs={x: i+step}) and f.evalf(subs={x: i}) > f.evalf(subs={x: i-step}):
        xlist.append(i)
        ylist.append(f.evalf(subs={x: i}))
    elif f.evalf(subs={x: i}) < f.evalf(subs={x: i+step}) and f.evalf(subs={x: i}) < f.evalf(subs={x: i-step}):
        xlist.append(i)
        ylist.append(f.evalf(subs={x: i}))
    i += step
xlist.append(endint)
ylist.append(f.evalf(subs={x: endint}))

for i in range(len(xlist) - 2):
    xl = np.arange(xlist[i], xlist[i + 1] + step, step)
    if f.evalf(subs={x: (xlist[i] + xlist[i + 1]) /2 }) > 0:
        line = '-'
    else:
        line = '--'
    if ylist[i] > ylist[i + 1]:
        color = 'red'
    else:
        color = 'blue'
    plt.rcParams['lines.linestyle'] = line
    yl = [f.evalf(subs={x: j}) for j in xl]
    plt.plot(xl, yl, color)

plt.grid()
plt.show()


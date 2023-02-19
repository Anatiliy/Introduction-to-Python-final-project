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
print(f)
print(f.evalf(subs={x: 1}))


limit = 10
step = 0.01
step_acr = 0.0001
line_style = '-'
color = 'b'
direct_up = True


def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style


def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


x_list = np.arange(-limit, limit + step, step)

x_change = [(-limit, 'limit')]

for i in range(len(x_list) - 2):
    if f.evalf(subs={x: x_list[i]}) * f.evalf(subs={x: x_list[i + 1]}) <= 0:
        x_acr = np.arange(x_list[i], x_list[i + 1] + step_acr, step_acr)
        #x_change.append((x_list[i], 'dir'))
        for j in range(len(x_acr) - 2):
            if f.evalf(subs={x: x_acr[j]}) * f.evalf(subs={x: x_acr[j + 1]}) <= 0:
                x_change.append((x_acr[j], 'zero'))
    if direct_up:
        if f.evalf(subs={x: x_list[i]}) > f.evalf(subs={x: x_list[i + 1]}):
            direct_up = False
            x_change.append((x_list[i], 'dir'))
    else:
        if f.evalf(subs={x: x_list[i]}) < f.evalf(subs={x: x_list[i + 1]}):
            direct_up = True
            x_change.append((x_list[i], 'dir'))

x_change.append((limit, 'limit'))

for i in range(len(x_change) - 2):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], f.evalf(subs={x: x_change[i][0]}), 'go')
        plt.rcParams['lines.linestyle'] = switch_line()
        y_list = [f.evalf(subs={x: j}) for j in cur_x]
        plt.plot(cur_x, y_list, color)
    else:
        y_list = [f.evalf(subs={x: j}) for j in cur_x]
        plt.plot(cur_x, y_list, switch_color())

plt.grid()
plt.show()


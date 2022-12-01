from task3 import point_derivative
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def partial_derivative(func, point, index_of_var):
    def temp_func(x):
        temp_point = list(point)
        temp_point[index_of_var] = x
        return func(*temp_point)

    return point_derivative(temp_func, point[index_of_var])


def gradient_at_point(func, x, y):
    gradient = []
    point = [x, y]
    for index, coord in enumerate(point):
        gradient.append(partial_derivative(func, point, index))
    norm = 0
    for i in gradient:
        norm += i ** 2
    norm = sqrt(norm)
    gradient = [i / norm for i in gradient]
    return np.array(gradient)


def f(x, y):
    return x ** 2 - y ** 2


fig = plt.figure(figsize=plt.figaspect(2.))
x, y = np.meshgrid(np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1))

ax = fig.add_subplot(2, 1, 1, projection='3d')
z = np.vectorize(f)(x, y)
ax.plot_surface(x, y, z, cmap=cm.coolwarm)

ax = fig.add_subplot(2, 1, 2)
gradients = np.vectorize(gradient_at_point, excluded=['func'], signature='(),(),()->(n)')(f, x, y)
u = gradients[:, :, 0]
v = gradients[:, :, 1]
plt.quiver(x, y, u, v)

plt.show()

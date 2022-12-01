import matplotlib.pyplot as plt

import numpy as np


def point_derivative(func, x, start_delta=0.01, epsilon=0.01):
    delta = start_delta

    def limit_iter(delta):
        return (func(x + delta) - func(x)) / delta

    prev_iter = limit_iter(delta)

    delta = delta / 2
    next_iter = limit_iter(delta)

    while abs(prev_iter - next_iter) >= epsilon:
        delta = delta / 2
        prev_iter = next_iter
        next_iter = limit_iter(delta)

    return next_iter


def derivative(func, left=0, right=10, step=0.01):
    x = np.arange(-5, 5, 0.01)
    y = [point_derivative(func, i) for i in x]
    return y

if __name__ == "__main__":
    x = np.arange(-5, 5, 0.01)
    y1 = np.sin(x)
    y2 = derivative(np.sin)
    plt.figure()

    plt.subplot(211)
    plt.plot(x, y1, )
    plt.title("sin(x)")

    plt.subplot(212)
    plt.plot(x, y2, "r")
    plt.title("derivative of sin(x)")

    plt.tight_layout()
    plt.show()

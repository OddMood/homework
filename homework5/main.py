import scipy.stats as sp
import matplotlib.pyplot as plt
import numpy as np


def is_discrete(distr):
    return isinstance(distr, sp.rv_discrete)


def plot_distr(distr, *args):
    plt.figure()
    x = np.linspace(distr.ppf(0.01, *args),distr.ppf(0.99, *args), 1000)
    if is_discrete(distr):
        plt.subplot(211)
        plt.bar(x, distr.cdf(x, *args))
        plt.subplot(212)
        plt.bar(x, distr.pmf(x, *args))
    else:
        plt.subplot(211)
        plt.plot(x, distr.cdf(x, *args))
        plt.subplot(212)
        plt.plot(x, distr.pdf(x, *args))

    plt.savefig(distr.name)


plot_distr(sp.uniform)

n = 20
p = 0.7
plot_distr(sp.binom, n, p)

mu = 0.6
plot_distr(sp.poisson, mu)

plot_distr(sp.norm)

plot_distr(sp.expon)


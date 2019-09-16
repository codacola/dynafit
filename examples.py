""" tests.py: test cases for this project
"""

__author__ = "Florian Helmhold"
__version__ = "0.1"
__email__ = "florian.helmhold@uni-tuebingen.de"
__status__ = "alpha"


from dynafit.simulation import lds
from dynafit.fit import fit_full, fit_skew
from dynafit.projection import project_rotmax


import numpy as np
import matplotlib.pyplot as plt


def plot_field(m, dims=(0, 1), size=10):
    x = np.arange(-size, size, size / 100.0)
    y = np.arange(-size, size, size / 100.0)

    X, Y = np.meshgrid(x, y)

    points = np.vstack([X.flat, Y.flat]).T

    responses = m[:, dims].dot(points.T)

    U = responses[0].reshape(len(x), len(y))
    V = responses[1].reshape(len(x), len(y))

    speed = np.sqrt(U * U + V * V)

    lw = 5 * speed / speed.max()
    plt.streamplot(X, Y, U, V, density=0.6, color='gray')#, linewidth=lw)


def plot_traces(traces, dims=(0, 1)):
    for t in traces:
        plt.plot(t[:, dims[0]], t[:, dims[1]])


def example_2d():

    m = np.array([[-0.1, -1],
                  [1, 0.2]]) * 0.01

    traces = lds(m, steps=200)

    plt.figure(figsize=(9, 3))

    plt.subplot(1, 3, 1)
    plt.title("original")
    plot_field(m, (0, 1), size=np.max(traces))
    plot_traces(traces)

    m_fit = fit_full(traces)

    plt.subplot(1, 3, 2)
    plt.title("full fit")
    plot_field(m_fit, size=np.max(traces))
    plot_traces(traces)

    m_skew = fit_skew(traces)

    plt.subplot(1, 3, 3)
    plt.title("skew fit")
    plot_field(m_skew, size=np.max(traces))
    plot_traces(traces)
    plt.show()


def example_projection():

    m = np.array([[-0.1, -1, 2],
                  [1, -0.1, -2],
                  [-2, 2, -1.2]]) * 0.01

    traces = lds(m, steps=200)

    m_skew = fit_skew(traces)

    traces_rmax = [project_rotmax(t, m_skew) for t in traces]

    plt.figure(figsize=(6, 3))

    plt.title("full fit")
    plt.subplot(1, 2, 1)
    plot_traces(traces)
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plot_traces(traces_rmax)
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    example_projection()
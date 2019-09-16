""" simulation.py: tools to simulate dynamical systems
"""

__author__ = "Florian Helmhold"
__version__ = "0.1"
__email__ = "florian.helmhold@uni-tuebingen.de"
__status__ = "alpha"


import numpy
import scipy.integrate


def lds(m, steps=20, repetitions=10, dt=1):
    """ Simulation of a linear dynamical system where the rate of change of
        a state-vector is a linear combination of the previous state-vector.

    Args:
        m (nxn matrix): Transfer Matrix
        steps (int, optional): Number of steps to simulate
        repetitions (int, optional): Number of repetitions with andom intial
                                     conditions

    Returns:
        list of arrays: List of repeated simulations, each entry is an array
                        composed of rows of consecutive state-vectors

    """
    n = m.shape[0]

    def step(x, _):
        return m.dot(x.T)

    trials = [scipy.integrate.odeint(step, numpy.random.rand(n) - 0.5,
                                     numpy.arange(steps) * dt)
              for _ in range(repetitions)]

    return trials

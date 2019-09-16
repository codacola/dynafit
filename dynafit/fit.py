""" utils.py: various functions
"""

__author__ = "Florian Helmhold"
__version__ = "0.1"
__email__ = "florian.helmhold@uni-tuebingen.de"
__status__ = "alpha"

import numpy
import scipy

from . import utils


def _preprocess(x):
    """ compute derivatives and package data
    """

    if isinstance(x, list):
        dx = numpy.vstack([numpy.gradient(x_i, axis=0) for x_i in x])
        x = numpy.vstack(x)
    else:
        dx = numpy.gradient(x, axis=0)

    return x, dx


def fit_full(x, verbose=False):
    """ Fit an unconstrained linear dynamic model to traces of state-vectors

    Args:
        x (list or array): list of trials or single trial of rows of
                           consecutive state-vectors
        verbose (bool, optional): print additional information on fit results

    Returns:
        matrix: Approximated system matrix
    """

    # Numerically differentiate state to get state change
    x, dx = _preprocess(x)

    # Fit the linear model
    m, resid, rank, s = scipy.linalg.lstsq(x, dx)

    if verbose:
        print("--- Fit full results ---")
        print("Residuals: {}".format(resid))
        print("Rank: {}".format(resid))
        print("singular values: {}".format(s))

    return m.T


def fit_skew(x, verbose=False):
    """ Fit a linear dynamic model with skew-symetric matrix to traces of
        state-vectors

    Args:
        x (list or array): list of trials or single trial of rows of
                           consecutive state-vectors

    Returns:
        matrix: Approximated (skew-symetric) system matrix
    """
    # Differentiate state observations to get state change
    x, dx = _preprocess(x)

    # Define loss function of the skew model
    def loss(k):
        m = utils.vec_to_skew(k)
        return numpy.linalg.norm(dx.T - m.dot(x.T))

    # Calculate intial value by applying the linear model
    m0 = fit_full(x)
    k0 = utils.skew_to_vec((m0 - m0.T) / 2.0)

    # Run optimization
    res = scipy.optimize.minimize(loss, k0)

    if verbose:
        print("--- Fit skew results ---")
        print(res)

    return utils.vec_to_skew(res.x)

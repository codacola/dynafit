""" utils.py: various functions
"""

__author__ = "Florian Helmhold"
__version__ = "0.1"
__email__ = "florian.helmhold@uni-tuebingen.de"
__status__ = "alpha"


import numpy


def get_skew(x):
    """ returns the skew-symetric component of a matrix
    """
    return 0.5 * (x - x.T)


def get_sym(x):
    """ returns the symetric component of a matrix
    """
    return 0.5 * (x + x.T)


def vec_to_skew(v):
    """ maps a vector onto a skew-symetric matrix
    """
    n = (1 + numpy.sqrt(8 * v.shape[0] + 1)) / 2
    assert n.is_integer()
    n = int(n)
    tri = numpy.zeros((n, n))
    tri[numpy.tril(numpy.ones((n, n), dtype=bool), -1)] = v
    return tri - tri.T


def skew_to_vec(m):
    """ maps the lower triangle of an skew-symetric matrix
        onto a vector
    """
    n = m.shape[0]
    return m[numpy.tril(numpy.ones((n, n), dtype=bool), -1)]

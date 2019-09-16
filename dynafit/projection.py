""" projection.py: various functions
"""

__author__ = "Florian Helmhold"
__version__ = "0.1"
__email__ = "florian.helmhold@uni-tuebingen.de"
__status__ = "alpha"


import numpy


def get_rotmax_vectors(m):
    """ Calculate the vectors that span planes with maximal rotation

    Args:
        m (matrix): skew-symetric matrix to process

    Returns:
        2D array: row wise projection vectors with decending magnitudes
                  of eigenvalues
    """
    # calculate and sort eigenvalues and -vectors
    vals, vecs = numpy.linalg.eig(m)
    idx = numpy.argsort(abs(vals))[::-1]
    vals = vals[idx]
    vecs = vecs[:, idx]

    # calculate max-rotation projection vectors
    vec_pairs = [(vecs[:, i * 2], vecs[:, i * 2 + 1])
                 for i in range(len(vals) // 2)]
    u = [(v[0] + v[1], 1j * (v[0] - v[1])) for v in vec_pairs]

    # remove residual imaginary parts and renormalize
    u = numpy.vstack(numpy.real(u)) / numpy.sqrt(2)

    return u


def project_rotmax(x, m):
    """ Project one or multiple samples onto the vectors that span
        planes of maximal rotation

    Args:
        x (2D array): Array of observations (samples x features)
        m (2D array): Skew-symetric matrix to process

    Returns:
        2D array: Projected observations (samples x features)
    """

    u = get_rotmax_vectors(m)
    return u.dot(x.T).T

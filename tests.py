""" tests.py: test cases for this project
"""

__author__ = "Florian Helmhold"
__version__ = "0.1"
__email__ = "florian.helmhold@uni-tuebingen.de"
__status__ = "alpha"


import unittest

import numpy

import dynafit.fit as fit
import dynafit.simulation as simulation
import dynafit.utils as utils
import dynafit.projection as projection


class TestUtils(unittest.TestCase):

    def setUp(self):

        n = 10
        self.m = numpy.arange(n ** 2).reshape(n, n)
        self.k = numpy.arange((n * (n - 1)) / 2) + 0.1

    def test_get_skew(self):
        skew = 0.5 * (self.m - self.m.T)
        t = utils.get_skew(self.m)

        self.assertTrue((t == skew).all())

    def test_get_sym(self):
        sym = 0.5 * (self.m + self.m.T)
        t = utils.get_sym(self.m)

        self.assertTrue((t == sym).all())

    def test_skew_to_vec(self):
        skew = 0.5 * (self.m - self.m.T)
        k = utils.skew_to_vec(skew)

        self.assertEqual(numpy.sum(numpy.abs(skew)),
                         numpy.sum(2.0 * numpy.abs(k)))
        self.assertEqual(numpy.sum(skew != 0),
                         len(k) * 2)

    def test_vec_to_skew(self):
        m = utils.vec_to_skew(self.k)
        self.assertAlmostEqual(numpy.sum(2.0 * numpy.abs(self.k)),
                               numpy.sum(numpy.abs(m)))
        self.assertEqual(len(self.k) * 2,
                         numpy.sum(m != 0))


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m_full = numpy.array(([-0.001, -0.020, 0.030],
                                   [0.020, -0.001, 0.020],
                                   [0.022, -0.001, -0.020])) * 0.1

        self.m_skew = numpy.array(([0.00, -0.02, -0.03],
                                   [0.02, 0.00, 0.01],
                                   [0.03, -0.01, 0.0])) * 0.1

        self.trials_full = simulation.lds(self.m_full, steps=200,
                                          repetitions=100)

        self.trials_skew = simulation.lds(self.m_skew, steps=200,
                                          repetitions=100)


class TestFit(TestMatrix):

    def test_fit(self):
        m_fit = fit.fit_full(self.trials_full)
        self.assertTrue((numpy.allclose(m_fit, self.m_full, rtol=0.01)))

    def test_fit_skew(self):
        m_fit = fit.fit_skew(self.trials_skew)

        self.assertTrue((numpy.allclose(m_fit, -m_fit.T)))
        self.assertTrue((numpy.allclose(m_fit, self.m_skew, rtol=0.01)))


class TestProjection(TestMatrix):

    def get_rotmax_vectors(self):
        u = projection.get_projection_vectors(self.m_skew)

        # test for pairwise orthogonality
        for i in range(len(u) // 2):
            self.assertAlmostEqual(numpy.dot(u[i * 2], u[i * 2 + 1]), 0.0)

        # test for unit length
        for u_i in u:
            self.assertAlmostEqual(numpy.linalg.norm(u_i), 1.0)


if __name__ == '__main__':
    unittest.main()

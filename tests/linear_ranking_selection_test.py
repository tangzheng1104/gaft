#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Test case for built-in Linear Ranking selection
'''

import unittest

from gaft.components.population import GAPopulation
from gaft.components.individual import BinaryIndividual
from gaft.operators import LinearRankingSelection

class LinearRankingSelectionTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff
        def fitness(indv):
            x, = indv.solution
            return x**3 - 60*x**2 + 900*x + 100
        self.fitness = fitness

    def test_selection(self):
        indv = BinaryIndividual(ranges=[(0, 30)], verbosity=0)
        p = GAPopulation(indv)
        p.init()

        selection = LinearRankingSelection()
        father, mother = selection.select(p, fitness=self.fitness)

        self.assertTrue(isinstance(father, BinaryIndividual))
        self.assertTrue(isinstance(mother, BinaryIndividual))
        self.assertNotEqual(father.chromsome, mother.chromsome)

if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(LinearRankingSelectionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


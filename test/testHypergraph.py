import unittest

from src.hypergraph import _cartesian, _dimensions, _tuplesToList, buildHypergraphEdges, fromHypergraphToConcepts


class TestHypergraph(unittest.TestCase):
    '''
    @TODO move this file into their own test folder
    '''
    def test_dimensionsEmpty(self):
        self.assertEqual(_tuplesToList(_dimensions([])), [])

    def test_dimensionsOfTwoColumns(self):
        list_dimensions = _tuplesToList(_dimensions([1, 2]))
        expected = [[0], [0, 1]]
        self.assertEqual(list_dimensions, expected)

    def test_cartesianEmpty(self):
        self.assertEqual(_cartesian([]), [[]])

    def test_cartesianProduct(self):
        product = _cartesian([[0, 1], [2, 3]])
        expected = [[0, 2], [0, 3], [1, 2], [1, 3]]
        self.assertEqual(product, expected)

    def test_buildHypergraphEmpty(self):
        context = [[], 0]
        hg = buildHypergraphEdges(context)
        self.assertEqual(hg, [])

    def test_buildHypergraphWithContext(self):
        context = [[[0, 1], [1, 2], [2, 3]], 3, 3]
        hg = buildHypergraphEdges(context)
        expected = [[0, 3], [0, 5], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5]]
        self.assertEqual(hg, expected)

    def test_fromHypergraphToConceptsShouldNotBeEmpty(self):
        hypergraph = """"""
        self.assertRaises(ValueError, fromHypergraphToConcepts, hypergraph)

    def test_fromHypergraphToConceptsShouldContainMoreThanOneLine(self):
        hypergraph = """1 2 3"""
        self.assertRaises(ValueError, fromHypergraphToConcepts, hypergraph)

    def test_fromHypergraphToConceptsCreatesConcept(self):
        hypergraph = """3 5 4\n3 5 1 2\n0 3 4 2\n0 1 2\n4\n\n0\n0\n0\n2\n2"""
        concept = fromHypergraphToConcepts(hypergraph)
        expected = [['3', '5', '4'], ['3', '5', '1', '2'], ['0', '3', '4', '2'], ['0', '1', '2']]
        self.assertEqual(concept, expected)

if __name__ == '__main__':
    unittest.main()
